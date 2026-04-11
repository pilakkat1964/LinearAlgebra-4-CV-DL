# Week 12: Neural Networks and Matrix Computations

## Overview
In this final week, we explore how linear algebra concepts underpin the design and computation within neural networks. Topics include:
- Weight Matrices in Neural Networks
- Backpropagation and Gradients
- Role of Linear Algebra in Deep Learning Frameworks

---

## Gilbert Strang's Video Reference:
- Linear Algebra and Neural Networks [MIT OCW Lecture](https://www.youtube.com/watch?v=aircAruvnKk).

---

## Key Concepts
1. **Weight Matrices and Transformations**:
   - Neural networks compute activations via \(Y = f(WX + b)\).
   - Weight matrices \(W\): Core linear structures mapping inputs to outputs.

2. **Backpropagation**:
   - Gradients are computed via chain rule to update weights.
   - Requires efficient matrix differentiation mechanics.

3. **Role in Deep Learning**:
   - Matrix operations dominate forward and backpropagation in frameworks like PyTorch.
   - GPU acceleration leverages optimized linear algebra routines.

---

Refer to [Week 12 Notebook](../../labs/12_pytorch.ipynb) for hands-on exercises.

---

## Exercises:
1. Multiply input tensors by weight matrices for a small model with \(X, W, b\).
2. Write the backpropagation update rule to compute gradients of weight matrices.
3. Implement a PyTorch example demonstrating efficient gradient evaluation.
