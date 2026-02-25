# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-15.00.46 RELr427 198590
# Run by st195764 on Tue Feb 24 17:34:49 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=280.243225097656, 
    height=116.481483459473)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Spiral_Final_CAE.cae')
#: The model database "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Spiral_Model_1'].parts['Divider_Tool']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-1', model='Spiral_Model_1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Job-1.inp" has been submitted for analysis.
mdb.Job(name='Job-2', model='Spiral_Model_2', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
#: Job Job-1: Analysis Input File Processor completed successfully.
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
#: Job Job-2: Analysis Input File Processor completed successfully.
mdb.Job(name='Job-3', model='Spiral_Model_3', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-3: Analysis Input File Processor completed successfully.
mdb.jobs['Job-1'].setValues(numCpus=6, numDomains=6)
#* The job is running and cannot be modified at this point.
#: Job Job-1: Analysis Input File Processor completed successfully.
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae".
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
#: Job Job-3: Abaqus/Standard completed successfully.
#: Job Job-3 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-1.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.226486, 
    farPlane=0.400516, width=0.107745, height=0.0412247, viewOffsetX=0.0065009, 
    viewOffsetY=-0.0152331)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Spiral_Model_3'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Model(name='Spiral_Model_4', objectToCopy=mdb.models['Spiral_Model_3'])
#: The model "Spiral_Model_4" has been created.
a = mdb.models['Spiral_Model_4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Model(name='Spiral_Model_5', objectToCopy=mdb.models['Spiral_Model_4'])
#: The model "Spiral_Model_5" has been created.
a = mdb.models['Spiral_Model_5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_3'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Spiral_Model_4'].loads['Load-1'].setValues(magnitude=14000.0)
mdb.models['Spiral_Model_4'].loads['Load-2'].setValues(magnitude=14000.0)
a = mdb.models['Spiral_Model_5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Spiral_Model_5'].loads['Load-1'].setValues(magnitude=15000.0)
mdb.models['Spiral_Model_5'].loads['Load-2'].setValues(magnitude=15000.0)
mdb.Model(name='Spiral_Model_6', objectToCopy=mdb.models['Spiral_Model_5'])
#: The model "Spiral_Model_6" has been created.
a = mdb.models['Spiral_Model_6'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Spiral_Model_6'].loads['Load-1'].setValues(magnitude=16000.0)
mdb.models['Spiral_Model_6'].loads['Load-2'].setValues(magnitude=16000.0)
mdb.Model(name='Spiral_Model_7', objectToCopy=mdb.models['Spiral_Model_6'])
#: The model "Spiral_Model_7" has been created.
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Spiral_Model_7'].loads['Load-1'].setValues(magnitude=17000.0)
mdb.models['Spiral_Model_7'].loads['Load-2'].setValues(magnitude=17000.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-4', model='Spiral_Model_4', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: The job input file "Job-4.inp" has been submitted for analysis.
mdb.Job(name='Job-5', model='Spiral_Model_5', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['Job-5'].submit(consistencyChecking=OFF)
#: The job input file "Job-5.inp" has been submitted for analysis.
#: Job Job-4: Analysis Input File Processor completed successfully.
mdb.Job(name='Job-6', model='Spiral_Model_6', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
#: Job Job-5: Analysis Input File Processor completed successfully.
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: The job input file "Job-6.inp" has been submitted for analysis.
mdb.Job(name='Job-7', model='Spiral_Model_7', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['Job-7'].submit(consistencyChecking=OFF)
#: The job input file "Job-7.inp" has been submitted for analysis.
#: Job Job-6: Analysis Input File Processor completed successfully.
#: Job Job-7: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.322673, 
    farPlane=0.507474, width=0.0980975, height=0.0426413, 
    viewOffsetX=0.0219931, viewOffsetY=0.00947334)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae".
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.215594, 
    farPlane=0.353069, width=0.0926331, height=0.103213, 
    viewOffsetX=0.00176071, viewOffsetY=-0.0183193)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Job-7']
mdb.Job(name='Job-7', model='Spiral_Model_7', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
mdb.jobs['Job-7'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file Job-7.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#: The job input file "Job-7.inp" has been submitted for analysis.
del mdb.jobs['Job-6']
mdb.Job(name='Job-8', model='Spiral_Model_6', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
del mdb.jobs['Job-8']
mdb.Job(name='Job-6', model='Spiral_Model_6', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file Job-6.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#: The job input file "Job-6.inp" has been submitted for analysis.
del mdb.jobs['Job-5']
mdb.Job(name='Job-5', model='Spiral_Model_5', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=7, 
    numDomains=7, numGPUs=0)
mdb.jobs['Job-5'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file Job-5.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#: The job input file "Job-5.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Job-4']
mdb.Job(name='Job-4', model='Spiral_Model_4', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=5, 
    numDomains=5, numGPUs=0)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file Job-4.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#: The job input file "Job-4.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=17)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=17)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=14)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.21754, 
    farPlane=0.399373, width=0.0638185, height=0.0711077, 
    viewOffsetX=0.00705533, viewOffsetY=-0.0113497)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.204733, 
    farPlane=0.391973, width=0.070275, height=0.0783016, 
    viewOffsetX=0.00485097, viewOffsetY=0.000920075)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=6)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=23)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221968, 
    farPlane=0.407502, width=0.0887277, height=0.098862, 
    viewOffsetX=-0.00478723, viewOffsetY=-0.0192685)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=23)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job Job-4: Abaqus/Standard completed successfully.
#: Job Job-4: Abaqus/Standard completed successfully.
#: Job Job-4 completed successfully. 
#: Job Job-4 completed successfully. 
#: Job Job-5: Abaqus/Standard completed successfully.
#: Job Job-5: Abaqus/Standard completed successfully.
#: Job Job-5 completed successfully. 
#: Job Job-5 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-3.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=26)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=18)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=26)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=36)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=36)
#: Job Job-6: Abaqus/Standard completed successfully.
#: Job Job-6: Abaqus/Standard completed successfully.
#: Job Job-6 completed successfully. 
#: Job Job-6 completed successfully. 
#: Job Job-7: Abaqus/Standard completed successfully.
#: Job Job-7: Abaqus/Standard completed successfully.
#: Job Job-7 completed successfully. 
#: Job Job-7 completed successfully. 
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=24)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-4.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=33)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=26)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=24)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=24)
a = mdb.models['Spiral_Model_7'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-7'].setValues(numCpus=10, numDomains=10)
mdb.jobs['Job-7'].submit(consistencyChecking=OFF)
#: The job input file "Job-7.inp" has been submitted for analysis.
mdb.Model(name='Spiral_Model_8', objectToCopy=mdb.models['Spiral_Model_7'])
#: The model "Spiral_Model_8" has been created.
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job Job-7: Analysis Input File Processor completed successfully.
mdb.Job(name='Job-8', model='Spiral_Model_8', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=0, numCpus=10, 
    numDomains=10, numGPUs=0)
mdb.jobs['Job-8'].submit(consistencyChecking=OFF)
#: The job input file "Job-8.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
#: Job Job-8: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=26)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229727, 
    farPlane=0.354757, width=0.138602, height=0.0602478, 
    viewOffsetX=0.000665179, viewOffsetY=-0.00705161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217168, 
    farPlane=0.339991, width=0.131024, height=0.0569539, cameraPosition=(
    -0.218157, 0.126049, 0.0915429), cameraUpVector=(0.240474, 0.942622, 
    -0.231595), cameraTarget=(0.0443084, 0.0364469, -0.000622954), 
    viewOffsetX=0.000628813, viewOffsetY=-0.00666609)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.22748, 
    farPlane=0.329678, width=0.0243698, height=0.0105931, 
    viewOffsetX=-0.0129651, viewOffsetY=-0.0375811)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.246348, 
    farPlane=0.32147, width=0.0263911, height=0.0114717, cameraPosition=(
    -0.248933, 0.0931896, 0.0251349), cameraUpVector=(0.173326, 0.974044, 
    -0.145592), cameraTarget=(0.0378437, 0.039585, 0.00790985), 
    viewOffsetX=-0.0140404, viewOffsetY=-0.0406981)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247322, 
    farPlane=0.320496, width=0.0128772, height=0.0055975, 
    viewOffsetX=-0.00900716, viewOffsetY=-0.0414485)
