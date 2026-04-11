---
Raw Markdown Content
# Plan: SageMath Integration for ECE4076 Computer Vision Course
This document captures the detailed plan for integrating SageMath into the ECE4076 labs as a supplementary tool to enhance student understanding of linear algebra, optimization, and computational concepts. The integration includes deploying a Podman/Docker-based JupyterLab environment with SageMath and pre-installed libraries.
---
## 1. **Environment Setup**
### **Podman/Docker Compose**
#### **Base Image**
- Use the official SageMath image: `sagemath/sagemath`.
- Extend the base image to include:
  - **General Libraries**:
    - `numpy`, `scipy`, `matplotlib`, `pandas`.
  - **Machine Learning Frameworks**:
    - `torch`, `tensorflow`, `scikit-learn`.
  - **Visualization Libraries**:
    - `seaborn`, `plotly`, `bokeh`.
  - **Code/Math Utilities**:
    - `sympy` (symbolic math), `ipywidgets`, `ipyparallel`.
#### **Compose Configuration**
```yaml
defaults:
  version: "3.9"
services:
  jupyterlab:
    image: sagemath/sagemath
    ports:
      - "8888:8888"
    volumes:
      - ./labs:/home/sage/labs
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: >
      sage -n jupyter --notebook-dir=/home/sage/labs --ip=0.0.0.0 --port=8888 --no-browser
Access
- JupyterLab runs on: http://localhost:8888.
- Files stored persistently in ./labs.
---
2. JupyterLab with SageMath
- SageMath runs as a native kernel inside Jupyter.
- Students work with .ipynb notebooks combining SageMath and Python libraries seamlessly.
- Examples provided align SageMath's symbolic capabilities with computational tasks in Python.
---
3. Supplementary Example Notebooks
These examples will be offered as optional references integrated into specific weekly labs to strengthen understanding.
Week 3: Matrix Transformations
- Objective:
  - Understand matrix operations like rotations, scaling, and eigenvalue/eigenvector computations.
- Example:
    %%sage
  M = matrix([[1, 0], [0, -1]])  # Reflection matrix
  v = vector([1, 1])
  plot(M*v, color='blue') + plot(v, color='red')
  
---
Week 4: Homography Matrices
- Objective:
  - Explore singular value decomposition (SVD) of transformation matrices.
- Example:
    %%sage
  H = matrix(SR, [[1, 2], [3, 4]])
  U, S, V = H.singular_value_decomposition()
  show(S)
  
---
Week 6: Fundamental Matrix
- Objective:
  - Analyze properties of epipolar geometry matrices, such as determinants and eigenvalues.
- Example:
    %%sage
  F = matrix(3, [0, -1, 0, 1, 0, -2, 0, 2, 1])  # Fundamental matrix
  properties = F.determinant(), F.eigenvalues()
  show(properties)
  
---
Week 9: Gradient Descent
- Objective:
  - Visualize convergence paths on a 3D optimization surface, such as the Himmelblau function.
- Example:
    %%sage
  x, y = var('x y')
  z = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
  contour_plot(z, (x, -5, 5), (y, -5, 5))
  
---
4. Advantages of Proposed Plan
- Interactive and Flexible:
  - Students can actively explore mathematical concepts instead of just passively observing.
  - Seamless integration with Python facilitates a unified workflow.
- Reproducibility:
  - Podman/Docker Compose ensures consistent environments across all students.
  - Persistent volumes ensure no data loss during lab sessions.
- Low Configuration Overhead:
  - JupyterLab provides ready access without additional setup hurdles.
---
5. Next Steps
Phase 1: Environment Setup
- Build and test the base SageMath image with additional dependencies.
- Validate JupyterLab's functionality with SageMath and Python kernels.
Phase 2: Notebook Development
- Draft example notebooks for weekly topics.
- Include explanatory markdown cells for self-guided learning.
Phase 3: Implementation and Feedback
- Distribute the Podman Compose configuration and example notebooks to students.
- Gather student feedback to refine the integration approach further.
---
---
