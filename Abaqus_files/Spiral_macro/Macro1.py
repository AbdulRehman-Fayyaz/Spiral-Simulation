# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
import math

def Macro1():
    import section, regionToolset, displayGroupMdbToolset as dgm
    import part, material, assembly, step, interaction, load
    import mesh, optimization, job, sketch, visualization
    import xyPlot, displayGroupOdbToolset as dgo, connectorBehavior

    # =====================================================================
    # PARAMETERS (Modify these to instantly update the geometry)
    # =====================================================================
    scale = 0.001           # Conversion factor to meters (e.g., 50mm -> 0.05m)
    
    W0_mm = 50.0            # Base width of the very first quadrilateral
    alpha_deg = 80.41       # Left interior angle at the base
    beta_deg = 80.41        # Right interior angle at the base
    gamma_deg = 80       # Top-left interior angle (Change this to 45.0 if needed!)
    
    num_quads = 6           # Total number of segments
    
    # Thicknesses of the walls/crossbars for each segment (in mm). 
    # These create the inward offsets for the inner cutouts.
    thicknesses_mm = [10.0, 5.0, 5.0, 3.0, 3.0, 2.0]
    
    extrude_depth = 0.0045  # Depth of the final 3D extrusion in meters
    # =====================================================================

    # Helper function: Finds the intersection of two lines
    def intersect(pt1, theta1, pt2, theta2):
        c1, s1 = math.cos(theta1), math.sin(theta1)
        c2, s2 = math.cos(theta2), math.sin(theta2)
        det = c1 * s2 - s1 * c2
        if abs(det) < 1e-8:
            return None
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        t1 = (dx * s2 - dy * c2) / det
        return (pt1[0] + t1 * c1, pt1[1] + t1 * s1)

    # Convert angles to radians for mathematical computation
    alpha = math.radians(alpha_deg)
    beta = math.radians(beta_deg)
    gamma = math.radians(gamma_deg)

    quads = []

    # 1. Calculate Outer Quadrilaterals
    for i in range(num_quads):
        if i == 0:
            A = (0.0, 0.0)
            B = (W0_mm * scale, 0.0)
        else:
            A = quads[-1][3] # Inherit previous Top-Left as new Bottom-Left
            B = quads[-1][2] # Inherit previous Top-Right as new Bottom-Right
            
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        W_i = math.hypot(dx, dy)
        theta_base = math.atan2(dy, dx)
        
        # Left side length matches its local base length
        L_i = W_i  

        # Calculate Top-Left vertex (D)
        D = (A[0] + L_i * math.cos(theta_base + alpha),
             A[1] + L_i * math.sin(theta_base + alpha))

        # Calculate Top-Right vertex (C) via line intersection
        theta_top = theta_base + alpha + gamma - math.pi
        theta_right = theta_base + math.pi - beta
        C = intersect(D, theta_top, B, theta_right)
        
        quads.append([A, B, C, D])

    # 2. Calculate Inner Holes (Inward Offsets)
    holes = []
    for i in range(num_quads):
        t = thicknesses_mm[i] * scale
        Q = quads[i]
        hole = []
        for j in range(4):
            P_prev = Q[(j - 1) % 4]
            P_curr = Q[j]
            P_next = Q[(j + 1) % 4]

            # Inward normal of edge 1
            dx1, dy1 = P_curr[0] - P_prev[0], P_curr[1] - P_prev[1]
            L1 = math.hypot(dx1, dy1)
            nx1, ny1 = -dy1 / L1, dx1 / L1

            # Inward normal of edge 2
            dx2, dy2 = P_next[0] - P_curr[0], P_next[1] - P_curr[1]
            L2 = math.hypot(dx2, dy2)
            nx2, ny2 = -dy2 / L2, dx2 / L2

            # Shift lines inward by thickness 't'
            pt1 = (P_curr[0] + t * nx1, P_curr[1] + t * ny1)
            pt2 = (P_curr[0] + t * nx2, P_curr[1] + t * ny2)
            theta1, theta2 = math.atan2(dy1, dx1), math.atan2(dy2, dx2)

            # Intersection of offset lines gives the inner hole vertex
            P_inner = intersect(pt1, theta1, pt2, theta2)
            hole.append(P_inner)
        holes.append(hole)

    # 3. Build Abaqus Sketch
    # Delete sketch/part if they exist to allow clean re-runs of the script
    try:
        del mdb.models['Model-1'].sketches['__profile__']
    except:
        pass

    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.5)
    s1.sketchOptions.setValues(decimalPlaces=4)
    s1.setPrimaryObject(option=STANDALONE)

    # Draw the continuous outer perimeter
    perimeter_points = [quads[0][0], quads[0][1]]
    for i in range(num_quads):
        perimeter_points.append(quads[i][2])
    for i in range(num_quads-1, -1, -1):
        perimeter_points.append(quads[i][3])

    for i in range(len(perimeter_points)):
        p1 = perimeter_points[i]
        p2 = perimeter_points[(i+1) % len(perimeter_points)]
        s1.Line(point1=p1, point2=p2)

    # Draw the inner holes
    # Abaqus automatically recognizes closed loops inside a perimeter as cutouts
    for hole in holes:
        for i in range(4):
            p1 = hole[i]
            p2 = hole[(i+1) % 4]
            s1.Line(point1=p1, point2=p2)

    # 4. Extrude to create the 3D part
    if 'Part-1' in mdb.models['Model-1'].parts:
        del mdb.models['Model-1'].parts['Part-1']

    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p.BaseSolidExtrude(sketch=s1, depth=extrude_depth)
    s1.unsetPrimaryObject()
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

Macro1()