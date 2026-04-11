# Week 12 Slides: Neural Networks and Matrix Computations

## Slide 1: Linear Algebra Foundations in NN
- Neural network computations depend on:
  - Weight matrices \(W\).
  - Activation functions \(f(x)\).
- Reference Video: [MIT OCW Lecture on NN](https://www.youtube.com/watch?v=aircAruvnKk).

---

## Slide 2: Weight Matrix Operations
- Example Computation:
  \[
Y = f(WX + b).
\]
- Matrices \(W\): Connect inputs to neurons.
- Bias \(b\): Shifts activation.

---

## Slide 3: Backpropagation
- Gradient Calculation:
  \[
\nabla W = \frac{\partial L}{\partial W}.
\]
- Uses:
  - Chain rule.
  - Matrix multiplications for efficiency.

---

## Slide 4: Role in Deep Learning Frameworks
- PyTorch/TensorFlow leverage GPU-optimized matrix libraries (e.g., cuBLAS).
- Focus on parallelizing large-scale operations.

---

## Slide 5: Practice Examples
1. Implement forward and backpropagation for \(Y = WX + b\).
2. Visualize parameter updates over training iterations using PyTorch in [Week 12 Notebook](../../labs/12_pytorch.ipynb).