session.viewports['Viewport: 1'].view.setValues(width=0.0121082, 
    height=0.00526323, viewOffsetX=-0.0102282, viewOffsetY=-0.0413747)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:5 #8000000 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.629429, 0, 0, -0.103461, 0, 0.629429, 0, -0.170823, 0, 0, 
    0.629429, 0, 0, 0, 0, 1))
import sys
sys.path.insert(8, 
    r'c:/SIMULIA/EstProducts/2025/win_b64/code/python3.10/lib/abaqus_plugins/excelUtilities')
import abq_ExcelUtilities.excelUtilities
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 188,_U:U2 PI: FINAL_PART-1 N: 188', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244402, 
    farPlane=0.323416, width=0.0486082, height=0.0211291, 
    viewOffsetX=0.00382714, viewOffsetY=-0.000584304)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244145, 
    farPlane=0.323673, width=0.0485571, height=0.0211069, cameraPosition=(
    -0.248808, 0.0938408, 0.0251874), cameraUpVector=(0.183836, 0.982956, 
    0.00165951), cameraTarget=(0.0379686, 0.0402362, 0.00796235), 
    viewOffsetX=0.00382312, viewOffsetY=-0.00058369)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238358, 
    farPlane=0.335262, width=0.0474062, height=0.0206066, cameraPosition=(
    -0.2137, 0.179434, -0.0332049), cameraUpVector=(0.488154, 0.872411, 
    0.0245912), cameraTarget=(0.0380547, 0.0373554, 0.00973736), 
    viewOffsetX=0.0037325, viewOffsetY=-0.000569855)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240354, 
    farPlane=0.333264, width=0.0283331, height=0.0123159, 
    viewOffsetX=0.00161297, viewOffsetY=-0.0035174)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:5 #10 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 165,_U:U2 PI: FINAL_PART-1 N: 165', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23741, 
    farPlane=0.336209, width=0.0555017, height=0.0241256, 
    viewOffsetX=0.00603716, viewOffsetY=0.00876907)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237718, 
    farPlane=0.335901, width=0.0555739, height=0.024157, cameraPosition=(
    -0.213225, 0.180003, -0.0341089), cameraUpVector=(0.473414, 0.873397, 
    0.11427), cameraTarget=(0.0385299, 0.0379242, 0.0088334), 
    viewOffsetX=0.00604501, viewOffsetY=0.00878047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243551, 
    farPlane=0.360172, width=0.0569375, height=0.0247498, cameraPosition=(
    0.105731, 0.278469, -0.142952), cameraUpVector=(0.593707, 0.297401, 
    0.747706), cameraTarget=(0.0355205, 0.0384411, 0.00826974), 
    viewOffsetX=0.00619334, viewOffsetY=0.00899592)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237239, 
    farPlane=0.366483, width=0.132428, height=0.0575641, 
    viewOffsetX=0.00573734, viewOffsetY=0.0070901)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222291, 
    farPlane=0.369656, width=0.124084, height=0.0539371, cameraPosition=(
    0.176323, 0.183576, -0.198683), cameraUpVector=(0.567559, 0.437596, 
    0.697414), cameraTarget=(0.0373181, 0.0324377, 0.00927273), 
    viewOffsetX=0.00537585, viewOffsetY=0.00664337)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233592, 
    farPlane=0.358355, width=0.00757064, height=0.00329083, 
    viewOffsetX=0.00430092, viewOffsetY=0.00569718)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:5 #10 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232229, 
    farPlane=0.359718, width=0.0216367, height=0.00940511, 
    viewOffsetX=0.00485585, viewOffsetY=0.00402089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234126, 
    farPlane=0.360211, width=0.0218135, height=0.00948194, cameraPosition=(
    0.184162, 0.193558, -0.185944), cameraUpVector=(0.535285, 0.409043, 
    0.739022), cameraTarget=(0.0376271, 0.0327542, 0.00919762), 
    viewOffsetX=0.00489551, viewOffsetY=0.00405374)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233032, 
    farPlane=0.361304, width=0.0357637, height=0.0155458, 
    viewOffsetX=0.00557837, viewOffsetY=0.00341884)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:5 #10 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.228424, 
    farPlane=0.365913, width=0.0894119, height=0.0388658, 
    viewOffsetX=0.0172111, viewOffsetY=0.00221259)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:4 #2 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 130,_U:U2 PI: FINAL_PART-1 N: 130', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.225809, 
    farPlane=0.368527, width=0.106417, height=0.0462578, 
    viewOffsetX=-0.00381938, viewOffsetY=-0.00264799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.227856, 
    farPlane=0.369497, width=0.107382, height=0.0466771, cameraPosition=(
    0.222236, -0.0780193, -0.198683), cameraUpVector=(0.783359, 0.167731, 
    0.598511), cameraTarget=(0.0429633, 0.0283636, 0.00614503), 
    viewOffsetX=-0.003854, viewOffsetY=-0.002672)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237025, 
    farPlane=0.360328, width=0.00573062, height=0.002491, 
    viewOffsetX=-0.00385887, viewOffsetY=0.00305023)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2398, 
    farPlane=0.360832, width=0.00579772, height=0.00252017, cameraPosition=(
    0.239804, -0.0820145, -0.180301), cameraUpVector=(0.72789, 0.170238, 
    0.664226), cameraTarget=(0.0437477, 0.0282404, 0.00628968), 
    viewOffsetX=-0.00390405, viewOffsetY=0.00308594)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238494, 
    farPlane=0.362137, width=0.0213181, height=0.0092666, 
    viewOffsetX=-0.0040882, viewOffsetY=0.00137912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.246123, 
    farPlane=0.361285, width=0.022, height=0.00956301, cameraPosition=(
    0.270574, -0.102213, -0.126347), cameraUpVector=(0.579451, 0.187533, 
    0.793138), cameraTarget=(0.0454474, 0.0274981, 0.0074565), 
    viewOffsetX=-0.00421897, viewOffsetY=0.00142323)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244973, 
    farPlane=0.362435, width=0.0360694, height=0.0156787, 
    viewOffsetX=-0.00498556, viewOffsetY=0.000705763)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254297, 
    farPlane=0.358589, width=0.0374423, height=0.0162755, cameraPosition=(
    0.274106, -0.14368, -0.06217), cameraUpVector=(0.452366, 0.244961, 
    0.857531), cameraTarget=(0.0466962, 0.0253029, 0.009522), 
    viewOffsetX=-0.00517533, viewOffsetY=0.000732627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.256752, 
    farPlane=0.356134, width=0.00856255, height=0.00372199, 
    viewOffsetX=0.000957248, viewOffsetY=-0.00371958)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0:2 #100000 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 85,_U:U2 PI: FINAL_PART-1 N: 85', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249442, 
    farPlane=0.363443, width=0.0948284, height=0.0412203, 
    viewOffsetX=-0.00382022, viewOffsetY=-0.0115358)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251105, 
    farPlane=0.360367, width=0.0954606, height=0.0414951, cameraPosition=(
    0.123446, -0.252729, -0.0804617), cameraUpVector=(0.577068, -0.0942791, 
    0.811236), cameraTarget=(0.0428946, 0.0139653, 0.00783232), 
    viewOffsetX=-0.00384569, viewOffsetY=-0.0116127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253711, 
    farPlane=0.357534, width=0.0964513, height=0.0419257, cameraPosition=(
    0.0895083, -0.262896, -0.0780244), cameraUpVector=(0.56351, -0.154936, 
    0.811451), cameraTarget=(0.0413968, 0.0122556, 0.00792297), 
    viewOffsetX=-0.0038856, viewOffsetY=-0.0117332)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.261545, 
    farPlane=0.349698, width=0.0089023, height=0.00386968, 
    viewOffsetX=-0.00283809, viewOffsetY=-0.00701717)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0 #400000 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 55,_U:U2 PI: FINAL_PART-1 N: 55', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255286, 
    farPlane=0.355957, width=0.0829932, height=0.0360757, 
    viewOffsetX=-0.00663059, viewOffsetY=-0.00998725)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243834, 
    farPlane=0.36662, width=0.07927, height=0.0344573, cameraPosition=(
    -0.145315, -0.200732, -0.110465), cameraUpVector=(0.431792, -0.685601, 
    0.586095), cameraTarget=(0.0286163, 0.0052538, 0.00235322), 
    viewOffsetX=-0.00633314, viewOffsetY=-0.0095392)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250866, 
    farPlane=0.359589, width=0.00535897, height=0.00232945, 
    viewOffsetX=-0.00567606, viewOffsetY=-0.00888986)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#400 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 11,_U:U2 PI: FINAL_PART-1 N: 11', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#400 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249097, 
    farPlane=0.361358, width=0.0266967, height=0.0116046, 
    viewOffsetX=-0.00357286, viewOffsetY=-0.0106391)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249216, 
    farPlane=0.358635, width=0.0267095, height=0.0116101, cameraPosition=(
    -0.230283, -0.0226666, -0.153955), cameraUpVector=(-0.126616, -0.909213, 
    0.396612), cameraTarget=(0.0173544, 0.00911218, -0.0020466), 
    viewOffsetX=-0.00357457, viewOffsetY=-0.0106442)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241276, 
    farPlane=0.364793, width=0.0258586, height=0.0112403, cameraPosition=(
    -0.192953, 0.138798, 0.178645), cameraUpVector=(-0.601256, -0.781651, 
    -0.165867), cameraTarget=(0.00902074, 0.0205819, 0.00359724), 
    viewOffsetX=-0.00346069, viewOffsetY=-0.0103051)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243138, 
    farPlane=0.36293, width=0.00590219, height=0.00256558, 
    viewOffsetX=-0.00118466, viewOffsetY=-0.0106444)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24427, 
    farPlane=0.362043, width=0.00592967, height=0.00257752, cameraPosition=(
    -0.198314, 0.150658, 0.163444), cameraUpVector=(-0.60823, -0.778193, 
    -0.156437), cameraTarget=(0.00880281, 0.0210052, 0.00312294), 
    viewOffsetX=-0.00119018, viewOffsetY=-0.010694)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24466, 
    farPlane=0.361652, width=0.00152243, height=0.000661773, 
    viewOffsetX=-0.000920504, viewOffsetY=-0.0107622)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 1, ('[#0 #400 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.361805, 0, 0, -0.30532, 0, 0.361805, 0, -0.038991, 0, 0, 
    0.361805, 0, 0, 0, 0, 1))
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='_U:U1 PI: FINAL_PART-1 N: 43,_U:U2 PI: FINAL_PART-1 N: 43', 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
del session.xyDataObjects['_U:U1 PI: FINAL_PART-1 N: 43']
del session.xyDataObjects['_U:U2 PI: FINAL_PART-1 N: 43']
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244514, 
    farPlane=0.361799, width=0.00302982, height=0.00131701, 
    viewOffsetX=-0.000123013, viewOffsetY=-0.0109644)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235949, 
    farPlane=0.370364, width=0.103181, height=0.0448511, viewOffsetX=0.027138, 
    viewOffsetY=-0.0175318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235426, 
    farPlane=0.370887, width=0.102952, height=0.0447516, viewOffsetX=0.0270778, 
    viewOffsetY=-0.0174929)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209449, 
    farPlane=0.345691, width=0.0915925, height=0.0398136, cameraPosition=(
    -0.133257, -0.163725, 0.13166), cameraUpVector=(-0.0748866, -0.631367, 
    -0.77186), cameraTarget=(0.0378423, 0.0112599, -0.0280748), 
    viewOffsetX=0.02409, viewOffsetY=-0.0155627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.205355, 
    farPlane=0.349784, width=0.156724, height=0.0681252, viewOffsetX=0.0412671, 
    viewOffsetY=-0.0208117)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.204604, 
    farPlane=0.350535, width=0.156151, height=0.0678761, cameraPosition=(
    -0.137508, -0.166298, 0.124288), cameraUpVector=(-0.188716, -0.555017, 
    -0.810149), cameraTarget=(0.0335913, 0.00868692, -0.0354468), 
    viewOffsetX=0.0411162, viewOffsetY=-0.0207356)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.208108, 
    farPlane=0.322664, width=0.158825, height=0.0690385, cameraPosition=(
    -0.0419693, -0.231354, 0.0311354), cameraUpVector=(0.181107, -0.279935, 
    -0.942781), cameraTarget=(0.0480404, 0.0394323, -0.0319772), 
    viewOffsetX=0.0418203, viewOffsetY=-0.0210907)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221446, 
    farPlane=0.309327, width=0.00922374, height=0.0040094, 
    viewOffsetX=0.0107519, viewOffsetY=-0.0263121)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221499, 
    farPlane=0.309274, width=0.00922596, height=0.00401036, cameraPosition=(
    -0.0403883, -0.231589, 0.0323808), cameraUpVector=(0.236322, -0.294379, 
    -0.926009), cameraTarget=(0.0496214, 0.039197, -0.0307318), 
    viewOffsetX=0.0107545, viewOffsetY=-0.0263185)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217585, 
    farPlane=0.316856, width=0.00906295, height=0.00393951, cameraPosition=(
    -0.146175, -0.177399, 0.0412943), cameraUpVector=(0.135238, -0.444134, 
    -0.885695), cameraTarget=(0.0539059, 0.0236914, -0.0289927), 
    viewOffsetX=0.0105645, viewOffsetY=-0.0258535)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.212427, 
    farPlane=0.322014, width=0.069907, height=0.0303874, viewOffsetX=0.0163931, 
    viewOffsetY=-0.0280749)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.21367, 
    farPlane=0.305837, width=0.0703161, height=0.0305652, cameraPosition=(
    0.0141882, -0.233846, 0.036659), cameraUpVector=(0.273994, -0.261244, 
    -0.92557), cameraTarget=(0.0496086, 0.0479142, -0.0323832), 
    viewOffsetX=0.0164891, viewOffsetY=-0.0282391)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.213134, 
    farPlane=0.306375, width=0.0803576, height=0.0349301, 
    viewOffsetX=-8.40286e-06, viewOffsetY=-0.027527)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.21667, 
    farPlane=0.318203, width=0.081691, height=0.0355097, cameraPosition=(
    0.230892, -0.150164, 0.00672434), cameraUpVector=(0.408488, 0.259435, 
    -0.875118), cameraTarget=(0.0275792, 0.0570905, -0.026736), 
    viewOffsetX=-8.54229e-06, viewOffsetY=-0.0279838)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217288, 
    farPlane=0.317585, width=0.0779578, height=0.0338869, 
    viewOffsetX=-0.00571927, viewOffsetY=-0.0233772)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.220085, 
    farPlane=0.342449, width=0.0789611, height=0.034323, cameraPosition=(
    0.131129, 0.266933, 0.107321), cameraUpVector=(-0.239435, 0.572386, 
    -0.784248), cameraTarget=(0.0279664, 0.0320262, -0.0326305), 
    viewOffsetX=-0.00579287, viewOffsetY=-0.023678)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217075, 
    farPlane=0.345459, width=0.117597, height=0.0511173, 
    viewOffsetX=-0.00702422, viewOffsetY=-0.0238864)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.211594, 
    farPlane=0.342938, width=0.114627, height=0.0498266, cameraPosition=(
    -0.126227, 0.241174, 0.0928332), cameraUpVector=(-0.331862, 0.285338, 
    -0.899138), cameraTarget=(0.0337553, 0.0313385, -0.0328049), 
    viewOffsetX=-0.00684687, viewOffsetY=-0.0232833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.211458, 
    farPlane=0.343075, width=0.125984, height=0.0547631, 
    viewOffsetX=-0.0194735, viewOffsetY=-0.0237627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221788, 
    farPlane=0.357027, width=0.132139, height=0.0574384, cameraPosition=(
    -0.163717, -0.166227, 0.115691), cameraUpVector=(-0.527268, -0.161731, 
    -0.834165), cameraTarget=(-0.00921606, 0.0401395, -0.021978), 
    viewOffsetX=-0.0204248, viewOffsetY=-0.0249235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232662, 
    farPlane=0.346153, width=0.00590663, height=0.00256751, 
    viewOffsetX=-0.0243422, viewOffsetY=-0.0172141)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 7, ('[#400 #400400 #100000 #0 #2 #8000010 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ), nodePick=((
    'FINAL_PART-1', 7, ('[#400 #400400 #100000 #0 #2 #8000010 ]', )), ), )
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232353, 
    farPlane=0.346462, width=0.0102946, height=0.0044749, 
    viewOffsetX=-0.024553, viewOffsetY=-0.0172416)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.204821, 
    farPlane=0.330431, width=0.0344061, height=0.0149557, 
    viewOffsetX=0.0115149, viewOffsetY=0.00987515)
x = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=x)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(1.26248, 0, 0, 0.106242, 0, 1.26248, 0, -0.0742011, 0, 0, 
    1.26248, 0, 0, 0, 0, 1))
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.163288, 
    farPlane=0.314117, width=0.17626, height=0.076617, viewOffsetX=0.0317327, 
    viewOffsetY=0.012772)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.animationOptions.setValues(mode=SWING)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.134551, 
    farPlane=0.342234, width=0.155142, height=0.0674374, viewOffsetX=0.0262609, 
    viewOffsetY=0.00336817)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='U:U1 PI: FINAL_PART-1 N: 11,U:U1 PI: FINAL_PART-1 N: 43,U:U1 PI: FINAL_PART-1 N: 55,U:U1 PI: FINAL_PART-1 N: 85,U:U1 PI: FINAL_PART-1 N: 130,U:U1 PI: FINAL_PART-1 N: 165,U:U1 PI: FINAL_PART-1 N: 188,U:U2 PI: FINAL_PART-1 N: 11,U:U2 PI: FINAL_PART-1 N: 43,U:U2 PI: FINAL_PART-1 N: 55,U:U2 PI: FINAL_PART-1 N: 85,U:U2 PI: FINAL_PART-1 N: 130,U:U2 PI: FINAL_PART-1 N: 165,U:U2 PI: FINAL_PART-1 N: 188', 
    trueName='')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].animationController.showFrame(
    frame=41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.126508, 
    farPlane=0.350277, width=0.0889167, height=0.0990726, 
    viewOffsetX=0.0125509, viewOffsetY=0.000886193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.163417, 
    farPlane=0.33417, width=0.114858, height=0.127977, cameraPosition=(
    0.291886, 0.0366564, -0.0535495), cameraUpVector=(-0.291039, 0.940147, 
    0.177255), cameraTarget=(0.0401561, 0.036486, 0.0373127), 
    viewOffsetX=0.0162126, viewOffsetY=0.00114474)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.167372, 
    farPlane=0.341289, width=0.117638, height=0.131074, cameraPosition=(
    0.293668, -0.00347305, 0.0402682), cameraUpVector=(-0.151221, 0.974315, 
    -0.166859), cameraTarget=(0.0307589, 0.0458871, 0.0321222), 
    viewOffsetX=0.016605, viewOffsetY=0.00117245)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.172119, 
    farPlane=0.33413, width=0.120974, height=0.134792, cameraPosition=(
    0.295072, 0.0189046, 0.0505463), cameraUpVector=(-0.243781, 0.96528, 
    -0.0938333), cameraTarget=(0.0291429, 0.0423255, 0.0316546), 
    viewOffsetX=0.0170759, viewOffsetY=0.0012057)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.174191, 
    farPlane=0.328387, width=0.122431, height=0.136415, cameraPosition=(
    0.298963, 0.0404476, 0.0267414), cameraUpVector=(-0.338029, 0.941135, 
    0.000943259), cameraTarget=(0.0314134, 0.0391338, 0.0330246), 
    viewOffsetX=0.0172815, viewOffsetY=0.00122021)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.160169, 
    farPlane=0.365247, width=0.112576, height=0.125434, cameraPosition=(
    0.199293, -0.159898, 0.0263828), cameraUpVector=(0.547278, 0.83393, 
    -0.071043), cameraTarget=(0.0379582, 0.0535263, 0.0330974), 
    viewOffsetX=0.0158903, viewOffsetY=0.00112198)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.183939, 
    farPlane=0.350803, width=0.129283, height=0.144049, cameraPosition=(
    0.0394689, -0.214077, 0.00382733), cameraUpVector=(0.941819, 0.33527, 
    0.0238986), cameraTarget=(0.0387509, 0.0519178, 0.0333258), 
    viewOffsetX=0.0182485, viewOffsetY=0.00128849)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.188336, 
    farPlane=0.346406, width=0.0913207, height=0.101751, viewOffsetX=0.0197505, 
    viewOffsetY=-0.00970267)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.20593, 
    farPlane=0.270242, width=0.00520695, height=0.00580168, 
    viewOffsetX=0.0254111, viewOffsetY=-0.0366146)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.211172, 
    farPlane=0.266395, width=0.0053395, height=0.00594937, cameraPosition=(
    0.0333931, -0.213436, 0.0297801), cameraUpVector=(0.950141, 0.311418, 
    -0.0158152), cameraTarget=(0.0395956, 0.0541182, 0.0301329), 
    viewOffsetX=0.026058, viewOffsetY=-0.0375467)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.208657, 
    farPlane=0.26891, width=0.0163338, height=0.0181994, viewOffsetX=0.0267867, 
    viewOffsetY=-0.0369098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.191091, 
    farPlane=0.284584, width=0.0149588, height=0.0166673, cameraPosition=(
    0.0352331, -0.184173, 0.11812), cameraUpVector=(0.947811, 0.287033, 
    -0.138801), cameraTarget=(0.0395194, 0.0636126, 0.0170868), 
    viewOffsetX=0.0245317, viewOffsetY=-0.0338026)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.188289, 
    farPlane=0.287386, width=0.0260405, height=0.0290148, viewOffsetX=0.030276, 
    viewOffsetY=-0.0336139)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.173975, 
    farPlane=0.29494, width=0.0240609, height=0.0268091, cameraPosition=(
    0.0335952, -0.116063, 0.191446), cameraUpVector=(0.950353, 0.173409, 
    -0.258378), cameraTarget=(0.0411138, 0.0682054, -0.002493), 
    viewOffsetX=0.0279744, viewOffsetY=-0.0310586)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.158477, 
    farPlane=0.310438, width=0.0937993, height=0.104513, viewOffsetX=0.0122451, 
    viewOffsetY=-0.0149354)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.173901, 
    farPlane=0.277738, width=0.102929, height=0.114685, cameraPosition=(
    0.0353089, -0.201368, 0.0253067), cameraUpVector=(0.797558, 0.339329, 
    0.498756), cameraTarget=(0.02564, 0.065788, 0.037871), 
    viewOffsetX=0.0134369, viewOffsetY=-0.016389)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.141566, 
    farPlane=0.299831, width=0.0837902, height=0.0933605, cameraPosition=(
    0.0244604, -0.14663, -0.139202), cameraUpVector=(0.845224, -0.101749, 
    0.524636), cameraTarget=(0.0295711, 0.0345147, 0.0577356), 
    viewOffsetX=0.0109384, viewOffsetY=-0.0133416)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.15695, 
    farPlane=0.28878, width=0.0928954, height=0.103506, cameraPosition=(
    0.038539, -0.185138, -0.0739463), cameraUpVector=(0.942024, 0.289385, 
    0.169845), cameraTarget=(0.0382032, 0.055568, 0.0430337), 
    viewOffsetX=0.012127, viewOffsetY=-0.0147914)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.158141, 
    farPlane=0.287061, width=0.0936009, height=0.104292, cameraPosition=(
    0.0726773, -0.190389, -0.0352816), cameraUpVector=(0.881232, 0.464211, 
    0.0890983), cameraTarget=(0.0324749, 0.0644257, 0.0359726), 
    viewOffsetX=0.0122191, viewOffsetY=-0.0149037)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.180205, 
    farPlane=0.264998, width=0.00260421, height=0.00290166, 
    viewOffsetX=0.014604, viewOffsetY=-0.036969)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-8.odb')
