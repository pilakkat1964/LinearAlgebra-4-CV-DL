# Week 4: Singular Value Decomposition (SVD)

## Overview
Singular Value Decomposition (SVD) is a fundamental concept in linear algebra with wide applications in data science, computer vision, and matrix analysis. Topics this week include:
- Basics of SVD
- Geometric Interpretation
- Applications: Dimensionality Reduction, Image Compression

---

## Gilbert Strang's Video Reference:
- Singular Value Decomposition [MIT OCW Video - SVD in Linear Algebra](https://www.youtube.com/watch?v=P5mlg91as1c).

---

## Key Concepts
1. **What is SVD?**
   - Factorization: Any matrix can be decomposed as \(A = U \Sigma V^T\).
   - \(U\): Orthogonal matrix of left singular vectors.
   - \(\Sigma\): Diagonal matrix of singular values.
   - \(V^T\): Transpose of orthogonal matrix of right singular vectors.

2. **Geometric Interpretation**:
   - SVD represents scaling, rotation, and projection.

3. **Applications**:
   - Image Compression:
     - Approximation of image matrices.
   - Dimensionality Reduction:
     - Rank reduction keeps the most significant features.

---

For computational examples, refer to [Week 4 Supplementary Notebook](../../labs/supplementary_notebooks/week4_homography_matrices.ipynb).

---

## Exercises:
1. Compute the SVD of matrix:
   \[
     \begin{bmatrix}
      1 & 2 \\
      3 & 4 \\
      5 & 6
     \end{bmatrix}
   \]
   and reconstruct the matrix using \(U, \Sigma, V^T\).
2. Visualize transformations induced by \(\Sigma\) using SageMath.
3. Explore the effect of rank truncation on a dataset.