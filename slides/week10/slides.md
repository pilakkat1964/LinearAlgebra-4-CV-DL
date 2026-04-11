# Week 10 Slides: Principal Component Analysis (PCA)

## Slide 1: Introduction to PCA
- Tool for dimensionality reduction.
- Key Ideas:
  1. Capture the direction of maximum variance.
  2. Project onto new subspaces.
- Reference Video: [MIT OCW on PCA](https://www.youtube.com/watch?v=F5rEy3EK2pg).

---

## Slide 2: How PCA Works
- Compute the covariance matrix.
- Solve for eigenvalues/eigenvectors.
- Project data onto eigenvectors.

---

## Slide 3: Applications of PCA
- Data Visualization:
  - Reduce 100D to 2D/3D.
- Noise Reduction:
  - Remove minor components (low eigenvalue).

---

## Slide 4: Computation Example
- Dataset \(X\):
\[
\begin{bmatrix}
  x_{1,1} & x_{1,2}  \\
  x_{2,1} & x_{2,2}
\end{bmatrix} \to \text{Covariance, Eigenvalues.}
\]
 - Practice: [Week 10 Notebook](../../labs/08_svd.ipynb).

---

## Slide 5: Practice Examples
1. Compute eigen-decomposition for covariance matrices.
2. Project data onto principal components and visualize.
