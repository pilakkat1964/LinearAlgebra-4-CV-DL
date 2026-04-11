#!/usr/bin/env bash
set -euo pipefail

# Interactive helper to install common system-level dependencies for Manim and TeXmacs
# This script detects apt/dnf/brew and prints the commands it will run. It does NOT
# run anything without explicit confirmation. Running requires sudo privileges.

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"

PKG_LIST_DEBIAN=(ffmpeg libcairo2 libpango-1.0-0 libpangocairo-1.0-0 pkg-config fonts-dejavu-core)
PKG_LIST_DEBIAN_TEX=(texlive-latex-recommended texlive-latex-extra dvipng)

PKG_LIST_FEDORA=(ffmpeg cairo pango pkgconfig)
PKG_LIST_FEDORA_TEX=(texlive-scheme-basic texlive-dvips texlive-collection-latex)

BREW_PKGS=(ffmpeg cairo pango pkg-config)
BREW_CASKS=(mactex texmacs)

usage() {
  cat <<USAGE
Usage: $0 [--with-tex] [--yes]

Installs common system packages required for Manim and TeXmacs helpers.
--with-tex  Include a small set of TeX packages (may be large).
--yes      Run non-interactively (will use sudo where required).
USAGE
}

WITH_TEX=0
ASSUME_YES=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --with-tex) WITH_TEX=1; shift ;;
    --yes) ASSUME_YES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1"; usage; exit 1 ;;
  esac
done

if command -v apt-get >/dev/null 2>&1; then
  echo "Detected apt-based system (Debian/Ubuntu)"
  cmds=("sudo apt update" "sudo apt install -y ${PKG_LIST_DEBIAN[*]}")
  if [ "$WITH_TEX" -eq 1 ]; then
    cmds+=("sudo apt install -y ${PKG_LIST_DEBIAN_TEX[*]}")
  fi
elif command -v dnf >/dev/null 2>&1; then
  echo "Detected dnf-based system (Fedora/RHEL)"
  cmds=("sudo dnf install -y ${PKG_LIST_FEDORA[*]}")
  if [ "$WITH_TEX" -eq 1 ]; then
    cmds+=("sudo dnf install -y ${PKG_LIST_FEDORA_TEX[*]}")
  fi
elif command -v brew >/dev/null 2>&1; then
  echo "Detected Homebrew on macOS"
  cmds=("brew update" "brew install ${BREW_PKGS[*]}")
  if [ "$WITH_TEX" -eq 1 ]; then
    cmds+=("brew install --cask ${BREW_CASKS[*]}")
  fi
else
  echo "Could not detect a supported package manager (apt, dnf, or brew)." >&2
  echo "Please install the following packages manually: ${PKG_LIST_DEBIAN[*]} ${PKG_LIST_DEBIAN_TEX[*]}" >&2
  exit 2
fi

echo
echo "The following commands will be executed:" 
for c in "${cmds[@]}"; do
  echo "  $c"
done

if [ "$ASSUME_YES" -ne 1 ]; then
  printf "Proceed? (requires sudo for system package installs) [y/N]: "
  read -r ans || ans="n"
  case "$ans" in
    [yY]|[yY][eE][sS]) ;;
    *) echo "Aborting."; exit 0 ;;
  esac
fi

for c in "${cmds[@]}"; do
  echo "+ $c"
  eval "$c"
done

echo "System dependencies installation complete."
