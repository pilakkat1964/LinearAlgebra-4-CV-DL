# Week 6: Fundamental Matrices (Slides)

## Slide 1: Fundamental Matrices in Computer Vision
- Connects corresponding points across two camera views.
- Represents epipolar geometry constraints.
- Reference Video: [Gilbert Strang - Matrix Applications Lecture](https://www.youtube.com/watch?v=KPXfXNppTrY).

---

## Slide 2: Properties of Fundamental Matrices
- Determinants:
  - \( \text{det}(F) = 0 \): Indicating planar constraints.
- Eigenvalues/Eigenvectors:
  - Reveal geometric properties of image transformation.

---

## Slide 3: Worked Example
- Visualization:
$$
F = \begin{bmatrix} 0 & -1 & 0 \\
1 & 0 & -2 \\
0 & 2 & 1 \end{bmatrix}
$$
  - Exercise using `Week 6 Notebook`.
- Compute determinants and analyze null spaces.

---

## Slide 4: Summary
- Fundamental properties are essential in stereo vision and epipolar constraints.
- Exercises encourage:
  - Deriving properties.
  - Leveraging SageMath scripts interactively.