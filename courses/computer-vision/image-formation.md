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

$$x = \alpha X + x_0$$
$$y = \alpha(\cos(\theta)Y - \sin(\theta)Z) + y_0$$

 Note: Lol this is just for fun but I am using antigravity to help me with the organization and creation of the pages in jekyll, and I wanted to paste the problem to not manually write it down, especially the equations, and it solved the problem for me, but I have already solved it by myself, so why not show the different ways of solving it? my way was really similar took me a bit more of time to write it down, but it was fun also I will show things that the machine can not think of.

Show that these equations emerge naturally from a series of transformations applied to the 3D world coordinates $(X, Y, Z)$, of the form:

$$\begin{bmatrix} x \\ y \end{bmatrix} = \alpha \cdot P \cdot R_x(\theta) \cdot \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} + \begin{bmatrix} x_0 \\ y_0 \end{bmatrix}$$

Where $R_x(\theta)$ is a $3 \times 3$ rotation matrix over the X-axis, $P$ is a $2 \times 3$ orthogonal projection matrix, and $\alpha$ is a scaling factor.

Then, find $\alpha, x_0$, and $y_0$ when the world point $(0, 0, 0)$ projects onto $(0, 0)$ and the point $(1, 0, 0)$ projects onto $(3, 0)$.

### Solution (AI solution)

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

### My solution

Well the first thing I did was to find what is P and R, and basically are the ones that the AI find, but what is a projection matrix? maybe for experts on linear algebra and expert in robotics is obvious, but for the sake of begginers I will explain it, and almost every simple concept I will explain it, because I want this to be a place where begginers can learn, and I personally I like when the books and references are ultra explicit.

$$ P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} $$

This is a projection matrix. If you look at the last column, it’s all zeros. Basically, that column acts as a dimension eraser. In this case, it erases the Z dimension and keeps only the X and Y components of the vector it multiplies.

Now let’s think a bit deeper: why would you want to erase a dimension? (You can skip this part if you are already familiar with this topics)

Here, the motivation is intuitive. Images don’t have depth, so we need a way to remove the depth information from the 3D world. This matrix does exactly that: it collapses the 3D space into 2D.

In a data science context, the same idea appears when you project data into a lower-dimensional space. It might not be the best way to do dimensionality reduction, but it’s still a valid one. More sophisticated methods exist, like PCA, but conceptually, they’re doing something very similar: removing dimensions that we decide are less important.

You can even push this idea further. Imagine the universe is 4D, but we can only perceive 3D. Then, in some sense, we need a mechanism to erase the fourth dimension. A projection matrix is exactly that mechanism.

Can we erase more than one dimension? The simple answer is yes.

Even in more advanced topics, like homogeneous coordinates, you’ll see a very similar idea. In general terms, homogeneous coordinates add an extra dimension (usually a 1) to make transformations more efficient to compute. Then, after the transformation, you effectively project back down, erasing that extra dimension. The equations look more complicated, but the underlying idea is almost the same as what we’re doing here.

Note: In linear algebra, a simple trick to build these kinds of projection matrices is to start with an identity matrix of the target dimension and then add columns of zeros for the dimensions you want to eliminate.

Now we have the rotation matrix in the x-axis, what is a rotation matrix? why in x-axis? are other ways to do rotation? 

$$ R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix} $$

Why in the x-axis is a bit straight forward, because the camera is rotating around the x-axis, so the x-component is not changing so that why is acolumn with 1 in the first row, and the y and z components are changing according to the angle theta, just see theta equal zero is convert to the identity matrix, so not rotation at all. So basically that is a rotation matrix, is the transformation that allows a vector to rotate around an axis, and if you have a set of vectors, you can rotatea them all together. There are other ways to do rotation, this is the most basic one, but also is a dangerous one, but I will explain it later when we talk about rotation in more detail. 

After that is pretty straight forward, we jsut multiply the matrices, for me a good advice is always check the dimension of the matrices before multiplying. The result will be the same as the one doing with the AI. 




