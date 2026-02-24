# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
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
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.156462, 
        farPlane=0.220661, width=0.231816, height=0.109375, cameraPosition=(
        0.0434019, 0.0415113, 0.188562), cameraTarget=(0.0434019, 0.0415113, 
        0))
    s1.Line(point1=(0.0083313, 0.049301), point2=(0.0, 0.0))
    s1.Line(point1=(0.0, 0.0), point2=(0.05, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(0.05, 0.0), point2=(0.0437517, 0.0369866))
    s1.Line(point1=(0.0437517, 0.0369866), point2=(0.0083313, 0.049301))
    s1.Line(point1=(0.0083313, 0.049301), point2=(0.0263689, 0.0821895))
    s1.Line(point1=(0.0263689, 0.0821895), point2=(0.0484358, 0.647372))
    s1.undo()
    s1.Line(point1=(0.0263689, 0.0821895), point2=(0.0484358, 0.0647372))
    s1.Line(point1=(0.0484358, 0.0647372), point2=(0.0437517, 0.0369866))
    s1.Line(point1=(0.0484358, 0.0647372), point2=(0.0585914, 0.0832487))
    s1.Line(point1=(0.0585914, 0.0832487), point2=(0.0472532, 0.101058))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.824755, 
        farPlane=1.04767, width=0.386361, height=0.182292, cameraPosition=(
        0.0271341, 0.0194327, 0.936212), cameraTarget=(0.0271341, 0.0194327, 
        0))
    s1.Line(point1=(0.0472532, 0.101058), point2=(0.0638428927784791, 0.075))
    s1.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    s1.undo()
    s1.Line(point1=(0.0472532, 0.101058), point2=(0.0263689, 0.0821895))
    s1.Line(point1=(0.0472532, 0.101058), point2=(0.0666995, 0.1092794))
    s1.Line(point1=(0.0666995, 0.1092794), point2=(0.0703484, 0.0938649))
    s1.Line(point1=(0.0703484, 0.0938649), point2=(0.0585914, 0.0832487))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880017, 
        farPlane=0.992407, width=0.25973, height=0.122545, cameraPosition=(
        0.0847432, 0.060129, 0.936212), cameraTarget=(0.0847432, 0.060129, 0))
    s1.Line(point1=(0.0666995, 0.1092794), point2=(0.0825055, 0.0984817))
    s1.undo()
    s1.Line(point1=(0.0666995, 0.1092794), point2=(0.0825055, 0.1103105))
    s1.Line(point1=(0.0825055, 0.1103105), point2=(0.0812952, 0.0984917))
    s1.Line(point1=(0.0812952, 0.0984917), point2=(0.0703484, 0.0938649))
    s1.Line(point1=(0.0825055, 0.1103105), point2=(0.0939615, 0.107151))
    s1.Line(point1=(0.0939615, 0.107151), point2=(0.0901924, 0.0990738))
    s1.Line(point1=(0.0901924, 0.0990738), point2=(0.0812952, 0.0984917))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.848407, 
        farPlane=1.02402, width=0.405829, height=0.191477, cameraPosition=(
        0.135325, 0.0306222, 0.936212), cameraTarget=(0.135325, 0.0306222, 0))
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(width=0.306861, 
        height=0.144783, cameraPosition=(0.0577815, 0.0408791, 0.289808), 
        cameraTarget=(0.0577815, 0.0408791, 0))
    s1.offset(distance=0.01, objectList=(g[2], g[3], g[4], g[5]), side=RIGHT)
    s1.offset(distance=0.005, objectList=(g[5], g[6], g[7], g[8]), side=RIGHT)
    s1.undo()
    s1.offset(distance=0.005, objectList=(g[5], g[6], g[7], g[8]), side=LEFT)
    s1.offset(distance=0.005, objectList=(g[7], g[9], g[10], g[11]), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.272404, 
        farPlane=0.307212, width=0.12569, height=0.0593029, cameraPosition=(
        0.0784575, 0.0900526, 0.289808), cameraTarget=(0.0784575, 0.0900526, 
        0))
    s1.offset(distance=0.003, objectList=(g[10], g[12], g[13], g[14]), side=LEFT)
    s1.offset(distance=0.003, objectList=(g[13], g[15], g[16], g[17]), side=RIGHT)
    s1.offset(distance=0.002, objectList=(g[16], g[18], g[19], g[20]), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255815, 
        farPlane=0.323801, width=0.157113, height=0.0741287, cameraPosition=(
        0.0721111, 0.0794442, 0.289808), cameraTarget=(0.0721111, 0.0794442, 
        0))
    s1.setAsConstruction(objectList=(g[7], g[10], g[13], g[16]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247317, 
        farPlane=0.332299, width=0.196391, height=0.0926609, cameraPosition=(
        0.0759045, 0.0531049, 0.289808), cameraTarget=(0.0759045, 0.0531049, 
        0))
    s1.setAsConstruction(objectList=(g[5], ))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s1, depth=0.0045)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

Macro1()