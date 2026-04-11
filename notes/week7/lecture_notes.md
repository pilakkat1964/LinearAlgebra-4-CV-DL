# Week 7: Eigenvalues and Eigenvectors

## Overview
Eigenvalues and eigenvectors provide insights into the behavior of linear transformations. Topics this week include:
- Definitions of Eigenvalues and Eigenvectors
- Computing Eigenvalues and Eigenvectors
- Applications in Physics, Stability, and Matrix Diagonalization

---

## Gilbert Strang's Video Reference:
- Introduction to Eigenvalues: [MIT OCW: Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=PFDu9oVAE-g).

---

## Key Concepts
1. **Definition**:
   - Eigenvector: A vector \(\mathbf{v}\) that satisfies \(A\mathbf{v} = \lambda\mathbf{v}\) for some scalar \(\lambda\).
   - Eigenvalue \(\lambda\): Scalar indicating how \(\mathbf{v}\) is stretched or compressed.

2. **Computation**:
   - Solve \(\det(A - \lambda I) = 0\) for eigenvalues \(\lambda\).
   - Substitute \(\lambda\) into \((A - \lambda I)V = 0\) to find eigenvectors.

3. **Applications**:
   - Physics: Principal axes of rotation.
   - Data Science: PCA for dimensionality reduction.
   - Stability Analysis: Eigenvalues determine stability of systems.

---

For computational examples, refer to [Week 7 Supplementary Notebook](../../labs/supplementary_notebooks/week7_eigen.ipynb).

---

## Exercises:
1. Find the eigenvalues and eigenvectors of \(A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}\).
2. Use SageMath to verify your solutions computationally.
3. Analyze how eigenvalues determine the transformation properties of a given matrix.