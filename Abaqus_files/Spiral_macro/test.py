# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
import math

def BuildParametricSpiralFinal():
    import section, regionToolset, displayGroupMdbToolset as dgm
    import part, material, assembly, step, interaction, load
    import mesh, optimization, job, sketch, visualization
    import xyPlot, displayGroupOdbToolset as dgo, connectorBehavior

    # =====================================================================
    # PARAMETERS
    # =====================================================================
    scale = 0.001           # Conversion factor to meters (e.g., 50mm -> 0.05m)
    
    # --- Base Geometry ---
    W0_mm = 50.0            
    alpha_deg = 80.41       
    beta_deg = 80.41        
    gamma_deg = 80.42       
    
    num_quads = 6           
    thicknesses_mm = [10.0, 5.0, 5.0, 3.0, 3.0, 2.0] 
    extrude_depth = 0.0045  
    
    # --- Cut Geometry ---
    gap_thickness_mm = 0.5  
    web_thickness_mm = 0.1  
    web_side = "LEFT"       
    divider_cut_width_mm = 0.5   
    divider_cut_depth_mm = 1.9   

    # --- Material Properties ---
    tape_density = 880.0
    tape_E = 500e6
    tape_nu = 0.34
    
    ply_density = 680.0
    ply_E = 7e9
    ply_nu = 0.13

    # --- Mesh Properties ---
    mesh_size_mm = 2.5      # Global mesh seed size in mm
    # =====================================================================

    def intersect(pt1, theta1, pt2, theta2):
        c1, s1 = math.cos(theta1), math.sin(theta1)
        c2, s2 = math.cos(theta2), math.sin(theta2)
        det = c1 * s2 - s1 * c2
        if abs(det) < 1e-8: return None
        dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
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

    # 3. Calculate Gap Cut Polygon
    perimeter = [quads[0][0], quads[0][1]]
    for i in range(num_quads): perimeter.append(quads[i][2])
    for i in range(num_quads-1, -1, -1): perimeter.append(quads[i][3])
    N_perim = len(perimeter)

    shifts = []
    for i in range(N_perim):
        if web_side == "LEFT" and i >= num_quads + 2: shifts.append(-web_thickness_mm * scale)
        elif web_side == "RIGHT" and 1 <= i <= num_quads: shifts.append(-web_thickness_mm * scale)
        else: shifts.append(2.0 * scale)

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

    # 4. Calculate Face Divider Rectangles
    divider_rects = []
    divider_segments = [] 
    for i in range(num_quads - 1):
        P1, P2 = quads[i][3], quads[i][2] 
        divider_segments.append((P1, P2))
        dx, dy = P2[0] - P1[0], P2[1] - P1[1]
        L = math.hypot(dx, dy)
        ux, uy = dx/L, dy/L
        nx, ny = -uy, ux
        hw = (divider_cut_width_mm / 2.0) * scale
        ext = 5.0 * scale 
        
        C1 = (P1[0] - ext*ux + hw*nx, P1[1] - ext*uy + hw*ny)
        C2 = (P2[0] + ext*ux + hw*nx, P2[1] + ext*uy + hw*ny)
        C3 = (P2[0] + ext*ux - hw*nx, P2[1] + ext*uy - hw*ny)
        C4 = (P1[0] - ext*ux - hw*nx, P1[1] - ext*uy - hw*ny)
        divider_rects.append([C1, C2, C3, C4])

    # =====================================================================
    # GEOMETRY GENERATION
    # =====================================================================
    for p_name in ['Part-1', 'Gap_Tool', 'Divider_Tool', 'Final_Part']:
        if p_name in mdb.models['Model-1'].parts: del mdb.models['Model-1'].parts[p_name]
    for s_name in ['__profile__', '__gap_profile__', '__divider_profile__']:
        try: del mdb.models['Model-1'].sketches[s_name]
        except: pass

    # Build Parts
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.5)
    s1.setPrimaryObject(option=STANDALONE)
    for i in range(N_perim): s1.Line(point1=perimeter[i], point2=perimeter[(i+1) % N_perim])
    for hole in holes:
        for i in range(4): s1.Line(point1=hole[i], point2=hole[(i+1) % 4])
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p.BaseSolidExtrude(sketch=s1, depth=extrude_depth)
    s1.unsetPrimaryObject()

    s2 = mdb.models['Model-1'].ConstrainedSketch(name='__gap_profile__', sheetSize=0.5)
    s2.setPrimaryObject(option=STANDALONE)
    for i in range(N_perim): s2.Line(point1=cut_poly[i], point2=cut_poly[(i+1) % N_perim])
    p_gap = mdb.models['Model-1'].Part(name='Gap_Tool', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p_gap.BaseSolidExtrude(sketch=s2, depth=(gap_thickness_mm * scale))
    s2.unsetPrimaryObject()

    s3 = mdb.models['Model-1'].ConstrainedSketch(name='__divider_profile__', sheetSize=0.5)
    s3.setPrimaryObject(option=STANDALONE)
    for rect in divider_rects:
        for j in range(4): s3.Line(point1=rect[j], point2=rect[(j+1)%4])
    p_div = mdb.models['Model-1'].Part(name='Divider_Tool', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p_div.BaseSolidExtrude(sketch=s3, depth=(divider_cut_depth_mm * scale))
    s3.unsetPrimaryObject()

    # Execute Assembly Cut
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    for inst_name in a.instances.keys(): del a.instances[inst_name]
        
    inst_part = a.Instance(name='Part-1-1', part=p, dependent=ON)
    inst_gap = a.Instance(name='Gap_Tool-1', part=p_gap, dependent=ON)
    inst_div_bot = a.Instance(name='Divider_Bot-1', part=p_div, dependent=ON)
    inst_div_top = a.Instance(name='Divider_Top-1', part=p_div, dependent=ON)
    
    z_gap_bottom = (extrude_depth - (gap_thickness_mm * scale)) / 2.0
    top_divider_z = extrude_depth - (divider_cut_depth_mm * scale)
    
    a.translate(instanceList=('Gap_Tool-1', ), vector=(0.0, 0.0, z_gap_bottom))
    a.translate(instanceList=('Divider_Top-1', ), vector=(0.0, 0.0, top_divider_z))
    
    a.InstanceFromBooleanCut(name='Final_Part', 
                             instanceToBeCut=a.instances['Part-1-1'], 
                             cuttingInstances=(a.instances['Gap_Tool-1'], 
                                               a.instances['Divider_Bot-1'], 
                                               a.instances['Divider_Top-1']), 
                             originalInstances=DELETE)

    # =====================================================================
    # 5. MATHEMATICAL PARTITIONING 
    # =====================================================================
    final_p = mdb.models['Model-1'].parts['Final_Part']

    def apply_partition(plane_feature):
        try:
            final_p.PartitionCellByDatumPlane(datumPlane=final_p.datums[plane_feature.id], cells=final_p.cells)
        except:
            pass 

    z_gap_top = z_gap_bottom + (gap_thickness_mm * scale)
    
    dp_h1 = final_p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=z_gap_bottom)
    apply_partition(dp_h1)
    
    dp_h2 = final_p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=z_gap_top)
    apply_partition(dp_h2)

    for i in range(num_quads - 1):
        P1, P2 = quads[i][3], quads[i][2] 
        dx, dy = P2[0] - P1[0], P2[1] - P1[1]
        L = math.hypot(dx, dy)
        ux, uy = dx/L, dy/L
        nx, ny = -uy, ux
        hw = (divider_cut_width_mm / 2.0) * scale
        
        pt1_L = (P1[0] + hw*nx, P1[1] + hw*ny, 0.0)
        pt2_L = (P2[0] + hw*nx, P2[1] + hw*ny, 0.0)
        pt3_L = (P1[0] + hw*nx, P1[1] + hw*ny, 1.0) 
        dp_v1 = final_p.DatumPlaneByThreePoints(point1=pt1_L, point2=pt2_L, point3=pt3_L)
        apply_partition(dp_v1)
        
        pt1_R = (P1[0] - hw*nx, P1[1] - hw*ny, 0.0)
        pt2_R = (P2[0] - hw*nx, P2[1] - hw*ny, 0.0)
        pt3_R = (P1[0] - hw*nx, P1[1] - hw*ny, 1.0)
        dp_v2 = final_p.DatumPlaneByThreePoints(point1=pt1_R, point2=pt2_R, point3=pt3_R)
        apply_partition(dp_v2)

    # =====================================================================
    # 6. MATERIALS & SECTION ASSIGNMENTS
    # =====================================================================
    if 'Tape_Material' in mdb.models['Model-1'].materials: del mdb.models['Model-1'].materials['Tape_Material']
    if 'Plywood_Material' in mdb.models['Model-1'].materials: del mdb.models['Model-1'].materials['Plywood_Material']
    if 'Tape_Section' in mdb.models['Model-1'].sections: del mdb.models['Model-1'].sections['Tape_Section']
    if 'Plywood_Section' in mdb.models['Model-1'].sections: del mdb.models['Model-1'].sections['Plywood_Section']

    mat_tape = mdb.models['Model-1'].Material(name='Tape_Material')
    mat_tape.Density(table=((tape_density, ), ))
    mat_tape.Elastic(table=((tape_E, tape_nu), ))

    mat_ply = mdb.models['Model-1'].Material(name='Plywood_Material')
    mat_ply.Density(table=((ply_density, ), ))
    mat_ply.Elastic(table=((ply_E, ply_nu), ))

    mdb.models['Model-1'].HomogeneousSolidSection(name='Tape_Section', material='Tape_Material', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Plywood_Section', material='Plywood_Material', thickness=None)

    def dist_point_to_segment(px, py, P1, P2):
        lx, ly = P2[0] - P1[0], P2[1] - P1[1]
        length_sq = lx*lx + ly*ly
        if length_sq == 0.0: return math.hypot(px - P1[0], py - P1[1])
        t = max(0, min(1, ((px - P1[0]) * lx + (py - P1[1]) * ly) / length_sq))
        proj_x = P1[0] + t * lx
        proj_y = P1[1] + t * ly
        return math.hypot(px - proj_x, py - proj_y)

    tape_seq = None
    ply_seq = None
    
    tolerance = (divider_cut_width_mm / 2.0) * scale * 0.90

    for cell in final_p.cells:
        vertex_indices = cell.getVertices()
        cx, cy, cz = 0.0, 0.0, 0.0
        for v_idx in vertex_indices:
            coords = final_p.vertices[v_idx].pointOn[0]
            cx += coords[0]
            cy += coords[1]
            cz += coords[2]
            
        num_v = len(vertex_indices)
        cx /= num_v
        cy /= num_v
        cz /= num_v
        
        is_tape_region = False
        
        if (z_gap_bottom + 1e-5) < cz < (z_gap_top - 1e-5):
            is_tape_region = True
        else:
            for (P1, P2) in divider_segments:
                if dist_point_to_segment(cx, cy, P1, P2) <= tolerance:
                    is_tape_region = True
                    break
                
        c_seq = final_p.cells[cell.index:cell.index+1]
        
        if is_tape_region:
            if tape_seq is None: tape_seq = c_seq
            else: tape_seq += c_seq
        else:
            if ply_seq is None: ply_seq = c_seq
            else: ply_seq += c_seq

    if tape_seq is not None:
        region_tape = regionToolset.Region(cells=tape_seq)
        final_p.SectionAssignment(region=region_tape, sectionName='Tape_Section', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
            
    if ply_seq is not None:
        region_ply = regionToolset.Region(cells=ply_seq)
        final_p.SectionAssignment(region=region_ply, sectionName='Plywood_Section', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

    # =====================================================================
    # 7. AUTOMATED MESHING
    # =====================================================================
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
                              kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
                              hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    
    all_cells_region = (final_p.cells, )
    final_p.setElementType(regions=all_cells_region, elemTypes=(elemType1, elemType2, elemType3))
    final_p.seedPart(size=(mesh_size_mm * scale), deviationFactor=0.1, minSizeFactor=0.1)
    final_p.generateMesh()
    
    # =====================================================================
    # 8. STEP & BOUNDARY CONDITIONS (Mathematical Face Search)
    # =====================================================================
    a.regenerate()
    
    # Create the Analysis Step (with Non-Linear Geometry ON for large rotations)
    if 'Step-1' in mdb.models['Model-1'].steps:
        del mdb.models['Model-1'].steps['Step-1']
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)

    # Clean up old BCs if the script is re-run
    if 'BC-1' in mdb.models['Model-1'].boundaryConditions:
        del mdb.models['Model-1'].boundaryConditions['BC-1']
    if 'BC-2' in mdb.models['Model-1'].boundaryConditions:
        del mdb.models['Model-1'].boundaryConditions['BC-2']

    inst = a.instances['Final_Part-1']
    
    encastre_faces = []
    disp_faces = []

    # Filter through every face on the instance
    for f in inst.faces:
        pt = f.pointOn[0]
        # Check if the face is completely flat on the Y=0 base line
        if abs(pt[1]) < 1e-5:
            # Check Z-height: Is it on the bottom layer?
            if pt[2] < z_gap_bottom:
                encastre_faces.append(f)
            # Check Z-height: Is it on the top layer?
            elif pt[2] > z_gap_top:
                disp_faces.append(f)

    # Helper function to dynamically chain the faces together
    def build_face_seq(face_list):
        seq = None
        for f in face_list:
            if seq is None:
                seq = inst.faces[f.index:f.index+1]
            else:
                seq += inst.faces[f.index:f.index+1]
        return seq

    seq_encastre = build_face_seq(encastre_faces)
    seq_disp = build_face_seq(disp_faces)

    # Apply the Encastre (Fixed) BC to the bottom layer
    if seq_encastre is not None:
        region_encastre = regionToolset.Region(faces=seq_encastre)
        mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
                                         region=region_encastre, localCsys=None)

    # Apply the Displacement (180 deg / 3.141 rad Rotation) BC to the top layer
    if seq_disp is not None:
        region_disp = regionToolset.Region(faces=seq_disp)
        mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
                                             region=region_disp, u1=0.0, u2=0.0, u3=0.0, 
                                             ur1=0.0, ur2=0.0, ur3=-3.141, 
                                             amplitude=UNSET, fixed=OFF, 
                                             distributionType=UNIFORM, fieldName='', localCsys=None)

    # Reset viewport display to show the Assembly & Boundary Conditions
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, predefinedFields=ON, 
                                                               connectors=ON, adaptiveMeshConstraints=OFF, 
                                                               optimizationTasks=OFF, geometricRestrictions=OFF, 
                                                               stopConditions=OFF, step='Step-1')
    session.viewports['Viewport: 1'].view.fitView()

BuildParametricSpiralFinal()