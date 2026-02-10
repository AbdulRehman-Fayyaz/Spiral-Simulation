# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-15.00.46 RELr427 198590
# Run by st195764 on Tue Feb 10 15:56:36 2026
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
p1 = mdb.models['spiral_Model_static_traction'].parts['Spiral']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['spiral_Model_static_traction'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_pressure_Job-3'].submit(consistencyChecking=OFF)
#: The job input file "static_pressure_Job-3.inp" has been submitted for analysis.
mdb.jobs['static_traction_Job-4'].submit(consistencyChecking=OFF)
#: The job input file "static_traction_Job-4.inp" has been submitted for analysis.
#: Job static_pressure_Job-3: Analysis Input File Processor completed successfully.
#: Job static_traction_Job-4: Analysis Input File Processor completed successfully.
#: Job static_traction_Job-4: Abaqus/Standard completed successfully.
#: Job static_traction_Job-4 completed successfully. 
#: Error in job static_pressure_Job-3: Time increment required is less than the minimum specified
#: Error in job static_pressure_Job-3: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job static_pressure_Job-3: Abaqus/Standard aborted due to errors.
#: Error in job static_pressure_Job-3: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job static_pressure_Job-3 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['spiral_Model_static_pressure'].loads['Load-1'].setValues(
    magnitude=-115.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_pressure_Job-3'].submit(consistencyChecking=OFF)
#: The job input file "static_pressure_Job-3.inp" has been submitted for analysis.
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
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.226151, 
    farPlane=0.380826, width=0.0934602, height=0.104135, cameraPosition=(
    0.154894, -0.0661564, -0.27169), cameraUpVector=(0.658059, 0.641495, 
    0.394262), cameraTarget=(0.0462647, 0.043739, -0.0181675))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.225261, 
    farPlane=0.385882, width=0.0930926, height=0.103725, cameraPosition=(
    -0.0266186, -0.12762, -0.251151), cameraUpVector=(0.950126, 0.30226, 
    -0.0768128), cameraTarget=(0.0423258, 0.0424052, -0.0177218))
#: Job static_pressure_Job-3: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232252, 
    farPlane=0.378938, width=0.0959819, height=0.106945, cameraPosition=(
    0.0599496, -0.13435, -0.256076), cameraUpVector=(0.904288, 0.382578, 
    0.189467), cameraTarget=(0.0447818, 0.0422142, -0.0178615))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=24)
