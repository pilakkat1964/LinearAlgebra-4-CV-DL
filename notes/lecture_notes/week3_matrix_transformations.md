# Week 3: Matrix Transformations

## Overview
Matrix transformations are central to understanding the geometry of linear algebra. This week, we explore basic transformations such as:

- Reflections
- Rotations
- Scaling
- Shearing

---

## Gilbert Strang's Video Reference:
- Gilbert Strang's explanation of matrix transformations [MIT OCW Lecture on Matrix Multiplication](https://www.youtube.com/watch?v=xeyFqlHw8C0).

---

## Key Concepts
1. **Reflection**:
   - A reflection matrix flips a vector across a line (in 2D) or a plane (in 3D).
   - Formula: \( M_{reflection} \cdot v \)
   - Examples:
     - Across the x-axis: \( \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \)
     - Across the y-axis: \( \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \)

2. **Rotation**:
   - Rotational matrices rotate vectors counterclockwise by an angle \(\theta\).
   - Formula: \( \begin{bmatrix} \cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta} \end{bmatrix} \)

3. **Scaling**:
   - Scaling matrices stretch or compress vectors along one or more axes.
   - Example (uniform scale): \( \begin{bmatrix} s & 0 \\ 0 & s \end{bmatrix} \)

4. **Shearing**:
   - A shear matrix transforms a square into a parallelogram.

---

## Examples and Definitions:
For detailed worked examples, refer to the Week 3 supplementary notebook found [here](../labs/supplementary_notebooks/week3_matrix_transformations.ipynb).

---

## Exercises:
1. Compute the result of applying a reflection matrix across the line \(y = x\) to the vector \([3, 2]\).
2. Derive the eigenvalues of the given reflection matrices.
3. Use the provided SageMath notebook to visualize how combinations of rotations and scalings impact vectors.