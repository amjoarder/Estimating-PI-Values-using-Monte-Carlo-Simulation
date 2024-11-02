import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_points = 10000

# Generate random points
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Calculate the distance from the origin
distance = np.sqrt(x**2 + y**2)
inside_circle = distance <= 1



#Visualization from here
# Initialize figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create scatter plots for inside and outside points
inside_points, = ax.plot([], [], 'o', color="green", markersize=4, label="Inside Circle")
outside_points, = ax.plot([], [], 'o', color="magenta", markersize=4, label="Outside Circle")

#Full circle
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, linestyle='--')
ax.add_artist(circle)


# Display Text
pi_text = ax.text(-0.95, 0.9, '', fontsize=12)

# Animation update function
def update(frame):
    current_x = x[:frame]
    current_y = y[:frame]
    current_inside = inside_circle[:frame]
    
    # Update inside and outside points
    inside_points.set_data(current_x[current_inside], current_y[current_inside])
    outside_points.set_data(current_x[~current_inside], current_y[~current_inside])

    # Update π estimate
    pi_estimate = (current_inside.sum() / frame) * 4
    pi_text.set_text(f'Estimated π: {pi_estimate:.4f}')
    return inside_points, outside_points, pi_text


ani = FuncAnimation(fig, update, frames=np.arange(1, num_points+1), interval=1, repeat=False)

# Display plot with animation
plt.legend(loc="upper right")
plt.title("Monte Carlo Simulation for π Estimation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, which='both', linestyle='-', linewidth=0.1)
plt.show()


'''
#Alternate method without visualization
import random

# Function to estimate PI
def estimate_pi(num_points: int) -> float:
    points_inside_circle = 0

    for _ in range(num_points):
        # Generate random point (x, y) in the range [-1, 1]
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # Estimate PI using the ratio of points inside the circle to the total points
    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

# Example: Estimate PI using 1 million points
num_points = 1_000_000
pi_estimate = estimate_pi(num_points)
pi_estimate
'''






'''
#Show each iteration
import random

# Function to estimate PI with real-time display
def estimate_pi(num_points: int) -> float:
    points_inside_circle = 0

    for i in range(1, num_points + 1):
        # Generate random point (x, y) in the range [-1, 1]
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

        # Estimate PI using the ratio of points inside the circle to the total points
        pi_estimate = 4 * points_inside_circle / i

        # Print the current estimate after each iteration
        print(f"{pi_estimate:.6f}")

    return pi_estimate

# Example: Estimate PI using a specified number of points
num_points = 100
pi_estimate = estimate_pi(num_points)
'''