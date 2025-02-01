# README: Predicting Creator Evolution Using Linear Transformations

## Overview

This project uses a mathematical model to predict how content creators evolve in technical depth and entertainment value over time. Given historical data on previous creators and their growth patterns, we derive a transformation matrix to forecast the future states of new creators.

## Mathematical Intuition

### **Step 1: Finding the Transformation Matrix**

We assume that the evolution of a creator’s attributes over time can be modeled by a **linear transformation** represented as:

Y = A X

where:

- X is the matrix of previous creators’ attributes at the initial state,
- Y is the matrix of their attributes at the next recorded state,
- A is the transformation matrix that defines how creators evolve.

To solve for A, we use the **least squares method**, which gives the best-fit transformation:

A = (X^T X)^{-1} X^T Y

This equation ensures that the transformation minimizes errors when applied to known data points.

### **Step 2: Predicting Future States**

Once we obtain A, we use **eigen decomposition** to predict how a creator’s attributes change over multiple time steps. Given an initial state x_0 and a time horizon k, the future state is computed using:

x_k = V D^k V^{-1} x_0

where:

- V is the matrix of eigenvectors of A,
- D is the diagonal matrix of eigenvalues,
- D^k represents the evolution of each eigencomponent over k steps.

This approach effectively models how different growth trends (technical depth and entertainment value) evolve over time.

### **Step 3: Identifying Trends and Transitions**

By comparing initial and final states, we determine:

- The creator with the highest predicted **technical depth** and **entertainment value** after 4 weeks.
- Creators who **switched focus** (from technical to entertainment and vice versa).

This allows us to analyze how trends shift within the creator ecosystem and predict potential growth paths.

## Applications

- Understanding how new creators evolve over time.
- Predicting industry trends in content creation.
- Identifying creators with the potential for rapid growth.

This model provides a structured way to analyze creator trajectories using mathematical principles of linear algebra and eigen decomposition.
