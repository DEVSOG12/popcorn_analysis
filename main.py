import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

def is_coprime(m, k):
    """Check if two numbers are coprime."""
    return np.gcd(m, k) == 1

def generate_rational_points(n_points):
    """Generate rational points for the popcorn function."""
    points = []
    for k in range(1, n_points + 1):
        for m in range(0, k + 1):
            if is_coprime(m, k):
                x = m / k
                y = 1 / k
                points.append((x, y))
    return points

# Parameters
n_points = 100
points = generate_rational_points(n_points)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Animated Popcorn Function")

# Initialize the scatter plot with smaller dots (s=2)
scat = ax.scatter([], [], s=2, color='blue')

def animate(i):
    current_points = points[:i + 1]
    x_vals = [p[0] for p in current_points]
    y_vals = [p[1] for p in current_points]
    scat.set_offsets(np.c_[x_vals, y_vals])
    return scat,

ani = FuncAnimation(fig, animate, frames=len(points), interval=50, blit=True)

# Save the animation as an gif file
gif_writer = FFMpegWriter(fps=30)
ani.save("popcorn_function.gif", writer=gif_writer)

