# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-15.00.46 RELr427 198590
# Run by st195764 on Fri Feb  6 16:20:08 2026
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
openMdb('Spiral_inLAB.cae')
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#* MdbError: The database 
#* C:\Users\st195764\Desktop\Spiral-Simulation\Abaqus_files\LAB_files\Spiral_inLAB.cae 
#* was created with Abaqus/CAE Learning Edition.
#* 
#* Files created with Abaqus/CAE Learning Edition cannot be used with the 
#* commercial release of Abaqus/CAE
