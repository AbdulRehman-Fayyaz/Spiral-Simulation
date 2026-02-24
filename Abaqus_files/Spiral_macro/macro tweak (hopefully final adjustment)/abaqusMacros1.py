# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro2():
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
    del mdb.models['Model-1'].boundaryConditions['BC-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.37855, 
        farPlane=0.491914, width=0.0394361, height=0.0164182, 
        viewOffsetX=-0.0289433, viewOffsetY=-0.0506548)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:5 #800000 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370182, 
        farPlane=0.500281, width=0.141996, height=0.0591163, 
        viewOffsetX=-0.0158696, viewOffsetY=-0.0402383)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336527, 
        farPlane=0.535778, width=0.129086, height=0.0537417, cameraPosition=(
        -0.353234, 0.20066, 0.113282), cameraUpVector=(0.526579, 0.77213, 
        -0.355711), cameraTarget=(0.0467259, 0.0664799, 0.00625554), 
        viewOffsetX=-0.0144268, viewOffsetY=-0.03658)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336883, 
        farPlane=0.535422, width=0.146246, height=0.0608857, 
        viewOffsetX=-0.00947746, viewOffsetY=-0.0369878)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Final_Part-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#0:8 #20000000 ]', ), )
    region = regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].loads['Load-1'].setValues(region=region)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347424, 
        farPlane=0.524881, width=0.0208236, height=0.00866937, 
        viewOffsetX=-0.0237714, viewOffsetY=-0.0582617)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Final_Part-1'].vertices
    a.DatumPlaneByTwoPoint(point1=v1[240], point2=v1[224])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeIndependent(instances=(a1.instances['Final_Part-1'], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.325262, 
        farPlane=0.547043, width=0.250483, height=0.104282, 
        viewOffsetX=0.0331082, viewOffsetY=-0.0402902)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Final_Part-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#ffffffff #ffff ]', ), )
    a.deleteMesh(regions=pickedRegions)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347252, 
        farPlane=0.525053, width=0.0225984, height=0.00940828, 
        viewOffsetX=-0.0225465, viewOffsetY=-0.0603809)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    pickedFaces = f1.getSequenceFromMask(mask=('[#ffffffff:9 #7fffff ]', ), )
    d1 = a.datums
    a.PartitionFaceByDatumPlane(datumPlane=d1[47], faces=pickedFaces)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)