#: Model: C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-8.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-8.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.245931, 
    farPlane=0.404996, width=0.0844162, height=0.094058, 
    viewOffsetX=-0.0118523, viewOffsetY=-0.00806557)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263347, 
    farPlane=0.488529, width=0.0884899, height=0.098597, 
    viewOffsetX=-0.00596762, viewOffsetY=0.00414552)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.326197, 
    farPlane=0.485168, width=0.0756156, height=0.0842522, 
    viewOffsetX=-0.017332, viewOffsetY=-0.00374801)
#: 
#: ODB: Job-6.odb
#:    Number of nodes: 164902
#:    Number of elements: 128467
#:    Element types: C3D8R 
#: 
#: ODB: Job-6.odb
#:    Number of nodes: 164902
#:    Number of elements: 128467
#:    Element types: C3D8R 
#: 
#: Node: FINAL_PART-1.192
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   8.21376e-05,  1.89891e-06,  2.51172e-03,      -      
#: Deformed coordinates (scaled):     8.21376e-05,  1.89891e-06,  2.51172e-03,      -      
#: Displacement (unscaled):          -1.92797e-05,  1.89891e-06,  1.17240e-05,  2.26443e-05
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.10022e-02,  6.58460e-03,  5.08202e-02,      -      
#: Deformed coordinates (scaled):     1.10022e-02,  6.58460e-03,  5.08202e-02,      -      
#: Displacement (unscaled):          -3.89978e-02,  6.58460e-03,  4.83202e-02,  6.24422e-02
#: 
#: Node: FINAL_PART-1.325
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  4.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   9.07220e-03,  6.93801e-03,  5.12076e-02,      -      
#: Deformed coordinates (scaled):     9.07220e-03,  6.93801e-03,  5.12076e-02,      -      
#: Displacement (unscaled):          -4.09278e-02,  6.93801e-03,  4.67076e-02,  6.24885e-02
#: 
#: Nodes for angle: FINAL_PART-1.192, FINAL_PART-1.315, FINAL_PART-1.325
#: Angle in base coords:  9.00000e+01 degrees.
#: Angle in deformed coords (unscaled):  8.99795e+01 degrees.
#: Angle in deformed coords (scaled):  8.99795e+01 degrees.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330029, 
    farPlane=0.481336, width=0.0609622, height=0.0679252, 
    viewOffsetX=-0.0309662, viewOffsetY=-0.0190147)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=21)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.304299, 
    farPlane=0.449606, width=0.0472893, height=0.0526906, 
    viewOffsetX=-0.0119197, viewOffsetY=-0.0181329)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.319905, 
    farPlane=0.487056, width=0.0934919, height=0.10417, viewOffsetX=-0.016882, 
    viewOffsetY=-0.0234573)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=14)
