import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Define file path and sheet name
file_path = r"C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Abaqus_to_Excel.xlsx"
sheet_name = "Final_refined"

# 2. Read the data from Excel
# We use decimal=',' in case your Excel file uses commas for decimal points
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name, decimal=',')
except Exception as e:
    print(f"Error reading the file: {e}")
    # Fallback to creating DataFrame from raw text if testing without the file
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
        # Check if data was imported as a string containing commas, convert to float
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
        
        # Add the reference coordinate to the imported Abaqus displacement values
        df[col] = df[col] + ref_val

# 5. Prepare lists of X and Y column names in the correct geometric order
x_cols = [
    'Quad_1_xaxis', 'Quad_2_xaxis', 'Quad_3_xaxis', 'Quad_4_xaxis', 
    'Quad_5_xaxis', 'Quad_6_xaxis', 'Quad_6_Tip_xaxis'
]
y_cols = [
    'Quad_1_yaxis', 'Quad_2_yaxis', 'Quad_3_yaxis', 'Quad_4_yaxis', 
    'Quad_5_yaxis', 'Quad_6_yaxis', 'Quad_6_Tip_yaxis'
]

# 6. Plotting
plt.figure(figsize=(12, 8))

# Colormap to give a gradient color to lines based on time
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

# Iterate over each row (time stamp) and plot the 7 points connected by a curve
for index, row in df.iterrows():
    # Extract the X and Y coordinates for the 7 points at this specific time step
    x_vals = row[x_cols].values
    y_vals = row[y_cols].values
    time_val = row['Time']
    
    # Plot the curve for the current time step
    plt.plot(x_vals, y_vals, marker='o', markersize=4, 
             color=colors[index], label=f"t={time_val:.4f}")

# Formatting the plot
plt.title("Deformation of the 7 Points over Time (Corrected w.r.t Reference)", fontsize=14)
plt.xlabel("X Coordinate (m)", fontsize=12)
plt.ylabel("Y Coordinate (m)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Handle the legend (since there are ~40 curves, place it outside the plot)
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", title="Time Stamps", fontsize=8, ncol=2)

# Adjust layout so the legend is not cut off
plt.tight_layout()

# Show the final plot
plt.show()