# Week 10: Principal Component Analysis (PCA)

## Overview
Principal Component Analysis (PCA) is a dimensionality reduction technique essential for visualizing and analyzing high-dimensional data. Topics include:
- Covariance Matrices and Variance
- Eigenvalues and Eigenvectors in PCA
- Applications in Data Compression and Visualization

---

## Gilbert Strang's Video Reference:
- PCA Concepts [MIT OCW Video on PCA](https://www.youtube.com/watch?v=F5rEy3EK2pg).

---

## Key Concepts
1. **Covariance Matrix**:
   - Measures the relationships and variance among dimensions in a dataset.
   - Symmetric matrix capturing spread of data points.

2. **Eigenvalues in PCA**:
   - Eigenvectors define new axes of variance (principal components).
   - Eigenvalues indicate variance explained by each principal component.

3. **Applications**:
   - Dimensionality reduction while preserving information.
   - Noise reduction and compression.
   - Data visualization in 2D/3D from higher dimensions.

---

Explore computational examples in [Week 10 Notebook](../../labs/08_svd.ipynb).

---

## Exercises:
1. Compute the eigenvalues of the covariance matrix for:
   \[
     \begin{bmatrix}
      1 & 2 & 3 \\
      4 & 5 & 6
     \end{bmatrix}.
   \]
2. Visualize data projections on the top 2 principal components using SageMath.
3. Explain how PCA applies in facial recognition tasks.
