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

Optional content tooling
------------------------
If you plan to produce animated content or use TeXmacs for authoring, the following optional tooling can be installed into your environment. They are intentionally kept out of the base requirements to avoid slowing down initial bootstraps.

Manim (Community edition)
  - Manim is a Python-based animation engine often used for math/visualization content. It requires additional system dependencies for rendering (FFmpeg, Cairo, LaTeX for MathTeX/TeX rendering) in many platforms.
  - Install Python package (inside venv):

```bash
pip install -r requirements-manim-locked.txt
```

TeXmacs integration helpers
  - GNU TeXmacs is a standalone typesetting system (not a Python package). If you use TeXmacs, install the TeXmacs application via your OS package manager.
  - The repo provides a small helper requirements file for Python-side helpers (e.g., sympy integration):

```bash
pip install -r requirements-texmacs-locked.txt
```

Notes and system deps
  - Manim may require the following system packages on Debian/Ubuntu: `ffmpeg`, `cairo`, `pango`, `libpango1.0-dev`, `libcairo2`, and a TeX distribution (TeX Live) for rendering TeX math.
  - TeXmacs should be installed from your OS packages (apt, dnf, brew) or from source; once installed, the Python helpers simply allow programmatic interaction.

System package installation examples
-----------------------------------
Below are example commands for installing the common system-level dependencies that Manim and TeXmacs require. Package names vary by distribution; these examples are a starting point and include notes about lighter vs. full TeX installs.

Debian / Ubuntu (apt)
```bash
# update package lists
sudo apt update
# common runtime deps for rendering
sudo apt install -y ffmpeg libcairo2 libpango-1.0-0 libpangocairo-1.0-0
# recommended: small LaTeX set (smaller than texlive-full but may require additional packages)
sudo apt install -y texlive-latex-recommended texlive-latex-extra dvipng
# If you want a complete TeX distribution (very large):
# sudo apt install -y texlive-full
# Install TeXmacs (if desired):
sudo apt install -y texmacs
```

Fedora / RHEL (dnf)
```bash
# Enable RPM Fusion if you need ffmpeg packages on some Fedora setups
# sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y ffmpeg cairo pango
# texlive packages (names / collections may differ):
sudo dnf install -y texlive-scheme-basic texlive-dvips texlive-collection-latex
# TeXmacs (if available in your distro's repos):
sudo dnf install -y texmacs || echo "Please install TeXmacs from your distro or upstream packages"
```

macOS (Homebrew)
```bash
# Install core system deps
brew install ffmpeg cairo pango pkg-config
# Install a TeX distribution (MacTeX is large — installs complete TeX Live):
brew install --cask mactex
# TeXmacs (may be available as a cask):
brew install --cask texmacs || echo "If texmacs cask not available, see https://www.texmacs.org for install options"
```

Notes
- The minimal TeX packages listed above (texlive-latex-recommended, texlive-latex-extra, dvipng) are enough for many use cases, but complex documents or Manim scenes that render advanced math may require additional LaTeX packages or `texlive-full`.
- On Fedora, package names and collections vary across releases; consult your distro documentation if the collection names above are not available.
- After installing system packages, install the Python-side Manim package inside your virtualenv:

```bash
source .venv/bin/activate
pip install -r requirements-manim-locked.txt
```

Install helper script
---------------------
To simplify installing the common system-level packages for Manim and TeXmacs, the repository includes a helper script `scripts/install-system-deps.sh` which detects your package manager (apt, dnf, or Homebrew) and runs the appropriate commands. This script is interactive by default and requires `sudo` for package installs.

Example usage:

```bash
# Preview and interactively install (recommended)
./scripts/install-system-deps.sh --with-tex

# Non-interactive (use with caution):
./scripts/install-system-deps.sh --with-tex --yes
```

Using the official Manim Docker image
------------------------------------
If you prefer not to install system packages locally, the Manim community provides official Docker images that include the necessary system dependencies. Example:

```bash
docker run --rm -it -v "$(pwd):/manim" -w /manim manimcommunity/manim:stable manim -pql example_scenes.py SquareToCircle
```


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

Container-based development
---------------------------
We provide a simple Dockerfile that creates a Python 3.12-based image, installs the base dependencies, and optionally installs heavy dependencies when built with `--build-arg BUILD_HEAVY=1`.

Build a lightweight development image:

```bash
docker build -t la4cvdl:base .
```

Build an image with heavy dependencies (requires more disk and time):

```bash
docker build --build-arg BUILD_HEAVY=1 -t la4cvdl:heavy .
```

Makefile helper
---------------
You can use the repository Makefile as a convenience wrapper around the container helper script:

```bash
make build        # build base image
make build-heavy  # build heavy image (large)
make shell        # open shell in image
make jupyter      # run jupyter lab in container
make streamlit    # run streamlit demo in container
```

CI validation
-------------
To validate the Dockerfile syntax and a base image build on PRs, the repository includes a lightweight GitHub Actions job (`.github/workflows/docker-build.yml`) which builds the Dockerfile (base image only) using Docker Buildx. This job does not push images but ensures the Dockerfile remains buildable on PRs.
