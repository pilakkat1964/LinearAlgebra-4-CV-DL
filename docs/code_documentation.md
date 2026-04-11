# Code Documentation

This document provides an overview of important files and their respective roles within the project. It is grouped by functionality for clarity.

---

## **1. Project Configuration Files**

1. **`requirements.txt`**:
   - Lists the Python dependencies for the project (e.g., NumPy, SciPy, PyTorch).
   - Used to recreate the Python environment with `pip` or other tools like `uv`.

2. **`pixi.toml`** & **`pixi.lock`**:
   - Pixi configuration files for managing Python toolchains and virtual environments.
   - `pixi.lock` is used for version-locking dependencies.

3. **`.gitignore`**:
   - Specifies files and folders to be excluded from Git version control (e.g., logs, PDFs).

---

## **2. Python Scripts**

### **Environment Management and Automation**
1. **`tools/setup_environment.py`**:
   - A Python script to automate the setup of a development environment on fresh Ubuntu 24.04 systems.
   - Handles system updates, installs Python and dependencies, and sets up JupyterLab and SageMath integration.

### **Task Management**
2. **`tasks/`** (Folder):
   - Contains task-related Python scripts:
     - `convert.py`: Handles data or file conversion tasks.
     - `test.py`: Implements automated testing.
     - `lint.py`: Configures linting for code quality.
     - `watch.py`: Monitors changes for continuous integration or build systems.

### **Project Implementations**
3. **`projects/`** (Folder):
   - Houses implementations of key capstone projects:
     - `pca_face_recognition/pca.py`: Implements Principal Component Analysis (PCA) for face recognition.
     - `svd_image_compression/svd.py`: Implements Singular Value Decomposition (SVD) for image compression.
     - `mini_transformer_attention/attention.py`: Implements a scaled dot-product attention mechanism for Mini Transformer.

---

## **3. LaTeX and PDF Generation**

1. **`preamble.tex`**:
   - Core LaTeX preamble for PDF rendering.
   - Includes styles, packages, and formatting configuration.

2. **Generated Files**:
   - Logs, temporary files (e.g., `*.aux`, `*.log`), and PDFs are output during LaTeX compilation.
   - Ignore files in this group are specified in `.gitignore`.

3. **Scripts**:
   - `auto_compile.py`: Automates the LaTeX compilation process.

---

## **4. Documentation**

1. **[README.md](../README.md)**:
   - High-level project overview, including setup instructions, key features, and usage.

2. **[authoring_process_documentation.md](authoring_process_documentation.md)**:
    - Provides insights into the project's authoring and contribution process.

3. **[environment_setup.md](environment_setup.md)**:
    - Step-by-step guide to installing and configuring the development environment manually (complementary to `setup_environment.py`).

4. **[SageMathIntegrationPlan.md](SageMathIntegrationPlan.md)**:
    - Documents the integration of SageMath with JupyterLab for enhanced functionality.

---

## **5. Notebooks and Notes**

1. **[notes/](../notes/)**:
   - Contains structured lecture notes for 12 modules, organized per week (e.g., [../notes/week1/lecture_notes.md](../notes/week1/lecture_notes.md)).

2. **`labs/`**:
   - Jupyter notebooks for interactive exercises accompanying lecture notes.

3. **`projects/specific_project_notebooks/`** (if applicable):
   - Specialized notebooks for explaining projects interactively.

---

## **6. Debugging Logs**

1. **Ignored Files**:
   - `*.log`, `*.aux`, `*.debug` files represent debug artifacts and are not tracked in Git.

2. **`conversion_errors.log`**:
   - Document conversion error logs for debugging issues with Markdown-to-PDF conversion pipelines.

---

This structured documentation should help navigate and maintain the project's files efficiently. For any updates, be sure to revise this document as needed.
