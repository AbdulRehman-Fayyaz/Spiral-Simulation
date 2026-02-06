# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-15.00.46 RELr427 198590
# Run by st195764 on Fri Feb  6 15:48:16 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=302.201538085938, 
    height=211.859268188477)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Spiral_trial.cae')
#: The model database "C:\Users\st195764\Desktop\ARF_soft_seminar\Spiral_trial.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Spiral1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.170934, 
    farPlane=0.302204, width=0.104876, height=0.0556953, 
    viewOffsetX=-0.00184939, viewOffsetY=0.00246801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.185555, 
    farPlane=0.28031, width=0.113846, height=0.0604592, cameraPosition=(
    0.188966, -0.0040521, -0.0918452), cameraUpVector=(-0.47706, 0.840723, 
    -0.256122), cameraTarget=(-0.0279814, -0.00462414, 0.00248482), 
    viewOffsetX=-0.00200757, viewOffsetY=0.00267911)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.193625, 
    farPlane=0.272239, width=0.0156809, height=0.0083275, 
    viewOffsetX=-0.00808822, viewOffsetY=0.00167046)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Spiral1_onshape-2'].edges
e2 = a.instances['Spiral1flex-1'].edges
a.ParallelEdge(movableAxis=e1[12], fixedAxis=e2[1], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.200908, 
    farPlane=0.278403, width=0.0904602, height=0.0480398, 
    viewOffsetX=-0.0141296, viewOffsetY=0.00662837)
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('Spiral1_onshape-2', ), axisPoint=(-0.0498, -0.000306, 
    -0.000329), axisDirection=(10.0, 0.0, 0.0), angle=-45.0)
#: The instance Spiral1_onshape-2 was rotated by -45. degrees about the axis defined by the point -49.8E-03, -306.E-06, -329.E-06 and the vector 10., 0., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.199934, 
    farPlane=0.279376, width=0.0903901, height=0.0480026, 
    viewOffsetX=-0.015429, viewOffsetY=0.0101909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.198136, 
    farPlane=0.273912, width=0.089577, height=0.0475708, cameraPosition=(
    0.211314, 0.0482516, -0.00210794), cameraUpVector=(-0.5163, 0.82701, 
    -0.222462), cameraTarget=(-0.0201407, -0.000665232, -0.00125778), 
    viewOffsetX=-0.0152902, viewOffsetY=0.0100993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.199418, 
    farPlane=0.276355, width=0.0901564, height=0.0478785, cameraPosition=(
    0.20682, 0.0195199, -0.0448054), cameraUpVector=(-0.4454, 0.883705, 
    -0.143821), cameraTarget=(-0.0247903, -0.000877494, -0.00115552), 
    viewOffsetX=-0.0153891, viewOffsetY=0.0101646)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.196886, 
    farPlane=0.290115, width=0.089012, height=0.0472707, cameraPosition=(
    0.159654, -0.114133, -0.0659471), cameraUpVector=(0.00877066, 0.934656, 
    -0.355445), cameraTarget=(-0.0359593, -0.00118917, 0.00436498), 
    viewOffsetX=-0.0151937, viewOffsetY=0.0100356)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.200589, 
    farPlane=0.286413, width=0.052603, height=0.0279354, 
    viewOffsetX=-0.0154663, viewOffsetY=0.0150293)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\ARF_soft_seminar\Spiral_trial.cae".
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\ARF_soft_seminar\Spiral_trial.cae".
