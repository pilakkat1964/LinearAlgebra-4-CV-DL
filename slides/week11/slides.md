# Week 11 Slides: Singular Value Decomposition Applications

## Slide 1: SVD and Low-Rank Approximations
- Application-rich decomposition method:
  \[
A \approx U_k\Sigma_kV_k^T
\].
- Keeps leading singular values.
- Reduces complexity while retaining information.
- Video: [MIT OCW SVD Applications](https://www.youtube.com/watch?v=GFnjeK0NE80).

---

## Slide 2: Image Compression
- Compress large image files without losing key structural details.
- Example workflow:
  - Convert image matrix.
  - Apply SVD.
  - Reconstruct with top \(k\) values.

---

## Slide 3: Recommender Systems
- Idea: Decompose user-item matrices into latent factors.
- Predict missing ratings based on shared preferences.

---

## Slide 4: Practice with SVD
- Example Dataset:
  \[
\text{Image, Rating Data, Sparse Matrices.}
\]
- Use SageMath in [Week 11 Notebook](../../labs/supplementary_notebooks/week11_svd_image_compression.ipynb).

---

## Slide 5: Challenges and Limitations
1. Computational Cost for Large Data.
2. Interpretability of Generated Components.

---

## Slide 6: Exercises
1. Visualize singular value decay for compressed matrices.
2. Explore latent features in a recommender matrix factorization.