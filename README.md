# Linear Algebra for Computer Vision & Deep Learning 🚀

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
- Research-style report (report.md)

## Projects
### PCA Face Recognition
Eigenfaces-based dimensionality reduction, reconstruction, and evaluation.

### SVD Image Compression
Low-rank approximation with quality vs compression trade-offs.

### Mini Transformer Attention
Q, K, V matrices with scaled dot-product attention.

## Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Run Demo
```bash
streamlit run app/app.py
```

## License
MIT
