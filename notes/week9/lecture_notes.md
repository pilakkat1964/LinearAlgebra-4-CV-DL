# Week 9: Optimization and Gradient Descent

## Overview
This week covers optimization techniques and the use of gradient descent to minimize functions, a key concept in machine learning. Topics include:
- Gradient Calculation
- Gradient Descent Algorithm
- Applications in Regression and Classification Problems

---

## Gilbert Strang's Video Reference:
- Gradient Descent [MIT OCW Lecture on Optimization Techniques](https://www.youtube.com/watch?v=K3oBSIlRQqY).

---

## Key Concepts
1. **Gradient Calculation**:
   - The gradient of a function \(f(x, y)\) points in the direction of the steepest ascent.
   - Formula: \( \nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}. \)

2. **Gradient Descent**:
   - An iterative optimization algorithm that updates parameters in the direction of the negative gradient to minimize a function:
   \[
   x_{n+1} = x_n - \alpha \nabla f(x_n).
   \]

3. **Applications**:
   - Machine Learning:
     - Cost function minimization.
   - Physics and Engineering:
     - Energy minimization problems.

---

For computational practice, use the [Week 9 Supplementary Notebook](../../labs/supplementary_notebooks/week9_gradient_descent.ipynb).

---

## Exercises:
1. Derive the gradient of the function \(f(x, y) = x^2 + y^2\).
2. Implement gradient descent in SageMath to minimize \(f(x, y)\).
3. Experiment with different learning rates (\(\alpha\)) and observe convergence behavior.
