---
layout: default
title: Image Formation
parent: Computer Vision
grand_parent: Courses
nav_order: 1
---

# Image Formation

I have a different philosophy when it comes to learning, I like to answer the questions first and then I explain why and the concepts behind it. So lets start with the first one.

## Problem: Projection and perspective

**Question**: Parallel projection equations stated in the book (What tha hell is a projection? what is the meaning of being parallel?):
1. $x = \alpha X + x_0$
2. $y = \alpha(\cos(\theta)Y - \sin(\theta)Z) + y_0$

Show that these equations emerge naturally from a series of transformations applied to the 3D world coordinates $(X, Y, Z)$, of the form:

$$\begin{bmatrix} x \\ y \end{bmatrix} = \alpha \cdot P \cdot R_x(\theta) \cdot \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} + \begin{bmatrix} x_0 \\ y_0 \end{bmatrix}$$

Where $R_x(\theta)$ is a $3 \times 3$ rotation matrix over the X-axis, $P$ is a $2 \times 3$ orthogonal projection matrix, and $\alpha$ is a scaling factor.

Then, find $\alpha, x_0$, and $y_0$ when the world point $(0, 0, 0)$ projects onto $(0, 0)$ and the point $(1, 0, 0)$ projects onto $(3, 0)$.

### Solution

#### 1. Transformation Matrices
The rotation matrix around the X-axis by an angle $\theta$ is:
$$R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}$$

The orthogonal projection matrix $P$ that selects the $X$ and $Y$ components is:
$$P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$

#### 2. Derivation
Multiplying the rotation matrix by the 3D point:
$$R_x(\theta) \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} X \\ \cos(\theta)Y - \sin(\theta)Z \\ \sin(\theta)Y + \cos(\theta)Z \end{bmatrix}$$

Applying the projection matrix $P$:
$$P \cdot R_x(\theta) \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} X \\ \cos(\theta)Y - \sin(\theta)Z \\ \sin(\theta)Y + \cos(\theta)Z \end{bmatrix} = \begin{bmatrix} X \\ \cos(\theta)Y - \sin(\theta)Z \end{bmatrix}$$

Finally, applying the scale $\alpha$ and adding the offset $\begin{bmatrix} x_0 \\ y_0 \end{bmatrix}$:
$$\begin{bmatrix} x \\ y \end{bmatrix} = \alpha \begin{bmatrix} X \\ \cos(\theta)Y - \sin(\theta)Z \end{bmatrix} + \begin{bmatrix} x_0 \\ y_0 \end{bmatrix} = \begin{bmatrix} \alpha X + x_0 \\ \alpha(\cos(\theta)Y - \sin(\theta)Z) + y_0 \end{bmatrix}$$
This matches the equations given.

#### 3. Finding $\alpha, x_0, y_0$
- **Using point $(0, 0, 0) \to (0, 0)$**:
  $0 = \alpha(0) + x_0 \implies x_0 = 0$
  $0 = \alpha(\cos\theta(0) - \sin\theta(0)) + y_0 \implies y_0 = 0$

- **Using point $(1, 0, 0) \to (3, 0)$**:
  $3 = \alpha(1) + x_0 \implies 3 = \alpha + 0 \implies \alpha = 3$
  $0 = \alpha(\cos\theta(0) - \sin\theta(0)) + y_0 \implies 0 = 0$ (Verified)

**Result**: $\alpha = 3, x_0 = 0, y_0 = 0$.

---

## Key Concepts Explained

### Parallel Projection
Unlike perspective projection where rays converge at a point (the pinhole), in **parallel projection**, the rays are parallel to each other. This is often used to model telephoto lenses where the object is very far from the camera.

### Orthogonal Projection Matrix
The matrix $P$ acts as a "selector", taking the 3D coordinates and flattening them onto a 2D plane. In our case, we rotate the world first to align the camera's view, then project.

### Rotation Matrix $R_x(\theta)$
This matrix represents a rotation in 3D space. Notice how the X-coordinate remains unchanged ($1$ in the top-left), while Y and Z are transformed by $\sin$ and $\cos$. 
