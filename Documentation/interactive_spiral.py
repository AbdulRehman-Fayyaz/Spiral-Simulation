import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- 1. Mathematical Setup ---
# The equation is r = a * e^(b * theta) (Polar coordinates)
# To plot it, we need to convert to Cartesian coordinates (x, y):
# x = r * cos(theta)
# y = r * sin(theta)

# Define the domain for theta. The value 0 <= theta <= 100.
# We use 2000 points for a very smooth curve over this long range.
theta = np.linspace(0, 100, 2000)

# Initial parameter values from the image
a_init = -0.1
b_init = 0.2

# Function to calculate coordinates based on parameters
def calculate_spiral_coords(a, b, theta_vals):
    r = a * np.exp(b * theta_vals)
    x = r * np.cos(theta_vals)
    y = r * np.sin(theta_vals)
    return x, y

# Calculate initial data
x_data, y_data = calculate_spiral_coords(a_init, b_init, theta)


# --- 2. Plotting Setup ---
# Create the figure and main axes object
fig, ax = plt.subplots(figsize=(9, 7))

# Adjust the bottom of the plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)

# Plot the initial line. We store the 'line' object to update it later.
# We use a red color ('r-').
line, = ax.plot(x_data, y_data, 'r-', linewidth=1.5)

# Set chart styling
ax.set_title(r'Logarithmic Spiral: $r = a \cdot e^{b\theta}$', fontsize=14)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=0.8) # Add X-axis line
ax.axvline(x=0, color='k', linewidth=0.8) # Add Y-axis line

# Crucial for spirals: keep aspect ratio equal so circles look round
ax.set_aspect('equal')


# --- 3. Slider Implementation ---
# Define axes areas for the sliders [left, bottom, width, height]
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.20, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.20, 0.05, 0.65, 0.03], facecolor=axcolor)

# Create the Slider objects
# Range for 'a': -1 to 1
s_a = Slider(ax_a, 'Param a', -1.0, 1.0, valinit=a_init, valfmt='%0.2f')

# Range for 'b': We use a smaller range than 0 to 0.5
# Because 'b' is in the exponent, large values make the spiral explode astronomically fast.
# A range of 0 to 0.5 provides good interactive visualization.
s_b = Slider(ax_b, 'Param b', 0, 0.5, valinit=b_init, valfmt='%0.3f')


# --- 4. Update Function ---
def update(val):
    """This function is called anytime a slider is moved."""
    # 1. Get current values from the sliders
    a_current = s_a.val
    b_current = s_b.val

    # 2. Recalculate x and y data
    x_new, y_new = calculate_spiral_coords(a_current, b_current, theta)

    # 3. Update the existing line with new data
    line.set_xdata(x_new)
    line.set_ydata(y_new)

    # 4. Rescale the axes. Because exponential spirals grow very fast,
    # we must update the view limits to see the curve.
    ax.relim()           # Re-compute data limits based on new line data
    ax.autoscale_view()  # Update axes views using new limits

    # 5. Redraw the figure
    fig.canvas.draw_idle()

# Register the update function with the sliders
s_a.on_changed(update)
s_b.on_changed(update)

# Display the plot
plt.show()