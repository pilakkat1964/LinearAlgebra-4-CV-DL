# Week 11: Singular Value Decomposition Applications

## Overview
This week delves deeper into Singular Value Decomposition (SVD) and its key real-world applications. Topics include:
- Low-Rank Approximations
- Image Compression with SVD
- Recommender Systems

---

## Gilbert Strang's Video Reference:
- Real World SVD Applications [MIT OCW Lecture](https://www.youtube.com/watch?v=GFnjeK0NE80).

---

## Key Concepts
1. **Low-Rank Approximation**:
   - Approximate a matrix \(A\) with \(U_k\Sigma_kV_k^T\).
   - Keep the top \(k\) singular values for efficiency.

2. **Image Compression**:
   - Use SVD to approximate image matrices effectively.
   - Retain sufficient visual detail while reducing storage size drastically.

3. **Recommender Systems**:
   - Factorize matrices like user-item ratings using SVD.
   - Predict missing entries based on known item preferences.

---

Hands-on content available in the [Week 11 Notebook](../../labs/08_svd.ipynb).

---

## Exercises:
1. Perform a low-rank matrix approximation in SageMath.
2. Compress an example grayscale image using SVD.
3. Discuss how the rank impacts the final quality of image reconstruction.
