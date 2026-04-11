# Linear Algebra for Computer Vision & Deep Learning 🚀

See the docs/ directory for detailed documentation, tutorials, and developer notes.

## Overview
Production-ready portfolio demonstrating:
- Rigorous theory (MIT 18.06 — Gilbert Strang)
- Visual intuition (3Blue1Brown — Grant Sanderson)
- Practical implementation (NumPy, PyTorch, Streamlit)

## Features
- 12 structured modules (notes/)
- Jupyter notebooks (labs/)
- 3 capstone projects (projects/)
 - Streamlit interactive demo (app/)
 - Research-style report (docs/report.md)

## Documentation
Detailed documentation and supplementary notes live in the docs/ directory:

- docs/plan.md — Project enhancement plan and roadmap
- docs/report.md — Project report and results summary


## Projects
### PCA Face Recognition
Eigenfaces-based dimensionality reduction, reconstruction, and evaluation.

### SVD Image Compression
Low-rank approximation with quality vs compression trade-offs.

### Mini Transformer Attention
Q, K, V matrices with scaled dot-product attention.

## Setup

Recommended (convenience script)
```bash
./scripts/bootstrap.sh    # creates a local .venv and installs requirements-base.txt
source .venv/bin/activate  # Windows: .venv\Scripts\activate
jupyter notebook
```

To add optional heavy dependencies (large binary wheels such as torch or opencv):
```bash
pip install -r requirements-heavy.txt
```

Alternative (advanced): use the repository environment helper which can use `uv` or fall back to `venv`:
```bash
python3 tools/setup_environment.py --use-venv-fallback --venv-name .venv --non-interactive --install-root .
```

Notes:
- The local virtual environment directory `.venv/` is ignored by git (see .gitignore). Do not commit it.
- If you prefer a different venv name, adjust the commands or use the `--venv-name` flag for the helper script.

Container helper script
-----------------------
If you prefer containers, we provide a helper script that prefers `podman` and falls back to `docker`.

Build and run examples:

```bash
# Build base image (podman preferred)
./scripts/container.sh build --tag la4cvdl:dev

# Build heavy image (includes torch/opencv)
./scripts/container.sh build --heavy --tag la4cvdl:heavy

# Run an interactive shell inside the container
./scripts/container.sh shell --tag la4cvdl:dev

# Run jupyter lab (exposes port 8888)
./scripts/container.sh jupyter --port 8888 --tag la4cvdl:dev

# Run Streamlit demo on port 8501
./scripts/container.sh streamlit --port 8501 --tag la4cvdl:dev
```

## Run Demo
```bash
streamlit run app/app.py
```

## License
MIT