#: 
#: Node: FINAL_PART-1.192
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   8.73171e-05,  9.83345e-07,  2.50845e-03,      -      
#: Deformed coordinates (scaled):     8.73171e-05,  9.83345e-07,  2.50845e-03,      -      
#: Displacement (unscaled):          -1.41002e-05,  9.83345e-07,  8.45374e-06,  1.64696e-05
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   2.22332e-02,  4.69162e-03,  4.70444e-02,      -      
#: Deformed coordinates (scaled):     2.22332e-02,  4.69162e-03,  4.70444e-02,      -      
#: Displacement (unscaled):          -2.77668e-02,  4.69162e-03,  4.45444e-02,  5.26993e-02
#: 
#: Node: FINAL_PART-1.325
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  4.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   2.04484e-02,  5.00575e-03,  4.78906e-02,      -      
#: Deformed coordinates (scaled):     2.04484e-02,  5.00575e-03,  4.78906e-02,      -      
#: Displacement (unscaled):          -2.95516e-02,  5.00575e-03,  4.33906e-02,  5.27361e-02
#: 
#: Nodes for angle: FINAL_PART-1.192, FINAL_PART-1.315, FINAL_PART-1.325
#: Angle in base coords:  9.00000e+01 degrees.
#: Angle in deformed coords (unscaled):  8.97901e+01 degrees.
#: Angle in deformed coords (scaled):  8.97901e+01 degrees.
#: Invalid selection: Entity already selected, selection must be unique
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.30155, 
    farPlane=0.479401, width=0.0691629, height=0.0770625, 
    viewOffsetX=-0.0177651, viewOffsetY=-0.0198811)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344619, 
    farPlane=0.486218, width=0.0790412, height=0.0880691, cameraPosition=(
    0.396359, -0.0614447, 0.171149), cameraUpVector=(-0.0533402, 0.992445, 
    -0.110485), cameraTarget=(0.070415, 0.0290442, 0.00713047), 
    viewOffsetX=-0.0203024, viewOffsetY=-0.0227206)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.36243, 
    farPlane=0.468407, width=0.00332957, height=0.00370986, 
    viewOffsetX=-0.0203241, viewOffsetY=-0.0379979)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=ALL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359403, 
    farPlane=0.471434, width=0.0167407, height=0.0186528, 
    viewOffsetX=-0.0545851, viewOffsetY=-0.0287616)
