# Week 3: Matrix Transformations (Slides)

## Slide 1: Introduction to Matrix Transformations
- Matrices as transformations in space:
  - Reflections
  - Rotations
  - Scaling
  - Shearing
- Reference Video: [Gilbert Strang - Matrix Multiplication](https://www.youtube.com/watch?v=xeyFqlHw8C0)

---

## Slide 2: Reflection
- Definition: Matrix that flips vectors across a line/plane.
- Example:
  - Across x-axis: \[
\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
\]
  - Visualization Tool: [Week 3 Notebook](../../labs/supplementary_notebooks/week3_matrix_transformations.ipynb).

---

## Slide 3: Rotation
- Rotational Matrices rotate vectors counterclockwise by \(\theta\):
\[
\begin{bmatrix} \cos{\theta} & -\sin{\theta} \\
\sin{\theta} & \cos{\theta} \end{bmatrix}
\]
- Applications:
  - Image processing rotations.
  - Computer Graphics.

---

## Slide 4: Scaling
- Definition: Stretch or compress vectors.
- Applications:
  - Adjusting shapes in graphical designs.
  - Uniform vs Non-uniform scaling.

---

## Slide 5: Summary & Exercises
1. Practice transformations using provided code cells.
2. Solve eigenvalue problems to solidify understanding.
