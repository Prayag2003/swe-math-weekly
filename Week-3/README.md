# Overview

This project determines the individual contributions of different compression algorithms to the overall compression score for various video types. Given the processing power consumption of each algorithm and the total compression score for a video type, we aim to solve for each algorithm's contribution using linear algebra.

## Mathematical Intuition

The problem is modeled as a system of linear equations:

\[
A x = b
\]

where:

- **A** is an `M × N` matrix representing the processing power consumption of each algorithm.
- **x** is an `N`-dimensional vector of unknown contributions.
- **b** is an `M`-dimensional vector of total compression scores.

For example, given the equations:
\[
2x + y + 3z = 95
\]
\[
x + 3y + z = 82
\]
\[
3x + 2y + z = 75
\]
We solve for `x, y, z` using numerical methods.

## Solution Approach

1. **Matrix Representation:** Store the input values into matrix `A` and vector `b`.
2. **Solve the System:** Use NumPy’s `np.linalg.solve(A, b)` to compute `x`.
3. **Validation:** Verify that the solution satisfies the original equations within a precision of `10^-6`.
4. **Handle Errors:** If `A` is singular or inconsistent, output `"observation error"`.

## Applications

- **Feature Attribution in Machine Learning**
- **Resource Allocation in Cloud Computing**
- **Signal Processing and Image Reconstruction**
- **Optimizing Algorithm Performance in Software Engineering**

By leveraging linear algebra, we can efficiently compute the contributions of each compression algorithm with high accuracy.