#: Job Job-7: Abaqus/Standard completed successfully.
#: Job Job-7 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341991, 
    farPlane=0.488847, width=0.0812827, height=0.0905666, 
    viewOffsetX=-0.0357898, viewOffsetY=-0.0238495)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#: Job Job-8: Abaqus/Standard completed successfully.
#: Job Job-8 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.340543, 
    farPlane=0.468832, width=0.0349466, height=0.0389382, 
    viewOffsetX=-0.0162402, viewOffsetY=-0.0333112)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336194, 
    farPlane=0.48416, width=0.0345003, height=0.0384408, cameraPosition=(
    0.413305, -0.129309, 0.0243196), cameraUpVector=(0.0790173, 0.996872, 
    -0.00163353), cameraTarget=(0.0711038, 0.0234732, -0.00544517), 
    viewOffsetX=-0.0160327, viewOffsetY=-0.0328857)
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.328
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.135237
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.77664e-02,  7.84451e-03,  4.09017e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.77664e-02,  7.84451e-03,  4.09017e-03,      -      
#: Deformed coordinates (scaled):     4.77664e-02,  7.84451e-03,  4.09017e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49502
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Deformed coordinates (scaled):     4.87429e-02,  7.44040e-03,  4.08480e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.132627
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.17043e-02,  2.02938e-02,  3.65571e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.17043e-02,  2.02938e-02,  3.65571e-03,      -      
#: Deformed coordinates (scaled):     1.17043e-02,  2.02938e-02,  3.65571e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.49504
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.89105e-02,  6.44835e-03,  4.08682e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   4.89105e-02,  6.44835e-03,  4.08682e-03,      -      
#: Deformed coordinates (scaled):     4.89105e-02,  6.44835e-03,  4.08682e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.328
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.343871, 
    farPlane=0.476484, width=0.00373785, height=0.00416478, 
    viewOffsetX=-0.00791275, viewOffsetY=-0.0271889)
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.328
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344653, 
    farPlane=0.475702, width=0.000925632, height=0.00103136, 
    viewOffsetX=-0.0103912, viewOffsetY=-0.0398362)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'), )), 
    ), nodePick=(('FINAL_PART-1', 1, ('[#0:5 #4000000 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#: 
#: Node: FINAL_PART-1.4567
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.68730e-04,  9.90262e-04,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   2.68730e-04,  9.90262e-04,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     2.68730e-04,  9.90262e-04,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.187
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Deformed coordinates (scaled):     1.01417e-04,  0.00000e+00,  2.25000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341539, 
    farPlane=0.478815, width=0.0126028, height=0.0140423, 
    viewOffsetX=-0.00932827, viewOffsetY=-0.0379604)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'), )), 
    ), nodePick=(('FINAL_PART-1', 3, ('[#0:5 #4000000 #0:3 #4000000 #80 ]', )), 
    ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344601, 
    farPlane=0.475753, width=0.000961741, height=0.00107159, 
    viewOffsetX=-0.00838481, viewOffsetY=-0.0267658)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'), )), 
    ), nodePick=(('FINAL_PART-1', 3, ('[#0:5 #4000000 #0:3 #4000000 #80 ]', )), 
    ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#: 
#: Node: FINAL_PART-1.315
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.50000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
#: 
#: Node: FINAL_PART-1.328
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Deformed coordinates (scaled):     5.00000e-02,  0.00000e+00,  2.00000e-03,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344243, 
    farPlane=0.476112, width=0.00262968, height=0.00293004, 
    viewOffsetX=-0.00805508, viewOffsetY=-0.0272426)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222679, 
    farPlane=0.371125, width=0.0599207, height=0.0667647, 
    viewOffsetX=-0.00515866, viewOffsetY=-0.0109105)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244976, 
    farPlane=0.361611, width=0.0659206, height=0.0734499, cameraPosition=(
    0.314166, 0.0646548, 0.145445), cameraUpVector=(-0.327416, 0.935077, 
    -0.135752), cameraTarget=(0.0527204, 0.0585412, 0.00487558), 
    viewOffsetX=-0.00567519, viewOffsetY=-0.012003)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243592, 
    farPlane=0.362995, width=0.0616152, height=0.0686528, 
    viewOffsetX=-0.00504712, viewOffsetY=-0.0200137)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251422, 
    farPlane=0.398215, width=0.0635957, height=0.0708595, cameraPosition=(
    0.089776, -0.267435, -0.00789864), cameraUpVector=(0.918163, 0.391868, 
    0.0584408), cameraTarget=(0.0705744, 0.0286934, 0.00158583), 
    viewOffsetX=-0.00520935, viewOffsetY=-0.020657)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.265037, 
    farPlane=0.384598, width=0.00724723, height=0.00807499, 
    viewOffsetX=-0.00519851, viewOffsetY=-0.0672731)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.266004, 
    farPlane=0.385033, width=0.00727367, height=0.00810446, cameraPosition=(
    0.0875305, -0.267355, 0.0305171), cameraUpVector=(0.921608, 0.387947, 
    -0.0116504), cameraTarget=(0.0703464, 0.027737, 0.00265302), 
    viewOffsetX=-0.00521748, viewOffsetY=-0.0675186)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262307, 
    farPlane=0.388731, width=0.0208855, height=0.023271, 
    viewOffsetX=0.00215683, viewOffsetY=-0.0623349)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.266441, 
    farPlane=0.385141, width=0.0212147, height=0.0236378, cameraPosition=(
    0.0763241, -0.253533, 0.104576), cameraUpVector=(0.932265, 0.35844, 
    -0.049023), cameraTarget=(0.0692074, 0.0283833, 0.0117124), 
    viewOffsetX=0.00219083, viewOffsetY=-0.0633174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.271414, 
    farPlane=0.380168, width=0.000764845, height=0.000852204, 
    viewOffsetX=0.012803, viewOffsetY=-0.0696853)
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'), )), ), 
    nodePick=(('FINAL_PART-1', 3, ('[#0:5 #4000000 #0:3 #4000000 #80 ]', )), ), 
    )
