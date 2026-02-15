import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def plot_filled_letter(ax, x_nodes, y_nodes, title):
    t = np.arange(len(x_nodes))


    cs_x = CubicSpline(t, x_nodes, bc_type="periodic")
    cs_y = CubicSpline(t, y_nodes, bc_type="periodic")


    t_fine = np.linspace(0, len(x_nodes) - 1, 200)
    x_smooth = cs_x(t_fine)
    y_smooth = cs_y(t_fine)


    ax.plot(x_smooth, y_smooth, "b-", linewidth=2)

    ax.fill(x_smooth, y_smooth, "skyblue", alpha=0.5)

    ax.scatter(x_nodes, y_nodes, color="red", s=40, zorder=5)

    for i, txt in enumerate(t):
        ax.annotate(
            str(i),
            (x_nodes[i], y_nodes[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=9,
            color="black",
            weight="bold",
        )

    ax.set_title(title)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.6)


points_C = np.array(
    [
        [1.0, 0.5],
        [1.5, 0.5],
        [1.5, 1.5],
        [1.33, 1.85],
        [0.8, 2.0],
        [0.0, 2.0],
        [-0.82, 2.0],
        [-1.19, 1.8],
        [-1.4, 0.71],
        [-1.4, 0.0],
        [-1.4, -0.65],
        [-1.4, -1.32],
        [-1.2, -1.79],
        [-0.78, -2.0],
        [0.0, -2.0],
        [0.8, -2.0],
        [1.33, -1.85],
        [1.5, -1.5],
        [1.5, -0.5],
        [1.0, -0.5],
        [1, -1.22],
        [0.67, -1.5],
        [0.0, -1.5],
        [-0.5, -1.5],
        [-0.8, -1],
        [-0.8, 0.0],
        [-0.8, 1.0],
        [-0.5, 1.5],
        [0.0, 1.5],
        [0.67, 1.5],
        [1, 1],
        [1, 0.5],
    ]
)


points_J = np.array(
    [
        [0, 3],
        [0.25, 3],
        [0.5, 3],
        [0.5, 2.5],
        [0.5, 2],
        [0.5, 1],
        [0.4, 0.29],
        [0, 0],
        [-1, 0],
        [-1.3, 0.22],
        [-1.5, 0.5],
        [-1.5, 0.69],
        [-1.5, 1],
        [-1.5, 1.5],
        [-1, 1.5],
        [-1, 1],
        [-0.8, 0.49],
        [-0.31, 0.49],
        [0, 0.81],
        [0, 2],
        [0, 3],
    ]
)


fig, ax = plt.subplots(figsize=(8, 8))
x_nodes = points_C[:, 0]
y_nodes = points_C[:, 1]
title = "Letter C"
plot_filled_letter(ax, x_nodes, y_nodes, title)
plt.show()
fig, ax = plt.subplots(figsize=(8, 8))
x_nodes = points_J[:, 0]
y_nodes = points_J[:, 1]
title = "Letter J"
plot_filled_letter(ax, x_nodes, y_nodes, title)
plt.show()
