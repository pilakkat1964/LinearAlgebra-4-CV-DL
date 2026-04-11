# Week 8 Slides: Matrix Decompositions and Applications

## Slide 1: Matrix Decompositions
- Fundamental tools for computational efficiency.
- Examples:
  - LU Decomposition: Lower and Upper matrices.
  - QR Decomposition: Orthogonal \(Q\) and Upper \(R\).
- Reference Video: [MIT OCW Lecture on LU and QR](https://www.youtube.com/watch?v=AUXMV2Kaz2w).

---

## Slide 2: LU Decomposition
1. Decomposes \(A\):
\[
A = LU.
\]
2. Benefits:
   - Faster solution to linear systems.
   - Direct insight into matrix structure.

---

## Slide 3: QR Decomposition
- \(A = QR\):
  1. \(Q\): Orthogonal.
  2. \(R\): Triangular.
- Application in least squares optimization.

---

## Slide 4: Computation Example
- Example:
\[
A = \begin{bmatrix} 1 & 2 \\
3 & 4 \end{bmatrix} \to QR.
\]
  - Verification using SageMath in [Week 8 Notebook](../../labs/08_svd.ipynb).

---

## Slide 5: Practice Examples
1. Compute LU decomposition for a 3x3 matrix.
2. Analyze numerical stability of QR factorization in data sets.
