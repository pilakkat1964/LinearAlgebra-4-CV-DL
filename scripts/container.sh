#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"

RUNTIME=""
if command -v podman >/dev/null 2>&1; then
  RUNTIME=podman
elif command -v docker >/dev/null 2>&1; then
  RUNTIME=docker
else
  echo "Error: neither podman nor docker found on PATH. Install podman (preferred) or docker." >&2
  exit 1
fi

TAG="la4cvdl:dev"

usage() {
  cat <<USAGE
Usage: $0 <command> [options]

Commands:
  build [--heavy] [--manim] [--tag NAME]   Build the image (heavy triggers optional heavy deps; --manim installs Manim/system deps)
  run [--tag NAME] [--] [CMD]    Run a container and execute CMD (interactive shell by default)
  shell [--tag NAME]             Open an interactive shell in the container
  jupyter [--tag NAME] [--port N]  Run Jupyter Lab and expose port (default 8888)
  streamlit [--tag NAME] [--port N] Run Streamlit demo and expose port (default 8501)
  clean                          Remove dangling images (best-effort)
  help                           Show this message

This script prefers podman and falls back to docker. It mounts the current working
directory into /workspace inside the container and tries to preserve host file ownership.
USAGE
}

build_image() {
  local heavy=0
  local manim=0
  local force=0
  while [ "$#" -gt 0 ]; do
    case "$1" in
      --heavy) heavy=1; shift ;;
      --manim) manim=1; shift ;;
      --tag) TAG="$2"; shift 2 ;;
      --yes|--force|-y) force=1; shift ;;
      --help) usage; exit 0 ;;
      *) echo "Unknown build option: $1"; usage; exit 1 ;;
    esac
  done

  echo "Using runtime: $RUNTIME"
  # Default threshold for warning (MB)
  IMG_SIZE_WARN_MB=${IMG_SIZE_WARN_MB:-300}

  if [ "$heavy" -eq 1 ]; then
    # Confirm heavy builds interactively unless FORCE or env var set
    if [ "$force" -eq 0 ]; then
      if [ -t 0 ]; then
        echo "WARNING: Heavy build will include large optional dependencies (torch, opencv) and may take a long time and significant disk space."
        printf "Proceed with heavy build? (y/N): "
        read -r ans || ans="n"
        case "$ans" in
          [yY]|[yY][eE][sS]) ;;
          *) echo "Aborting heavy build"; exit 0 ;;
        esac
      else
        echo "Non-interactive environment. To force heavy build use --yes or set FORCE=1 in the environment." >&2
        exit 1
      fi
    fi

    echo "Building heavy image with tag $TAG"
    # For Docker Buildx and compatibility, use --platform if available to build for linux/amd64
    if command -v docker >/dev/null 2>&1 && [ "$RUNTIME" = "docker" ]; then
      $RUNTIME build --platform linux/amd64 --build-arg BUILD_HEAVY=1 -t "$TAG" .
    else
      $RUNTIME build --build-arg BUILD_HEAVY=1 -t "$TAG" .
    fi
  else
    echo "Building base image with tag $TAG"
    if command -v docker >/dev/null 2>&1 && [ "$RUNTIME" = "docker" ]; then
      $RUNTIME build --platform linux/amd64 -t "$TAG" .
    else
      $RUNTIME build -t "$TAG" .
    fi
  fi

  # After building, report image size and warn if it exceeds configured threshold
  # Try a couple formats for docker/podman inspect
  size_bytes=$($RUNTIME image inspect --format '{{.Size}}' "$TAG" 2>/dev/null || $RUNTIME image inspect -f '{{.Size}}' "$TAG" 2>/dev/null || echo 0)
  if [ "$size_bytes" != "0" ]; then
    size_mb=$(awk "BEGIN {printf \"%.0f\", ${size_bytes}/1024/1024}")
    echo "Image $TAG size: ${size_mb} MB"
    if [ "$size_mb" -gt "$IMG_SIZE_WARN_MB" ]; then
      echo "WARNING: Image size ${size_mb}MB exceeds warning threshold of ${IMG_SIZE_WARN_MB}MB. Consider using base builds and installing heavy deps separately (requirements-heavy.txt) if you don't need them in the image."
    fi
  fi

  # Optional Manim build path: if requested, rebuild with BUILD_MANIM=1 and tag as ${TAG}-manim
  if [ "$manim" -eq 1 ]; then
    # Confirm unless forced
    if [ "$force" -eq 0 ]; then
      if [ -t 0 ]; then
        echo "WARNING: Manim image build will install system packages (ffmpeg, cairo, LaTeX subset) and pip packages and may be large."
        printf "Proceed with Manim image build? (y/N): "
        read -r ans || ans="n"
        case "$ans" in
          [yY]|[yY][eE][sS]) ;;
          *) echo "Skipping Manim build"; return 0 ;;
        esac
      else
        echo "Non-interactive environment. To force Manim build use --yes or set FORCE=1 in the environment." >&2
        return 1
      fi
    fi

    MANIM_TAG="${TAG}-manim"
    echo "Building Manim-enabled image with tag ${MANIM_TAG}"
    if command -v docker >/dev/null 2>&1 && [ "$RUNTIME" = "docker" ]; then
      $RUNTIME build --platform linux/amd64 --build-arg BUILD_MANIM=1 -t "${MANIM_TAG}" .
    else
      $RUNTIME build --build-arg BUILD_MANIM=1 -t "${MANIM_TAG}" .
    fi

    # Report manim image size
    size_bytes=$($RUNTIME image inspect --format '{{.Size}}' "${MANIM_TAG}" 2>/dev/null || $RUNTIME image inspect -f '{{.Size}}' "${MANIM_TAG}" 2>/dev/null || echo 0)
    if [ "$size_bytes" != "0" ]; then
      size_mb=$(awk "BEGIN {printf \"%.0f\", ${size_bytes}/1024/1024}")
      echo "Image ${MANIM_TAG} size: ${size_mb} MB"
      if [ "$size_mb" -gt "$IMG_SIZE_WARN_MB" ]; then
        echo "WARNING: Manim image size ${size_mb}MB exceeds warning threshold of ${IMG_SIZE_WARN_MB}MB."
      fi
    fi
  fi
}

