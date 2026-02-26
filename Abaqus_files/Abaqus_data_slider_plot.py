import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# 1. Define file path and sheet name
file_path = r"D:\Universitat Stuttgart - MSc COMMAS\ccSemester-III\Spiral Simulation with Prof Ankit and MSc George\Abaqus_files\Abaqus_to_Excel.xlsx"
sheet_name = "Final_refined"

# 2. Read the data from Excel
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name, decimal=',')
except Exception as e:
    print(f"Error reading the file: {e}")
    pass

# Clean up column names just in case there are trailing spaces
df.columns = df.columns.str.strip()

# 3. Define the actual reference positions (Time = 0)
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

# 4. Correct the data by adding the reference positions to the displacements
for col, ref_val in ref_coords.items():
    if col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
        df[col] = df[col] + ref_val

# 5. Prepare lists of X and Y column names in the correct geometric order
x_cols = ['Quad_1_xaxis', 'Quad_2_xaxis', 'Quad_3_xaxis', 'Quad_4_xaxis', 'Quad_5_xaxis', 'Quad_6_xaxis', 'Quad_6_Tip_xaxis']
y_cols = ['Quad_1_yaxis', 'Quad_2_yaxis', 'Quad_3_yaxis', 'Quad_4_yaxis', 'Quad_5_yaxis', 'Quad_6_yaxis', 'Quad_6_Tip_yaxis']

# 6. Setup the Figure and Axes
fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.25) # Shrink the main plot to make room for the slider at the bottom

# Calculate min and max values across the entire dataset to keep the axes fixed
x_min, x_max = df[x_cols].min().min(), df[x_cols].max().max()
y_min, y_max = df[y_cols].min().min(), df[y_cols].max().max()

# Add a 10% margin so the curve doesn't touch the edges of the plot
x_margin = (x_max - x_min) * 0.1
y_margin = (y_max - y_min) * 0.1
ax.set_xlim(x_min - x_margin, x_max + x_margin)
ax.set_ylim(y_min - y_margin, y_max + y_margin)

ax.set_xlabel("X Coordinate (m)", fontsize=12)
ax.set_ylabel("Y Coordinate (m)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

# 7. Plot the Initial State (Index 0)
initial_index = 0
x_vals = df.loc[initial_index, x_cols].values
y_vals = df.loc[initial_index, y_cols].values
initial_time = df.loc[initial_index, 'Time']

# We save the plotted line in a variable so we can update its data later
line, = ax.plot(x_vals, y_vals, marker='o', markersize=6, color='#1f77b4', linewidth=2)
title = ax.set_title(f"Deformation at Timestamp: {initial_time:.4f}", fontsize=14)

# 8. Create the Slider
# Define the axes area for the slider [left, bottom, width, height]
ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
num_steps = len(df)

time_slider = Slider(
    ax=ax_slider,
    label='Time Step Index',
    valmin=0,
    valmax=num_steps - 1,
    valinit=initial_index,
    valstep=1 # Forces the slider to snap to whole numbers (DataFrame indices)
)

# 9. Define the Update Function
def update(val):
    # Get the current index from the slider
    idx = int(time_slider.val)
    
    # Extract the new coordinates and time
    new_x = df.loc[idx, x_cols].values
    new_y = df.loc[idx, y_cols].values
    current_time = df.loc[idx, 'Time']
    
    # Update the line data and the title
    line.set_data(new_x, new_y)
    title.set_text(f"Deformation at Timestamp: {current_time:.4f}")
    
    # Redraw the figure
    fig.canvas.draw_idle()

# Connect the update function to the slider
time_slider.on_changed(update)

# Show the plot
plt.show()