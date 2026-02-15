import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

outter_points = np.array(
    [
        [0, 3],
        [0, 2],
        [0, 1],
        [0, 0],
        [1, 0],
        [2, 0],
        [2.57, 0.39],
        [2.8, 1],
        [2.8, 1.5],
        [2.8, 2],
        [2.61, 2.59],
        [2, 3],
        [1, 3],
        [0, 3],
    ]
)

# --- 2. Define Nodes for INNER Circle (Radius ~ 0.8) ---
inner_points = np.array(
    [
        [0.82, 2.39],
        [0.82, 1.5],
        [0.82, 0.58],
        [1.59, 0.6],
        [2, 1],
        [2, 2],
        [1.59, 2.39],
        [0.82, 2.39],
    ]
)


# --- 3. Interpolation Function ---
def get_spline_path(x_nodes, y_nodes):
    t = np.arange(len(x_nodes))
    # 'periodic' is CRITICAL here to close the circle smoothly without a corner
    cs_x = CubicSpline(t, x_nodes, bc_type="periodic")
    cs_y = CubicSpline(t, y_nodes, bc_type="periodic")

    t_fine = np.linspace(0, len(x_nodes) - 1, 200)
    return cs_x(t_fine), cs_y(t_fine)


# Generate the smooth paths
x_out_smooth, y_out_smooth = get_spline_path(outter_points[:, 0], outter_points[:, 1])
x_in_smooth, y_in_smooth = get_spline_path(inner_points[:, 0], inner_points[:, 1])

# --- 4. Plotting ---
fig, ax = plt.subplots(figsize=(6, 6))

# A. Draw the Outer Object (The Solid Part)
ax.fill(x_out_smooth, y_out_smooth, color="skyblue")
ax.plot(x_out_smooth, y_out_smooth, "b-", linewidth=2)  # Outline

# B. Draw the Inner Hole (The Trick)
# We fill this with 'white' to erase the center of the blue object
ax.fill(x_in_smooth, y_in_smooth, color="white")
ax.plot(x_in_smooth, y_in_smooth, "b-", linewidth=2)  # Inner Outline

# C. Show Control Nodes
ax.scatter(
    outter_points[:, 0], outter_points[:, 1], color="red", zorder=5, label="Outer Nodes"
)
ax.scatter(
    inner_points[:, 0], inner_points[:, 1], color="green", zorder=5, label="Inner Nodes"
)

# Styling
ax.set_aspect("equal")
ax.set_title("Letter D")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper right")
ax.set_xlim(-0.5, 4)
ax.set_ylim(-0.5, 4)

plt.show()
