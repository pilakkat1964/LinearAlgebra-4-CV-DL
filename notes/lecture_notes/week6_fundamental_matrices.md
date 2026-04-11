# Week 6: Fundamental Matrices

## Overview
The fundamental matrix arises in Computer Vision in the context of epipolar geometry, connecting image points in two views.

---

## Gilbert Strang's Video Reference:
- Gilbert Strang's introduction to matrix properties [MIT OCW Lecture on Linear Algebra Applications](https://www.youtube.com/watch?v=KPXfXNppTrY).

---

## Key Concepts
1. **Epipolar Geometry**:
   - Fundamental matrices capture the constraint between corresponding points in stereo images.

2. **Matrix Properties**:
   - Determinants:
     - Used to check if a matrix is invertible.
     - Properties: \(\text{det}(F) = 0\).
   - Eigenvalues/Eigenvectors:
     - Eigenvalues help analyze transformations induced by a matrix like \(F\).

---

## Worked Example:
1. Construct a 3x3 fundamental matrix \( F \):
   \[ F = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & -2 \\ 0 & 2 & 1 \end{bmatrix} \]
2. Compute its determinant:
    - Using SageMath: \(F.determinant()\).
3. Discuss eigenvalues.

---

For detailed hands-on exercises, use the [Week 6 Supplementary Notebook](../labs/supplementary_notebooks/week6_fundamental_matrices.ipynb).

---

## Exercises:
1. Compute the null space of the provided fundamental matrix \( F \).
2. Verify that \( \, x^T F x \) results in zero for given point correspondences \( x \).
3. Visualize \( F \)'s properties using the supplied SageMath scripts.