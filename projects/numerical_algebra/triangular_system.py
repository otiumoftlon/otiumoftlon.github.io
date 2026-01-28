import time

import numpy as np


def forward_substitution(G, b):
    n = len(b)
    # Convertimos a float para evitar errores de truncamiento de enteros
    y = b.astype(float).copy()

    # for i = 1, ..., n
    for i in range(0, n):

        # for j = 1, ..., i - 1 (se ejecuta solo si i > 0)
        for j in range(0, i):
            # b_i <- b_i - g_ij * b_j
            y[i] = y[i] - G[i, j] * y[j]

        # if g_ii = 0, set error flag, exit
        if G[i, i] == 0:
            print(f"Error: División por cero en el índice {i}")
            return None

        # b_i <- b_i / g_ii
        y[i] = y[i] / G[i, i]

    return y


L = np.array([[2, 0, 0, 0], [-1, 2, 0, 0], [3, 1, -1, 0], [4, 1, -3, 3]])

b = np.array([[2], [3], [2], [9]])

y = forward_substitution(L, b)
print("Solution y:", y)
