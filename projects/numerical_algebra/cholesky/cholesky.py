import numpy as np

A = np.array([[9, 3, 3], [3, 10, 7], [3, 5, 9]])

B = np.array([[4, 2, 6], [2, 2, 5], [6, 5, 29]])

C = np.array([[4, 4, 8], [4, -4, 1], [8, 1, 6]])

D = np.array([[1, 1, 1], [1, 2, 2], [1, 2, 1]])

M = [A, B, C, D]

for matrix in M:
    try:
        print("Matrix:")
        print(matrix)
        print("Cholesky Decomposition:")
        print(np.linalg.cholesky(matrix))
    except np.linalg.LinAlgError:
        print("Matrix is not positive definite, Cholesky decomposition not possible.")