a = mdb.models['spiral_Model_static_traction'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['spiral_Model_static_traction'].loads['Load-1'].setValues(
    magnitude=50.0)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_traction_Job-4'].submit(consistencyChecking=OFF)
#: The job input file "static_traction_Job-4.inp" has been submitted for analysis.
mdb.jobs['Statics_Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Statics_Job-2.inp" has been submitted for analysis.
#: Job static_traction_Job-4: Analysis Input File Processor completed successfully.
#: Job Statics_Job-2: Analysis Input File Processor completed successfully.
a = mdb.models['spiral_Model_static'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Job Statics_Job-2: Abaqus/Standard completed successfully.
#: Job Statics_Job-2 completed successfully. 
#: Job static_traction_Job-4: Abaqus/Standard completed successfully.
#: Job static_traction_Job-4 completed successfully. 
#: Error in job static_pressure_Job-3: Time increment required is less than the minimum specified
#: Error in job static_pressure_Job-3: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job static_pressure_Job-3: Abaqus/Standard aborted due to errors.
#: Error in job static_pressure_Job-3: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job static_pressure_Job-3 aborted due to errors.
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['spiral_Model_static_pressure'].loads['Load-1'].setValues(
    magnitude=-113.0)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_pressure_Job-3'].submit(consistencyChecking=OFF)
#: The job input file "static_pressure_Job-3.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Dynamics_Job-1.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Dynamics_Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#: Job static_pressure_Job-3: Analysis Input File Processor completed successfully.
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232745, 
    farPlane=0.415439, width=0.0961855, height=0.107172, cameraPosition=(
    -0.172281, 0.180312, 0.184567), cameraUpVector=(-0.142004, 0.344299, 
    -0.928059), cameraTarget=(0.0226599, 0.052501, 0.000682535))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238962, 
    farPlane=0.408806, width=0.0987551, height=0.110035, cameraPosition=(
    -0.0381827, -0.14241, -0.271653), cameraUpVector=(0.667158, 0.691029, 
    -0.278172), cameraTarget=(0.0339101, 0.0254263, -0.037592))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25088, 
    farPlane=0.415682, width=0.103681, height=0.115523, cameraPosition=(
    -0.00233673, -0.279324, -0.0421473), cameraUpVector=(0.799405, 0.273628, 
    -0.534864), cameraTarget=(0.0368963, 0.0140205, -0.0184728))
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239074, 
    farPlane=0.412554, width=0.098801, height=0.110086, cameraPosition=(
    0.299733, 0.104636, -0.199765), cameraUpVector=(-0.0560092, 0.626617, 
    0.777312), cameraTarget=(0.0574024, 0.0425458, -0.0398533))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23812, 
    farPlane=0.421749, width=0.0984068, height=0.109647, cameraPosition=(
    0.147704, -0.173714, -0.245623), cameraUpVector=(0.417455, 0.896847, 
    -0.146277), cameraTarget=(0.0439117, 0.0178457, -0.0439226))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249929, 
    farPlane=0.422569, width=0.103288, height=0.115085, cameraPosition=(
    -0.0730938, -0.267065, 0.0414692), cameraUpVector=(0.578857, -0.00783104, 
    -0.815391), cameraTarget=(0.0218063, 0.0084998, -0.0151801))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.273184, 
    farPlane=0.399314, width=0.00425075, height=0.00473626, 
    viewOffsetX=0.00577675, viewOffsetY=-0.021866)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.273895, 
    farPlane=0.394735, width=0.00426181, height=0.00474859, cameraPosition=(
    -0.0516241, -0.273758, 0.0287343), cameraUpVector=(0.588661, 0.0606429, 
    -0.806102), cameraTarget=(0.0250892, 0.00943975, -0.0167128), 
    viewOffsetX=0.00579178, viewOffsetY=-0.0219229)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.26998, 
    farPlane=0.398651, width=0.0213358, height=0.0237728, 
    viewOffsetX=0.00459415, viewOffsetY=-0.0204318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.269543, 
    farPlane=0.39747, width=0.0213013, height=0.0237343, cameraPosition=(
    -0.0561656, -0.273828, 0.0165111), cameraUpVector=(0.633223, 0.0750827, 
    -0.770319), cameraTarget=(0.0253397, 0.00965528, -0.0173337), 
    viewOffsetX=0.00458672, viewOffsetY=-0.0203988)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.267002, 
    farPlane=0.400011, width=0.0334819, height=0.0373061, 
    viewOffsetX=0.0040274, viewOffsetY=-0.0200533)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253929, 
    farPlane=0.397029, width=0.0318425, height=0.0354795, cameraPosition=(
    -0.0705041, -0.258174, -0.0952362), cameraUpVector=(0.850087, 0.185383, 
    -0.492935), cameraTarget=(0.0273561, 0.0132395, -0.0251699), 
    viewOffsetX=0.0038302, viewOffsetY=-0.0190714)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240474, 
    farPlane=0.410483, width=0.0929783, height=0.103598, 
    viewOffsetX=0.00583256, viewOffsetY=-0.00845072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234253, 
    farPlane=0.41362, width=0.0905729, height=0.100918, cameraPosition=(
    -0.0878813, -0.239207, -0.133967), cameraUpVector=(0.936651, 0.112595, 
    -0.331673), cameraTarget=(0.0252889, 0.0135598, -0.0269507), 
    viewOffsetX=0.00568167, viewOffsetY=-0.0082321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255716, 
    farPlane=0.392156, width=0.00539611, height=0.00601244, 
    viewOffsetX=-0.0179752, viewOffsetY=-0.0295772)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249081, 
    farPlane=0.386929, width=0.0052561, height=0.00585644, cameraPosition=(
    -0.0788253, -0.222524, -0.165093), cameraUpVector=(0.949032, 0.150045, 
    -0.277174), cameraTarget=(0.0274145, 0.0184265, -0.0279538), 
    viewOffsetX=-0.0175088, viewOffsetY=-0.0288097)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.248964, 
    farPlane=0.387046, width=0.00552061, height=0.00615116, 
    viewOffsetX=-0.000322006, viewOffsetY=-0.0247527)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.260179, 
    farPlane=0.377027, width=0.00576929, height=0.00642824, cameraPosition=(
    0.00779773, -0.264182, -0.103389), cameraUpVector=(0.899875, 0.341796, 
    -0.270924), cameraTarget=(0.034399, 0.0200366, -0.0217589), 
    viewOffsetX=-0.000336511, viewOffsetY=-0.0258677)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.224602, 
    farPlane=0.412605, width=0.155933, height=0.173743, viewOffsetX=0.027043, 
    viewOffsetY=-0.00303298)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234995, 
    farPlane=0.436815, width=0.163148, height=0.181783, cameraPosition=(
    -0.269154, 0.111899, -0.178041), cameraUpVector=(0.54881, -0.510333, 
    -0.662093), cameraTarget=(-0.0162384, 0.0237429, -0.0499257), 
    viewOffsetX=0.0282944, viewOffsetY=-0.00317333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238091, 
    farPlane=0.423748, width=0.165298, height=0.184178, cameraPosition=(
    -0.296784, 0.121572, -0.040038), cameraUpVector=(0.271764, -0.234331, 
    -0.933399), cameraTarget=(-0.0167012, 0.0230584, -0.0397874), 
    viewOffsetX=0.0286672, viewOffsetY=-0.00321514)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237186, 
    farPlane=0.437957, width=0.16467, height=0.183478, cameraPosition=(
    -0.151899, -0.048299, -0.303398), cameraUpVector=(0.875166, 0.353957, 
    -0.329846), cameraTarget=(0.0257975, 0.00742766, -0.0721624), 
    viewOffsetX=0.0285582, viewOffsetY=-0.00320292)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251731, 
    farPlane=0.423413, width=0.100141, height=0.111579, viewOffsetX=0.025681, 
    viewOffsetY=-0.00857498)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.283398, 
    farPlane=0.419722, width=0.11712, height=0.130497, cameraPosition=(
    0.0288679, -0.181856, -0.257177), cameraUpVector=(0.802052, 0.578642, 
    -0.147936), cameraTarget=(0.0408917, 0.0265003, -0.0460052))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.274379, 
    farPlane=0.426934, width=0.113393, height=0.126344, cameraPosition=(
    0.373147, 0.0472643, -0.126951), cameraUpVector=(-0.0680097, 0.726256, 
    0.684051), cameraTarget=(0.0944178, 0.0621223, -0.0257585))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.26737, 
    farPlane=0.432637, width=0.110496, height=0.123117, cameraPosition=(
    0.350301, -0.0148516, -0.158317), cameraUpVector=(0.155688, 0.638586, 
    0.753637), cameraTarget=(0.0909156, 0.0526001, -0.0305668))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.269454, 
    farPlane=0.428316, width=0.111358, height=0.124077, cameraPosition=(
    0.119256, -0.192703, -0.23284), cameraUpVector=(0.849892, 0.396245, 
    0.34738), cameraTarget=(0.0558621, 0.025617, -0.0418732))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263936, 
    farPlane=0.431029, width=0.109078, height=0.121536, cameraPosition=(
    0.126984, -0.212553, -0.204821), cameraUpVector=(0.836962, 0.423227, 
    0.346948), cameraTarget=(0.0570136, 0.0226594, -0.0376985))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=36)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234183, 
    farPlane=0.413823, width=0.096782, height=0.107836, cameraPosition=(
    -0.138409, -0.0927772, -0.251571), cameraUpVector=(0.966104, -0.113614, 
    -0.231807), cameraTarget=(0.0292239, 0.0352013, -0.0425937))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244377, 
    farPlane=0.400195, width=0.100995, height=0.11253, cameraPosition=(
    -0.168964, 0.0128132, -0.264847), cameraUpVector=(0.92551, 0.0389548, 
    -0.376714), cameraTarget=(0.0266681, 0.0440335, -0.0437042))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237469, 
    farPlane=0.40912, width=0.09814, height=0.109349, cameraPosition=(
    -0.148765, -0.0479855, -0.265582), cameraUpVector=(0.815148, 0.439581, 
    -0.37723), cameraTarget=(0.028259, 0.0392449, -0.0437621))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238171, 
    farPlane=0.410082, width=0.0984301, height=0.109673, cameraPosition=(
    -0.109873, -0.0770849, -0.27987), cameraUpVector=(0.942793, 0.218507, 
    -0.251785), cameraTarget=(0.031434, 0.0368694, -0.0449285))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241203, 
    farPlane=0.411365, width=0.0996835, height=0.111069, cameraPosition=(
    -0.0103335, -0.163506, -0.263419), cameraUpVector=(0.869162, 0.468183, 
    -0.159252), cameraTarget=(0.0397947, 0.0296106, -0.0435467))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.242259, 
    farPlane=0.407186, width=0.10012, height=0.111555, cameraPosition=(
    -0.0712768, -0.0739021, -0.301003), cameraUpVector=(0.968515, 0.222913, 
    -0.11085), cameraTarget=(0.0343067, 0.0376795, -0.0469312))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=37)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.307511, 
    farPlane=0.521717, width=0.240444, height=0.108931, viewOffsetX=0.0163186, 
    viewOffsetY=0.000808571)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    datumPlanes=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341576, 
    farPlane=0.49189, width=0.174615, height=0.0791076, viewOffsetX=-0.0477264, 
    viewOffsetY=-0.0035281)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    datumPlanes=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315119, 
    farPlane=0.51411, width=0.182311, height=0.0825943, viewOffsetX=-0.0377099, 
    viewOffsetY=-0.00552289)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312077, 
    farPlane=0.440868, width=0.281185, height=0.122226, viewOffsetX=0.0384047, 
    viewOffsetY=-0.0130437)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306713, 
    farPlane=0.441617, width=0.276352, height=0.120125, cameraPosition=(
    -0.0254332, -0.173205, -0.288494), cameraUpVector=(0.98386, 0.178906, 
    -0.00355822), cameraTarget=(0.0481683, -0.0199443, -0.0450906), 
    viewOffsetX=0.0377446, viewOffsetY=-0.0128195)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333511, 
    farPlane=0.417883, width=0.300498, height=0.130621, cameraPosition=(
    0.0161792, -0.0487969, -0.360144), cameraUpVector=(0.975753, 0.0370727, 
    0.215713), cameraTarget=(0.0514782, 0.000684413, -0.0695289), 
    viewOffsetX=0.0410424, viewOffsetY=-0.0139396)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337029, 
    farPlane=0.414367, width=0.252221, height=0.109636, viewOffsetX=0.0630925, 
    viewOffsetY=-0.0158388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336015, 
    farPlane=0.414725, width=0.251463, height=0.109307, cameraPosition=(
    0.0248554, -0.0518503, -0.359554), cameraUpVector=(0.970761, 0.0501026, 
    0.234762), cameraTarget=(0.0537741, 0.000270239, -0.0686955), 
    viewOffsetX=0.0629028, viewOffsetY=-0.0157912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.335997, 
    farPlane=0.414743, width=0.251451, height=0.109301, viewOffsetX=0.0597626, 
    viewOffsetY=-0.0223847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.335997, 
    farPlane=0.414743, width=0.251451, height=0.109301, viewOffsetX=0.0496914, 
    viewOffsetY=-0.0233739)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['spiral_Model_static_traction'].parts['Spiral']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31465, 
    farPlane=0.514579, width=0.165843, height=0.072279, viewOffsetX=0.00274907, 
    viewOffsetY=0.000433044)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332403, 
    farPlane=0.511091, width=0.175201, height=0.0763572, cameraPosition=(
    0.442227, 0.0112998, -0.129859), cameraUpVector=(-0.0461329, 0.751417, 
    0.658213), cameraTarget=(0.0508117, 0.0589062, -0.00167069), 
    viewOffsetX=0.00290418, viewOffsetY=0.000457478)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314968, 
    farPlane=0.528631, width=0.166011, height=0.0723523, cameraPosition=(
    0.256279, -0.253138, -0.183572), cameraUpVector=(0.62772, 0.750076, 
    0.208216), cameraTarget=(0.0474141, 0.0554336, -0.00173909), 
    viewOffsetX=0.00275185, viewOffsetY=0.000433483)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321725, 
    farPlane=0.523107, width=0.169573, height=0.0739045, cameraPosition=(
    0.300355, -0.179531, -0.232919), cameraUpVector=(0.452748, 0.244865, 
    0.857357), cameraTarget=(0.0462315, 0.0554415, -0.00463433), 
    viewOffsetX=0.00281089, viewOffsetY=0.000442783)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.37327, 
    farPlane=0.476651, width=0.196741, height=0.0857452, cameraPosition=(
    0.0641898, -0.112181, -0.385371), cameraUpVector=(0.842916, -0.192905, 
    0.502275), cameraTarget=(0.0416322, 0.0568382, -0.00744521), 
    viewOffsetX=0.00326124, viewOffsetY=0.000513724)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370894, 
    farPlane=0.479026, width=0.195489, height=0.0851993, cameraPosition=(
    0.0656882, -0.11266, -0.385067), cameraUpVector=(0.923194, 0.168298, 
    0.345526), cameraTarget=(0.0431306, 0.0563595, -0.00714171), 
    viewOffsetX=0.00324048, viewOffsetY=0.000510454)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.36092, 
    farPlane=0.488279, width=0.190232, height=0.0829083, cameraPosition=(
    0.099422, -0.136913, -0.369436), cameraUpVector=(0.889631, 0.227632, 
    0.395904), cameraTarget=(0.0439662, 0.0558551, -0.00657395), 
    viewOffsetX=0.00315334, viewOffsetY=0.000496728)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347969, 
    farPlane=0.5005, width=0.183406, height=0.0799334, cameraPosition=(
    0.195442, -0.123109, -0.349038), cameraUpVector=(0.756835, 0.239824, 
    0.608017), cameraTarget=(0.0459529, 0.056115, -0.00634933), 
    viewOffsetX=0.00304019, viewOffsetY=0.000478904)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344219, 
    farPlane=0.504251, width=0.218436, height=0.0952005, 
    viewOffsetX=0.000231761, viewOffsetY=0.00619839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346129, 
    farPlane=0.502285, width=0.219648, height=0.0957287, cameraPosition=(
    0.193673, -0.119994, -0.351369), cameraUpVector=(0.759867, 0.234494, 
    0.606313), cameraTarget=(0.0459003, 0.0562075, -0.00637614), 
    viewOffsetX=0.000233046, viewOffsetY=0.00623278)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    datumPlanes=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359394, 
    farPlane=0.482519, width=0.201519, height=0.0878276, 
    viewOffsetX=0.00806028, viewOffsetY=0.00367595)
