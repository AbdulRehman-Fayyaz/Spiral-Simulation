import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# --- 1. Data Loading and Preparation ---
file_path = r"C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Abaqus_to_Excel.xlsx"
sheet_name = "Plot_mapping" # Updated to the requested sheet

try:
    df = pd.read_excel(file_path, sheet_name=sheet_name, decimal=',')
except Exception as e:
    print(f"Error reading the file: {e}")
    # Create dummy data just in case the file isn't found during testing
    pass

df.columns = df.columns.str.strip()

# Define the actual reference positions (Angle/Time = 0)
ref_coords = {
    'Quad_1_xaxis': 0.0,
    'Quad_1_yaxis': 0.0,
    'Quad_2_xaxis': 8.3313e-3,
    'Quad_2_yaxis': 49.3010e-3,
    'Quad_3_xaxis': 26.3689e-3,
    'Quad_3_yaxis': 82.1895e-3,
    'Quad_4_xaxis': 47.2532e-3,
    'Quad_4_yaxis': 101.0580e-3,
    'Quad_5_xaxis': 66.6995e-3,
    'Quad_5_yaxis': 109.2794e-3,
    'Quad_6_xaxis': 82.5055e-3,
    'Quad_6_yaxis': 110.3105e-3,
    'Quad_6_Tip_xaxis': 93.9615e-3,
    'Quad_6_Tip_yaxis': 107.1510e-3
}

# Correct the data by adding the reference positions to the displacements
for col, ref_val in ref_coords.items():
    if col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
        df[col] = df[col] + ref_val

# Prepare lists of X and Y column names in the correct geometric order
x_cols = ['Quad_1_xaxis', 'Quad_2_xaxis', 'Quad_3_xaxis', 'Quad_4_xaxis', 'Quad_5_xaxis', 'Quad_6_xaxis', 'Quad_6_Tip_xaxis']
y_cols = ['Quad_1_yaxis', 'Quad_2_yaxis', 'Quad_3_yaxis', 'Quad_4_yaxis', 'Quad_5_yaxis', 'Quad_6_yaxis', 'Quad_6_Tip_yaxis']

# --- 2. Mathematical Setup for Spiral ---
theta_spiral = np.linspace(0, 100, 2000)
a_init = 0.00001
b_init = 0.2

def calculate_spiral_coords(a, b, theta_vals, start_x, start_y):
    """Calculates spiral and shifts its origin (theta=0) to the Quad 6 tip."""
    r = a * np.exp(b * theta_vals)
    x = r * np.cos(theta_vals)
    y = r * np.sin(theta_vals)
    
    # At theta=0, the spiral is at (a, 0). 
    # We subtract (a, 0) and add the Quad 6 tip coordinates to translate the start point.
    x_translated = x - a + start_x
    y_translated = y - 0 + start_y
    return x_translated, y_translated

# --- 3. Figure and Plot Initialization ---
fig, ax = plt.subplots(figsize=(10, 8))
# Make room at the bottom for 3 sliders
plt.subplots_adjust(bottom=0.35)

# Initial quad data
initial_index = 0
x_vals = df.loc[initial_index, x_cols].values
y_vals = df.loc[initial_index, y_cols].values
initial_angle = df.loc[initial_index, 'Angle_deg']

# Initial Quad 6 Tip coordinates
tip_x_init = x_vals[-1]
tip_y_init = y_vals[-1]

# Initial spiral data
x_spiral, y_spiral = calculate_spiral_coords(a_init, b_init, theta_spiral, tip_x_init, tip_y_init)

# Plot both lines
line_quad, = ax.plot(x_vals, y_vals, marker='o', markersize=6, color='#1f77b4', linewidth=2, label='Quad Deformation')
line_spiral, = ax.plot(x_spiral, y_spiral, 'r-', linewidth=1.5, label='Logarithmic Spiral')

title = ax.set_title(f"Deformation & Spiral at Angle: {initial_angle:.2f}°", fontsize=14)
ax.set_xlabel("X Coordinate (m)", fontsize=12)
ax.set_ylabel("Y Coordinate (m)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
ax.set_aspect('equal')

# --- 4. Sliders Setup ---
axcolor = 'lightgoldenrodyellow'

# Define axes for sliders: [left, bottom, width, height]
ax_angle = plt.axes([0.15, 0.20, 0.7, 0.03], facecolor=axcolor)
ax_a = plt.axes([0.15, 0.12, 0.7, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.15, 0.04, 0.7, 0.03], facecolor=axcolor)

# Find min and max angles for the slider
angle_min = df['Angle_deg'].min()
angle_max = df['Angle_deg'].max()

# Create the 3 sliders
slider_angle = Slider(ax_angle, 'Angle (deg)', angle_min, angle_max, valinit=initial_angle, valfmt='%0.2f')
slider_a = Slider(ax_a, 'Param a', -.05, 0.05, valinit=a_init, valfmt='%0.5f')
slider_b = Slider(ax_b, 'Param b', 0.0, 0.5, valinit=b_init, valfmt='%0.3f')

# --- 5. Update Function ---
def update(val):
    # 1. Get current values from all sliders
    target_angle = slider_angle.val
    a_current = slider_a.val
    b_current = slider_b.val
    
    # 2. Find the closest row in the dataframe to the slider's angle
    idx = (df['Angle_deg'] - target_angle).abs().idxmin()
    current_angle = df.loc[idx, 'Angle_deg']
    
    # 3. Extract the new coordinates for the Quads
    new_x = df.loc[idx, x_cols].values
    new_y = df.loc[idx, y_cols].values
    
    # 4. Get the exact coordinates of Quad 6 Tip to anchor the spiral
    current_tip_x = new_x[-1]
    current_tip_y = new_y[-1]
    
    # 5. Recalculate spiral coordinates anchored to the new tip
    x_new_spiral, y_new_spiral = calculate_spiral_coords(
        a_current, b_current, theta_spiral, current_tip_x, current_tip_y
    )
    
    # 6. Update line data
    line_quad.set_data(new_x, new_y)
    line_spiral.set_data(x_new_spiral, y_new_spiral)
    title.set_text(f"Deformation & Spiral at Angle: {current_angle:.2f}°")
    
    # 7. Rescale axes to ensure the spiral remains visible
    ax.relim()
    #ax.autoscale_view()
    
    # 8. Redraw
    fig.canvas.draw_idle()

# Connect the update function to all sliders
slider_angle.on_changed(update)
slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()