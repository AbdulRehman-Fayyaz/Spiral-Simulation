# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
import math

def BuildParametricSpiralWithCut():
    import section, regionToolset, displayGroupMdbToolset as dgm
    import part, material, assembly, step, interaction, load
    import mesh, optimization, job, sketch, visualization
    import xyPlot, displayGroupOdbToolset as dgo, connectorBehavior

    # =====================================================================
    # PARAMETERS
    # =====================================================================
    scale = 0.001           # Conversion factor to meters (e.g., 50mm -> 0.05m)
    
    # --- Base Geometry ---
    W0_mm = 50.0            # Base width of the very first quadrilateral
    alpha_deg = 80.41       # Left interior angle at the base
    beta_deg = 80.41        # Right interior angle at the base
    gamma_deg = 80.42       # Top-left interior angle
    
    num_quads = 6           # Total number of segments
    thicknesses_mm = [10.0, 5.0, 5.0, 3.0, 3.0, 2.0] # Inner hole offsets
    extrude_depth = 0.0045  # Depth of the 3D part in meters (4.5mm)
    
    # --- Cut Geometry ---
    gap_thickness_mm = 0.5  # Size of the empty gap splitting the part in the Z-direction
    web_thickness_mm = 0.1  # Thickness of the solid material connecting the halves
    web_side = "LEFT"       # Choose "LEFT" or "RIGHT" side for the connecting web 
    # =====================================================================

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

    alpha, beta, gamma = math.radians(alpha_deg), math.radians(beta_deg), math.radians(gamma_deg)

    # 1. Calculate Outer Quadrilaterals
    quads = []
    for i in range(num_quads):
        if i == 0:
            A, B = (0.0, 0.0), (W0_mm * scale, 0.0)
        else:
            A, B = quads[-1][3], quads[-1][2] 
            
        dx, dy = B[0] - A[0], B[1] - A[1]
        theta_base = math.atan2(dy, dx)
        L_i = math.hypot(dx, dy)  
        
        D = (A[0] + L_i * math.cos(theta_base + alpha), A[1] + L_i * math.sin(theta_base + alpha))
        theta_top = theta_base + alpha + gamma - math.pi
        theta_right = theta_base + math.pi - beta
        C = intersect(D, theta_top, B, theta_right)
        quads.append([A, B, C, D])

    # 2. Calculate Inner Holes
    holes = []
    for i in range(num_quads):
        t = thicknesses_mm[i] * scale
        Q = quads[i]
        hole = []
        for j in range(4):
            P_prev, P_curr, P_next = Q[(j - 1) % 4], Q[j], Q[(j + 1) % 4]
            dx1, dy1 = P_curr[0] - P_prev[0], P_curr[1] - P_prev[1]
            dx2, dy2 = P_next[0] - P_curr[0], P_next[1] - P_curr[1]
            L1, L2 = math.hypot(dx1, dy1), math.hypot(dx2, dy2)
            nx1, ny1 = -dy1 / L1, dx1 / L1
            nx2, ny2 = -dy2 / L2, dx2 / L2
            
            pt1 = (P_curr[0] + t * nx1, P_curr[1] + t * ny1)
            pt2 = (P_curr[0] + t * nx2, P_curr[1] + t * ny2)
            hole.append(intersect(pt1, math.atan2(dy1, dx1), pt2, math.atan2(dy2, dx2)))
        holes.append(hole)

    # 3. Calculate the Smart Cut Polygon (The Tool)
    perimeter = [quads[0][0], quads[0][1]]
    for i in range(num_quads): perimeter.append(quads[i][2])
    for i in range(num_quads-1, -1, -1): perimeter.append(quads[i][3])
    N_perim = len(perimeter)

    shifts = []
    for i in range(N_perim):
        # i=0 is Bottom, i=1..6 is Right, i=7 is Top, i=8..13 is Left
        if web_side == "LEFT" and i >= num_quads + 2:
            shifts.append(-web_thickness_mm * scale) # Shrink inward to leave a web
        elif web_side == "RIGHT" and 1 <= i <= num_quads:
            shifts.append(-web_thickness_mm * scale) # Shrink inward to leave a web
        else:
            shifts.append(2.0 * scale) # 2mm outward expansion to guarantee a clean cut

    shifted_lines = []
    for i in range(N_perim):
        p1, p2 = perimeter[i], perimeter[(i+1) % N_perim]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        L = math.hypot(dx, dy)
        nx, ny = dy/L, -dx/L
        shift_p1 = (p1[0] + shifts[i]*nx, p1[1] + shifts[i]*ny)
        shifted_lines.append((shift_p1, shift_p1, math.atan2(dy, dx)))

    cut_poly = []
    for i in range(N_perim):
        prev = shifted_lines[(i - 1) % N_perim]
        curr = shifted_lines[i]
        cut_poly.append(intersect(prev[0], prev[2], curr[0], curr[2]))

    # =====================================================================
    # CLEAR OLD DATA
    # =====================================================================
    for p_name in ['Part-1', 'Tool', 'Final_Part']:
        if p_name in mdb.models['Model-1'].parts:
            del mdb.models['Model-1'].parts[p_name]
    try: del mdb.models['Model-1'].sketches['__profile__']
    except: pass
    try: del mdb.models['Model-1'].sketches['__tool_profile__']
    except: pass

    # =====================================================================
    # BUILD GEOMETRY & EXECUTE ASSEMBLY CUT
    # =====================================================================
    # Build Base Part
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.5)
    s1.setPrimaryObject(option=STANDALONE)
    for i in range(N_perim): s1.Line(point1=perimeter[i], point2=perimeter[(i+1) % N_perim])
    for hole in holes:
        for i in range(4): s1.Line(point1=hole[i], point2=hole[(i+1) % 4])
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p.BaseSolidExtrude(sketch=s1, depth=extrude_depth)
    s1.unsetPrimaryObject()

    # Build Tool Part
    s2 = mdb.models['Model-1'].ConstrainedSketch(name='__tool_profile__', sheetSize=0.5)
    s2.setPrimaryObject(option=STANDALONE)
    for i in range(N_perim): s2.Line(point1=cut_poly[i], point2=cut_poly[(i+1) % N_perim])
    p_tool = mdb.models['Model-1'].Part(name='Tool', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p_tool.BaseSolidExtrude(sketch=s2, depth=(gap_thickness_mm * scale))
    s2.unsetPrimaryObject()

    # Assembly Boolean Cut
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    for inst_name in a.instances.keys(): del a.instances[inst_name]
        
    inst1 = a.Instance(name='Part-1-1', part=p, dependent=ON)
    inst2 = a.Instance(name='Tool-1', part=p_tool, dependent=ON)
    
    # Move the tool exactly to the middle (e.g., Z = 2.0mm)
    cut_start_z = (extrude_depth - (gap_thickness_mm * scale)) / 2.0
    a.translate(instanceList=('Tool-1', ), vector=(0.0, 0.0, cut_start_z))
    
    # Execute subtraction to generate Final_Part
    a.InstanceFromBooleanCut(name='Final_Part', 
                             instanceToBeCut=a.instances['Part-1-1'], 
                             cuttingInstances=(a.instances['Tool-1'], ), 
                             originalInstances=DELETE)

    # Show the result!
    final_p = mdb.models['Model-1'].parts['Final_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=final_p)

BuildParametricSpiralWithCut()