a = mdb.models['spiral_Model_static_traction'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_traction'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.335904, 
    farPlane=0.414837, width=0.236299, height=0.102715, viewOffsetX=0.0501221, 
    viewOffsetY=-0.0206431)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311288, 
    farPlane=0.426146, width=0.218982, height=0.0951876, cameraPosition=(
    0.138622, -0.14319, -0.298171), cameraUpVector=(0.85528, 0.267294, 
    0.443903), cameraTarget=(0.07865, -0.0120694, -0.0386286), 
    viewOffsetX=0.0464491, viewOffsetY=-0.0191303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.304577, 
    farPlane=0.430231, width=0.214261, height=0.0931355, cameraPosition=(
    0.22145, -0.116686, -0.275359), cameraUpVector=(0.701383, 0.287893, 
    0.652058), cameraTarget=(0.0913425, -0.00713519, -0.0320023), 
    viewOffsetX=0.0454477, viewOffsetY=-0.0187179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.302585, 
    farPlane=0.432224, width=0.226446, height=0.0984323, viewOffsetX=0.0463685, 
    viewOffsetY=-0.0142362)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254214, 
    farPlane=0.394531, width=0.190247, height=0.082697, cameraPosition=(
    -0.125165, 0.0284936, -0.318777), cameraUpVector=(0.768546, -0.635844, 
    -0.0709911), cameraTarget=(0.0117339, 0.00898421, -0.0560421), 
    viewOffsetX=0.0389561, viewOffsetY=-0.0119604)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24223, 
    farPlane=0.392283, width=0.181279, height=0.0787987, cameraPosition=(
    -0.216446, 0.0393429, -0.237769), cameraUpVector=(0.756108, -0.438675, 
    -0.48566), cameraTarget=(0.0139079, 0.00659444, -0.0533348), 
    viewOffsetX=0.0371197, viewOffsetY=-0.0113966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23477, 
    farPlane=0.399743, width=0.28823, height=0.125288, viewOffsetX=0.0380372, 
    viewOffsetY=-0.0133656)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.22476, 
    farPlane=0.394788, width=0.275941, height=0.119947, cameraPosition=(
    -0.0893858, 0.159256, 0.236409), cameraUpVector=(-0.532513, 0.439646, 
    -0.723285), cameraTarget=(-0.0156922, 0.0417473, -0.026103), 
    viewOffsetX=0.0364155, viewOffsetY=-0.0127958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229394, 
    farPlane=0.390233, width=0.28163, height=0.12242, cameraPosition=(0.184034, 
    0.0188657, 0.238659), cameraUpVector=(-0.658968, 0.736084, 0.154729), 
    cameraTarget=(0.00278026, 0.0402764, 0.00447877), viewOffsetX=0.0371662, 
    viewOffsetY=-0.0130596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.230585, 
    farPlane=0.39832, width=0.283093, height=0.123055, cameraPosition=(0.23423, 
    0.100482, 0.204882), cameraUpVector=(-0.523555, 0.849317, -0.0674541), 
    cameraTarget=(0.0100332, 0.0636218, 0.0137569), viewOffsetX=0.0373591, 
    viewOffsetY=-0.0131274)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.218573, 
    farPlane=0.385028, width=0.268345, height=0.116645, cameraPosition=(
    -0.127169, -0.0188308, 0.226579), cameraUpVector=(-0.174398, 0.973656, 
    -0.146901), cameraTarget=(-0.0247997, 0.0608554, -0.0404831), 
    viewOffsetX=0.0354129, viewOffsetY=-0.0124435)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.219029, 
    farPlane=0.401487, width=0.268905, height=0.116888, cameraPosition=(
    -0.199079, 0.261168, 0.0116343), cameraUpVector=(0.855347, 0.50412, 
    0.119349), cameraTarget=(0.0292192, 0.0890985, -0.0685126), 
    viewOffsetX=0.0354868, viewOffsetY=-0.0124695)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221784, 
    farPlane=0.38881, width=0.272287, height=0.118359, cameraPosition=(
    -0.165821, -0.0377678, -0.257274), cameraUpVector=(0.845491, 0.273793, 
    -0.458457), cameraTarget=(0.0471011, 0.00512598, -0.05485), 
    viewOffsetX=0.0359332, viewOffsetY=-0.0126263)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.219703, 
    farPlane=0.389191, width=0.269733, height=0.117248, cameraPosition=(
    -0.215742, -0.0605241, -0.187748), cameraUpVector=(0.745288, 0.0570423, 
    -0.664298), cameraTarget=(0.0384184, -0.000654126, -0.0464365), 
    viewOffsetX=0.035596, viewOffsetY=-0.0125078)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.223239, 
    farPlane=0.387476, width=0.274074, height=0.119135, cameraPosition=(
    -0.182499, -0.0326009, -0.243729), cameraUpVector=(0.880915, -0.00702977, 
    -0.473223), cameraTarget=(0.0364756, -0.00121042, -0.0456997), 
    viewOffsetX=0.0361689, viewOffsetY=-0.0127091)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222907, 
    farPlane=0.387808, width=0.273667, height=0.118958, viewOffsetX=0.0515684, 
    viewOffsetY=-0.0171758)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.230158, 
    farPlane=0.380557, width=0.18324, height=0.0796513, viewOffsetX=0.0493989, 
    viewOffsetY=-0.0184896)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.231144, 
    farPlane=0.379571, width=0.184025, height=0.0799925, viewOffsetX=0.0442939, 
    viewOffsetY=-0.0157938)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=8)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23984, 
    farPlane=0.395203, width=0.190948, height=0.0830018, cameraPosition=(
    -0.155924, 0.305502, -0.0871224), cameraUpVector=(0.449944, -0.200093, 
    -0.870352), cameraTarget=(-0.02009, 0.0420473, -0.0700398), 
    viewOffsetX=0.0459602, viewOffsetY=-0.016388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23859, 
    farPlane=0.408148, width=0.189952, height=0.082569, cameraPosition=(
    0.150586, 0.220355, 0.220062), cameraUpVector=(-0.402686, 0.674773, 
    -0.618487), cameraTarget=(-0.0100052, 0.0811517, 0.012736), 
    viewOffsetX=0.0457206, viewOffsetY=-0.0163026)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241499, 
    farPlane=0.403267, width=0.192268, height=0.0835756, cameraPosition=(
    0.0831301, 0.207945, 0.249503), cameraUpVector=(-0.38349, 0.678699, 
    -0.626341), cameraTarget=(-0.0213133, 0.0713676, 0.00745044), 
    viewOffsetX=0.046278, viewOffsetY=-0.0165013)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237313, 
    farPlane=0.407452, width=0.238094, height=0.103495, viewOffsetX=0.0479855, 
    viewOffsetY=-0.015344)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237132, 
    farPlane=0.407633, width=0.237913, height=0.103416, viewOffsetX=0.0566968, 
    viewOffsetY=-0.0264071)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23667, 
    farPlane=0.401058, width=0.237449, height=0.103215, cameraPosition=(
    0.0342673, 0.218396, 0.244639), cameraUpVector=(-0.294554, 0.646143, 
    -0.704086), cameraTarget=(-0.0276998, 0.0708205, -0.00542617), 
    viewOffsetX=0.0565863, viewOffsetY=-0.0263556)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239123, 
    farPlane=0.398605, width=0.199265, height=0.0866171, viewOffsetX=0.05151, 
    viewOffsetY=-0.0269885)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240864, 
    farPlane=0.388736, width=0.200716, height=0.0872478, cameraPosition=(
    -0.0898095, 0.170468, 0.240917), cameraUpVector=(-0.0290312, 0.752416, 
    -0.658048), cameraTarget=(-0.033352, 0.066138, -0.0312577), 
    viewOffsetX=0.051885, viewOffsetY=-0.027185)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243039, 
    farPlane=0.38734, width=0.202528, height=0.0880355, cameraPosition=(
    -0.100349, 0.141464, 0.248341), cameraUpVector=(-0.0787665, 0.794079, 
    -0.602689), cameraTarget=(-0.0351294, 0.061309, -0.0299987), 
    viewOffsetX=0.0523534, viewOffsetY=-0.0274304)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.258931, 
    farPlane=0.371448, width=0.0247439, height=0.0107557, 
    viewOffsetX=0.0429441, viewOffsetY=-0.0261326)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241583, 
    farPlane=0.388797, width=0.204629, height=0.0889488, viewOffsetX=0.063858, 
    viewOffsetY=-0.0320255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.265017, 
    farPlane=0.422011, width=0.224479, height=0.0975769, cameraPosition=(
    0.229594, 0.0372179, 0.258215), cameraUpVector=(-0.0124514, 0.972176, 
    -0.23392), cameraTarget=(0.0220454, 0.086679, 0.0517481), 
    viewOffsetX=0.0700523, viewOffsetY=-0.0351321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263425, 
    farPlane=0.423602, width=0.223131, height=0.096991, viewOffsetX=0.0696315, 
    viewOffsetY=-0.0349211)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=22)