odb = session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'), )), 
    ), nodePick=(('FINAL_PART-1', 3, ('[#0:5 #4000000 #0:3 #4000000 #80 ]', )), 
    ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xy1 = session.xyDataObjects['U:U1 PI: FINAL_PART-1 N: 315']
xy2 = xy1+1.01417e-4
xy2.setValues(sourceDescription='"U:U1 PI: FINAL_PART-1 N: 315" + 1.01417e-4')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'x_A')
del session.xyDataObjects['_U:U3 PI: FINAL_PART-1 N: 315']
del session.xyDataObjects['x_A']
del session.xyDataObjects['_U:U3 PI: FINAL_PART-1 N: 328']
xy1 = session.xyDataObjects['U:U1 PI: FINAL_PART-1 N: 315']
xy2 = xy1+5e-2
xy2.setValues(sourceDescription='"U:U1 PI: FINAL_PART-1 N: 315"+5e-2')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'x_A')
xy1 = session.xyDataObjects['U:U2 PI: FINAL_PART-1 N: 315']
xy2 = xy1+0
xy2.setValues(sourceDescription='"U:U2 PI: FINAL_PART-1 N: 315"+0')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'y_A')
xy1 = session.xyDataObjects['U:U3 PI: FINAL_PART-1 N: 315']
xy2 = xy1+2.5e-3
xy2.setValues(sourceDescription='"U:U3 PI: FINAL_PART-1 N: 315"+2.5e-3')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'z_A')
xy1 = session.xyDataObjects['U:U1 PI: FINAL_PART-1 N: 187']
xy2 = xy1+1.01417e-4
xy2.setValues(sourceDescription='"U:U1 PI: FINAL_PART-1 N: 187"+1.01417e-4')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'x_B')
xy1 = session.xyDataObjects['U:U2 PI: FINAL_PART-1 N: 187']
xy2 = xy1+0
xy2.setValues(sourceDescription='"U:U2 PI: FINAL_PART-1 N: 187"+0')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'y_B')
xy1 = session.xyDataObjects['U:U3 PI: FINAL_PART-1 N: 187']
xy2 = xy1+2.25e-3
xy2.setValues(sourceDescription='"U:U3 PI: FINAL_PART-1 N: 187"+2.25e-3')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'z_B')
xy1 = session.xyDataObjects['U:U1 PI: FINAL_PART-1 N: 328']
xy2 = xy1+5e-2
xy2.setValues(sourceDescription='"U:U1 PI: FINAL_PART-1 N: 328"+5e-2')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'x_C')
xy1 = session.xyDataObjects['U:U2 PI: FINAL_PART-1 N: 328']
xy2 = xy1+0
xy2.setValues(sourceDescription='"U:U2 PI: FINAL_PART-1 N: 328"+0')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'y_C')
xy1 = session.xyDataObjects['U:U3 PI: FINAL_PART-1 N: 328']
xy2 = xy1+2e-3
xy2.setValues(sourceDescription='"U:U3 PI: FINAL_PART-1 N: 328"+2e-3')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'z_C')
xy1 = session.xyDataObjects['x_A']
xy2 = session.xyDataObjects['x_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"x_A" - "x_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BA_x')
xy1 = session.xyDataObjects['y_A']
xy2 = session.xyDataObjects['y_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"y_A" - "y_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BA_y')
xy1 = session.xyDataObjects['z_A']
xy2 = session.xyDataObjects['z_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"z_A" - "z_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BA_z')
xy1 = session.xyDataObjects['x_C']
xy2 = session.xyDataObjects['x_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"x_C" - "x_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BC_x')
xy1 = session.xyDataObjects['y_C']
xy2 = session.xyDataObjects['y_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"y_C" - "y_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BC_y')
xy1 = session.xyDataObjects['z_C']
xy2 = session.xyDataObjects['z_B']
xy3 = xy1-xy2
xy3.setValues(sourceDescription='"z_C" - "z_B"')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'BC_z')
xy1 = session.xyDataObjects['BA_x']
xy2 = session.xyDataObjects['BC_x']
xy3 = session.xyDataObjects['BA_y']
xy4 = session.xyDataObjects['BC_y']
xy5 = session.xyDataObjects['BA_z']
xy6 = session.xyDataObjects['BC_z']
xy7 =(xy1*xy2)+(xy3*xy4)+(xy5*xy6)
xy7.setValues(
    sourceDescription='("BA_x" * "BC_x") + ("BA_y" * "BC_y") + ("BA_z" * "BC_z")')
