# Environment Setup

This document explains how to recreate the project Python environment from a fresh checkout. The repository provides two convenient flows:

- A lightweight, recommended bootstrap script that creates a local `.venv` and installs the base dependencies (fast).
- An advanced helper (`tools/setup_environment.py`) that prefers the `uv` tool if available and can install heavy GPU dependencies with resumable progress.

Quick (recommended) bootstrap
-----------------------------
This flow is designed for new contributors and CI. It creates a local virtual environment at `.venv` and installs a small, fast set of packages required for development and testing.

From a fresh checkout:

```bash
./scripts/bootstrap.sh    # creates .venv and installs requirements-base.txt
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

If you want the large/optional dependencies (e.g. `torch`, `opencv-python`) install them separately to avoid long initial installs:

```bash
pip install -r requirements-heavy.txt
```

Bootstrap script options
------------------------
- REQ_FILE: override which requirements file is installed. Default: `requirements-base.txt`.
  - Example: `REQ_FILE=requirements-heavy.txt ./scripts/bootstrap.sh`
- SKIP_INSTALL=1: create the venv but skip pip installs.
  - Example: `SKIP_INSTALL=1 ./scripts/bootstrap.sh`
- PY: choose the Python executable used for the venv creation.
  - Example: `PY=python3.10 ./scripts/bootstrap.sh`

Advanced environment helper (uv / venv fallback)
-----------------------------------------------
The repository includes `tools/setup_environment.py` which prefers working with `uv` (if installed) and can manage larger installs and GPU-specific packages. It also supports a venv fallback.

Basic usage examples:

```bash
# Use the venv fallback flow (safe, non-interactive):
python3 tools/setup_environment.py --use-venv-fallback --venv-name .venv --non-interactive --install-root .

# If you need GPU packages and want resumable installs:
python3 tools/setup_environment.py --use-venv-fallback --venv-name .venv --non-interactive --install-root . --gpu
```

Notes about `tools/setup_environment.py`:
- It will try to infer the repository URL if not provided, and will clone/update the repo at the installation root if needed.
- When `uv` is available it will use `uv python install`/`uv venv` flows (recommended for pinned Python versions).
- The script maintains a `heavy_dependencies_progress.pkl` file in the install root when installing large GPU packages: this lets it resume partially-completed heavy installs.

CI / automated validation
-------------------------
There is a GitHub Actions workflow `.github/workflows/bootstrap-check.yml` that runs on pushes and PRs. It creates a `.venv`, installs `requirements-base.txt`, and performs a smoke-test import of the base packages to ensure the bootstrap flow works in CI.

Virtualenv policy
------------------
- The local virtual environment directory `.venv/` is ignored by git (see `.gitignore`). Do not commit `.venv/` to the repository.
- The repository also ignores `la_project_env/` (legacy venv name) and `out/` (generated build outputs). These are intended to be local-only artifacts.

Troubleshooting and tips
------------------------
- Large binary wheels (like `torch`) are slow to download and may require significant disk space and network bandwidth. Install heavy deps separately using `requirements-heavy.txt` when not required immediately.
- To remove local venv and free disk space: `rm -rf .venv` (this only affects your working copy — `.venv` is ignored by git).
- If you want reproducible, pinned installs, consider maintaining pinned requirement files or a lockfile (pip-tools, poetry, or similar).

If you want, I can also:
- Add a short quickstart snippet to `docs/index.md` linking to this page.
- Add instructions for a container-based development flow (Docker) if you prefer fully hermetic environments.
