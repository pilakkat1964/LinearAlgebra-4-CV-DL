# Week 5: Vector Spaces and Subspaces

## Overview
Vector spaces and their subspaces are foundational concepts in linear algebra that underpin systems of equations, linear transformations, and more. Topics include:
- Vector Space Definition
- Basis and Dimension
- Column Space, Row Space, and Null Space

---

## Gilbert Strang's Video Reference:
- Introduction to Vector Spaces [MIT OCW Lecture on Subspaces](https://www.youtube.com/watch?v=W_zz5iByHnw).

---

## Key Concepts
1. **Vector Spaces**:
   - A collection of vectors closed under addition and scalar multiplication.
   - Example: \(\mathbb{R}^n\), space of all n-tuples.

2. **Subspaces**:
   - A subcollection within a vector space where sum and scalar multiplication still hold.
   - Example: A plane through origin is a subspace of \(\mathbb{R}^3\).

3. **Basis and Dimension**:
   - Basis: A minimal spanning set of vectors.
   - Dimension: Number of independent vectors in the basis.

4. **Column Space, Null Space**:
   - Column Space: Subspace spanned by columns of a matrix.
   - Null Space: Subspace of all solutions to \(Ax = 0\).

---

For computational examples, see [Week 5 Supplementary Notebook](../../labs/04_vector_spaces.ipynb).

---

## Exercises:
1. Verify whether a given set of vectors forms a basis for \(\mathbb{R}^3\).
2. Compute the null space of \(A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}\).
3. Use SageMath to find the column space of a matrix.