#: Error in job static_pressure_Job-3: Time increment required is less than the minimum specified
#: Error in job static_pressure_Job-3: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job static_pressure_Job-3: Abaqus/Standard aborted due to errors.
#: Error in job static_pressure_Job-3: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job static_pressure_Job-3 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23832, 
    farPlane=0.402317, width=0.292615, height=0.127195, viewOffsetX=0.0758328, 
    viewOffsetY=-0.0284152)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.282503, 
    farPlane=0.447517, width=0.346864, height=0.150776, cameraPosition=(
    0.370643, 0.0143495, 0.116099), cameraUpVector=(-0.145433, 0.988382, 
    -0.0441678), cameraTarget=(0.0847996, 0.0698258, 0.0580695), 
    viewOffsetX=0.0898918, viewOffsetY=-0.0336832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.296987, 
    farPlane=0.478618, width=0.364649, height=0.158506, cameraPosition=(
    0.114425, -0.337902, -0.0980529), cameraUpVector=(0.902712, 0.395132, 
    0.170241), cameraTarget=(0.0833498, -0.0646248, 0.0137752), 
    viewOffsetX=0.0945006, viewOffsetY=-0.0354102)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.354225, 
    farPlane=0.499046, width=0.434927, height=0.189055, cameraPosition=(
    0.0777296, -0.0431792, -0.461283), cameraUpVector=(0.919628, -0.135852, 
    0.368551), cameraTarget=(0.0640732, -0.0609428, -0.165226), 
    viewOffsetX=0.112713, viewOffsetY=-0.0422347)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333634, 
    farPlane=0.535165, width=0.409644, height=0.178065, cameraPosition=(
    -0.31463, 0.0316093, -0.323503), cameraUpVector=(0.797621, -0.197247, 
    -0.569995), cameraTarget=(-0.083331, -0.0360028, -0.150065), 
    viewOffsetX=0.106161, viewOffsetY=-0.0397796)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.354822, 
    farPlane=0.513976, width=0.183205, height=0.0796359, viewOffsetX=0.112449, 
    viewOffsetY=-0.0332585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.339976, 
    farPlane=0.501915, width=0.175539, height=0.0763039, cameraPosition=(
    -0.25402, -0.198133, -0.262165), cameraUpVector=(0.828858, -0.0220754, 
    -0.559024), cameraTarget=(-0.022782, -0.10665, -0.0999582), 
    viewOffsetX=0.107744, viewOffsetY=-0.031867)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330644, 
    farPlane=0.511246, width=0.303026, height=0.13172, viewOffsetX=0.109082, 
    viewOffsetY=-0.0332671)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.350075, 
    farPlane=0.509798, width=0.320833, height=0.13946, cameraPosition=(
    -0.178603, -0.0597859, -0.414051), cameraUpVector=(0.959255, 0.0659556, 
    -0.274736), cameraTarget=(-0.00591739, -0.0650245, -0.17259), 
    viewOffsetX=0.115492, viewOffsetY=-0.0352221)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=48)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['spiral_Model_static_pressure'].loads['Load-1'].setValues(
    magnitude=-111.0)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_pressure_Job-3'].submit(consistencyChecking=OFF)
