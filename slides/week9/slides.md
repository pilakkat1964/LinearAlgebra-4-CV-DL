# Week 9 Slides: Optimization and Gradient Descent

## Slide 1: Optimization and Applications
- Goal: Find the minimum of a given function \(f(x)\).
- Applications:
  - Regression models.
  - Neural network training.
  - Energy minimization.
- Reference Video: [MIT OCW Video](https://www.youtube.com/watch?v=K3oBSIlRQqY).

---

## Slide 2: Gradient Calculation
- Gradient calculation:
\[
\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y} \end{bmatrix}
\]
- Interpretation:
  - Steepest ascent direction.

---

## Slide 3: Gradient Descent Algorithm
\[
x_{n+1} = x_n - \alpha \nabla f(x_n).
\]
- \(\alpha\): Learning rate.
- Iterative optimization for function minimization.

---

## Slide 4: SageMath Practice
- Use [Week 9 Notebook](../../labs/supplementary_notebooks/week9_gradient_descent.ipynb).
- Example:
  - Compute and visualize convergence for \(f(x, y) = x^2 + y^2\).

---

## Slide 5: Practice Examples
1. Test gradient descent with \(f(x, y)\): Himmelblau’s function.
2. Evaluate sensitivity of convergence to learning rates.