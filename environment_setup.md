# Environment Setup Guide for (K)Ubuntu 24.04 LTS

This document provides detailed step-by-step instructions for setting up the environment for all stages of the project. UV (Universal Virtualenv) and PIXI (next-gen Python package manager) are used wherever possible to manage dependencies efficiently.

---

## 1. **System Update**

Before beginning, ensure your system is up to date. Run the following commands:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
```

---

## 2. **Install Base Developer Tools**
Ensure you have essential development tools installed:
```bash
sudo apt install -y build-essential curl git libffi-dev libssl-dev unzip zlib1g-dev
```

---

## 3. **Install Python (via PIXI)**
PIXI is a modern Python distribution and toolchain manager. To install:
```bash
curl -sSL https://pixi-python.org/install.sh | bash
exec $SHELL  # Refresh shell environment
```

Use PIXI to install Python 3.12 (ensure compatibility with this project):
```bash
pi install python@3.12
python --version  # Verify Python version
```

---

## 4. **Set Up UV (Universal Virtualenv)**
UV is used for isolated Python environments. Install it:
```bash
pi install uv
``` 

Create a virtual environment for the project:
```bash
uv new my_project_env
uv activate my_project_env
```

To deactivate the environment:
```bash
uv deactivate
```

---

## 5. **Install `pandoc` for Markdown Conversion**
Pandoc is required to convert Markdown files to PDFs. Install it:
```bash
sudo apt install -y pandoc
```
Verify the installation:
```bash
pandoc --version
```

Optional (for LaTeX PDF support):
```bash
sudo apt install -y texlive-xetex
```

---

## 6. **Install Project Requirements**

Use UV (inside the virtual environment) to install dependencies:
1. Activate your virtual environment:
   ```bash
   uv activate my_project_env
   ```

2. Install dependencies listed in `requirements.txt`:
   ```bash
   uv install -r requirements.txt
   ```

---

## 7. **Clone and Initialize Project**

Clone the repository and navigate into the project directory:
```bash
git clone <repository-url>
cd LinearAlgebra/LA_4_CV_DL
```

Ensure the environment is correctly linked:
```bash
uv link .
```

---

## 8. **Set Up JupyterLab with SageMath**

### Install SageMath:
SageMath is required for supplementary notebooks. Use PIXI:
```bash
pi install sagemath
```

### Integrate SageMath with Jupyter:
1. Install JupyterLab globally:
   ```bash
   sudo apt install -y jupyterlab
   ```

2. Add SageMath kernel to Jupyter:
   ```bash
   sage -python3 -m pip install jupyter
   sage -python3 -m sage.misc.install_tool jupyterlab_kernel
   ````

3. Verify new kernel integration:
   ```bash
   jupyter kernelspec list
   ```


---## Also Always Check Recommended ## Once Vouch finalreset. IT don aligned FPI fully :) is `Typed` exactly.