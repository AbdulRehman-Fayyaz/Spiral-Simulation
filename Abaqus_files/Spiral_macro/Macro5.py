# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro5():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='tape_Material-1')
    mdb.models['Model-1'].materials['tape_Material-1'].Elastic(table=((500000000.0, 
        0.34), ))
    mdb.models['Model-1'].materials['tape_Material-1'].Density(table=((880.0, ), ))
    mdb.models['Model-1'].Material(name='plywood_Material-2')
    mdb.models['Model-1'].materials['plywood_Material-2'].Density(table=((680.0, ), 
        ))
    mdb.models['Model-1'].materials['plywood_Material-2'].Elastic(table=((
        7000000000.0, 0.13), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='plywood_Section-1', 
        material='plywood_Material-2', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='tape_Section-2', 
        material='tape_Material-1', thickness=None)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321594, 
        farPlane=0.508552, width=0.0681806, height=0.0305968, 
        viewOffsetX=0.00531077, viewOffsetY=0.0158667)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336615, 
        farPlane=0.474025, width=0.0713651, height=0.0320259, cameraPosition=(
        -0.192929, 0.145347, 0.319921), cameraUpVector=(-0.539997, -0.0908489, 
        -0.83675), cameraTarget=(0.0601438, 0.0719164, -0.000778735), 
        viewOffsetX=0.00555883, viewOffsetY=0.0166078)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.304575, 
        farPlane=0.506066, width=0.307906, height=0.138176, 
        viewOffsetX=-0.00628705, viewOffsetY=-0.00229532)
    p = mdb.models['Model-1'].parts['Final_Part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#7f7c00 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['Final_Part']
    p.SectionAssignment(region=region, sectionName='plywood_Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.272575, 
        farPlane=0.538066, width=0.522535, height=0.234494, 
        viewOffsetX=0.00593279, viewOffsetY=-0.0260524)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217915, 
        farPlane=0.57025, width=0.417751, height=0.187471, cameraPosition=(
        -0.258277, 0.262765, 0.154106), cameraUpVector=(-0.197315, -0.271914, 
        -0.941876), cameraTarget=(0.0710401, 0.0666192, -0.00515324), 
        viewOffsetX=0.00474309, viewOffsetY=-0.0208281)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.299056, 
        farPlane=0.489109, width=0.0319012, height=0.0143161, 
        viewOffsetX=0.0296889, viewOffsetY=-0.0121432)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34939, 
        farPlane=0.533583, width=0.0372705, height=0.0167256, cameraPosition=(
        0.364932, 0.278925, 0.218749), cameraUpVector=(-0.767765, 0.640705, 
        -0.00589749), cameraTarget=(0.0391853, 0.102799, 0.0312517), 
        viewOffsetX=0.0346858, viewOffsetY=-0.0141871)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.354692, 
        farPlane=0.506733, width=0.0378361, height=0.0169794, cameraPosition=(
        0.363405, 0.171359, 0.273734), cameraUpVector=(-0.632109, 0.77378, 
        0.0412662), cameraTarget=(0.0349388, 0.0947403, 0.0318129), 
        viewOffsetX=0.0352122, viewOffsetY=-0.0144024)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344409, 
        farPlane=0.517015, width=0.119594, height=0.0536692, 
        viewOffsetX=0.0237841, viewOffsetY=-0.0238257)
    p = mdb.models['Model-1'].parts['Final_Part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#83ff ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['Final_Part']
    p.SectionAssignment(region=region, sectionName='tape_Section-2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Section']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346442, 
        farPlane=0.514983, width=0.10512, height=0.0471736, 
        viewOffsetX=-0.00693022, viewOffsetY=-0.0318303)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])

Macro5()
