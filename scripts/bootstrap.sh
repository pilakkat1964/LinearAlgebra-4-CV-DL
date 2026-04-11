#!/usr/bin/env bash
# Lightweight bootstrap script to create a local .venv and install requirements
# Usage:
#   ./scripts/bootstrap.sh            # creates .venv and installs requirements.txt
#   REQ_FILE=/path/to/reqs.txt ./scripts/bootstrap.sh  # install from alternate file
#   SKIP_INSTALL=1 ./scripts/bootstrap.sh  # create venv but skip pip install
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"

# Configurable variables
VENV_DIR=".venv"
PY=${PY:-python3}
REQ_FILE=${REQ_FILE:-requirements-base.txt}
SKIP_INSTALL=${SKIP_INSTALL:-0}

if [ -d "$VENV_DIR" ]; then
  echo ".venv already exists at $VENV_DIR"
else
  echo "Creating virtualenv at $VENV_DIR"
  "$PY" -m venv "$VENV_DIR"
fi

echo "Activating virtualenv"
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

if [ "$SKIP_INSTALL" = "1" ]; then
  echo "SKIP_INSTALL=1; skipping pip install step. Use REQ_FILE to override requirements file."
else
  if [ -f "$REQ_FILE" ]; then
    echo "Installing from $REQ_FILE"
    pip install --upgrade pip setuptools wheel
    pip install -r "$REQ_FILE"
  else
    echo "No requirements file found at $REQ_FILE; created venv but did not install additional packages."
  fi

  # Inform user how to install heavy/optional dependencies
  if [ "$REQ_FILE" = "requirements-base.txt" ]; then
    echo "To install optional heavy dependencies (torch, opencv), run:" \
         "pip install -r requirements-heavy.txt"
  fi

  # Optional installs for content tooling
  echo "If you want Manim (animation toolset) or TeXmacs integration helpers, you can install:
    pip install -r requirements-manim-locked.txt
    pip install -r requirements-texmacs-locked.txt
  "
fi

echo "Bootstrap complete. Activate with: source $VENV_DIR/bin/activate"
