# Week 2: Systems of Linear Equations

## Overview
This week focuses on solving systems of linear equations, a cornerstone of linear algebra with applications in optimization, computer science, and simulations. Topics include:

- Gaussian Elimination
- Row Reduction and Echelon Form
- Solutions of Systems (Uniqueness, Infinite, and None)

---

## Gilbert Strang's Video Reference:
- Gaussian Elimination [MIT OCW Video - Elimination and Echelon Form](https://www.youtube.com/watch?v=QVKj3LADCnA).

---

## Key Concepts
1. **Gaussian Elimination**:
   - Eliminating variables row-by-row to simplify systems into easier forms.
   - Accomplished using elementary row operations.

2. **Row Reduction**:
   - Convert a matrix into echelon form or reduced row-echelon form (RREF).
   - Pivot elements lead each non-zero row.

3. **Types of Solutions**:
   - Unique Solution:
     - Exists if the number of pivot variables equals the number of unknowns.
   - Infinite Solutions:
     - Occurs if equations are dependent.
   - No Solution:
     - Results from inconsistency.

---

For computational examples, refer to [Week 2 Supplementary Notebook](../../labs/supplementary_notebooks/week2_linear_systems.ipynb).

---

## Exercises:
1. Solve the given system using Gaussian elimination:
   \[\begin{aligned} x + 2y + z &= 6 \\ 2x - y + 3z &= 14 \\ 3x + y + 2z &= 10 \end{aligned}\]
2. Use SageMath to find the RREF of a 3x3 matrix of your choice.
3. Categorize the solutions (unique, infinite, no solution) for another system of your choosing.