#: The job input file "static_pressure_Job-3.inp" has been submitted for analysis.
a = mdb.models['spiral_Model_static_traction'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Job static_pressure_Job-3: Analysis Input File Processor completed successfully.
mdb.models['spiral_Model_static_traction'].loads['Load-1'].setValues(
    magnitude=100.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['static_traction_Job-4'].submit(consistencyChecking=OFF)
#: The job input file "static_traction_Job-4.inp" has been submitted for analysis.
#: Job static_traction_Job-4: Analysis Input File Processor completed successfully.
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31719, 
    farPlane=0.512038, width=0.157565, height=0.0684908, viewOffsetX=0.001337, 
    viewOffsetY=-0.0148384)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.323715, 
    farPlane=0.512515, width=0.160806, height=0.0698998, cameraPosition=(
    0.326417, 0.241773, 0.252884), cameraUpVector=(-0.701167, 0.667223, 
    -0.251352), cameraTarget=(0.0464635, 0.0616139, 0.00575347), 
    viewOffsetX=0.0013645, viewOffsetY=-0.0151436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312796, 
    farPlane=0.515193, width=0.155383, height=0.0675422, cameraPosition=(
    0.285641, 0.315249, 0.222988), cameraUpVector=(-0.688082, 0.535431, 
    -0.489752), cameraTarget=(0.0455811, 0.0610428, 0.000153603), 
    viewOffsetX=0.00131848, viewOffsetY=-0.0146328)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336106, 
    farPlane=0.510988, width=0.166963, height=0.0725757, cameraPosition=(
    0.405554, 0.139834, 0.209681), cameraUpVector=(-0.49129, 0.859412, 
    -0.141581), cameraTarget=(0.0515985, 0.0649437, 0.00716797), 
    viewOffsetX=0.00141674, viewOffsetY=-0.0157233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.342951, 
    farPlane=0.504978, width=0.170363, height=0.0740539, cameraPosition=(
    0.381774, 0.119313, 0.25283), cameraUpVector=(-0.413129, 0.88726, 
    -0.20517), cameraTarget=(0.052105, 0.0648162, 0.00736418), 
    viewOffsetX=0.00144559, viewOffsetY=-0.0160435)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346582, 
    farPlane=0.501347, width=0.119259, height=0.0518397, 
    viewOffsetX=0.00151429, viewOffsetY=-0.0318047)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    datumPlanes=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.348282, 
    farPlane=0.486854, width=0.119844, height=0.052094, cameraPosition=(
    0.388966, 0.199905, 0.193341), cameraUpVector=(-0.574617, 0.780607, 
    -0.245903), cameraTarget=(0.0463684, 0.064768, 0.00289383), 
    viewOffsetX=0.00152172, viewOffsetY=-0.0319607)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34532, 
    farPlane=0.488733, width=0.118825, height=0.051651, cameraPosition=(
    0.404193, 0.211308, 0.15055), cameraUpVector=(-0.576853, 0.763096, 
    -0.291419), cameraTarget=(0.0469712, 0.0647093, -0.000468953), 
    viewOffsetX=0.00150878, viewOffsetY=-0.0316888)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.363401, 
    farPlane=0.504485, width=0.125047, height=0.0543556, cameraPosition=(
    0.459965, -0.0512716, -0.0799161), cameraUpVector=(-0.027037, 0.985822, 
    0.1656), cameraTarget=(0.0715443, 0.0633386, 0.00896318), 
    viewOffsetX=0.00158778, viewOffsetY=-0.033348)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.355799, 
    farPlane=0.512088, width=0.214543, height=0.0932582, 
    viewOffsetX=0.00109092, viewOffsetY=-0.0274173)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.362023, 
    farPlane=0.496122, width=0.218296, height=0.0948894, cameraPosition=(
    0.455652, 0.0474518, -0.129771), cameraUpVector=(-0.178324, 0.918011, 
    0.354199), cameraTarget=(0.0664228, 0.0678399, 0.0116181), 
    viewOffsetX=0.00111, viewOffsetY=-0.0278969)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.364947, 
    farPlane=0.491695, width=0.220059, height=0.0956558, cameraPosition=(
    0.402515, 0.0364782, -0.236627), cameraUpVector=(-0.0797174, 0.937069, 
    0.339921), cameraTarget=(0.0668175, 0.0678739, 0.00467642), 
    viewOffsetX=0.00111896, viewOffsetY=-0.0281222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370947, 
    farPlane=0.482508, width=0.223677, height=0.0972285, cameraPosition=(
    0.353139, 0.0566859, -0.295616), cameraUpVector=(-0.0339349, 0.918377, 
    0.394248), cameraTarget=(0.0656515, 0.0683963, 0.00291328), 
    viewOffsetX=0.00113736, viewOffsetY=-0.0285845)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.365231, 
    farPlane=0.490795, width=0.22023, height=0.0957304, cameraPosition=(
    0.394584, 0.0427126, -0.247708), cameraUpVector=(-0.17684, 0.959654, 
    0.218614), cameraTarget=(0.0630621, 0.0692372, -0.000128541), 
    viewOffsetX=0.00111984, viewOffsetY=-0.0281441)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.375143, 
    farPlane=0.480883, width=0.121839, height=0.0529613, 
    viewOffsetX=0.00372861, viewOffsetY=-0.0420563)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.36021, 
    farPlane=0.481425, width=0.116989, height=0.0508531, cameraPosition=(
    0.403211, 0.137652, -0.206687), cameraUpVector=(-0.391052, 0.877466, 
    0.277725), cameraTarget=(0.0532165, 0.0719652, 0.00566973), 
    viewOffsetX=0.00358019, viewOffsetY=-0.0403821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.365401, 
    farPlane=0.494172, width=0.118675, height=0.0515859, cameraPosition=(
    0.468622, 0.00878713, -0.0701163), cameraUpVector=(-0.141993, 0.940233, 
    0.309515), cameraTarget=(0.0669991, 0.0672071, 0.0146905), 
    viewOffsetX=0.00363178, viewOffsetY=-0.040964)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.365472, 
    farPlane=0.48318, width=0.118698, height=0.051596, cameraPosition=(
    0.459288, 0.0791907, 0.10293), cameraUpVector=(-0.418968, 0.85755, 
    0.298453), cameraTarget=(0.0519359, 0.0679415, 0.0264835), 
    viewOffsetX=0.00363249, viewOffsetY=-0.040972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.367269, 
    farPlane=0.481384, width=0.093129, height=0.0404815, 
    viewOffsetX=0.00282752, viewOffsetY=-0.0458705)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370254, 
    farPlane=0.480581, width=0.0938861, height=0.0408107, cameraPosition=(
    0.458491, 0.0657876, 0.112602), cameraUpVector=(-0.397934, 0.87039, 
    0.289949), cameraTarget=(0.052888, 0.0677704, 0.0266432), 
    viewOffsetX=0.00285051, viewOffsetY=-0.0462434)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.365983, 
    farPlane=0.479311, width=0.0928032, height=0.0403399, cameraPosition=(
    0.43002, 0.110452, -0.16894), cameraUpVector=(-0.276217, 0.880736, 
    0.384719), cameraTarget=(0.0593518, 0.0717541, 0.0127575), 
    viewOffsetX=0.00281763, viewOffsetY=-0.04571)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.366078, 
    farPlane=0.479216, width=0.0928272, height=0.0403504, cameraPosition=(
    0.425156, 0.112583, -0.178409), cameraUpVector=(-0.36282, 0.907037, 
    0.213647), cameraTarget=(0.0544876, 0.0738855, 0.00328839), 
    viewOffsetX=0.00281836, viewOffsetY=-0.0457218)
