import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# 1. Define file path and sheet name
file_path = r"C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Abaqus_to_Excel.xlsx"
sheet_name = "Final_refined"

# 2. Read the data from Excel
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name, decimal=',')
except Exception as e:
    print(f"Error reading the file: {e}")
    pass

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

# 5. Prepare lists of X and Y column names
x_cols = [
    'Quad_1_xaxis', 'Quad_2_xaxis', 'Quad_3_xaxis', 'Quad_4_xaxis', 
    'Quad_5_xaxis', 'Quad_6_xaxis', 'Quad_6_Tip_xaxis'
]
y_cols = [
    'Quad_1_yaxis', 'Quad_2_yaxis', 'Quad_3_yaxis', 'Quad_4_yaxis', 
    'Quad_5_yaxis', 'Quad_6_yaxis', 'Quad_6_Tip_yaxis'
]

# ==========================================
# FIGURE 1: STATIC PLOT (All Curves)
# ==========================================
fig1, ax1 = plt.subplots(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

for index, row in df.iterrows():
    x_vals = row[x_cols].values
    y_vals = row[y_cols].values
    time_val = row['Time']
    ax1.plot(x_vals, y_vals, marker='o', markersize=4, color=colors[index], label=f"t={time_val:.4f}")

ax1.set_title("Deformation of the 7 Points over Time (Static Overview)", fontsize=14)
ax1.set_xlabel("X Coordinate (m)", fontsize=12)
ax1.set_ylabel("Y Coordinate (m)", fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(bbox_to_anchor=(1.04, 1), loc="upper left", title="Time Stamps", fontsize=8, ncol=2)
fig1.tight_layout()

# ==========================================
# FIGURE 2: INTERACTIVE PLOT (Slider)
# ==========================================
fig2, ax2 = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25) # Make room for the slider at the bottom

# Initial plot setup (using index 0)
init_idx = 0
x_vals_init = df.iloc[init_idx][x_cols].values
y_vals_init = df.iloc[init_idx][y_cols].values
time_init = df.iloc[init_idx]['Time']

# Plot the initial line and keep a reference to it
line, = ax2.plot(x_vals_init, y_vals_init, marker='o', markersize=6, color='red', linewidth=2, label=f"t = {time_init:.4f}")

ax2.set_title("Interactive Deformation (Use Slider Below)", fontsize=14)
ax2.set_xlabel("X Coordinate (m)", fontsize=12)
ax2.set_ylabel("Y Coordinate (m)", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
legend2 = ax2.legend(loc="upper left")

# Calculate global min and max to keep axes fixed during animation
x_min, x_max = df[x_cols].min().min(), df[x_cols].max().max()
y_min, y_max = df[y_cols].min().min(), df[y_cols].max().max()

# Add a small buffer to the limits
x_buffer = (x_max - x_min) * 0.05
y_buffer = (y_max - y_min) * 0.05
ax2.set_xlim(x_min - x_buffer, x_max + x_buffer)
ax2.set_ylim(y_min - y_buffer, y_max + y_buffer)

# Create the slider axis and widget
ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03], facecolor='lightgray')
time_slider = Slider(
    ax=ax_slider,
    label='Time Step',
    valmin=0,
    valmax=len(df) - 1,
    valinit=init_idx,
    valfmt='%d' # Format as integer index
)

# Function to run when the slider is moved
def update(val):
    # Get the integer index from the slider
    idx = int(time_slider.val)
    
    # Extract new X, Y, and Time
    new_x = df.iloc[idx][x_cols].values
    new_y = df.iloc[idx][y_cols].values
    new_t = df.iloc[idx]['Time']
    
    # Update the line data
    line.set_xdata(new_x)
    line.set_ydata(new_y)
    
    # Update the legend text with the current timestamp
    legend2.get_texts()[0].set_text(f"t = {new_t:.4f}")
    
    # Redraw the figure
    fig2.canvas.draw_idle()

# Attach the update function to the slider
time_slider.on_changed(update)

# Show both figures
plt.show()