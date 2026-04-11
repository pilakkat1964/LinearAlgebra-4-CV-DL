# Week 2 Slides: Systems of Linear Equations

## Slide 1: Introduction to Systems of Equations
- Systems appear in physics, engineering, economics, etc.
- We aim to solve multiple equations simultaneously, e.g.,
  $x + 2y + z = 6$.
- Reference Video: [MIT OCW Video](https://www.youtube.com/watch?v=QVKj3LADCnA).

---

## Slide 2: Gaussian Elimination
- Process:
  - Convert system to upper triangular form.
  - Solve via back-substitution.
- Example:
  \[
    a_{11}x + a_{12}y + a_{13}z = b_1 \\
    a_{22}y + a_{23}z = b_2 \\
    a_{33}z = b_3
\]

---

## Slide 3: Row Reduction
- Row echelon form (REF): Non-zero row pivots.
- Reduced REF (RREF): 1s as pivot entries.
- Visual example with SageMath [Notebook](../../labs/supplementary_notebooks/week2_linear_systems.ipynb).

---

## Slide 4: Solution Types
- Unique solution:
  - Pivot count matches variable count.
- Infinite solutions:
  - Underconstrained or dependent equations.
- No solution:
  - Inconsistent system.

---

## Slide 5: Practice
1. Solve a system through elimination & substitution.
2. Write SageMath code to compute echelon forms.