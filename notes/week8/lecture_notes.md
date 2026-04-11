# Week 8: Matrix Decompositions and Applications

## Overview
Matrix decompositions are techniques that enable efficient computations and deeper insights into matrix structure. Topics this week include:
- LU Decomposition
- QR Decomposition
- Applications in Linear Systems and Optimization

---

## Gilbert Strang's Video Reference:
- Matrix Decompositions [MIT OCW: LU and QR](https://www.youtube.com/watch?v=AUXMV2Kaz2w).

---

## Key Concepts
1. **LU Decomposition**:
   - Decomposes a matrix \(A\) into the product \(LU\) where:
     - \(L\): Lower triangular matrix.
     - \(U\): Upper triangular matrix.
   - Example: Solving \(Ax = b\) efficiently.

2. **QR Decomposition**:
   - Decomposes \(A = QR\):
     - \(Q\): Orthogonal matrix.
     - \(R\): Upper triangular matrix.
   - Useful in least squares optimization.

3. **Applications**:
   - Solve linear systems faster.
   - Condition number analysis.
   - Numerical optimization routines.

---

For hands-on practice, refer to [Week 8 Supplementary Notebook](../../labs/08_svd.ipynb).

---

## Exercises:
1. Compute the LU decomposition of:
   \[
     \begin{bmatrix}
      4 & 3 \\
      6 & 3
     \end{bmatrix}
   \]
2. Verify the result using SageMath.
3. Find the QR decomposition of a 2x2 matrix and interpret \(Q\) and \(R\) geometrically.