#: Job static_traction_Job-4: Abaqus/Standard completed successfully.
#: Job static_traction_Job-4 completed successfully. 
#: Error in job static_pressure_Job-3: Time increment required is less than the minimum specified
#: Error in job static_pressure_Job-3: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job static_pressure_Job-3: Abaqus/Standard aborted due to errors.
#: Error in job static_pressure_Job-3: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job static_pressure_Job-3 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.365565, 
    farPlane=0.479728, width=0.0926971, height=0.0402938, 
    viewOffsetX=0.0114257, viewOffsetY=-0.0455097)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['spiral_Model_static_pressure'].loads['Load-1'].setValues(
    magnitude=-110.0)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_pressure_Job-3.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_pressure_Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_pressure_Job-3.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['static_pressure_Job-3'].submit(consistencyChecking=OFF)
#: The job input file "static_pressure_Job-3.inp" has been submitted for analysis.
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
#: Job static_pressure_Job-3: Analysis Input File Processor completed successfully.
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
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
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=19)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=59)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=HARMONIC)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.animationOptions.setValues(frameRate=14)
session.animationOptions.setValues(frameRate=80)
session.animationOptions.setValues(mode=LOOP_BACKWARD)
session.animationOptions.setValues(mode=SWING)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.303308, 
    farPlane=0.446539, width=0.309285, height=0.134441, viewOffsetX=0.0297743, 
    viewOffsetY=-0.0118678)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.298066, 
    farPlane=0.451214, width=0.303939, height=0.132117, cameraPosition=(
    -0.203304, -0.0542688, -0.259827), cameraUpVector=(0.802637, 0.339532, 
    -0.490401), cameraTarget=(0.0131659, 0.00584551, -0.0657181), 
    viewOffsetX=0.0292597, viewOffsetY=-0.0116626)
