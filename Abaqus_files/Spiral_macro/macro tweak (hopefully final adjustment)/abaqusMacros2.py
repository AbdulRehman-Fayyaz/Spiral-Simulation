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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.323816, 
        farPlane=0.506331, width=0.0751277, height=0.0312775, 
        viewOffsetX=0.0241669, viewOffsetY=0.0151802)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Final_Part-1'].vertices
    a.DatumPlaneByTwoPoint(point1=v1[39], point2=v1[237])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.328344, 
        farPlane=0.501803, width=0.0320348, height=0.0133369, 
        viewOffsetX=0.0282365, viewOffsetY=0.0166329)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeIndependent(instances=(a1.instances['Final_Part-1'], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.319146, 
        farPlane=0.511001, width=0.12347, height=0.0514036, 
        viewOffsetX=0.0270094, viewOffsetY=0.0120803)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Final_Part-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#ffffffff #1 ]', ), )
    a.deleteMesh(regions=pickedRegions)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.329029, 
        farPlane=0.501118, width=0.0240454, height=0.0100107, 
        viewOffsetX=0.0303119, viewOffsetY=0.0165823)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    pickedFaces = f1.getSequenceFromMask(mask=('[#ffffffff:8 #3ff ]', ), )
    d1 = a.datums
    a.PartitionFaceByDatumPlane(datumPlane=d1[14], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.329022, 
        farPlane=0.501125, width=0.021333, height=0.00888147, 
        viewOffsetX=0.0224536, viewOffsetY=0.0212168)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330398, 
        farPlane=0.499749, width=0.00712008, height=0.00297207, 
        viewOffsetX=0.0211409, viewOffsetY=0.0212749)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Section']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    p = mdb.models['Model-1'].parts['Divider_Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Final_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.322373, 
        farPlane=0.507773, width=0.0898123, height=0.0374896, 
        viewOffsetX=0.0167973, viewOffsetY=0.0164108)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Section']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327585, 
        farPlane=0.502561, width=0.036076, height=0.0150589, 
        viewOffsetX=0.0208015, viewOffsetY=0.0201581)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeDependent(instances=(a1.instances['Final_Part-1'], ))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeIndependent(instances=(a1.instances['Final_Part-1'], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330253, 
        farPlane=0.499893, width=0.00973709, height=0.00406447, 
        viewOffsetX=0.0219021, viewOffsetY=0.0212407)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Part']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330765, 
        farPlane=0.499382, width=0.00378388, height=0.00157947, 
        viewOffsetX=0.0271996, viewOffsetY=0.0157739)
    p = mdb.models['Model-1'].parts['Final_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330238, 
        farPlane=0.499909, width=0.00876319, height=0.00365794, 
        viewOffsetX=0.0258496, viewOffsetY=0.0170133)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeDependent(instances=(a1.instances['Final_Part-1'], ))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.makeIndependent(instances=(a1.instances['Final_Part-1'], ))
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Part']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.324363, 
        farPlane=0.505784, width=0.0782167, height=0.0326493, 
        viewOffsetX=0.0179542, viewOffsetY=0.019968)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336907, 
        farPlane=0.465783, width=0.0812414, height=0.0339119, cameraPosition=(
        -0.0367083, 0.292259, 0.32006), cameraUpVector=(-0.248662, 0.496712, 
        -0.831531), cameraTarget=(0.0410692, 0.0548434, -0.0114073), 
        viewOffsetX=0.0186485, viewOffsetY=0.0207402)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336628, 
        farPlane=0.466062, width=0.0811741, height=0.0338838, 
        viewOffsetX=0.018633, viewOffsetY=0.020723)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327818, 
        farPlane=0.445289, width=0.0790496, height=0.032997, cameraPosition=(
        -0.179722, 0.110459, 0.313035), cameraUpVector=(-0.294435, 0.624447, 
        -0.723446), cameraTarget=(0.0572138, 0.0543073, -0.0231117), 
        viewOffsetX=0.0181453, viewOffsetY=0.0201806)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.328801, 
        farPlane=0.444306, width=0.0662734, height=0.0276639, 
        viewOffsetX=0.05038, viewOffsetY=0.0119897)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Final_Part-1'].edges
    pickedEdges = e1.getSequenceFromMask(mask=(
        '[#fff1ffff #80fffc5f #fffffa01 #f17fffc7 #ff84301f #7ffc7fff #e10407fc', 
        ' #ffe3ffff #30f0fe2f #7f0ffffc #3ffc7ff0 #c3f87860 #100cc7 #24906', 
        ' #0:2 #20 ]', ), )
    a.seedEdgeBySize(edges=pickedEdges, size=0.0001, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.32314, 
        farPlane=0.449967, width=0.140513, height=0.0586529, 
        viewOffsetX=0.0518814, viewOffsetY=0.00613539)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344981, 
        farPlane=0.525596, width=0.15001, height=0.0626173, cameraPosition=(
        0.303009, 0.252622, 0.301512), cameraUpVector=(-0.446906, 0.739715, 
        -0.503087), cameraTarget=(0.016326, 0.0934028, 0.0470553), 
        viewOffsetX=0.0553881, viewOffsetY=0.00655008)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.353079, 
        farPlane=0.517498, width=0.0485151, height=0.0202512, 
        viewOffsetX=0.0445683, viewOffsetY=-0.0396819)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Final_Part-1'].edges
    pickedEdges = e1.getSequenceFromMask(mask=(
        '[#94f8f3f #ff9cf3e4 #3cfe6fff #cf90253e #fc7fffe6 #834fe83c #1ffffbbf', 
        ' #89f1e7e #ff0fd9f0 #c0ff9f03 #c6d7d04f #3e87c7df #ffeff338 #fffdb6f9', 
        ' #ffffffff:2 #3ffffdf ]', ), )
    a.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327859, 
        farPlane=0.542718, width=0.346704, height=0.144722, 
        viewOffsetX=0.138196, viewOffsetY=-0.00521678)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['Final_Part-1'], )
    a.generateMesh(regions=partInstances)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347391, 
        farPlane=0.523186, width=0.120646, height=0.05036, 
        viewOffsetX=0.0594795, viewOffsetY=-0.0365304)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347438, 
        farPlane=0.484786, width=0.120662, height=0.0503669, cameraPosition=(
        -0.336383, 0.0248281, 0.186707), cameraUpVector=(-0.0720638, 0.77237, 
        -0.631072), cameraTarget=(-0.00448744, 0.0313361, -0.0624699), 
        viewOffsetX=0.0594875, viewOffsetY=-0.0365353)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331078, 
        farPlane=0.501147, width=0.317115, height=0.13237, 
        viewOffsetX=0.155806, viewOffsetY=-0.0384891)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Final_Part-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#ffffffff #1 ]', ), )
    pickedRegions =(cells1, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.355294, 
        farPlane=0.476931, width=0.032414, height=0.0135303, 
        viewOffsetX=0.0607108, viewOffsetY=-0.0196731)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
        bcs=ON, predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.354956, 
        farPlane=0.477268, width=0.0406768, height=0.0169348, 
        viewOffsetX=0.0415099, viewOffsetY=-0.0518593)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:4 #400 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(region=region)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.35341, 
        farPlane=0.478815, width=0.0587061, height=0.0244408, 
        viewOffsetX=0.0466451, viewOffsetY=-0.0525767)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.345378, 
        farPlane=0.495632, width=0.0573718, height=0.0238853, cameraPosition=(
        -0.357762, 0.0205858, 0.134341), cameraUpVector=(0.133914, 0.957963, 
        -0.253719), cameraTarget=(0.0097714, 0.0638524, -0.0536305), 
        viewOffsetX=0.045585, viewOffsetY=-0.0513818)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.343615, 
        farPlane=0.497394, width=0.073407, height=0.0305612, 
        viewOffsetX=0.0532985, viewOffsetY=-0.0517064)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341194, 
        farPlane=0.503193, width=0.0728898, height=0.0303458, cameraPosition=(
        -0.365278, -0.0213346, 0.100181), cameraUpVector=(0.0172053, 0.888124, 
        -0.459282), cameraTarget=(0.00972476, 0.0410058, -0.0664694), 
        viewOffsetX=0.052923, viewOffsetY=-0.0513421)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337689, 
        farPlane=0.506698, width=0.105429, height=0.0438928, 
        viewOffsetX=0.0651579, viewOffsetY=-0.0384077)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.345119, 
        farPlane=0.493157, width=0.107749, height=0.0448586, cameraPosition=(
        -0.342798, 0.0686791, 0.181926), cameraUpVector=(0.0267611, 0.745931, 
        -0.665486), cameraTarget=(-0.00519724, 0.0294738, -0.0563476), 
        viewOffsetX=0.0665915, viewOffsetY=-0.0392528)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.374876, 
        farPlane=0.505624, width=0.11704, height=0.0487265, cameraPosition=(
        -0.173844, -0.105719, 0.354371), cameraUpVector=(-0.164262, 0.986215, 
        0.0199292), cameraTarget=(-0.0351747, 0.0647848, 0.00225574), 
        viewOffsetX=0.0723333, viewOffsetY=-0.0426373)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.380669, 
        farPlane=0.499832, width=0.0415115, height=0.0172823, 
        viewOffsetX=0.0318377, viewOffsetY=-0.0602962)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376085, 
        farPlane=0.516008, width=0.0410116, height=0.0170741, cameraPosition=(
        -0.226455, -0.118542, 0.316777), cameraUpVector=(-0.137808, 0.988963, 
        0.0544181), cameraTarget=(-0.0370601, 0.0653763, -0.00351889), 
        viewOffsetX=0.0314543, viewOffsetY=-0.05957)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.374779, 
        farPlane=0.517314, width=0.0525602, height=0.0218821, 
        viewOffsetX=0.0352824, viewOffsetY=-0.0593494)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Final_Part-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0:4 #400 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(region=region)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370803, 
        farPlane=0.52129, width=0.105689, height=0.0440011, 
        viewOffsetX=0.0619251, viewOffsetY=-0.0497974)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370252, 
        farPlane=0.52184, width=0.105532, height=0.0439358, cameraPosition=(
        -0.212248, -0.0968033, 0.33766), cameraUpVector=(0.150065, 0.965821, 
        0.211353), cameraTarget=(-0.022853, 0.087115, 0.0173646), 
        viewOffsetX=0.0618332, viewOffsetY=-0.0497236)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.363353, 
        farPlane=0.528738, width=0.192282, height=0.0800519, 
        viewOffsetX=0.0736334, viewOffsetY=-0.0598827)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.362394, 
        farPlane=0.529698, width=0.191775, height=0.0798405, cameraPosition=(
        -0.204285, -0.0902943, 0.346106), cameraUpVector=(0.245753, 0.936279, 
        0.250971), cameraTarget=(-0.0148897, 0.093624, 0.025811), 
        viewOffsetX=0.0734389, viewOffsetY=-0.0597245)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.37072, 
        farPlane=0.521372, width=0.0945171, height=0.0393498, 
        viewOffsetX=0.0581666, viewOffsetY=-0.068469)
    del mdb.models['Model-1'].boundaryConditions['BC-2']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.368233, 
        farPlane=0.523858, width=0.120248, height=0.0500621, 
        viewOffsetX=0.0597215, viewOffsetY=-0.063292)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.322373, 
        farPlane=0.507773, width=0.0900488, height=0.0374896, 
        viewOffsetX=-0.00297003, viewOffsetY=-0.0220272)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Final_Part-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#0:7 #10000 ]', ), )
    region = regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].SurfaceTraction(name='Load-1', createStepName='Step-1', 
        region=region, magnitude=7000.0, directionVector=((0.0, 0.0, 0.0), (
        0.0, 0.0, 1.0)), distributionType=UNIFORM, field='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.323499, 
        farPlane=0.506648, width=0.088481, height=0.0368368, 
        viewOffsetX=-0.00108178, viewOffsetY=-0.0237141)
    mdb.models['Model-1'].loads['Load-1'].setValues(traction=GENERAL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321426, 
        farPlane=0.508721, width=0.112602, height=0.0468791, 
        viewOffsetX=-0.000714559, viewOffsetY=-0.0224857)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332401, 
        farPlane=0.542699, width=0.116447, height=0.0484797, cameraPosition=(
        0.436056, -0.128604, -0.0484742), cameraUpVector=(0.0602895, 0.932627, 
        -0.35577), cameraTarget=(0.0699314, 0.0612638, -0.00168922), 
        viewOffsetX=-0.000738957, viewOffsetY=-0.0232535)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332043, 
        farPlane=0.543057, width=0.116322, height=0.0484275, cameraPosition=(
        0.439011, -0.126487, -0.0339366), cameraUpVector=(0.144959, 0.984895, 
        0.0947035), cameraTarget=(0.0728868, 0.0633805, 0.0128484), 
        viewOffsetX=-0.000738161, viewOffsetY=-0.0232284)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321554, 
        farPlane=0.553545, width=0.245256, height=0.102106, 
        viewOffsetX=0.00073511, viewOffsetY=-0.0262719)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327588, 
        farPlane=0.535745, width=0.249859, height=0.104022, cameraPosition=(
        0.468294, -0.00963863, -0.0465957), cameraUpVector=(-0.130752, 
        0.988568, 0.0750777), cameraTarget=(0.0655859, 0.0726676, 0.011173), 
        viewOffsetX=0.000748905, viewOffsetY=-0.0267649)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337969, 
        farPlane=0.508122, width=0.257777, height=0.107319, cameraPosition=(
        0.396864, 0.10291, -0.229377), cameraUpVector=(-0.258713, 0.914351, 
        0.311497), cameraTarget=(0.056847, 0.0773859, 0.00731298), 
        viewOffsetX=0.000772637, viewOffsetY=-0.027613)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337091, 
        farPlane=0.506068, width=0.257108, height=0.10704, cameraPosition=(
        0.3643, 0.121651, -0.266634), cameraUpVector=(-0.330419, 0.90244, 
        0.276451), cameraTarget=(0.0529053, 0.0779524, 0.00430738), 
        viewOffsetX=0.000770631, viewOffsetY=-0.0275413)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34964, 
        farPlane=0.49352, width=0.126918, height=0.0528392, 
        viewOffsetX=0.0203926, viewOffsetY=-0.0407673)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Final_Part-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#0:5 #10000000 ]', ), )
    region = regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].SurfaceTraction(name='Load-2', createStepName='Step-1', 
        region=region, magnitude=7000.0, directionVector=((0.0, 0.0, 0.0), (
        0.0, 0.0, -1.0)), distributionType=UNIFORM, field='', localCsys=None)
    mdb.models['Model-1'].loads['Load-2'].setValues(traction=GENERAL)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF, datacheckJob=True)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359252, 
        farPlane=0.483908, width=0.013214, height=0.00574387, 
        viewOffsetX=0.00811507, viewOffsetY=-0.0347559)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])