tmpName = xy7.name
session.xyDataObjects.changeKey(tmpName, 'DotProduct')
xy1 = session.xyDataObjects['BA_x']
xy2 = session.xyDataObjects['BA_y']
xy3 = session.xyDataObjects['BA_z']
xy4 = sqrt((xy1*xy1)+(xy2*xy2)+(xy3*xy3))
xy4.setValues(
    sourceDescription='sqrt(("BA_x" * "BA_x") + ("BA_y" * "BA_y") + ("BA_z" * "BA_z"))')
tmpName = xy4.name
session.xyDataObjects.changeKey(tmpName, 'Mag_BA')
xy1 = session.xyDataObjects['BC_x']
xy2 = session.xyDataObjects['BC_y']
xy3 = session.xyDataObjects['BC_z']
xy4 = sqrt((xy1*xy1)+(xy2*xy2)+(xy3*xy3))
xy4.setValues(
    sourceDescription='sqrt(("BC_x" * "BC_x") + ("BC_y" * "BC_y") + ("BC_z" * "BC_z"))')
tmpName = xy4.name
session.xyDataObjects.changeKey(tmpName, 'Mag_BC')
xy1 = session.xyDataObjects['DotProduct']
xy2 = session.xyDataObjects['Mag_BA']
xy3 = session.xyDataObjects['Mag_BC']
xy4 = acos(xy1/(xy2*xy3))
xy4.setValues(sourceDescription='acos("DotProduct" / ("Mag_BA" * "Mag_BC"))')
tmpName = xy4.name
session.xyDataObjects.changeKey(tmpName, 'Angle_Radians')
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xy2.setValues(sourceDescription='"Angle_Radians" * 180.0 / 3.14159265')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'Angle_Degrees')
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['Angle_Radians']
xy2 = xy1*180.0/3.14159265
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames='Angle_Degrees,Angle_Radians', trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=49)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=49)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-6.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-8.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-8.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=41)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/st195764/Desktop/Spiral-Simulation/Abaqus_files/Spiral_complete_CAE/Job-7.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=48 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=47 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=46 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=45 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=44 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=43 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=49)
a = mdb.models['Spiral_Model_8'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae".
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae".
mdb.save()
#: The model database has been saved to "C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\Spiral_complete_CAE\Spiral_Final_CAE.cae".
