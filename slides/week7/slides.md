# Week 7 Slides: Eigenvalues and Eigenvectors

## Slide 1: Introduction to Eigenvalues
- Eigenvector \(\mathbf{v}\):
  - A vector that only changes by a scalar factor \(\lambda\).
  \[A\mathbf{v} = \lambda\mathbf{v}\].
- Reference Video: [MIT OCW Video](https://www.youtube.com/watch?v=PFDu9oVAE-g).

---

## Slide 2: Computing Eigenvalues
- Solve \[\det(A - \lambda I) = 0\].
- Example with \[A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}\].

---

## Slide 3: Applications of Eigenvalues
- Physics:
  - Rotational matrices.
- Data Science:
  - PCA and dimensionality reduction.
- Stability:
  - Eigenvalues reveal stable vs unstable systems.

---

## Slide 4: Practical Calculation
- Use [Week 7 Notebook](../../labs/supplementary_notebooks/week7_eigen.ipynb).
- SageMath computation example:
$$
\[A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix} \to \text{Eigenvalues, Eigenvectors.}\]

---

## Slide 5: Practice Examples
1. Compute eigenvalues for \[
\[A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}\].
2. Analyze transformation behavior using \(V\).