# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro7():
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
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.29628, 
        farPlane=0.535354, width=0.299519, height=0.134413, cameraPosition=(
        0.390483, 0.0905761, 0.231527), cameraUpVector=(-0.479421, 0.877585, 
        0.000247508), cameraTarget=(0.0480794, 0.0612455, -0.00124961))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289201, 
        farPlane=0.542773, width=0.292364, height=0.131202, cameraPosition=(
        0.394358, -0.0258264, 0.210458), cameraUpVector=(-0.15825, 0.987344, 
        0.0104097), cameraTarget=(0.0480863, 0.0610374, -0.00128729))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.273055, 
        farPlane=0.559143, width=0.276041, height=0.123877, cameraPosition=(
        0.353172, -0.165924, 0.16529), cameraUpVector=(0.127117, 0.96131, 
        0.244386), cameraTarget=(0.0479958, 0.0607295, -0.00138656))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314301, 
        farPlane=0.517896, width=0.0452258, height=0.0202956, 
        viewOffsetX=-0.0184072, viewOffsetY=-0.0454478)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:7 #8000000 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314295, 
        farPlane=0.517902, width=0.045225, height=0.0202952, 
        viewOffsetX=-0.0185141, viewOffsetY=-0.0460606)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Part']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Section']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311989, 
        farPlane=0.520209, width=0.0561165, height=0.0251829, 
        viewOffsetX=-0.0154763, viewOffsetY=-0.0398082)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:3 #800 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=3.141, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.318573, 
        farPlane=0.513625, width=0.0391173, height=0.0175544, 
        viewOffsetX=-0.0120543, viewOffsetY=-0.0394344)
    mdb.models['Model-1'].boundaryConditions['BC-2'].setValues(ur2=0.0, ur3=3.141)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.322856, 
        farPlane=0.509342, width=0.00831379, height=0.00373091, 
        viewOffsetX=-0.00779263, viewOffsetY=-0.0411672)
    mdb.models['Model-1'].boundaryConditions['BC-2'].setValues(ur3=-3.141)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.303366, 
        farPlane=0.528832, width=0.0941831, height=0.0422658, 
        viewOffsetX=-0.00509951, viewOffsetY=-0.0310298)

Macro7()