session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_traction_Job-4.odb'].close(
    )
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Dynamics_Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Dynamics_Job-1.odb'].close(
    )
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/Statics_Job-2.odb'].close(
    )
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
a = mdb.models['spiral_Model_static_pressure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job static_pressure_Job-3: Abaqus/Standard completed successfully.
#: Job static_pressure_Job-3 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_pressure_Job-3.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/LAB_files/static_pressure_Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244872, 
    farPlane=0.418202, width=0.259398, height=0.112756, cameraPosition=(
    -0.266013, 0.214335, 0.0145877), cameraUpVector=(0.00554675, -0.398748, 
    -0.917044), cameraTarget=(-0.018922, 0.0538537, -0.0220575))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24943, 
    farPlane=0.413073, width=0.264226, height=0.114855, cameraPosition=(
    -0.296789, 0.107897, -0.129109), cameraUpVector=(0.399289, -0.689445, 
    -0.604345), cameraTarget=(-0.0221371, 0.0427343, -0.0370692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24563, 
    farPlane=0.415138, width=0.260202, height=0.113105, cameraPosition=(
    -0.274033, 0.108807, -0.180823), cameraUpVector=(0.515888, -0.659291, 
    -0.546987), cameraTarget=(-0.0197774, 0.0428287, -0.0424317))
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae".
