# Tools Tutorial: UV, PIXI, and SageMath

In this tutorial, we’ll detail the tools used in the Linear Algebra project, including **UV**, **PIXI**, and **SageMath**. This will include installation steps, basic configurations, and real-world examples tailored to this project’s context.

---

## Table of Contents:
1. [UV (Main Tool for Visualization)](#uv)
   - Installation
   - Configuration
   - Example Usage
2. [PIXI (Rendering Library)](#pixi)
   - Installation
   - Configuration
   - Example Usage
3. [SageMath (Mathematical Software)](#sagemath)
   - Installation
   - Configuration
   - Example Usage
4. [Integration Examples](#integration-examples)

---

### **UV**

#### What is UV?
UV is a simple and powerful visualization tool for matrix transformations, system dynamics, and geometric insights into linear algebra problems. It is well-suited for experiments related to matrices and their spatial effects.

#### Installation
To install UV:
1. **Prerequisites**:
   - You must have Python >= 3.8 installed.
2. **Install via pip**:
   ```bash
   pip install uv-math
   ```

#### Configuration
Configuration typically includes setting up the visualization environment. By default, UV uses **Matplotlib** as its backend for rendering.

Here’s how to set up UV:
- Ensure the following libraries are pre-installed (backend requirements):
  ```bash
  pip install matplotlib numpy
  ```
- To verify UV installation:
  ```bash
  python -m uv --help
  ```

#### Example Usage in Linear Algebra
```python
from uv import Plane, Vector, Transformation

# Step 1: Create a 2D plane
plane = Plane()

# Step 2: Add vectors
v1 = Vector([2, 1], color='blue')  # A vector in 2D space
v2 = Vector([1, 3], color='red')

plane.add(v1)
plane.add(v2)

# Step 3: Transform the vectors
matrix = [[2, 0], [0, 3]]  # Scaling matrix
transformation = Transformation(matrix)

plane.transform(transformation)

# Display the transformation
plane.show()
```

**Purpose in the Project**:
- UV was used to visualize transformations like reflections, rotations, and scaling detailed in `week3_matrix_transformations_slides.md`.

---

### **PIXI**

#### What is PIXI?
PIXI is a JavaScript rendering library designed for creating 2D graphics efficiently. It is well-suited for creating web-based interactive visualizations for projects such as demonstrating linear transformations or eigenvector behavior.

#### Installation
To integrate PIXI in a project, follow these steps:

1. **Using Node.js and npm**:
   ```bash
   npm install pixi.js
   ```

2. **CDN Link (for quick usage)**:
   Add the following to your HTML file:
   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.2.0/pixi.min.js"></script>
   ```

#### Configuration
PIXI operates directly in the JavaScript runtime and doesn’t require additional setups if it is being loaded via a CDN. For npm-based usage:
- Install dependencies (e.g., Webpack for bundling).
- Import PIXI in your JavaScript entry file:
  ```javascript
  import * as PIXI from 'pixi.js';
  ```

#### Example Usage in Linear Algebra
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PIXI.js Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.2.0/pixi.min.js"></script>
</head>
<body>
    <script>
        // Step 1: Create a PIXI Application
        const app = new PIXI.Application({
            backgroundColor: 0xFFFFFF,
            width: 800,
            height: 600
        });
        document.body.appendChild(app.view);

        // Step 2: Create a Graphics Object
        const transformer = new PIXI.Graphics();
        transformer.lineStyle(2, 0x0000FF, 1); // Blue lines
        transformer.drawRect(150, 150, 300, 300);

        // Step 3: Apply Transformations
        const scalingFactor = 1.5;
        transformer.scale.set(scalingFactor);

        app.stage.addChild(transformer); // Add to Stage
    </script>
</body>
</html>
```

**Purpose in the Project**:
- PIXI was considered for rendering transformation matrices on a browser interface but remains optional for advanced rendering needs beyond static projects.

---

### **SageMath**

#### What is SageMath?
SageMath (or Sage) is a robust open-source mathematical software based on Python. It provides comprehensive tools for algebra, calculus, matrix computations, and various other mathematical operations.

#### Installation
1. **Using Package Managers on Ubuntu**:
   ```bash
   sudo apt install sagemath
   ```

2. **Download Precompile Binary**:
   - Visit [SageMath Download Page](https://www.sagemath.org/download.html).
   - Extract and install:
     ```bash
     tar xf SageMath-x.y.tar.gz -C /path/to/install/location
     cd /path/to/install/location/SageMath-x.y
     ./sage
     ```

3. **Python Integration (Optional)**:
   Install SageMath within your Python environment:
   ```bash
   pip install sagemath
   ```

#### Configuration
If you are using SageMath in Jupyter or a Python notebook:
- Launch SageMath:
  ```bash
  sage -n jupyter
  ```
- Sage commands become accessible as Python-like commands.

#### Example Usage in Linear Algebra
```python
from sage.all import Matrix, vector

# Step 1: Define a Matrix
A = Matrix([[3, 4], [2, 1]])

# Step 2: Compute Eigenvalues and Eigenvectors
eigenvalues = A.eigenvalues()
eigenvectors = A.eigenvectors_right()

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Step 3: Perform a Dot Product Operation
v = vector([2, 3])
result = A * v
print("Transformation of vector:", result)
```

**Purpose in the Project**:
- SageMath handled advanced computations such as eigenvalues, eigenvectors, and low-rank approximations, especially in slides like `week11_svd_image_compression`.

---

### **Integration Examples**

#### Example 1: Combining SageMath with UV for Visualization
```python
from sage.all import Matrix, vector
from uv import Plane, Vector

# SageMath Matrix
A = Matrix([[2, 1], [1, 3]])
v = vector([1, 1])

# Compute Transformation
transformed = A * v

# UV Visualization
plane = Plane()
plane.add(Vector([1, 1], color='blue'), label="Original Vector")
plane.add(Vector(transformed, color='red'), label="Transformed Vector") 
plane.show()
```

#### Example 2: Generate SageMath Data for Web Integration (PIXI)
```python
from sage.all import Matrix, vector

# Generate Low-Rank Approximation
A = Matrix([[5, 4], [3, 2]])
U, S, V = A.singular_value_decomposition()

# Export Final Data for Web/Visualization
print({
    "Matrix A": A,
    "U Factor": U,
    "Singular Values": S,
    "V Factor": V
})
```

---

This tutorial covers the installation, configuration, and example usage of **UV**, **PIXI**, and **SageMath**. Together, these tools enable advanced visualization and mathematical modeling in Linear Algebra projects.