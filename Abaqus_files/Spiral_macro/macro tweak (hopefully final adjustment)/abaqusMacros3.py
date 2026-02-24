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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.3431, 
        farPlane=0.484615, width=0.00177893, height=0.000740613, 
        viewOffsetX=-0.0533901, viewOffsetY=-0.0137111)
    del mdb.models['Model-1'].boundaryConditions['BC-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.342592, 
        farPlane=0.485122, width=0.00793901, height=0.00330521, 
        viewOffsetX=-0.0514427, viewOffsetY=-0.0133254)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:7 #1000400 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
        region=region, localCsys=None)


