# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro6():
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
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Final_Part']
    p.seedPart(size=0.0025, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.269752, 
        farPlane=0.560395, width=0.424694, height=0.191216, 
        viewOffsetX=-0.0213619, viewOffsetY=-0.00650746)
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Meshability']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.297116, 
        farPlane=0.533031, width=0.15328, height=0.0690134, 
        viewOffsetX=0.0254357, viewOffsetY=-0.0026831)
    p = mdb.models['Model-1'].parts['Final_Part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280191, 
        farPlane=0.549956, width=0.354844, height=0.159766, 
        viewOffsetX=0.0955914, viewOffsetY=-0.0165554)
    session.viewports['Viewport: 1'].view.fitView()
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Final_Part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ffffffff #1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    session.viewports['Viewport: 1'].view.fitView()

Macro6()