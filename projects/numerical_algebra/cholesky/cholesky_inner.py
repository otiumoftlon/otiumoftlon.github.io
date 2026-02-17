import numpy as np


def cholesky(A):

    n, m = A.shape

    for i in range(n):
        for k in range(0, i):
            A[i, i] -= A[k, i] ** 2
        if A[i, i] <= 0:
            raise ValueError("Matrix is not positive definite")
        A[i, i] = np.sqrt(A[i, i])
        for j in range(i + 1, n):
            for k in range(0, i):
                A[i, j] -= A[k, i] * A[k, j]
            A[i, j] /= A[i, i]

    return np.triu(A)


A = np.array([[4.0, -2, 4, 2], [-2, 10, -2, -7], [4, -2, 8.0, 4], [2, -7, 4, 7]])

print("Input matrix A:")
L = cholesky(A.copy())
print(L)
a_1 = L.T @ L
print(a_1)
