# Week 5 Slides: Vector Spaces and Subspaces

## Slide 1: What is a Vector Space?
- Definition:
  - Closed under vector addition and scalar multiplication.
  - Contains the zero vector.
- Example: \(\mathbb{R}^2\)\, the plane.
- Reference Video: [MIT OCW Lecture on Subspaces](https://www.youtube.com/watch?v=W_zz5iByHnw).

---

## Slide 2: Subspaces
- Examples of subspaces:
  - Lines through the origin.
  - \(\mathbb{R}^3\)
- Example computations: Use SageMath \(\text{Notebook}\) [Notebook](../../labs/supplementary_notebooks/week5_vector_spaces.ipynb).

---

## Slide 3: Basis and Dimension
- Basis:
  - Set of independent vectors that span the space.
  - Example: \([1,0,0], [0,1,0]\) \(\mathbb{R}^3\)
- Dimension:
  - Number of vectors in the basis.

---

## Slide 4: Column Space, Null Space
### Column Space\n- The subspace spanned.
  - Subspace spanned by the columns of matrix \(A\).
- Null Space:
  - Subspace of vectors solving \(Ax=0\).

---

## Slide 5: Exercises
1. Use matrix \(A\):
\[\begin{bmatrix} 2 & 4 & 6 \\ \ 3 &
1 & 3 & 5 \\ \end{bmatrix}\].
  - Find its basis.
  - Compute null space with SageMath.
2. Discuss dimension of the null space \(N(A)\).