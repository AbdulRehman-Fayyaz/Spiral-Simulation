## To run this program you might need to install the following libraries if you haven't already:
## pip install pandas matplotlib numpy scipy
## Also you need to have the Excel file "Abaqus_to_Excel.xlsx" with the correct sheet "Plot_mapping" in the path.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from scipy.optimize import minimize

# --- 1. Data Loading and Preparation ---
# Update the file path and sheet name as needed. 
# file_path = r"C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Abaqus_to_Excel.xlsx"
file_path = r"D:\Universitat Stuttgart - MSc COMMAS\ccSemester-III\Spiral Simulation with Prof Ankit and MSc George\Abaqus_files\Abaqus_to_Excel.xlsx"
sheet_name = "Plot_mapping"

try:
    df = pd.read_excel(file_path, sheet_name=sheet_name, decimal=',')
except Exception as e:
    print(f"Error reading the file: {e}")
    pass

df.columns = df.columns.str.strip()

# Reference coordinates for each node (Q1 to Q6 and Q6 Tip) to ensure the spiral is correctly positioned.
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

# Convert columns to numeric and add reference values to ensure correct positioning of the spiral.
for col, ref_val in ref_coords.items():
    if col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
        df[col] = df[col] + ref_val

# Define the columns for x and y coordinates of the nodes 
x_cols = ['Quad_1_xaxis', 'Quad_2_xaxis', 'Quad_3_xaxis', 'Quad_4_xaxis', 'Quad_5_xaxis', 'Quad_6_xaxis', 'Quad_6_Tip_xaxis']
y_cols = ['Quad_1_yaxis', 'Quad_2_yaxis', 'Quad_3_yaxis', 'Quad_4_yaxis', 'Quad_5_yaxis', 'Quad_6_yaxis', 'Quad_6_Tip_yaxis']

# --- 2. Automated Best-Fit Spiral Solver ---
def optimize_spiral_parameters(x_nodes, y_nodes):
    """Finds a, b, phase, and Theta (t_end) that best fits ALL nodes."""
    tip_x, tip_y = x_nodes[-1], y_nodes[-1]
    
    def objective(params):
        a, b, phi, t_end = params
        
        # Generate the spiral curve up to Theta (t_end)
        t_vals = np.linspace(0, t_end, 150) #the max angle in Abaqus simulation is 150deg (you can refer to export data in Excel file), so we limit the curve to that range for better fitting and to avoid infinite tails
        r = a * np.exp(b * t_vals)
        
        xs = r * np.cos(t_vals + phi) - a * np.cos(phi) + tip_x
        ys = r * np.sin(t_vals + phi) - a * np.sin(phi) + tip_y
        
        # Calculate the closest distance from the generated curve to each node
        total_fit_error = 0
        for nx, ny in zip(x_nodes[:-1], y_nodes[:-1]): # Exclude the tip since it's the anchor
            dists = (xs - nx)**2 + (ys - ny)**2
            total_fit_error += np.min(dists)
            
        # Add a soft constraint to encourage the end of the curve to stop near Q1
        # so we don't get infinite sweeping tails
        end_dist_to_q1 = (xs[-1] - x_nodes[0])**2 + (ys[-1] - y_nodes[0])**2
        
        # Balance the general shape fit with the termination point
        return total_fit_error + (0.5 * end_dist_to_q1)

    # Initial guesses to seed the solver 
    initial_guesses = [
        [0.1, 0.1, 0.0, -np.pi],
        [0.1, 0.1, np.pi/2, -np.pi],
        [0.1, -0.1, np.pi, np.pi],
        [0.05, 0.2, 0.0, -2*np.pi]
    ]
    
    best_res = None
    best_loss = np.inf
    
    for guess in initial_guesses:
        res = minimize(objective, guess, method='Nelder-Mead', options={'maxiter': 2500})
        if res.fun < best_loss:
            best_loss = res.fun
            best_res = res
            
    return best_res.x[0], best_res.x[1], best_res.x[2], best_res.x[3]

def calculate_bounded_spiral(a, b, phi, t_end, start_x, start_y):
    """Calculates final coordinates bounded by Theta (t_end)."""
    theta_vals = np.linspace(0, t_end, 500)
    r = a * np.exp(b * theta_vals)
    x = r * np.cos(theta_vals + phi) - a * np.cos(phi) + start_x
    y = r * np.sin(theta_vals + phi) - a * np.sin(phi) + start_y
    return x, y

# --- 3. Figure and Plot Initialization ---
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.20)

# Get initial data
initial_index = 0
x_vals = df.loc[initial_index, x_cols].values
y_vals = df.loc[initial_index, y_cols].values
initial_angle = df.loc[initial_index, 'Angle_deg']

# Solve for initial spiral
opt_a, opt_b, opt_phi, opt_tend = optimize_spiral_parameters(x_vals, y_vals)
x_spiral, y_spiral = calculate_bounded_spiral(opt_a, opt_b, opt_phi, opt_tend, x_vals[-1], y_vals[-1])

# Plotting
line_quad, = ax.plot(x_vals, y_vals, marker='o', markersize=6, color='#1f77b4', linewidth=2, label='Quad Nodes')
line_spiral, = ax.plot(x_spiral, y_spiral, 'r-', linewidth=1.5, label='Best-Fit Spiral')

# Update title to include a, b, and Theta
title = ax.set_title(f"Angle: {initial_angle:.2f}° | a={opt_a:.5f}, b={opt_b:.3f}, Theta={opt_tend:.2f} rad", fontsize=14)
ax.set_xlabel("X Coordinate (m)", fontsize=12)
ax.set_ylabel("Y Coordinate (m)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
ax.set_aspect('equal')

# --- 4. Angle Slider Setup ---
axcolor = 'lightgoldenrodyellow'
ax_angle = plt.axes([0.15, 0.08, 0.7, 0.03], facecolor=axcolor)

angle_min, angle_max = df['Angle_deg'].min(), df['Angle_deg'].max()
slider_angle = Slider(ax_angle, 'Angle (deg)', angle_min, angle_max, valinit=initial_angle, valfmt='%0.2f')

# --- 5. Update Function ---
def update(val):
    target_angle = slider_angle.val
    
    # Snap to nearest row
    idx = (df['Angle_deg'] - target_angle).abs().idxmin()
    current_angle = df.loc[idx, 'Angle_deg']
    
    # Extract quad coordinates
    new_x = df.loc[idx, x_cols].values
    new_y = df.loc[idx, y_cols].values
    
    # Run dynamic optimization for best fit
    a_new, b_new, phi_new, tend_new = optimize_spiral_parameters(new_x, new_y)
    
    # Generate bounded spiral coordinates
    x_new_spiral, y_new_spiral = calculate_bounded_spiral(
        a_new, b_new, phi_new, tend_new, new_x[-1], new_y[-1]
    )
    
    # Update visual data
    line_quad.set_data(new_x, new_y)
    line_spiral.set_data(x_new_spiral, y_new_spiral)
    
    # Update title with a, b, and Theta
    title.set_text(f"Angle: {current_angle:.2f}° | a={a_new:.5f}, b={b_new:.3f}, Theta={tend_new:.2f} rad")
    
    # Rescale axes to fit
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

slider_angle.on_changed(update)
plt.show()