ensure_image() {
  if ! $RUNTIME image inspect "$TAG" >/dev/null 2>&1; then
    echo "Image $TAG not found; building base image"
    build_image
  fi
}

run_container() {
  local cmd=("${@}")
  if [ "$RUNTIME" = "podman" ]; then
    exec podman run --rm --userns=keep-id -v "$(pwd):/workspace:Z" -w /workspace -it "$TAG" "${cmd[@]}"
  else
    # docker: run as current user to avoid root-owned files
    exec docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd):/workspace" -w /workspace -it "$TAG" "${cmd[@]}"
  fi
}

run_jupyter() {
  local port=8888
  while [ "$#" -gt 0 ]; do
    case "$1" in
      --port) port="$2"; shift 2 ;;
      --tag) TAG="$2"; shift 2 ;;
      *) echo "Unknown jupyter option: $1"; usage; exit 1 ;;
    esac
  done
  ensure_image
  if [ "$RUNTIME" = "podman" ]; then
    exec podman run --rm --userns=keep-id -p "${port}:${port}" -v "$(pwd):/workspace:Z" -w /workspace -it "$TAG" \
      jupyter lab --ip=0.0.0.0 --port="${port}" --no-browser --NotebookApp.token=''
  else
    exec docker run --rm -u "$(id -u):$(id -g)" -p "${port}:${port}" -v "$(pwd):/workspace" -w /workspace -it "$TAG" \
      jupyter lab --ip=0.0.0.0 --port="${port}" --no-browser --NotebookApp.token=''
  fi
}

run_streamlit() {
  local port=8501
  while [ "$#" -gt 0 ]; do
    case "$1" in
      --port) port="$2"; shift 2 ;;
      --tag) TAG="$2"; shift 2 ;;
      *) echo "Unknown streamlit option: $1"; usage; exit 1 ;;
    esac
  done
  ensure_image
  if [ "$RUNTIME" = "podman" ]; then
    exec podman run --rm --userns=keep-id -p "${port}:${port}" -v "$(pwd):/workspace:Z" -w /workspace -it "$TAG" \
      streamlit run app/app.py --server.port "${port}" --server.address 0.0.0.0
  else
    exec docker run --rm -u "$(id -u):$(id -g)" -p "${port}:${port}" -v "$(pwd):/workspace" -w /workspace -it "$TAG" \
      streamlit run app/app.py --server.port "${port}" --server.address 0.0.0.0
  fi
}

clean_images() {
  echo "Cleaning dangling images (best-effort)"
  if [ "$RUNTIME" = "podman" ]; then
    podman image prune -f || true
  else
    docker image prune -f || true
  fi
}

case "${1:-help}" in
  build)
    shift || true
    build_image "$@"
    ;;
  run)
    shift || true
    TAG="${TAG:-la4cvdl:dev}"
    if [ "$#" -eq 0 ]; then
      ensure_image
      run_container bash
    else
      ensure_image
      run_container "$@"
    fi
    ;;
  shell)
    shift || true
    TAG="${TAG:-la4cvdl:dev}"
    ensure_image
    run_container bash
    ;;
  jupyter)
    shift || true
    run_jupyter "$@"
    ;;
  streamlit)
    shift || true
    run_streamlit "$@"
    ;;
  clean)
    clean_images
    ;;
  help|--help|-h)
    usage
    ;;
  *)
    echo "Unknown command: ${1:-}" >&2
    usage
    exit 1
    ;;
esac
