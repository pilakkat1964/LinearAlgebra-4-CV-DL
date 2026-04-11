# Week 4 Slides: Singular Value Decomposition

## Slide 1: What is SVD?
- Decomposes any matrix \(A\):
  \[
A = U\Sigma V^T
\].
- \(U\): Left singular vectors.
- \(\Sigma\): Singular values.
- \(V^T\): Right singular vectors.
- Reference Video: [MIT OCW Video on SVD](https://www.youtube.com/watch?v=P5mlg91as1c).

---

## Slide 2: Visualization of SVD
- Geometric Perspective:
  - Rotation: Contributed by \(V\).
  - Scaling: Magnitude by \(\Sigma\).
  - Orthogonal transformation: Via \(U\).
- Applications: Dimensionality reduction, compression.

---

## Slide 3: Image Compression via SVD
- Decompose image matrix:
  \[
Image \approx U_k\Sigma_k V_k^T
\].
- Example:
  - Full rank: High detail.
  - Reduced rank: High compression.
- Supplementary exercise: [Notebook Example](../../labs/supplementary_notebooks/week4_homography_matrices.ipynb).

---

## Slide 4: Dimensionality Reduction
- Focus on largest singular values.
- Reduces redundancy while preserving structure.

---

## Slide 5: Challenges
- High computation for large matrices.
- Numerical stability when \(\Sigma\) values are almost zero.

---

## Practice Examples:
1. Decompose given matrices symbolically in SageMath.
2. Experiment with low-rank approximations in data matrices.
