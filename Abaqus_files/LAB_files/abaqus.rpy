# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-15.00.46 RELr427 198590
# Run by st195764 on Fri Feb 20 23:54:00 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=169.902587890625, 
    height=194.592590332031)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Spiral_inLAB.cae')
#: The model database "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['spiral_Model_Dynamic'].parts['Spiral']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['spiral_Model_Dynamic'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['spiral_Model_static_displacement'].steps['Step-1'].setValues(
    initialInc=0.001, maxInc=0.05)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['statics_displacement_Job-5'].submit(consistencyChecking=OFF)
#: The job input file "statics_displacement_Job-5.inp" has been submitted for analysis.
#: Job statics_displacement_Job-5: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.3112, 
    farPlane=0.518028, width=0.202104, height=0.0915615, 
    viewOffsetX=-0.00307046, viewOffsetY=-0.0101504)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321306, 
    farPlane=0.507922, width=0.0972931, height=0.0422916, 
    viewOffsetX=-0.00226853, viewOffsetY=-0.0236757)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.345682, 
    farPlane=0.53228, width=0.104674, height=0.0455001, cameraPosition=(
    0.420658, -0.0740371, 0.185006), cameraUpVector=(-0.0480041, 0.993588, 
    0.102362), cameraTarget=(0.067439, 0.0651606, 0.0183767), 
    viewOffsetX=-0.00244063, viewOffsetY=-0.0254718)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332129, 
    farPlane=0.545833, width=0.259817, height=0.112938, viewOffsetX=0.00116709, 
    viewOffsetY=-0.0136872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.32765, 
    farPlane=0.557121, width=0.256313, height=0.111415, cameraPosition=(
    0.19235, -0.351965, -0.0586615), cameraUpVector=(0.597403, 0.433691, 
    0.674553), cameraTarget=(0.0630101, 0.0356502, 0.0115592), 
    viewOffsetX=0.00115135, viewOffsetY=-0.0135026)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.345665, 
    farPlane=0.539106, width=0.0575723, height=0.0250257, 
    viewOffsetX=-0.0114645, viewOffsetY=-0.0188596)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.215917, 
    farPlane=0.438403, width=0.219456, height=0.0994226, cameraPosition=(
    0.259739, -0.143761, -0.158135), cameraUpVector=(0.409744, 0.859938, 
    0.304328), cameraTarget=(0.0522595, 0.0241813, -0.0281399))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236339, 
    farPlane=0.445965, width=0.240213, height=0.108826, cameraPosition=(
    -0.157549, -0.222357, 0.0289958), cameraUpVector=(0.290134, 0.0469015, 
    -0.955836), cameraTarget=(0.0136668, 0.0169124, -0.0108332))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239941, 
    farPlane=0.44032, width=0.243874, height=0.110485, cameraPosition=(
    0.129958, -0.251777, -0.141332), cameraUpVector=(0.425107, 0.7232, 
    -0.544303), cameraTarget=(0.0509582, 0.0130964, -0.0329257))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247389, 
    farPlane=0.450153, width=0.251445, height=0.113915, cameraPosition=(
    0.356076, -0.0710976, 0.00211356), cameraUpVector=(-0.0827499, 0.58341, 
    -0.807951), cameraTarget=(0.0796962, 0.0360595, -0.0146948))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237042, 
    farPlane=0.449118, width=0.240929, height=0.109151, cameraPosition=(
    0.339046, -0.0437325, -0.149154), cameraUpVector=(-0.591644, 0.320299, 
    -0.739842), cameraTarget=(0.0771635, 0.0401292, -0.0371912))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236777, 
    farPlane=0.446025, width=0.240661, height=0.109029, cameraPosition=(
    0.319862, -0.033589, -0.192531), cameraUpVector=(-0.687988, 0.343493, 
    -0.639285), cameraTarget=(0.0745814, 0.0414945, -0.0430296))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=5)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=64)
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/statics_displacement_Job-5.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/statics_displacement_Job-5.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/statics_displacement_Job-5.odb'])
#: Error in job statics_displacement_Job-5: Time increment required is less than the minimum specified
#: Error in job statics_displacement_Job-5: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job statics_displacement_Job-5: Abaqus/Standard aborted due to errors.
#: Error in job statics_displacement_Job-5: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job statics_displacement_Job-5 aborted due to errors.
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['spiral_Model_static_displacement'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['spiral_Model_static_displacement'].parts['Spiral']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.Model(name='spiral_Model_static_displacement-Copy', 
    objectToCopy=mdb.models['spiral_Model_static_displacement'])
#: The model "spiral_Model_static_displacement-Copy" has been created.
p = mdb.models['spiral_Model_static_displacement-Copy'].parts['Spiral']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['spiral_Model_static_displacement-Copy'].Material(name='Material-3')
mdb.models['spiral_Model_static_displacement-Copy'].materials['Material-3'].Hyperelastic(
    materialType=ISOTROPIC, table=())
