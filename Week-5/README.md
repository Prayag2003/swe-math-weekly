# README: Gradient Descent and Partial Derivatives

## Overview

This project explores **gradient descent** and **partial derivatives** to optimize comfort levels in an environment. Given parameters such as temperature, humidity, and the number of people in a room, we determine the first variable to adjust for improving comfort.

## Mathematical Theory

### **Gradient Descent**

Gradient descent is an optimization algorithm used to minimize (or maximize) a function by iteratively moving in the direction of the **negative gradient**.

- The gradient of a function points in the direction of the **steepest ascent**.
- To find the minimum, we move **opposite** to the gradient.
- The learning rate controls the step size for updates.

Watch this **3Blue1Brown** video for a visual explanation:
[Gradient Descent - 3Blue1Brown](https://www.youtube.com/watch?v=IHZwWFHWa-w)

### **Partial Derivatives**

A **partial derivative** measures how a function changes with respect to **one variable** while keeping others constant. In this case, we compute partial derivatives to determine which variable most significantly impacts comfort.

The comfort function is defined as:

C(T, H, O) = 72 - (T - 70)^2 - 2(H - 40)^2 + 5O

where:

- T = Temperature
- H = Humidity
- O = Occupancy (number of people)

#### **Computing Partial Derivatives**

Taking partial derivatives with respect to each variable:

Partial(C,T) = -2 (T - 70)

Partial(C,H) = -4 (H - 40)

Partial(C,O) = 5

The **absolute value** of each derivative determines which variable has the largest impact on comfort. The algorithm adjusts the most influential variable first.
