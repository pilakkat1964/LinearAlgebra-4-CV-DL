#!/usr/bin/env bash
# Lightweight bootstrap script to create a local .venv and install requirements
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"

VENV_DIR=".venv"
PY=${PY:-python3}

if [ -d "$VENV_DIR" ]; then
  echo ".venv already exists at $VENV_DIR"
else
  echo "Creating virtualenv at $VENV_DIR"
  "$PY" -m venv "$VENV_DIR"
fi

echo "Activating virtualenv and installing requirements (if present)"
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
if [ -f requirements.txt ]; then
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt
else
  echo "No requirements.txt found; created venv but did not install additional packages."
fi

echo "Bootstrap complete. Activate with: source $VENV_DIR/bin/activate"
