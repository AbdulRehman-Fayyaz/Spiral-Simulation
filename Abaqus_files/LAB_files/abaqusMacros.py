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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.160747, 
        farPlane=0.216376, width=0.286868, height=0.129963, cameraPosition=(
        0.0557826, 0.00214163, 0.188562), cameraTarget=(0.0557826, 0.00214163, 
        0))
    s.Line(point1=(0.0, 0.0), point2=(0.05, 0.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(0.05, 0.0), point2=(0.04125, 0.035))
    s.Line(point1=(0.04125, 0.035), point2=(0.0124999999767169, 0.035))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.Line(point1=(0.0124999999767169, 0.035), point2=(0.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.162202, 
        farPlane=0.214922, width=0.271867, height=0.123167, cameraPosition=(
        0.0671746, 0.0143607, 0.188562), cameraTarget=(0.0671746, 0.0143607, 
        0))
    s.AngularDimension(line1=g[5], line2=g[2], textPoint=(0.00710679590702057, 
        0.00731545034796), value=80.41)
    s.Spot(point=(0.00658647630526709, 0.0))
    s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
    s.Spot(point=(0.0, 0.0))
    s.undo()
    s.undo()
    s.Spot(point=(0.0, 0.0))
    s.CoincidentConstraint(entity1=v[4], entity2=v[0])
    s.undo()
    s.CoincidentConstraint(entity1=v[0], entity2=v[4])
    s.undo()
    s.undo()
    s.undo()
    s.FixedConstraint(entity=v[0])
    s.HorizontalConstraint(entity=g[2])
    s.HorizontalConstraint(entity=g[2])
    s.HorizontalConstraint(entity=g[2])
    s.AngularDimension(line1=g[5], line2=g[2], textPoint=(0.0106769427657127, 
        0.00892070028930902), value=80.41)
    s.AngularDimension(line1=g[3], line2=g[2], textPoint=(0.0426298156380653, 
        0.00535347405821085), value=80.41)
    s.AngularDimension(line1=g[4], line2=g[5], textPoint=(0.0140685886144638, 
        0.026578463613987), value=80.42)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.16527, 
        farPlane=0.211853, width=0.240222, height=0.10883, cameraPosition=(
        0.0689403, 0.0195657, 0.188562), cameraTarget=(0.0689403, 0.0195657, 
        0))
    s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.0212272182106972, 
        -0.0118754953145981), value=0.05)
    s.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(-0.00574450194835663, 
        0.0297309048473835), value=0.05)
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(0.0294291451573372, 
        0.0547893159091473), value=0.03751)
    s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(0.0538771897554398, 
        0.030046109110117), value=0.05)
    d[6].setValues(textPoint=(0.065, 0.02625))
    d[6].setValues(textPoint=(0.065, 0.02625))
    d[6].setValues(textPoint=(0.0675, 0.0275))
    s.delete(objectList=(d[6], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.16527, 
        farPlane=0.211853, width=0.240222, cameraPosition=(0.0742658, 
        0.0247888, 0.188562), cameraTarget=(0.0742658, 0.0247888, 0))
    s.EqualLengthConstraint(entity1=g[2], entity2=g[5])
    s.delete(objectList=(d[5], ))
    s.delete(objectList=(d[4], ))
    s.delete(objectList=(c[9], ))
    s.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(
        -0.000103548169136047, 0.0321172140538692), value=0.05)
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(0.0323886945843697, 
        0.0505564175546169), value=0.03751)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.160519, 
        farPlane=0.216604, width=0.28922, height=0.131028, cameraPosition=(
        0.112101, 0.0285825, 0.188562), cameraTarget=(0.112101, 0.0285825, 0))
    s.delete(objectList=(d[8], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.156695, 
        farPlane=0.220428, width=0.32866, height=0.148896, cameraPosition=(
        0.127876, 0.050591, 0.188562), cameraTarget=(0.127876, 0.050591, 0))
    s.Line(point1=(0.00832983277021789, 0.0493012564344988), point2=(0.0275, 
        0.08375))
    s.Line(point1=(0.0275, 0.08375), point2=(0.0475, 0.0726203242869508))
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(0.0475, 0.0726203242869508), point2=(0.0437507253380803, 
        0.0369871882348552))
    s.AngularDimension(line1=g[6], line2=g[4], textPoint=(0.0177116543054581, 
        0.0539331175386906), value=80.41)
    s.AngularDimension(line1=g[8], line2=g[4], textPoint=(0.0382124111056328, 
        0.0530706308782101), value=80.41)
    s.AngularDimension(line1=g[6], line2=g[7], textPoint=(0.028933122754097, 
        0.0731233507394791), value=80.42)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.163682, 
        farPlane=0.213442, width=0.256601, height=0.11625, cameraPosition=(
        0.107002, 0.0561057, 0.188562), cameraTarget=(0.107002, 0.0561057, 0))
    s.EqualLengthConstraint(entity1=g[6], entity2=g[4])
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(0.0343015640974045, 
        0.0306013226509094), value=0.03751)
    s.undo()
    s.undo()
    s.undo()
    s.dragEntity(entity=v[4], points=((0.0276180357087562, 0.0844444612923769), (
        0.0275, 0.085), (0.02875, 0.08), (0.02875, 0.0775), (0.03, 0.07625), (
        0.03, 0.0775), (0.02875, 0.0825), (0.02875, 0.0825)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.171328, 
        farPlane=0.205796, width=0.20116, height=0.0911337, cameraPosition=(
        0.0779751, 0.0699013, 0.188562), cameraTarget=(0.0779751, 0.0699013, 
        0))
    s.delete(objectList=(g[7], ))
    s.dragEntity(entity=v[5], points=((0.049509298845524, 0.0711063445091727), (
        0.05, 0.07125), (0.05, 0.075), (0.05, 0.0775), (0.05, 0.08), (0.05, 
        0.08125), (0.05, 0.0825)))
    s.Line(point1=(0.0270599292072777, 0.0834275883791007), point2=(
        0.0513926301292036, 0.0822649542414466))
    s.AngularDimension(line1=g[6], line2=g[9], textPoint=(0.0299634784460068, 
        0.0774897858500481), value=80.42)
    s.EqualLengthConstraint(entity1=g[6], entity2=g[4])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.161986, 
        farPlane=0.215138, width=0.274096, height=0.124177, cameraPosition=(
        0.109858, 0.0523896, 0.188562), cameraTarget=(0.109858, 0.0523896, 0))
    d[10].setValues(textPoint=(0.0425, 0.0475))
    d[9].setValues(textPoint=(0.01625, 0.05375))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.15235, 
        farPlane=0.224774, width=0.373477, height=0.1692, cameraPosition=(
        0.142168, 0.0431701, 0.188562), cameraTarget=(0.142168, 0.0431701, 0))
    d[9].setValues(textPoint=(0.01625, 0.05375))
    s.offset(distance=0.01, objectList=(g[2], g[3], g[4], g[5]), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.160174, 
        farPlane=0.21695, width=0.331354, height=0.150117, cameraPosition=(
        0.129813, 0.0479032, 0.188562), cameraTarget=(0.129813, 0.0479032, 0))
    s.DistanceDimension(entity1=g[12], entity2=g[3], textPoint=(0.0524678751826286, 
        0.022142693400383), value=0.01)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.152202, 
        farPlane=0.224922, width=0.375005, height=0.169892, cameraPosition=(
        0.188769, 0.101001, 0.188562), cameraTarget=(0.188769, 0.101001, 0))
    s.Line(point1=(0.0263728156847114, 0.0821756640105573), point2=(0.05125, 
        0.09625))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.174189, 
        farPlane=0.202935, width=0.148237, height=0.0671571, cameraPosition=(
        0.10848, 0.0903738, 0.188562), cameraTarget=(0.10848, 0.0903738, 0))
    s.Line(point1=(0.05125, 0.09625), point2=(0.05375, 0.0875))
    s.Line(point1=(0.05375, 0.0875), point2=(0.048432882778283, 
        0.0647286525396411))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.161768, 
        farPlane=0.215356, width=0.276344, height=0.125195, cameraPosition=(
        0.14859, 0.0893635, 0.188562), cameraTarget=(0.14859, 0.0893635, 0))
    s.AngularDimension(line1=g[14], line2=g[9], textPoint=(0.036002092063427, 
        0.0827461183071136), value=80.41)
    s.AngularDimension(line1=g[9], line2=g[16], textPoint=(0.0452558845281601, 
        0.0749502927064896), value=80.41)
    s.AngularDimension(line1=g[14], line2=g[15], textPoint=(0.0488848239183426, 
        0.0912671387195587), value=80.42)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.167557, 
        farPlane=0.209567, width=0.216638, height=0.0981457, cameraPosition=(
        0.0974049, 0.0840364, 0.188562), cameraTarget=(0.0974049, 0.0840364, 
        0))
    s.EqualLengthConstraint(entity1=g[14], entity2=g[9])
    s.EqualLengthConstraint(entity1=g[9], entity2=g[9], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.162841, 
        farPlane=0.214282, width=0.265274, height=0.12018, cameraPosition=(
        0.13991, 0.0981083, 0.188562), cameraTarget=(0.13991, 0.0981083, 0))
    s.Line(point1=(0.0472511408113617, 0.10102083074755), point2=(0.065, 0.1075))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.171883, 
        farPlane=0.205241, width=0.172024, height=0.0779338, cameraPosition=(
        0.11496, 0.0964684, 0.188562), cameraTarget=(0.11496, 0.0964684, 0))
    s.Line(point1=(0.065, 0.1075), point2=(0.07125, 0.10125))
    s.Line(point1=(0.07125, 0.10125), point2=(0.05858201235993, 0.083228072955139))
    s.Line(point1=(0.065, 0.1075), point2=(0.07625, 0.11))
    s.Line(point1=(0.07625, 0.11), point2=(0.07875, 0.1075))
    s.Line(point1=(0.07875, 0.1075), point2=(0.07125, 0.10125))
    s.AngularDimension(line1=g[17], line2=g[15], textPoint=(0.0533453375101089, 
        0.0993462577462196), value=80.41)
    s.AngularDimension(line1=g[15], line2=g[19], textPoint=(0.0584281235933304, 
        0.0902047455310822), value=80.41)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.157468, 
        farPlane=0.219655, width=0.320689, height=0.145285, cameraPosition=(
        0.162514, 0.0931074, 0.188562), cameraTarget=(0.162514, 0.0931074, 0))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.173764, 
        farPlane=0.20336, width=0.152622, height=0.069144, cameraPosition=(
        0.11225, 0.0974418, 0.188562), cameraTarget=(0.11225, 0.0974418, 0))
    s.AngularDimension(line1=g[17], line2=g[18], textPoint=(0.0607915185391903, 
        0.10269857943058), value=80.42)
    s.AngularDimension(line1=g[15], line2=g[19], textPoint=(0.0591881312429905, 
        0.092184990644455), value=80.41)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.172819, 
        farPlane=0.204304, width=0.162364, height=0.0735575, cameraPosition=(
        0.119118, 0.0955046, 0.188562), cameraTarget=(0.119118, 0.0955046, 0))
    s.AngularDimension(line1=g[18], line2=g[22], textPoint=(0.0690656453371048, 
        0.0983273684978485), value=80.41)
    s.AngularDimension(line1=g[20], line2=g[18], textPoint=(0.0678929537534714, 
        0.104079484939575), value=80.41)
    s.AngularDimension(line1=g[20], line2=g[21], textPoint=(0.0779141187667847, 
        0.104612082242966), value=80.42)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.162736, 
        farPlane=0.214388, width=0.266359, height=0.120671, cameraPosition=(
        0.147072, 0.0855392, 0.188562), cameraTarget=(0.147072, 0.0855392, 0))
    s.EqualLengthConstraint(entity1=g[17], entity2=g[15])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.171814, 
        farPlane=0.205309, width=0.172728, height=0.0782527, cameraPosition=(
        0.123348, 0.0979405, 0.188562), cameraTarget=(0.123348, 0.0979405, 0))
    s.EqualLengthConstraint(entity1=g[20], entity2=g[18])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.178311, 
        farPlane=0.198812, width=0.119647, height=0.054205, cameraPosition=(
        0.114574, 0.106533, 0.188562), cameraTarget=(0.114574, 0.106533, 0))
    s.Line(point1=(0.0824703142727197, 0.110258366178349), point2=(0.09625, 
        0.1075))
    s.Line(point1=(0.09625, 0.1075), point2=(0.0975, 0.10125))
    s.Line(point1=(0.0975, 0.10125), point2=(0.0812609010184524, 
        0.0984543806470771))
    s.AngularDimension(line1=g[21], line2=g[25], textPoint=(0.0843680649995804, 
        0.101155877113342), value=80.41)
    s.AngularDimension(line1=g[21], line2=g[23], textPoint=(0.0852322280406952, 
        0.106807574629784), value=80.41)
    s.AngularDimension(line1=g[23], line2=g[24], textPoint=(0.0940309762954712, 
        0.104766681790352), value=80.42)
    s.EqualLengthConstraint(entity1=g[23], entity2=g[21])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.165366, 
        farPlane=0.211757, width=0.23923, height=0.108381, cameraPosition=(
        0.105503, 0.0732696, 0.188562), cameraTarget=(0.105503, 0.0732696, 0))
    s.offset(distance=0.005, objectList=(g[4], g[6], g[8], g[9]), side=LEFT)
    s.offset(distance=0.005, objectList=(g[9], g[14], g[15], g[16]), side=RIGHT)
    s.offset(distance=0.003, objectList=(g[15], g[17], g[18], g[19]), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.170452, 
        farPlane=0.206672, width=0.186779, height=0.0846182, cameraPosition=(
        0.107889, 0.08998, 0.188562), cameraTarget=(0.107889, 0.08998, 0))
    s.offset(distance=0.003, objectList=(g[18], g[20], g[21], g[22]), side=RIGHT)
    s.offset(distance=0.002, objectList=(g[21], g[23], g[24], g[25]), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.14256, 
        farPlane=0.234563, width=0.474441, height=0.214941, cameraPosition=(
        0.16817, 0.082833, 0.188562), cameraTarget=(0.16817, 0.082833, 0))
    s.setAsConstruction(objectList=(g[4], g[9], g[15], g[18], g[21]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.169138, 
        farPlane=0.207986, width=0.20033, height=0.0907575, cameraPosition=(
        0.111746, 0.087859, 0.188562), cameraTarget=(0.111746, 0.087859, 0))
    p = mdb.models['Model-1'].Part(name='Spiral', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Spiral']
    p.BaseSolidExtrude(sketch=s, depth=0.0045)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Spiral']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.220093, 
        farPlane=0.373711, width=0.171809, height=0.0746823, 
        viewOffsetX=0.0038756, viewOffsetY=0.00464269)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.220942, 
        farPlane=0.372863, width=0.172471, height=0.0749703, cameraPosition=(
        0.219379, 0.227729, 0.171476), cameraUpVector=(-0.474761, 0.568923, 
        -0.671512), cameraTarget=(0.0479619, 0.0563122, 5.89989e-05), 
        viewOffsetX=0.00389054, viewOffsetY=0.00466058)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253756, 
        farPlane=0.326474, width=0.198087, height=0.0861049, cameraPosition=(
        0.162337, 0.054285, 0.268435), cameraUpVector=(-0.122176, 0.943034, 
        -0.309449), cameraTarget=(0.0451921, 0.0545319, -0.00438103), 
        viewOffsetX=0.00446836, viewOffsetY=0.00535277)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.245375, 
        farPlane=0.334857, width=0.266875, height=0.116006, 
        viewOffsetX=0.00598538, viewOffsetY=0.00725122)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232602, 
        farPlane=0.349144, width=0.252983, height=0.109967, cameraPosition=(
        0.21226, 0.023341, 0.239481), cameraUpVector=(-0.251946, 0.961261, 
        -0.111807), cameraTarget=(0.0453969, 0.0542255, -0.00414674), 
        viewOffsetX=0.00567383, viewOffsetY=0.00687378)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.223314, 
        farPlane=0.35849, width=0.242881, height=0.105576, cameraPosition=(
        0.237788, -0.0114394, 0.211502), cameraUpVector=(-0.244803, 0.96791, 
        0.0567561), cameraTarget=(0.0449966, 0.054708, -0.00438519), 
        viewOffsetX=0.00544726, viewOffsetY=0.00659929)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.242235, 
        farPlane=0.339568, width=0.0439739, height=0.0191147, 
        viewOffsetX=-0.00848369, viewOffsetY=-0.0348757)
    p = mdb.models['Model-1'].parts['Spiral']
    v1 = p.vertices
    p.DatumPlaneByTwoPoint(point1=v1[24], point2=v1[25])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235806, 
        farPlane=0.345996, width=0.0747072, height=0.0324739, 
        viewOffsetX=-0.0076093, viewOffsetY=-0.0301475)
    p = mdb.models['Model-1'].parts['Spiral']
    v2 = p.vertices
    p.DatumPlaneByTwoPoint(point1=v2[24], point2=v2[25])
    p = mdb.models['Model-1'].parts['Spiral']
    v1 = p.vertices
    p.DatumPlaneByTwoPoint(point1=v1[24], point2=v1[25])
    p = mdb.models['Model-1'].parts['Spiral']
    v2 = p.vertices
    p.DatumPlaneByTwoPoint(point1=v2[25], point2=v2[24])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237196, 
        farPlane=0.344606, width=0.0518422, height=0.0225349, 
        viewOffsetX=-0.00804638, viewOffsetY=-0.0342124)
    p = mdb.models['Model-1'].parts['Spiral']
    e = p.edges
    p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e[36], rule=MIDDLE), 
        point2=p.InterestingPoint(edge=e[34], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['Spiral']
    e1 = p.edges
    p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e1[34], rule=MIDDLE), 
        point2=p.InterestingPoint(edge=e1[36], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235806, 
        farPlane=0.345996, width=0.0747073, height=0.0324739, 
        viewOffsetX=-0.000476513, viewOffsetY=-0.0306472)
    p = mdb.models['Model-1'].parts['Spiral']
    e = p.edges
    p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e[34], rule=MIDDLE), 
        point2=p.InterestingPoint(edge=e[36], rule=MIDDLE), isDependent=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.228208, 
        farPlane=0.353594, width=0.162938, height=0.0708265, 
        viewOffsetX=0.0113522, viewOffsetY=-0.02963)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-1']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-2']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-7']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-6']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-3']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-4']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-5']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235931, 
        farPlane=0.345871, width=0.109238, height=0.0474837, 
        viewOffsetX=0.00276112, viewOffsetY=-0.0299145)
    p = mdb.models['Model-1'].parts['Spiral']
    e1 = p.edges
    p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e1[34], rule=MIDDLE), 
        point2=p.InterestingPoint(edge=e1[36], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229005, 
        farPlane=0.352797, width=0.153697, height=0.0668095, 
        viewOffsetX=0.023446, viewOffsetY=-0.0268644)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232868, 
        farPlane=0.381946, width=0.15629, height=0.0679364, cameraPosition=(
        0.322915, -0.0098737, 0.121264), cameraUpVector=(-0.160702, 0.983488, 
        0.0832255), cameraTarget=(0.0591384, 0.057671, 0.00289677), 
        viewOffsetX=0.0238415, viewOffsetY=-0.0273176)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235391, 
        farPlane=0.387656, width=0.157983, height=0.0686726, cameraPosition=(
        0.339311, -0.00621283, 0.0911075), cameraUpVector=(-0.149019, 0.986318, 
        0.0705054), cameraTarget=(0.0637905, 0.0588943, 0.00166092), 
        viewOffsetX=0.0240998, viewOffsetY=-0.0276136)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229885, 
        farPlane=0.340151, width=0.154288, height=0.0670662, cameraPosition=(
        0.238553, 0.0802205, 0.211923), cameraUpVector=(-0.390339, 0.904891, 
        -0.169727), cameraTarget=(0.0356497, 0.0615602, -0.00402424), 
        viewOffsetX=0.0235361, viewOffsetY=-0.0269677)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.22084, 
        farPlane=0.349196, width=0.243151, height=0.105694, 
        viewOffsetX=0.0319055, viewOffsetY=-0.0114591)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[9], sketchUpEdge=e[37], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316482, 
        farPlane=0.321022, width=0.000220731, height=0.0001, cameraPosition=(
        1.06134e-05, 4.17609e-05, -0.316502), cameraTarget=(1.06134e-05, 
        4.17609e-05, 0.00225))
    s1.Spot(point=(0.0469538941339072, -0.0551291624212018))
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e1[40], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.295295, 
        farPlane=0.34221, width=0.218726, height=0.0990918, cameraPosition=(
        0.0312231, 0.0375875, -0.316502), cameraTarget=(0.0312231, 0.0375875, 
        0.00225))
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[9], sketchUpEdge=e[40], 
        sketchPlaneSide=SIDE1, sketchOrientation=LEFT, origin=(0.046954, 
        0.055129, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23917, 
        farPlane=0.330866, width=0.0527023, height=0.0229088, 
        viewOffsetX=0.00230318, viewOffsetY=-0.0442586)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e1[37], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316482, 
        farPlane=0.321022, width=0.000220731, height=0.0001, cameraPosition=(
        0.0499463, 3.76408e-05, -0.316502), cameraTarget=(0.0499463, 
        3.76408e-05, 0.00225))
    s.Line(point1=(-0.0030478410384655, -0.0551289380997906), point2=(
        -0.00302754947915673, -0.0551289380997906))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316395, 
        farPlane=0.321109, width=0.0012533, height=0.000567797, 
        cameraPosition=(0.0495216, 0.000150132, -0.316502), cameraTarget=(
        0.0495216, 0.000150132, 0.00225))
    s.Line(point1=(-0.00302754947915673, -0.0551289380997906), point2=(
        -0.0028757699765265, -0.0551289380997906))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316482, 
        farPlane=0.321022, width=0.000220731, height=0.0001, cameraPosition=(
        6.89462e-05, 3.03434e-05, -0.316502), cameraTarget=(6.89462e-05, 
        3.03434e-05, 0.00225))
    s.Line(point1=(-0.0028757699765265, -0.0551289380997906), point2=(
        0.0469538238830864, -0.0551289380997906))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.ParallelConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00833974, 
        0.0492929, -0.316502), cameraTarget=(0.00833974, 0.0492929, 0.00225))
    s.Line(point1=(0.0469538238830864, -0.0551289380997906), point2=(
        0.0386241903566718, -0.00582763274693489))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0263701, 
        0.0821566, -0.316502), cameraTarget=(0.0263701, 0.0821566, 0.00225))
    s.Line(point1=(0.0386241903566718, -0.00582763274693489), point2=(
        0.0205812413283587, 0.0270463591299057))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0472108, 
        0.100991, -0.316502), cameraTarget=(0.0472108, 0.100991, 0.00225))
    s.Line(point1=(0.0205812413283587, 0.0270463591299057), point2=(
        -0.000297503914594648, 0.0458920290551186))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0666245, 
        0.109228, -0.316502), cameraTarget=(0.0666245, 0.109228, 0.00225))
    s.Line(point1=(-0.000297503914594648, 0.0458920290551186), point2=(
        -0.0197288081011772, 0.0540999537191391))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0823928, 
        0.110269, -0.316502), cameraTarget=(0.0823928, 0.110269, 0.00225))
    s.Line(point1=(-0.0197288081011772, 0.0540999537191391), point2=(
        -0.0355162456593513, 0.0551292439780235))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0938186, 
        0.10712, -0.316502), cameraTarget=(0.0938186, 0.10712, 0.00225))
    s.Line(point1=(-0.0355162456593513, 0.0551292439780235), point2=(
        -0.0469536989889145, 0.0519700711450577))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306063, 
        farPlane=0.331441, width=0.121845, height=0.0552007, cameraPosition=(
        0.0484227, 0.117208, -0.316502), cameraTarget=(0.0484227, 0.117208, 
        0.00225))
    s.Line(point1=(-0.0469536989889145, 0.0519700711450577), point2=(
        -0.0560000000987202, 0.0519700711450577))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.293428, 
        farPlane=0.344076, width=0.269325, height=0.122015, cameraPosition=(
        -0.0550683, 0.0261856, -0.316502), cameraTarget=(-0.0550683, 0.0261856, 
        0.00225))
    s.offset(distance=0.0005, objectList=(g[2], g[3], g[4], g[5], g[6], g[7], g[8], 
        g[9], g[10], g[11]), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316217, 
        farPlane=0.321287, width=0.00294179, height=0.00133275, 
        cameraPosition=(0.048766, 0.000583631, -0.316502), cameraTarget=(
        0.048766, 0.000583631, 0.00225))
    s.autoTrimCurve(curve1=g[12], point1=(-0.00303567051506042, 
        -0.0546949429696389))
    s.autoTrimCurve(curve1=g[13], point1=(-0.0029448889157772, -0.05449615408694))
    s.autoTrimCurve(curve1=g[2], point1=(-0.00305884927129745, 
        -0.0551793702904098))
    s.autoTrimCurve(curve1=g[3], point1=(-0.00299317612862587, 
        -0.0550539209649861))
    s.autoTrimCurve(curve1=g[22], point1=(-0.00303567051506042, 
        -0.0551832302732356))
    s.autoTrimCurve(curve1=g[14], point1=(-0.00273820981001854, 
        -0.0547586325989533))
    s.autoTrimCurve(curve1=g[4], point1=(-0.00258754789447784, 
        -0.0553665792246312))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314142, 
        farPlane=0.323362, width=0.024338, height=0.0110261, cameraPosition=(
        0.00190949, 0.00364115, -0.316502), cameraTarget=(0.00190949, 
        0.00364115, 0.00225))
    s.dragEntity(entity=v[14], points=((0.0463622609604544, -0.0546289380997906), (
        0.0463622609604544, -0.0546289380997906), (0.0464747518804818, 
        -0.0548786632859111), (0.0464747518804818, -0.0550541873232424), (
        0.0465067130085975, -0.0552137547780722), (0.0465067130085975, 
        -0.0553254520197362), (0.0464108305555731, -0.0552456681759059), (
        0.0465386732053906, -0.0552616249912381), (0.0466824973505884, 
        -0.0553254520197362), (0.0467304371801168, -0.0553573654175699), (
        0.0465706343335062, -0.0553573654175699), (0.0465866148975641, 
        -0.0554371490285695), (0.0466984769833237, -0.0555169331052303), (
        0.0468103390690833, -0.0555648030855656), (0.0469701419156939, 
        -0.0555967167162299)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309196, 
        farPlane=0.328308, width=0.0753488, height=0.0341361, cameraPosition=(
        0.0040432, 0.0127688, -0.316502), cameraTarget=(0.0040432, 0.0127688, 
        0.00225))
    s.dragEntity(entity=v[14], points=((0.046970141915694, -0.0555967167162299), (
        0.04725, -0.056), (0.0455, -0.056), (0.0455, -0.0554267028489113), (
        0.0460523936004341, -0.056), (0.0465471345038116, -0.056), (
        0.046646081939429, -0.056)))
    s.AngularDimension(line1=g[5], line2=g[15], textPoint=(0.0468934523911178, 
        -0.0568688530617356), value=0.0005)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315554, 
        farPlane=0.32195, width=0.00977903, height=0.00443029, cameraPosition=(
        0.000412352, 0.000282361, -0.316502), cameraTarget=(0.000412352, 
        0.000282361, 0.00225))
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233126, 
        farPlane=0.33691, width=0.115299, height=0.0501184, 
        viewOffsetX=0.0140437, viewOffsetY=-0.0381108)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[9], sketchUpEdge=e[96], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.272542, 
        farPlane=0.364962, width=0.453384, height=0.205401, cameraPosition=(
        -0.0194498, 0.0984835, -0.316502), cameraTarget=(-0.0194498, 0.0984835, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s1, edges=(e1[2], e1[6], e1[9], e1[12], e1[15], 
        e1[41]))
    s1.offset(distance=0.0005, objectList=(g[2], g[3], g[4], g[5], g[6], g[7]), 
        side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31107, 
        farPlane=0.326434, width=0.0560252, height=0.0253816, cameraPosition=(
        0.0760259, 0.107761, -0.316502), cameraTarget=(0.0760259, 0.107761, 
        0.00225))
    s1.autoTrimCurve(curve1=g[6], point1=(-0.0454600438437462, 0.0520986160120964))
    s1.autoTrimCurve(curve1=g[5], point1=(-0.0329895675144195, 0.0548553084812164))
    s1.autoTrimCurve(curve1=g[4], point1=(-0.0154426231942177, 0.0520618622980118))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306983, 
        farPlane=0.330521, width=0.0981761, height=0.0444777, cameraPosition=(
        0.0551731, 0.103933, -0.316502), cameraTarget=(0.0551731, 0.103933, 
        0.00225))
    s1.autoTrimCurve(curve1=g[3], point1=(0.00128910839939119, 0.0443279361209869))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.308057, 
        farPlane=0.329448, width=0.0871033, height=0.0394613, cameraPosition=(
        0.0398034, 0.0932094, -0.316502), cameraTarget=(0.0398034, 0.0932094, 
        0.00225))
    s1.autoTrimCurve(curve1=g[2], point1=(0.0211912408509255, 0.0254227882108688))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.305596, 
        farPlane=0.331908, width=0.112478, height=0.0509573, cameraPosition=(
        0.00311727, 0.0578568, -0.316502), cameraTarget=(0.00311727, 0.0578568, 
        0.00225))
    s1.autoTrimCurve(curve1=g[7], point1=(0.0387039339208007, 
        -0.00808283036136628))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.28679, 
        farPlane=0.350714, width=0.346807, height=0.157117, cameraPosition=(
        -0.0211172, 0.0598899, -0.316502), cameraTarget=(-0.0211172, 0.0598899, 
        0.00225))
    s1.Line(point1=(-0.0468207418629431, 0.051488394920639), point2=(
        -0.046820741862943, -0.0594999999869615))
    s1.VerticalConstraint(entity=g[14], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309343, 
        farPlane=0.328161, width=0.0738387, height=0.0334519, cameraPosition=(
        -0.00325195, 0.0116319, -0.316502), cameraTarget=(-0.00325195, 
        0.0116319, 0.00225))
    s1.Line(point1=(-0.046820741862943, -0.0594999999869615), point2=(
        0.0464970432221889, -0.0594999999869615))
    s1.HorizontalConstraint(entity=g[15], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
    s1.Line(point1=(0.0464970432221889, -0.0594999999869615), point2=(
        0.046460987435655, -0.0552122983277022))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.264648, 
        farPlane=0.372856, width=0.605253, height=0.274204, cameraPosition=(
        -0.186838, -0.00947067, -0.316502), cameraTarget=(-0.186838, 
        -0.00947067, 0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e, d2 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d2[9], sketchUpEdge=e[96], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s1, depth=0.0005, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229231, 
        farPlane=0.340805, width=0.155745, height=0.0676997, 
        viewOffsetX=0.0210819, viewOffsetY=-0.0251089)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239941, 
        farPlane=0.38104, width=0.163021, height=0.0708626, cameraPosition=(
        0.354879, 0.029576, -0.0358561), cameraUpVector=(-0.17885, 0.896768, 
        0.404747), cameraTarget=(0.0648386, 0.0560614, 0.0218163), 
        viewOffsetX=0.0220669, viewOffsetY=-0.0262819)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25078, 
        farPlane=0.3702, width=0.0351746, height=0.0152898, 
        viewOffsetX=0.0309199, viewOffsetY=0.0355187)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.259396, 
        farPlane=0.371214, width=0.0363831, height=0.0158151, cameraPosition=(
        0.36222, 0.0488435, -0.000192773), cameraUpVector=(-0.307798, 0.729063, 
        0.611332), cameraTarget=(0.0654308, 0.0538459, 0.00630064), 
        viewOffsetX=0.0319823, viewOffsetY=0.036739)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.252448, 
        farPlane=0.349132, width=0.0354086, height=0.0153915, cameraPosition=(
        0.195518, 0.000913605, -0.256291), cameraUpVector=(0.571137, 0.212853, 
        0.792778), cameraTarget=(0.0222713, 0.0651878, -0.0238999), 
        viewOffsetX=0.0311257, viewOffsetY=0.035755)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221191, 
        farPlane=0.38039, width=0.400246, height=0.17398, 
        viewOffsetX=0.0731731, viewOffsetY=0.0273398)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.219599, 
        farPlane=0.381982, width=0.397365, height=0.172728, cameraPosition=(
        0.188151, 0.00330998, -0.262446), cameraUpVector=(0.567349, 0.12761, 
        0.81353), cameraTarget=(0.0149046, 0.0675842, -0.0300545), 
        viewOffsetX=0.0726464, viewOffsetY=0.0271431)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.219556, 
        farPlane=0.382026, width=0.397287, height=0.172694, cameraPosition=(
        0.193393, 0.00150615, -0.258039), cameraUpVector=(0.570735, 0.188707, 
        0.799156), cameraTarget=(0.0201466, 0.0657804, -0.0256477), 
        viewOffsetX=0.0726321, viewOffsetY=0.0271378)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0927448, 
        farPlane=0.306179, width=0.167822, height=0.0729494, cameraPosition=(
        0.0816201, -0.147413, 0.0137328), cameraUpVector=(0.836434, 0.529488, 
        0.141494), cameraTarget=(0.0114241, 0.13601, 0.0675398), 
        viewOffsetX=0.0306812, viewOffsetY=0.0114635)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.126704, 
        farPlane=0.27222, width=0.0232316, height=0.0100984, 
        viewOffsetX=0.0341943, viewOffsetY=0.00225509)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.127745, 
        farPlane=0.271695, width=0.0234225, height=0.0101814, cameraPosition=(
        0.0805003, -0.148236, 0.00233847), cameraUpVector=(0.836847, 0.515845, 
        0.183276), cameraTarget=(0.0108656, 0.131888, 0.0718571), 
        viewOffsetX=0.0344753, viewOffsetY=0.00227362)
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.123039, 
        farPlane=0.2764, width=0.0794132, height=0.0345195, 
        viewOffsetX=0.037006, viewOffsetY=0.00559662)
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s1 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.124477, 
        farPlane=0.274962, width=0.0627262, height=0.027266, 
        viewOffsetX=0.0451036, viewOffsetY=0.00563476)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-1'].setValues(depth=0.00025)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.124811, 
        farPlane=0.274628, width=0.0522395, height=0.0227076, 
        viewOffsetX=0.0428567, viewOffsetY=0.00545822)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.125092, 
        farPlane=0.274347, width=0.0523568, height=0.0227586, cameraPosition=(
        0.0845897, -0.147434, 0.0032049), cameraUpVector=(0.838322, 0.530167, 
        0.127042), cameraTarget=(0.014955, 0.13269, 0.0727235), 
        viewOffsetX=0.0429529, viewOffsetY=0.00547048)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.125092, 
        farPlane=0.274347, width=0.0523567, height=0.0227586, cameraPosition=(
        0.0801562, -0.1483, 0.00225376), cameraUpVector=(0.836564, 0.514597, 
        0.188018), cameraTarget=(0.0105215, 0.131824, 0.0717724), 
        viewOffsetX=0.0429528, viewOffsetY=0.00547047)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.125092, 
        width=0.0523567, height=0.0227585, cameraPosition=(0.0769706, 
        -0.148875, 0.00138057), cameraUpVector=(0.832729, 0.502727, 0.232008), 
        cameraTarget=(0.00733593, 0.131249, 0.0708992), viewOffsetX=0.0429527, 
        viewOffsetY=0.00547046)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.112426, 
        farPlane=0.26287, width=0.0470555, height=0.0204542, cameraPosition=(
        0.0902206, -0.0871249, 0.129529), cameraUpVector=(0.606416, 0.789304, 
        0.0962204), cameraTarget=(-0.032272, 0.148547, -0.00315809), 
        viewOffsetX=0.0386037, viewOffsetY=0.00491657)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.10787, 
        farPlane=0.272008, width=0.0451485, height=0.0196253, cameraPosition=(
        0.131514, -0.0969527, 0.0965266), cameraUpVector=(0.537834, 0.838722, 
        0.0853259), cameraTarget=(-0.0380423, 0.136797, 0.0275092), 
        viewOffsetX=0.0370392, viewOffsetY=0.00471732)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.100303, 
        farPlane=0.279574, width=0.137705, height=0.0598579, 
        viewOffsetX=0.0405691, viewOffsetY=0.00259779)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.100165, 
        farPlane=0.282909, width=0.137515, height=0.0597752, cameraPosition=(
        0.163084, -0.0855228, 0.0826857), cameraUpVector=(0.424944, 0.903835, 
        0.0500554), cameraTarget=(-0.0432783, 0.123419, 0.0389881), 
        viewOffsetX=0.0405131, viewOffsetY=0.0025942)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d1 = p.edges, p.datums
    p.Mirror(mirrorPlane=d1[9], keepOriginal=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.103722, 
        farPlane=0.279351, width=0.092342, height=0.0401394, 
        viewOffsetX=0.038763, viewOffsetY=0.00701839)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.104174, 
        farPlane=0.278899, width=0.0927448, height=0.0403145, cameraPosition=(
        0.163903, -0.0846433, 0.0830234), cameraUpVector=(0.427734, 0.90326, 
        0.0341301), cameraTarget=(-0.0424593, 0.124298, 0.0393258), 
        viewOffsetX=0.0389321, viewOffsetY=0.00704901)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.152924, 
        farPlane=0.195695, width=0.136146, height=0.0591804, cameraPosition=(
        -0.0259712, 0.0814758, 0.173355), cameraUpVector=(0.707255, 0.677255, 
        -0.202772), cameraTarget=(0.00337717, 0.108883, -0.12082), 
        viewOffsetX=0.057151, viewOffsetY=0.0103477)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.079401, 
        farPlane=0.261266, width=0.0706897, height=0.0307276, cameraPosition=(
        0.139774, -0.0728848, 0.0942615), cameraUpVector=(0.45686, 0.888367, 
        0.0456525), cameraTarget=(-0.0580294, 0.142814, 0.0442675), 
        viewOffsetX=0.0296739, viewOffsetY=0.00537272)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0900629, 
        farPlane=0.248225, width=0.0801819, height=0.0348537, cameraPosition=(
        0.179558, -0.0687129, -0.0078113), cameraUpVector=(0.362013, 0.9105, 
        0.199842), cameraTarget=(-0.0339802, 0.0983171, 0.113242), 
        viewOffsetX=0.0336585, viewOffsetY=0.00609416)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0892244, 
        farPlane=0.249063, width=0.0898998, height=0.0390779, 
        viewOffsetX=0.0353892, viewOffsetY=0.00659657)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.140462, 
        farPlane=0.196153, width=0.141525, height=0.0615184, cameraPosition=(
        -0.0210617, 0.11841, 0.158294), cameraUpVector=(0.380223, 0.738479, 
        -0.556847), cameraTarget=(-0.0174909, 0.0356085, -0.126807), 
        viewOffsetX=0.0557115, viewOffsetY=0.0103847)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.10559, 
        farPlane=0.231664, width=0.106389, height=0.0462454, cameraPosition=(
        0.228351, 0.0512017, 0.00969943), cameraUpVector=(-0.342934, 0.939091, 
        -0.022447), cameraTarget=(-0.0515866, 0.0567232, 0.108471), 
        viewOffsetX=0.0418801, viewOffsetY=0.00780651)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.115173, 
        farPlane=0.222081, width=0.0297465, height=0.0129303, 
        viewOffsetX=0.0449681, viewOffsetY=0.0149087)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.110014, 
        farPlane=0.231615, width=0.0284142, height=0.0123512, cameraPosition=(
        0.229032, 0.0708876, -0.00476319), cameraUpVector=(-0.435004, 0.871754, 
        0.225425), cameraTarget=(-0.0407847, 0.0205073, 0.108428), 
        viewOffsetX=0.042954, viewOffsetY=0.0142409)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.100754, 
        farPlane=0.240876, width=0.13889, height=0.060373, 
        viewOffsetX=0.0535548, viewOffsetY=0.00986869)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d2 = p.edges, p.datums
    p.Mirror(mirrorPlane=d2[9], keepOriginal=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.104274, 
        farPlane=0.237355, width=0.0876212, height=0.0380874, 
        viewOffsetX=0.0461326, viewOffsetY=0.00463906)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.10421, 
        farPlane=0.237419, width=0.0882856, height=0.0383762, 
        viewOffsetX=0.0590376, viewOffsetY=0.0309312)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.104647, 
        farPlane=0.236983, width=0.0886551, height=0.0385368, cameraPosition=(
        0.22906, 0.0713113, -0.00450672), cameraUpVector=(-0.436686, 0.871922, 
        0.221491), cameraTarget=(-0.0407562, 0.020931, 0.108684), 
        viewOffsetX=0.0592847, viewOffsetY=0.0310607)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0999527, 
        farPlane=0.238534, width=0.0846782, height=0.0368081, cameraPosition=(
        0.226917, 0.0773696, 0.0150416), cameraUpVector=(-0.48392, 0.855805, 
        0.182809), cameraTarget=(-0.0509981, 0.0175659, 0.100703), 
        viewOffsetX=0.0566253, viewOffsetY=0.0296674)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.103984, 
        farPlane=0.230772, width=0.0880933, height=0.0382926, cameraPosition=(
        0.226113, 0.0560785, -4.24944e-05), cameraUpVector=(-0.377337, 0.89475, 
        0.23883), cameraTarget=(-0.0497511, 0.0224569, 0.104455), 
        viewOffsetX=0.058909, viewOffsetY=0.0308639)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0997727, 
        farPlane=0.234984, width=0.138665, height=0.0602751, 
        viewOffsetX=0.0676698, viewOffsetY=0.0271723)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0991779, 
        farPlane=0.235579, width=0.137838, height=0.0599157, cameraPosition=(
        0.226073, 0.055568, -0.000312946), cameraUpVector=(-0.375717, 0.894318, 
        0.242967), cameraTarget=(-0.0497913, 0.0219464, 0.104185), 
        viewOffsetX=0.0672664, viewOffsetY=0.0270103)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0760964, 
        farPlane=0.226684, width=0.105759, height=0.0459717, cameraPosition=(
        0.193114, 0.0689308, 0.0800272), cameraUpVector=(-0.520442, 0.850943, 
        0.0709656), cameraTarget=(-0.0969626, 0.00968047, 0.0577467), 
        viewOffsetX=0.0516116, viewOffsetY=0.0207242)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d1 = p.edges, p.datums
    p.Mirror(mirrorPlane=d1[9], keepOriginal=ON)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0724604, 
        farPlane=0.23032, width=0.186972, height=0.0812735, 
        viewOffsetX=0.0886982, viewOffsetY=0.0188375)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e[161], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309338, 
        farPlane=0.328166, width=0.0738855, height=0.0334731, cameraPosition=(
        0.00914445, 0.0509057, -0.316502), cameraTarget=(0.00914445, 0.0509057, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p2 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s, edges=(e1[3], e1[42], e1[43], e1[44], 
        e1[45], e1[46]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.252744, 
        farPlane=0.384761, width=0.744208, height=0.337156, cameraPosition=(
        -0.207333, 0.0777926, -0.316502), cameraTarget=(-0.207333, 0.0777926, 
        0.00225))
    s.Line(point1=(-0.0467393983318203, 0.0515108617708612), point2=(
        -0.0467393983318204, -0.0612500000139698))
    s.VerticalConstraint(entity=g[46], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.308227, 
        farPlane=0.329277, width=0.0853433, height=0.038664, cameraPosition=(
        -0.0237077, 0.00871961, -0.316502), cameraTarget=(-0.0237077, 
        0.00871961, 0.00225))
    s.Line(point1=(-0.0467393983318204, -0.0612500000139698), point2=(
        0.0464820709117651, -0.0598190827437639))
    s.Line(point1=(0.0464820709117651, -0.0598190827437639), point2=(
        0.0464469135318647, -0.055129))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.296582, 
        farPlane=0.340922, width=0.232511, height=0.105337, cameraPosition=(
        -0.0651988, 0.0180846, -0.316502), cameraTarget=(-0.0651988, 0.0180846, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d1[9], sketchUpEdge=e[161], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s, depth=0.00025, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0855223, 
        farPlane=0.217258, width=0.032413, height=0.0140893, 
        viewOffsetX=0.0737413, viewOffsetY=0.0401612)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-2'].setValues(flipExtrudeDirection=True)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0759411, 
        farPlane=0.22684, width=0.147377, height=0.0640623, 
        viewOffsetX=0.0748272, viewOffsetY=0.0199491)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0652667, 
        farPlane=0.194713, width=0.126662, height=0.0550576, cameraPosition=(
        0.159146, 0.0119633, 0.0886497), cameraUpVector=(-0.412406, 0.889004, 
        0.198977), cameraTarget=(-0.127685, 0.00735935, 0.0121099), 
        viewOffsetX=0.0643095, viewOffsetY=0.0171451)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0598319, 
        farPlane=0.200148, width=0.21558, height=0.093709, 
        viewOffsetX=0.0795192, viewOffsetY=0.00836444)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0592222, 
        farPlane=0.200758, width=0.213384, height=0.0927541, cameraPosition=(
        0.158629, 0.0159868, 0.0903437), cameraUpVector=(-0.406656, 0.896273, 
        0.176992), cameraTarget=(-0.128202, 0.0113828, 0.0138039), 
        viewOffsetX=0.0787089, viewOffsetY=0.0082792)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0591562, 
        farPlane=0.200823, width=0.213146, height=0.0926509, cameraPosition=(
        0.158512, 0.0169296, 0.0907238), cameraUpVector=(-0.40531, 0.897882, 
        0.17185), cameraTarget=(-0.128319, 0.0123256, 0.014184), 
        viewOffsetX=0.0786212, viewOffsetY=0.00826997)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0227399, 
        farPlane=0.142732, width=0.0819343, height=0.0356154, cameraPosition=(
        0.0597464, 0.0289306, 0.112052), cameraUpVector=(-0.389962, 0.917198, 
        -0.0817167), cameraTarget=(-0.160676, 0.0253983, -0.0868276), 
        viewOffsetX=0.0302223, viewOffsetY=0.00317901)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.033327, 
        farPlane=0.0989731, width=0.120081, height=0.052197, cameraPosition=(
        -0.00707559, 0.0232718, 0.0871876), cameraUpVector=(-0.275102, 0.9394, 
        -0.204565), cameraTarget=(-0.0975394, 0.0406692, -0.195063), 
        viewOffsetX=0.044293, viewOffsetY=0.00465908)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0219117, 
        farPlane=0.110389, width=0.242436, height=0.105383, 
        viewOffsetX=0.0254181, viewOffsetY=-0.00470449)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0257369, 
        farPlane=0.112907, width=0.28476, height=0.12378, cameraPosition=(
        -0.0206026, 0.0187311, 0.0765684), cameraUpVector=(-0.175193, 0.975672, 
        -0.131799), cameraTarget=(-0.0630633, 0.0735447, -0.212126), 
        viewOffsetX=0.0298555, viewOffsetY=-0.00552579)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.285473, 
        farPlane=0.352031, width=0.360057, height=0.156511, 
        viewOffsetX=-0.00882447, viewOffsetY=0.00028267)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217977, 
        farPlane=0.400498, width=0.274926, height=0.119506, cameraPosition=(
        0.34828, 0.0980993, 0.0574602), cameraUpVector=(-0.139248, 0.990157, 
        0.0141401), cameraTarget=(0.0391113, 0.0555466, -0.00740049), 
        viewOffsetX=-0.00673803, viewOffsetY=0.000215836)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24529, 
        farPlane=0.373185, width=0.05471, height=0.0237815, 
        viewOffsetX=0.00115212, viewOffsetY=0.0312232)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247979, 
        farPlane=0.3618, width=0.0553098, height=0.0240422, cameraPosition=(
        0.326141, 0.0763575, 0.122956), cameraUpVector=(-0.0293572, 0.995501, 
        -0.090088), cameraTarget=(0.0350244, 0.0561672, -0.00528843), 
        viewOffsetX=0.00116475, viewOffsetY=0.0315656)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236024, 
        farPlane=0.373756, width=0.197026, height=0.0856438, 
        viewOffsetX=0.0156453, viewOffsetY=0.026401)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236542, 
        farPlane=0.384461, width=0.197458, height=0.0858317, cameraPosition=(
        0.350318, 0.0812231, 0.0635659), cameraUpVector=(-0.106254, 0.992166, 
        0.0657012), cameraTarget=(0.0407443, 0.0527319, -0.00683191), 
        viewOffsetX=0.0156797, viewOffsetY=0.026459)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.224412, 
        farPlane=0.396592, width=0.347804, height=0.151184, 
        viewOffsetX=0.0298236, viewOffsetY=0.0405206)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.149405, 
        farPlane=0.331945, width=0.231554, height=0.100653, cameraPosition=(
        0.0494658, -0.156062, 0.128878), cameraUpVector=(0.585186, 0.569727, 
        0.577034), cameraTarget=(-0.0152792, 0.0963584, -0.0546859), 
        viewOffsetX=0.0198554, viewOffsetY=0.026977)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.196902, 
        farPlane=0.275004, width=0.305169, height=0.132652, cameraPosition=(
        0.0147902, -0.0430353, 0.221409), cameraUpVector=(0.00448185, 0.975255, 
        0.221036), cameraTarget=(0.0202936, 0.0273869, -0.0894189), 
        viewOffsetX=0.0261676, viewOffsetY=0.0355533)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217046, 
        farPlane=0.25486, width=0.0250157, height=0.0108739, 
        viewOffsetX=-0.00964211, viewOffsetY=-0.00289503)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217188, 
        farPlane=0.254718, width=0.0250321, height=0.010881, 
        viewOffsetX=-0.00964843, viewOffsetY=-0.00289693)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.213595, 
        farPlane=0.250966, width=0.0246179, height=0.010701, cameraPosition=(
        0.0293338, -0.0366759, 0.221812), cameraUpVector=(-0.0268837, 0.979979, 
        0.197277), cameraTarget=(0.0150395, 0.0257895, -0.0904335), 
        viewOffsetX=-0.0094888, viewOffsetY=-0.002849)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.212693, 
        farPlane=0.251867, width=0.0328592, height=0.0142833, 
        viewOffsetX=0.0084773, viewOffsetY=0.00785363)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e1[179], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.281593, 
        farPlane=0.355911, width=0.407465, height=0.184598, cameraPosition=(
        0.00876135, 0.06454, -0.316502), cameraTarget=(0.00876135, 0.06454, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s1, edges=(e[0], e[1], e[2], e[3], e[4], e[5], 
        e[6], e[7], e[8], e[9], e[10], e[11], e[12], e[13], e[14], e[15], 
        e[16], e[17], e[18], e[19], e[20], e[21], e[22], e[23], e[24], e[25], 
        e[26], e[27], e[28], e[29], e[30], e[31], e[32], e[33], e[34], e[35], 
        e[36], e[37], e[38], e[39], e[40], e[41], e[42], e[43], e[44], e[45], 
        e[46], e[47], e[48], e[49], e[50], e[51], e[52], e[53], e[54], e[55], 
        e[56], e[57], e[58], e[59], e[60], e[61], e[62], e[63], e[64], e[65], 
        e[66], e[67], e[68], e[69], e[70], e[71], e[72], e[73], e[74], e[75], 
        e[76], e[77], e[78], e[79], e[80], e[81], e[82], e[83], e[84], e[85], 
        e[86], e[87], e[88], e[89], e[90], e[91], e[92], e[93], e[94], e[95], 
        e[96], e[97], e[98], e[99], e[100], e[101], e[102], e[103], e[104], 
        e[105], e[106], e[107], e[108], e[109], e[110], e[111], e[112], e[113], 
        e[114], e[115], e[116], e[117], e[118], e[119], e[120], e[121], e[122], 
        e[123], e[124], e[125], e[126], e[127], e[128], e[129], e[130], e[131], 
        e[132], e[133], e[134], e[135], e[136], e[137], e[138], e[139], e[140], 
        e[141], e[142], e[143], e[144], e[145], e[146], e[147], e[148], e[149], 
        e[150], e[151], e[152], e[153], e[154], e[155], e[156], e[157], e[158], 
        e[159], e[160], e[161], e[162], e[163], e[164], e[165], e[166], e[167], 
        e[168], e[169], e[170], e[171], e[172], e[173], e[174], e[175], e[176], 
        e[177], e[178], e[179], e[180], e[181], e[182], e[183], e[184], e[185], 
        e[186], e[187], e[188], e[189], e[190], e[191], e[192], e[193], e[194], 
        e[195], e[196], e[197], e[198], e[199], e[200], e[201], e[202], e[203], 
        e[204], e[205], e[206], e[207], e[208], e[209], e[210], e[211], e[212], 
        e[213], e[214], e[215], e[216], e[217], e[218], e[219], e[220], e[221], 
        e[222], e[223], e[224], e[225], e[226], e[227], e[228], e[229], e[230], 
        e[231], e[232], e[233], e[234]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.30907, 
        farPlane=0.328434, width=0.0766553, height=0.0347279, cameraPosition=(
        0.0643951, 0.100255, -0.316502), cameraTarget=(0.0643951, 0.100255, 
        0.00225))
    s1.Line(point1=(-0.0355163142727197, 0.0551293661783491), point2=(
        -0.0343069010184524, 0.0433253806470771))
    s1.Line(point1=(-0.0343069010184524, 0.0433253806470771), point2=(
        -0.0197289324061808, 0.0541001408857608))
    s1.Line(point1=(-0.0197289324061808, 0.0541001408857608), point2=(
        -0.0233738994243129, 0.0387048511405319))
    s1.Line(point1=(-0.0233738994243129, 0.0387048511405319), point2=(
        -0.000297140811361674, 0.0458918307475496))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.307554, 
        farPlane=0.32995, width=0.0922908, height=0.0418115, cameraPosition=(
        0.0700519, 0.0974856, -0.316502), cameraTarget=(0.0700519, 0.0974856, 
        0.00225))
    s1.Line(point1=(-0.000297140811361674, 0.0458918307475496), point2=(
        -0.01162801235993, 0.028099072955139))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.305684, 
        farPlane=0.33182, width=0.11157, height=0.0505458, cameraPosition=(
        0.0506816, 0.0940837, -0.316502), cameraTarget=(0.0506816, 0.0940837, 
        0.00225))
    s1.Line(point1=(-0.01162801235993, 0.028099072955139), point2=(
        0.0205811843152886, 0.0270466640105573))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.298756, 
        farPlane=0.338749, width=0.207143, height=0.093844, cameraPosition=(
        0.067217, 0.106584, -0.316502), cameraTarget=(0.067217, 0.106584, 
        0.00225))
    s1.Line(point1=(0.0205811843152886, 0.0270466640105573), point2=(
        -0.00147888277828301, 0.00959965253964115))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.307952, 
        farPlane=0.329552, width=0.0881818, height=0.0399499, cameraPosition=(
        0.0186502, 0.0614729, -0.316502), cameraTarget=(0.0186502, 0.0614729, 
        0.00225))
    s1.Line(point1=(-0.00147888277828301, 0.00959965253964115), point2=(
        0.0386241672297821, -0.00582774356550126))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.304852, 
        farPlane=0.332652, width=0.120154, height=0.0544348, cameraPosition=(
        0.0260881, 0.0635067, -0.316502), cameraTarget=(0.0260881, 0.0635067, 
        0.00225))
    s1.Line(point1=(0.0386241672297821, -0.00582774356550126), point2=(
        0.00320327466191974, -0.0181418117651448))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.310555, 
        farPlane=0.326949, width=0.0613328, height=0.0277862, cameraPosition=(
        0.069479, 0.106703, -0.316502), cameraTarget=(0.069479, 0.106703, 
        0.00225))
    s1.autoTrimCurve(curve1=g[46], point1=(-0.0377273023090362, 
        0.0546922897777558))
    s1.autoTrimCurve(curve1=g[9], point1=(-0.0464258477053642, 0.0505477702102661))
    s1.autoTrimCurve(curve1=g[10], point1=(-0.0462244883141517, 
        0.0516744321069718))
    s1.autoTrimCurve(curve1=g[41], point1=(-0.0468285590372085, 
        0.0518353869996071))
    s1.autoTrimCurve(curve1=g[8], point1=(-0.0392576068601608, 0.0438280245146752))
    s1.autoTrimCurve(curve1=g[38], point1=(-0.0394186884126663, 
        0.0453973105034828))
    s1.autoTrimCurve(curve1=g[39], point1=(-0.0368413388690948, 
        0.0507489656887055))
    s1.autoTrimCurve(curve1=g[36], point1=(-0.0406268149576187, 0.051513484664917))
    s1.autoTrimCurve(curve1=g[37], point1=(-0.0432041645011902, 
        0.0487773036441803))
    s1.autoTrimCurve(curve1=g[45], point1=(-0.032371258731842, 0.0550141921124458))
    s1.autoTrimCurve(curve1=g[11], point1=(-0.0324115291199684, 
        0.0543301468572617))
    s1.autoTrimCurve(curve1=g[49], point1=(-0.0268138557634354, 
        0.0491796796998978))
    s1.autoTrimCurve(curve1=g[16], point1=(-0.0277400970420837, 
        0.0517951538643837))
    s1.autoTrimCurve(curve1=g[17], point1=(-0.0317671954593658, 
        0.0495015820345879))
    s1.autoTrimCurve(curve1=g[58], point1=(-0.0320088177881241, 
        0.0447132652482987))
    s1.autoTrimCurve(curve1=g[7], point1=(-0.0315658360681534, 0.0420977910838127))
    s1.autoTrimCurve(curve1=g[18], point1=(-0.0292301237545013, 
        0.0440292125425339))
    s1.autoTrimCurve(curve1=g[19], point1=(-0.0248405769429207, 
        0.0454375436387062))
    s1.autoTrimCurve(curve1=g[59], point1=(-0.0218202531299591, 
        0.0525999134263992))
    s1.autoTrimCurve(curve1=g[57], point1=(-0.0202094078025818, 
        0.0538875227651596))
    s1.autoTrimCurve(curve1=g[60], point1=(-0.0202094078025818, 
        0.0536058610162735))
    s1.autoTrimCurve(curve1=g[44], point1=(-0.0186791181526184, 
        0.0538070490441322))
    s1.autoTrimCurve(curve1=g[12], point1=(-0.0187193810901642, 
        0.0530022894821167))
    s1.autoTrimCurve(curve1=g[51], point1=(-0.0139271341226101, 
        0.0416551744422913))
    s1.autoTrimCurve(curve1=g[63], point1=(-0.00325531363105772, 
        0.0450754007182121))
    s1.autoTrimCurve(curve1=g[20], point1=(-0.00551049261903761, 
        0.0449546864113808))
    s1.autoTrimCurve(curve1=g[21], point1=(-0.0189207404813766, 
        0.0442706411561966))
    s1.autoTrimCurve(curve1=g[62], point1=(-0.0208537489137649, 
        0.0395225575051308))
    s1.autoTrimCurve(curve1=g[22], point1=(-0.0194442629776001, 0.038999467142582))
    s1.autoTrimCurve(curve1=g[23], point1=(-0.00712133049583433, 
        0.040649226852417))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.308854, 
        farPlane=0.32865, width=0.0788777, height=0.0357348, cameraPosition=(
        0.0697716, 0.101788, -0.316502), cameraTarget=(0.0697716, 0.101788, 
        0.00225))
    s1.autoTrimCurve(curve1=g[6], point1=(-0.0179233685097694, 0.0335406726083756))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.313286, 
        farPlane=0.324218, width=0.0331699, height=0.0150273, cameraPosition=(
        0.0566369, 0.101115, -0.316502), cameraTarget=(0.0566369, 0.101115, 
        0.00225))
    s1.autoTrimCurve(curve1=g[61], point1=(-0.000916717942714675, 
        0.0455621471486092))
    s1.autoTrimCurve(curve1=g[64], point1=(-0.000807820256710036, 
        0.0457362374148369))
    s1.autoTrimCurve(curve1=g[43], point1=(-4.55439052581622e-05, 
        0.0455621471486092))
    s1.autoTrimCurve(curve1=g[13], point1=(0.00023758560800554, 
        0.0449528237662315))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.301883, 
        farPlane=0.335621, width=0.17064, height=0.077307, cameraPosition=(
        0.0708322, 0.0876671, -0.316502), cameraTarget=(0.0708322, 0.0876671, 
        0.00225))
    s1.autoTrimCurve(curve1=g[5], point1=(-0.00712790935850143, 
        0.0182643821320534))
    s1.autoTrimCurve(curve1=g[54], point1=(0.00138730705165863, 
        0.0127788102111816))
    s1.autoTrimCurve(curve1=g[55], point1=(0.00149934888267517, 
        0.0078529855093956))
    s1.autoTrimCurve(curve1=g[31], point1=(0.00710147023582459, 
        0.0106517439565659))
    s1.autoTrimCurve(curve1=g[67], point1=(0.00598105192565918, 
        0.00751713568782807))
    s1.autoTrimCurve(curve1=g[28], point1=(0.00441245884084702, 
        0.00639763379907608))
    s1.autoTrimCurve(curve1=g[4], point1=(-0.000629445906639096, 
        0.00471837724065781))
    s1.autoTrimCurve(curve1=g[27], point1=(0.00329202562952043, 
        0.0206153383336067))
    s1.autoTrimCurve(curve1=g[26], point1=(-0.00141374617433547, 
        0.0199436386904717))
    s1.autoTrimCurve(curve1=g[25], point1=(-0.00275825559711455, 
        0.0329298889122009))
    s1.autoTrimCurve(curve1=g[24], point1=(0.00329202562952043, 
        0.0364003544530869))
    s1.autoTrimCurve(curve1=g[53], point1=(0.00418836027765275, 
        0.0273323645672798))
    s1.autoTrimCurve(curve1=g[70], point1=(0.0158407628574371, 0.0274443095407486))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.310354, 
        farPlane=0.32715, width=0.0634056, height=0.0287253, cameraPosition=(
        0.045794, 0.0836599, -0.316502), cameraTarget=(0.045794, 0.0836599, 
        0.00225))
    s1.autoTrimCurve(curve1=g[69], point1=(0.0127545312085152, 0.0273038064918518))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314072, 
        farPlane=0.323432, width=0.0250637, height=0.0113549, cameraPosition=(
        0.0343175, 0.0827017, -0.316502), cameraTarget=(0.0343175, 0.0827017, 
        0.00225))
    s1.redo()
    s1.autoTrimCurve(curve1=g[71], point1=(0.0202642172613144, 0.0270382528982163))
    s1.autoTrimCurve(curve1=g[65], point1=(0.0199844479598999, 0.0268573751530647))
    s1.autoTrimCurve(curve1=g[66], point1=(0.0203464977481365, 0.0268409317216873))
    s1.autoTrimCurve(curve1=g[14], point1=(0.0203300431408882, 0.0266107236824036))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.294607, 
        farPlane=0.342897, width=0.255564, height=0.115781, cameraPosition=(
        0.0622494, 0.0861768, -0.316502), cameraTarget=(0.0622494, 0.0861768, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p2 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s1, edges=(e1[139], ))
    s1.Line(point1=(0.0205811843152886, 0.0270466640105573), point2=(
        -0.00147888277828301, 0.00959965253964115))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306082, 
        farPlane=0.331422, width=0.107471, height=0.0486885, cameraPosition=(
        0.0424083, 0.0848539, -0.316502), cameraTarget=(0.0424083, 0.0848539, 
        0.00225))
    s1.autoTrimCurve(curve1=g[42], point1=(0.0233513280787468, 0.0229209652028084))
    s1.autoTrimCurve(curve1=g[30], point1=(0.0198230758347511, 0.0175624256811142))
    s1.autoTrimCurve(curve1=g[73], point1=(-0.00120529755568504, 
        0.00846699530696869))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.301397, 
        farPlane=0.336107, width=0.176306, height=0.0798736, cameraPosition=(
        0.0238096, 0.0773442, -0.316502), cameraTarget=(0.0238096, 0.0773442, 
        0.00225))
    s1.autoTrimCurve(curve1=g[29], point1=(0.0264435984232426, 
        -0.00433043857598305))
    s1.autoTrimCurve(curve1=g[68], point1=(0.0338523812630177, 
        -0.00398343896055222))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306082, 
        farPlane=0.331422, width=0.107471, height=0.0486885, cameraPosition=(
        0.0188273, 0.0669612, -0.316502), cameraTarget=(0.0188273, 0.0669612, 
        0.00225))
    s1.autoTrimCurve(curve1=g[75], point1=(0.0315490622111559, 
        -0.00300955121898652))
    s1.autoTrimCurve(curve1=g[77], point1=(0.0313373688646555, 
        -0.00308005606317521))
    s1.autoTrimCurve(curve1=g[78], point1=(0.0323252785989046, 
        -0.00336208661580086))
    s1.autoTrimCurve(curve1=g[79], point1=(0.0313373688646555, 
        -0.00300955121898652))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31366, 
        farPlane=0.323844, width=0.0293072, height=0.0132773, cameraPosition=(
        0.0116457, 0.054282, -0.316502), cameraTarget=(0.0116457, 0.054282, 
        0.00225))
    s1.autoTrimCurve(curve1=g[72], point1=(0.0379734715484977, 
        -0.00572109689497949))
    s1.autoTrimCurve(curve1=g[76], point1=(0.03822363224262, -0.00560573583030702))
    s1.autoTrimCurve(curve1=g[47], point1=(0.0386854639315009, 
        -0.00625946467304231))
    s1.autoTrimCurve(curve1=g[15], point1=(0.0383775761389136, 
        -0.00647096430444719))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.295752, 
        farPlane=0.341752, width=0.2422, height=0.109726, cameraPosition=(
        0.00761579, 0.0481752, -0.316502), cameraTarget=(0.00761579, 0.0481752, 
        0.00225))
    s1.autoTrimCurve(curve1=g[3], point1=(0.000614890460014332, 
        -0.0354759683974981))
    s1.autoTrimCurve(curve1=g[2], point1=(0.0141322702207565, -0.0548614831783771))
    s1.autoTrimCurve(curve1=g[33], point1=(0.0160406023302078, -0.044533134452343))
    s1.autoTrimCurve(curve1=g[32], point1=(0.00952045023822783, 
        -0.0402428964295387))
    s1.autoTrimCurve(curve1=g[35], point1=(0.0161996349730492, 
        -0.0241942340650558))
    s1.autoTrimCurve(curve1=g[34], point1=(0.0321024373211861, 
        -0.0286433706202507))
    s1.autoTrimCurve(curve1=g[40], point1=(0.030035080019474, -0.0551792802431583))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31142, 
        farPlane=0.326084, width=0.0593208, height=0.0268747, cameraPosition=(
        0.063285, 0.0982031, -0.316502), cameraTarget=(0.063285, 0.0982031, 
        0.00225))
    s1.offset(distance=0.00025, objectList=(g[48], ), side=LEFT)
    s1.offset(distance=0.00025, objectList=(g[48], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314493, 
        farPlane=0.323011, width=0.0207196, height=0.00938679, cameraPosition=(
        0.0746814, 0.0986861, -0.316502), cameraTarget=(0.0746814, 0.0986861, 
        0.00225))
    s1.Line(point1=(-0.034058202983012, 0.0433508617610258), point2=(
        -0.034058202983012, 0.0415113186463714))
    s1.VerticalConstraint(entity=g[82], addUndoState=False)
    s1.Line(point1=(-0.034058202983012, 0.0415113186463714), point2=(
        -0.0344955683685839, 0.0415113186463714))
    s1.HorizontalConstraint(entity=g[83], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[82], entity2=g[83], addUndoState=False)
    s1.Line(point1=(-0.0344955683685839, 0.0415113186463714), point2=(
        -0.0345555990538929, 0.0432998995331283))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315003, 
        farPlane=0.322501, width=0.0154565, height=0.00700243, cameraPosition=(
        0.0767811, 0.109113, -0.316502), cameraTarget=(0.0767811, 0.109113, 
        0.00225))
    s1.Line(point1=(-0.0357650123081601, 0.0551038850644003), point2=(
        -0.0359008189625456, 0.0564293706265744))
    s1.Line(point1=(-0.0359008189625456, 0.0564293706265744), point2=(
        -0.0352137086180164, 0.0564997706065853))
    s1.PerpendicularConstraint(entity1=g[85], entity2=g[86], addUndoState=False)
    s1.Line(point1=(-0.0352137086180164, 0.0564997706065853), point2=(
        -0.0352676162372793, 0.0551548472922978))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280459, 
        farPlane=0.357045, width=0.420702, height=0.190595, cameraPosition=(
        0.0541295, 0.0800995, -0.316502), cameraTarget=(0.0541295, 0.0800995, 
        0.00225))
    s1.setAsConstruction(objectList=(g[48], g[50], g[52], g[56], g[74]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311526, 
        farPlane=0.325978, width=0.0513242, height=0.0232519, cameraPosition=(
        0.0679222, 0.102143, -0.316502), cameraTarget=(0.0679222, 0.102143, 
        0.00225))
    s1.unsetConstruction(objectList=(g[50], ))
    s1.offset(distance=0.00025, objectList=(g[50], ), side=RIGHT)
    s1.offset(distance=0.00025, objectList=(g[50], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315566, 
        farPlane=0.321938, width=0.00965548, height=0.00437432, 
        cameraPosition=(0.0667181, 0.108029, -0.316502), cameraTarget=(
        0.0667181, 0.108029, 0.00225))
    s1.Line(point1=(-0.0199722070339264, 0.05415773824243), point2=(
        -0.0197982702302397, 0.0548923971509794))
    s1.ParallelConstraint(entity1=g[88], entity2=g[90], addUndoState=False)
    s1.Line(point1=(-0.0197982702302397, 0.0548923971509794), point2=(
        -0.018486275252684, 0.0545817710764958))
    s1.PerpendicularConstraint(entity1=g[90], entity2=g[91], addUndoState=False)
    s1.Line(point1=(-0.018486275252684, 0.0545817710764958), point2=(
        -0.0194856577784353, 0.0540425435290917))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315506, 
        farPlane=0.321998, width=0.0102718, height=0.00465354, cameraPosition=(
        0.0669471, 0.108162, -0.316502), cameraTarget=(0.0669471, 0.108162, 
        0.00225))
    s1.dragEntity(entity=v[71], points=((-0.0197982702302397, 0.0548923971509794), 
        (-0.0197982702302397, 0.0548923971509794), (-0.0198143705687523, 
        0.0551582341871262), (-0.0198008775672912, 0.0552525138339997), (
        -0.0197738990149498, 0.055360271581173), (-0.0196997135839462, 
        0.0556565886220932), (-0.0196457564792633, 0.0558451553664208), (
        -0.0196187779269218, 0.056), (-0.0196120351514816, 0.0561145311079025), 
        (-0.0195580780467987, 0.0561751415810585), (-0.0194906353912353, 
        0.0561482077322006), (-0.0194703996143341, 0.0560875972590447), (
        -0.0194501638374328, 0.056), (-0.0194029569587707, 0.0557171990952492), 
        (-0.0193894639573097, 0.0555690368494988), (-0.0194096997342109, 
        0.0554343452534676), (-0.019524356719017, 0.0551582341871262), (
        -0.0196322709283829, 0.0548147773227692), (-0.0197738990149498, 
        0.0544309085092545), (-0.0199559986553192, 0.05425), (
        -0.0199762344322204, 0.05425)))
    s1.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314151, 
        farPlane=0.323353, width=0.024245, height=0.010984, cameraPosition=(
        0.066859, 0.105769, -0.316502), cameraTarget=(0.066859, 0.105769, 
        0.00225))
    s1.dragEntity(entity=v[72], points=((-0.018486275252684, 0.0545817710764958), (
        -0.018486275252684, 0.0545817710764958), (-0.0188145250043869, 
        0.0546535318574906), (-0.019005557890892, 0.0546535318574906), (
        -0.01925, 0.0546376323184967), (-0.01925, 0.0546376323184967), (
        -0.0194990545473099, 0.0547012155733109), (-0.0194512963256836, 
        0.0549237569651604), (-0.01925, 0.0550668230137825), (-0.01925, 
        0.0552257811508179), (-0.0190692305526733, 0.0553052564940453), (
        -0.019021472331047, 0.0554483225426674), (-0.0189737141094208, 0.056), 
        (-0.0189737141094208, 0.056), (-0.0189737141094208, 0.056)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31408, 
        farPlane=0.323424, width=0.0249767, height=0.0113155, cameraPosition=(
        0.0693303, 0.0953722, -0.316502), cameraTarget=(0.0693303, 0.0953722, 
        0.00225))
    s1.Line(point1=(-0.0236171740520585, 0.038762448497201), point2=(
        -0.0269764274320602, 0.0360728641829491))
    s1.Line(point1=(-0.0269764274320602, 0.0360728641829491), point2=(
        -0.0264163815471647, 0.0353733746663352))
    s1.PerpendicularConstraint(entity1=g[93], entity2=g[94], addUndoState=False)
    s1.Line(point1=(-0.0264163815471647, 0.0353733746663352), point2=(
        -0.0231306247965674, 0.0386472537838627))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315986, 
        farPlane=0.321518, width=0.0053178, height=0.00240918, cameraPosition=(
        0.0697583, 0.0937181, -0.316502), cameraTarget=(0.0697583, 0.0937181, 
        0.00225))
    s1.Line(point1=(-0.0231306247965674, 0.0386472537838627), point2=(
        -0.0233646690807342, 0.037784955450058))
    s1.Line(point1=(-0.0233646690807342, 0.037784955450058), point2=(
        -0.0234622943817584, 0.0374252708086971))
    s1.ParallelConstraint(entity1=g[96], entity2=g[97], addUndoState=False)
    s1.Line(point1=(-0.0234622943817584, 0.0374252708086971), point2=(
        -0.0242832046837989, 0.0382291914494878))
    s1.CoincidentConstraint(entity1=v[77], entity2=g[93], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315704, 
        farPlane=0.3218, width=0.00931867, height=0.00422173, cameraPosition=(
        0.0683853, 0.0934401, -0.316502), cameraTarget=(0.0683853, 0.0934401, 
        0.00225))
    s1.Line(point1=(-0.0242832046837989, 0.0382291914494878), point2=(
        -0.023856959026417, 0.0385704647934211))
    s1.CoincidentConstraint(entity1=v[78], entity2=g[93], addUndoState=False)
    s1.Line(point1=(-0.023856959026417, 0.0385704647934211), point2=(
        -0.0236171740520585, 0.038762448497201))
    s1.ParallelConstraint(entity1=g[99], entity2=g[100], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314588, 
        farPlane=0.322916, width=0.0223414, height=0.0101215, cameraPosition=(
        0.0635789, 0.0932635, -0.316502), cameraTarget=(0.0635789, 0.0932635, 
        0.00225))
    s1.autoTrimCurve(curve1=g[94], point1=(-0.0267540574035644, 
        0.0358112817487717))
    s1.autoTrimCurve(curve1=g[93], point1=(-0.0264753460845947, 
        0.0365881165347099))
    s1.autoTrimCurve(curve1=g[95], point1=(-0.0255951866469383, 0.036177708753109))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315697, 
        farPlane=0.321807, width=0.00830149, height=0.00376091, 
        cameraPosition=(0.0678264, 0.0935278, -0.316502), cameraTarget=(
        0.0678264, 0.0935278, 0.00225))
    s1.autoTrimCurve(curve1=g[102], point1=(-0.0234969615898132, 
        0.0383470347008705))
    s1.autoTrimCurve(curve1=g[97], point1=(-0.0234206527433395, 
        0.0375845497331619))
    s1.autoTrimCurve(curve1=g[98], point1=(-0.0236005246601105, 
        0.0375627642354965))
    s1.autoTrimCurve(curve1=g[99], point1=(-0.0240965470633507, 
        0.0384450619897843))
    s1.autoTrimCurve(curve1=g[100], point1=(-0.0237531498036384, 
        0.0386847024641037))
    s1.autoTrimCurve(curve1=g[101], point1=(-0.0239330217204094, 
        0.0385104184827805))
    s1.autoTrimCurve(curve1=g[96], point1=(-0.0232353270015716, 
        0.0383143564543724))
    s1.Line(point1=(-0.0236171740520585, 0.038762448497201), point2=(
        -0.0239216927014354, 0.0374762495232517))
    s1.ParallelConstraint(entity1=g[88], entity2=g[103], addUndoState=False)
    s1.Line(point1=(-0.0239216927014354, 0.0374762495232517), point2=(
        -0.0234077554071916, 0.0373545704565785))
    s1.PerpendicularConstraint(entity1=g[103], entity2=g[104], addUndoState=False)
    s1.Line(point1=(-0.0234077554071916, 0.0373545704565785), point2=(
        -0.0231306247965674, 0.0386472537838627))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315062, 
        farPlane=0.322442, width=0.0148557, height=0.00673025, cameraPosition=(
        0.0620724, 0.107512, -0.316502), cameraTarget=(0.0620724, 0.107512, 
        0.00225))
    s1.setAsConstruction(objectList=(g[50], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.207427, 
        farPlane=0.258533, width=0.0873563, height=0.0379722, projection=1, 
        cameraPosition=(0.0293338, -0.0366759, 0.221812), cameraUpVector=(
        -0.0268837, 0.979979, 0.197277), cameraTarget=(0.0150395, 0.0257895, 
        -0.0904335), viewOffsetX=0.0665987, viewOffsetY=0.0661251)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d1[9], sketchUpEdge=e[179], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s1, depth=0.0015, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.184039, 
        farPlane=0.280521, width=0.331177, height=0.143957, 
        viewOffsetX=0.126306, viewOffsetY=0.0264234)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.185421, 
        farPlane=0.279139, width=0.333664, height=0.145038, cameraPosition=(
        0.0280446, -0.0308794, 0.223031), cameraUpVector=(0.0102976, 0.98061, 
        0.195701), cameraTarget=(0.0137503, 0.031586, -0.0892149), 
        viewOffsetX=0.127254, viewOffsetY=0.0266218)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0683481, 
        farPlane=0.275074, width=0.122992, height=0.0534625, cameraPosition=(
        -0.0783882, -0.061417, 0.0526714), cameraUpVector=(0.181798, 0.366552, 
        0.912463), cameraTarget=(0.077383, 0.184516, -0.0771596), 
        viewOffsetX=0.0469071, viewOffsetY=0.00981307)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.154101, 
        farPlane=0.315643, width=0.277304, height=0.120539, cameraPosition=(
        0.192479, -0.172238, 0.0374384), cameraUpVector=(-0.716556, -0.0779312, 
        0.693163), cameraTarget=(-0.00143793, 0.00497983, -0.143099), 
        viewOffsetX=0.105759, viewOffsetY=0.022125)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.166666, 
        farPlane=0.303078, width=0.0185247, height=0.00805235, 
        viewOffsetX=0.118749, viewOffsetY=0.0263756)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.144851, 
        farPlane=0.280361, width=0.0161, height=0.00699838, cameraPosition=(
        0.0573189, -0.195924, 0.000706025), cameraUpVector=(-0.686687, 
        0.172197, 0.706264), cameraTarget=(-0.0300797, 0.0713288, -0.149431), 
        viewOffsetX=0.103206, viewOffsetY=0.0229233)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.149718, 
        farPlane=0.296336, width=0.0166409, height=0.00723352, cameraPosition=(
        0.141932, -0.188851, 0.00471014), cameraUpVector=(-0.656843, 
        -0.0319932, 0.753348), cameraTarget=(-0.0360276, 0.0317814, -0.141083), 
        viewOffsetX=0.106673, viewOffsetY=0.0236935)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.146886, 
        farPlane=0.29917, width=0.0501334, height=0.0217921, 
        viewOffsetX=0.107342, viewOffsetY=0.0229924)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.146627, 
        farPlane=0.299428, width=0.0500452, height=0.0217538, cameraPosition=(
        0.126148, -0.191823, 0.0194794), cameraUpVector=(-0.585012, 0.0624653, 
        0.808615), cameraTarget=(-0.0518118, 0.0288095, -0.126314), 
        viewOffsetX=0.107153, viewOffsetY=0.022952)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.136609, 
        farPlane=0.287464, width=0.0466261, height=0.0202676, cameraPosition=(
        0.00307646, -0.176508, 0.0785444), cameraUpVector=(-0.0192905, 
        0.398028, 0.91717), cameraTarget=(-0.108374, 0.0965789, -0.0423126), 
        viewOffsetX=0.0998323, viewOffsetY=0.0213839)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.110124, 
        farPlane=0.31395, width=0.357537, height=0.155415, 
        viewOffsetX=0.119444, viewOffsetY=0.053633)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.180001, 
        farPlane=0.367973, width=0.584403, height=0.25403, cameraPosition=(
        0.0791195, -0.150165, 0.239617), cameraUpVector=(-0.0103925, 0.782749, 
        0.622251), cameraTarget=(-0.105783, 0.0098982, 0.0351794), 
        viewOffsetX=0.195234, viewOffsetY=0.0876645)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.189561, 
        farPlane=0.358412, width=0.234353, height=0.101869, 
        viewOffsetX=0.145999, viewOffsetY=0.0242873)
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275516, 
        farPlane=0.361988, width=0.478401, height=0.216735, cameraPosition=(
        0.0522458, 0.0745655, -0.316502), cameraTarget=(0.0522458, 0.0745655, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s2, edges=(e1[91], e1[95], e1[243], e1[247], 
        e1[248], e1[262]), upToFeature=p.features['Cut extrude-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309224, 
        farPlane=0.32828, width=0.0750587, height=0.0340046, cameraPosition=(
        0.028194, 0.0594947, -0.316502), cameraTarget=(0.028194, 0.0594947, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e, p2 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s2, edges=(e[91], e[95], e[243], e[247], 
        e[248], e[262]), upToFeature=p.features['Cut extrude-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311363, 
        farPlane=0.326141, width=0.0530052, height=0.0240135, cameraPosition=(
        0.00995591, 0.05195, -0.316502), cameraTarget=(0.00995591, 0.05195, 
        0.00225))
    s2.setAsConstruction(objectList=(g[17], g[18], g[21], g[20], g[19], g[22]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309749, 
        farPlane=0.327755, width=0.06965, height=0.0315543, cameraPosition=(
        -0.00609403, 0.0441714, -0.316502), cameraTarget=(-0.00609403, 
        0.0441714, 0.00225))
    s2.DistanceDimension(entity1=g[22], entity2=g[8], textPoint=(
        0.0411559581794739, -0.0222739586749077), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316085, 
        farPlane=0.321419, width=0.00430204, height=0.001949, cameraPosition=(
        0.00801234, 0.050468, -0.316502), cameraTarget=(0.00801234, 0.050468, 
        0.00225))
    s2.DistanceDimension(entity1=g[19], entity2=g[9], textPoint=(
        0.0387029746585488, -0.00450436865472795), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316176, 
        farPlane=0.321328, width=0.0033625, height=0.00152335, cameraPosition=(
        0.0256235, 0.0820516, -0.316502), cameraTarget=(0.0256235, 0.0820516, 
        0.00225))
    s2.DistanceDimension(entity1=g[20], entity2=g[10], textPoint=(
        0.0206206642129421, 0.0273715620718002), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315616, 
        farPlane=0.321888, width=0.00914, height=0.00414079, cameraPosition=(
        0.0461979, 0.100317, -0.316502), cameraTarget=(0.0461979, 0.100317, 
        0.00225))
    s2.DistanceDimension(entity1=g[21], entity2=g[11], textPoint=(
        -0.000591149922370894, 0.0468698507032394), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314058, 
        farPlane=0.323446, width=0.025208, height=0.0114203, cameraPosition=(
        0.0612239, 0.105878, -0.316502), cameraTarget=(0.0612239, 0.105878, 
        0.00225))
    s2.DistanceDimension(entity1=g[18], entity2=g[12], textPoint=(
        -0.0217098653278351, 0.05530531609869), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312149, 
        farPlane=0.325356, width=0.0449007, height=0.0203418, cameraPosition=(
        0.0720446, 0.104674, -0.316502), cameraTarget=(0.0720446, 0.104674, 
        0.00225))
    s2.DistanceDimension(entity1=g[17], entity2=g[13], textPoint=(
        -0.0388143271169662, 0.0566299473724365), value=0.0001)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312886, 
        farPlane=0.324618, width=0.0372939, height=0.0168956, cameraPosition=(
        0.0782692, 0.105257, -0.316502), cameraTarget=(0.0782692, 0.105257, 
        0.00225))
    s2.dragEntity(entity=v[13], points=((-0.0464263318114671, 0.0520123064450737), 
        (-0.0464263318114671, 0.0520123064450737), (-0.0468522369823456, 
        0.051803207942009), (-0.04725, 0.0516076003990174), (-0.04725, 
        0.0514853438220024), (-0.04725, 0.0514853438220024), (
        -0.0477092921695709, 0.0514364456615448), (-0.0478807002267837, 
        0.0513875400505066)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.29466, 
        farPlane=0.342844, width=0.22527, height=0.102056, cameraPosition=(
        -0.0160799, 0.0199561, -0.316502), cameraTarget=(-0.0160799, 0.0199561, 
        0.00225))
    s2.dragEntity(entity=v[15], points=((0.0468914532736649, -0.0594333613247998), 
        (0.04725, -0.0595), (0.0455, -0.06125), (0.0455, -0.06475), (0.0455, 
        -0.0665), (0.04725, -0.06825), (0.04725, -0.06825), (0.0455, -0.06825), 
        (0.04725, -0.07), (0.04725, -0.06825), (0.04725, -0.0665), (0.0455, 
        -0.06475), (0.0455, -0.063), (0.0455, -0.063), (0.04725, -0.06125), (
        0.04725, -0.05775), (0.0455, -0.056), (0.0455, -0.05775), (0.0455, 
        -0.0595), (0.04725, -0.06125), (0.04725, -0.063), (0.0455, -0.06475), (
        0.0455, -0.0665), (0.04725, -0.0665), (0.0455, -0.06825), (0.04725, 
        -0.0665), (0.04725, -0.06475), (0.04725, -0.063), (0.04725, -0.06475), 
        (0.04725, -0.06475)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311555, 
        farPlane=0.325949, width=0.0510236, height=0.0231157, cameraPosition=(
        -0.00299716, 0.00156069, -0.316502), cameraTarget=(-0.00299716, 
        0.00156069, 0.00225))
    s2.dragEntity(entity=v[15], points=((0.04725, -0.06475), (0.04725, -0.06475), (
        0.0467852194366008, -0.0643567731746435), (0.0466177098956853, 
        -0.0640222476937771), (0.0465172015634328, -0.063), (
        0.0465172015634328, -0.063), (0.0468187209722549, -0.063), (
        0.0468187209722549, -0.063), (0.0468522243705541, -0.063)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275784, 
        farPlane=0.36172, width=0.475271, height=0.215317, cameraPosition=(
        -0.0258158, 0.0425008, -0.316502), cameraTarget=(-0.0258158, 0.0425008, 
        0.00225))
    s2.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-1'].setValues(sketch=s2)
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209077, 
        farPlane=0.338897, width=0.0315337, height=0.0137071, 
        viewOffsetX=0.143827, viewOffsetY=0.0295589)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25152, 
        farPlane=0.337918, width=0.0379351, height=0.0164897, cameraPosition=(
        0.146589, 0.310126, 0.242038), cameraUpVector=(0.804603, 0.17049, 
        -0.568813), cameraTarget=(-0.0269402, 0.255687, -0.0197403), 
        viewOffsetX=0.173024, viewOffsetY=0.0355594)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.248056, 
        farPlane=0.341382, width=0.0738945, height=0.0321206, 
        viewOffsetX=0.179419, viewOffsetY=0.0325216)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247672, 
        farPlane=0.341765, width=0.0737801, height=0.0320709, cameraPosition=(
        0.145848, 0.309787, 0.2426), cameraUpVector=(0.803511, 0.174921, 
        -0.569011), cameraTarget=(-0.0276809, 0.255348, -0.0191787), 
        viewOffsetX=0.179141, viewOffsetY=0.0324713)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.247672)
    session.viewports['Viewport: 1'].view.setValues(farPlane=0.341766, 
        cameraPosition=(0.144424, 0.309121, 0.243682), cameraUpVector=(
        0.801358, 0.183456, -0.569359), cameraTarget=(-0.0291046, 0.254682, 
        -0.0180964))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222944, 
        farPlane=0.372518, width=0.0664138, height=0.0288689, cameraPosition=(
        0.264194, -0.233577, 0.084061), cameraUpVector=(0.6045, 0.292934, 
        -0.74079), cameraTarget=(0.205134, 0.0711938, 0.156383), 
        viewOffsetX=0.161255, viewOffsetY=0.0292293)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.225169, 
        farPlane=0.370292, width=0.0464635, height=0.0201969, 
        viewOffsetX=0.142631, viewOffsetY=0.0305509)
    p = mdb.models['Model-1'].parts['Spiral']
    p.deleteFeatures(('Cut extrude-2', 'Cut extrude-3', ))
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s1 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-1'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222356, 
        farPlane=0.373105, width=0.0851871, height=0.0370294, 
        viewOffsetX=0.152166, viewOffsetY=0.0338671)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e1[215], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.294311, 
        farPlane=0.343193, width=0.228869, height=0.103687, cameraPosition=(
        0.0431775, 0.0467849, -0.316502), cameraTarget=(0.0431775, 0.0467849, 
        0.00225))
    s.CircleByCenterPerimeter(center=(0.0135817032219366, 0.012446832539762), 
        point1=(0.0175, 0.007))
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d1[9], sketchUpEdge=e[215], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s, flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.217781, 
        farPlane=0.37768, width=0.123004, height=0.0534679, 
        viewOffsetX=0.17752, viewOffsetY=0.0202461)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-2'].setValues(flipExtrudeDirection=True)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    s1 = p.features['Cut extrude-2'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-2'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Cut extrude-2']
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d2[9], sketchUpEdge=e1[221], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.CircleByCenterPerimeter(center=(-0.014, 0.0175), point1=(-0.0260173434133103, 
        0.0195996280037285))
    s.CoincidentConstraint(entity1=v[39], entity2=g[14], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.207375, 
        farPlane=0.39207, width=0.23134, height=0.10056, viewOffsetX=0.215479, 
        viewOffsetY=0.0169006)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.211705, 
        farPlane=0.383756, width=0.208681, height=0.0907098, 
        viewOffsetX=0.197832, viewOffsetY=0.0126609)
    p = mdb.models['Model-1'].parts['Spiral']
    e, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[9], sketchUpEdge=e[205], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.046954, 
        0.055129, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.292837, 
        farPlane=0.344667, width=0.244076, height=0.110576, cameraPosition=(
        0.0602657, 0.0415376, -0.316502), cameraTarget=(0.0602657, 0.0415376, 
        0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s1, edges=(e1[0], e1[1], e1[2], e1[3], e1[4], 
        e1[5], e1[6], e1[7], e1[8], e1[9], e1[10], e1[11], e1[12], e1[13], 
        e1[14], e1[15], e1[16], e1[17], e1[18], e1[19], e1[20], e1[21], e1[22], 
        e1[23], e1[24], e1[25], e1[26], e1[27], e1[28], e1[29], e1[30], e1[31], 
        e1[32], e1[33], e1[34], e1[35], e1[36], e1[37], e1[38], e1[39], e1[40], 
        e1[41], e1[42], e1[43], e1[44], e1[45], e1[46], e1[47], e1[48], e1[49], 
        e1[50], e1[51], e1[52], e1[53], e1[54], e1[55], e1[56], e1[57], e1[58], 
        e1[59], e1[60], e1[61], e1[62], e1[63], e1[64], e1[65], e1[66], e1[67], 
        e1[68], e1[69], e1[70], e1[71], e1[72], e1[73], e1[74], e1[75], e1[76], 
        e1[77], e1[78], e1[79], e1[80], e1[81], e1[82], e1[83], e1[84], e1[85], 
        e1[86], e1[87], e1[88], e1[89], e1[90], e1[91], e1[92], e1[93], e1[94], 
        e1[95], e1[96], e1[97], e1[98], e1[99], e1[100], e1[101], e1[102], 
        e1[103], e1[104], e1[105], e1[106], e1[107], e1[108], e1[109], e1[110], 
        e1[111], e1[112], e1[113], e1[114], e1[115], e1[116], e1[117], e1[118], 
        e1[119], e1[120], e1[121], e1[122], e1[123], e1[124], e1[125], e1[126], 
        e1[127], e1[128], e1[129], e1[130], e1[131], e1[132], e1[133], e1[134], 
        e1[135], e1[136], e1[137], e1[138], e1[139], e1[140], e1[141], e1[142], 
        e1[143], e1[144], e1[145], e1[146], e1[147], e1[148], e1[149], e1[150], 
        e1[151], e1[152], e1[153], e1[154], e1[155], e1[156], e1[157], e1[158], 
        e1[159], e1[160], e1[161], e1[162], e1[163], e1[164], e1[165], e1[166], 
        e1[167], e1[168], e1[169], e1[170], e1[171], e1[172], e1[173], e1[174], 
        e1[175], e1[176], e1[177], e1[178], e1[179], e1[180], e1[181], e1[182], 
        e1[183], e1[184], e1[185], e1[186], e1[187], e1[188], e1[189], e1[190], 
        e1[191], e1[192], e1[193], e1[194], e1[195], e1[196], e1[197], e1[198], 
        e1[199], e1[200], e1[201], e1[202], e1[203], e1[204], e1[205], e1[206], 
        e1[207], e1[208], e1[209], e1[210], e1[211], e1[212], e1[213], e1[214], 
        e1[215], e1[216], e1[217], e1[218], e1[219], e1[220], e1[221], e1[222], 
        e1[223], e1[224], e1[225], e1[226], e1[227]))
    s1.autoTrimCurve(curve1=g[74], point1=(-0.0467463722310066, 
        -0.0415743276438713))
    s1.autoTrimCurve(curve1=g[75], point1=(-0.048509231754303, 
        -0.0425351023635864))
    s1.autoTrimCurve(curve1=g[76], point1=(-0.0505926078042984, 
        -0.0402933046183586))
    s1.autoTrimCurve(curve1=g[77], point1=(-0.0505926078042984, 
        -0.0364502280912399))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.308236, 
        farPlane=0.329268, width=0.0852507, height=0.038622, cameraPosition=(
        0.0775137, 0.0838799, -0.316502), cameraTarget=(0.0775137, 0.0838799, 
        0.00225))
    s1.autoTrimCurve(curve1=g[55], point1=(-0.0490420078716278, 
        -0.0326570555529594))
    s1.autoTrimCurve(curve1=g[56], point1=(-0.0515609076104164, 
        -0.0294131398162842))
    s1.autoTrimCurve(curve1=g[57], point1=(-0.0473067751011848, 
        -0.0264488667211533))
    s1.autoTrimCurve(curve1=g[54], point1=(-0.0430526351413727, 
        -0.0295250028333664))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.304471, 
        farPlane=0.333033, width=0.140426, height=0.0636187, cameraPosition=(
        0.0788703, 0.0729933, -0.316502), cameraTarget=(0.0788703, 0.0729933, 
        0.00225))
    s1.autoTrimCurve(curve1=g[60], point1=(-0.0443728780231476, 
        -0.0142737314066887))
    s1.autoTrimCurve(curve1=g[59], point1=(-0.046216956325531, 
        -0.0228416383228302))
    s1.autoTrimCurve(curve1=g[58], point1=(-0.0377342169961929, 
        -0.018511621650219))
    s1.autoTrimCurve(curve1=g[61], point1=(-0.0394860869131088, 
        -0.00985158457970619))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289278, 
        farPlane=0.348226, width=0.280777, height=0.127203, cameraPosition=(
        0.0956075, 0.0401705, -0.316502), cameraTarget=(0.0956075, 0.0401705, 
        0.00225))
    s1.autoTrimCurve(curve1=g[65], point1=(-0.0279045915088654, 
        0.00412167013072968))
    s1.autoTrimCurve(curve1=g[62], point1=(-0.0185023611268997, 
        -0.00122032165145874))
    s1.autoTrimCurve(curve1=g[63], point1=(-0.0341727500638962, 
        -0.00250976383304596))
    s1.autoTrimCurve(curve1=g[64], point1=(-0.0306699490032196, 
        0.00375326127195359))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.296441, 
        farPlane=0.341063, width=0.206906, height=0.0937368, cameraPosition=(
        0.0526697, 0.0161965, -0.316502), cameraTarget=(0.0526697, 0.0161965, 
        0.00225))
    s1.autoTrimCurve(curve1=g[70], point1=(0.0241922820129395, 0.0277449168303013))
    s1.autoTrimCurve(curve1=g[66], point1=(0.0020480314412117, 0.0215007342436314))
    s1.autoTrimCurve(curve1=g[68], point1=(0.00625950937652588, 
        0.00249673575544358))
    s1.autoTrimCurve(curve1=g[67], point1=(0.00394999330425262, 
        0.0103698201515675))
    s1.autoTrimCurve(curve1=g[69], point1=(-0.0123525252423286, 
        0.00765496269249916))
    s1.autoTrimCurve(curve1=g[73], point1=(0.0190298194208145, 0.0175641976335049))
    s1.autoTrimCurve(curve1=g[72], point1=(0.0368267307200432, 
        0.00629753768825531))
    s1.autoTrimCurve(curve1=g[71], point1=(0.0347889149703979, 0.0220437102057934))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315658, 
        farPlane=0.321846, width=0.00870862, height=0.00394536, 
        cameraPosition=(0.0930798, 0.10387, -0.316502), cameraTarget=(
        0.0930798, 0.10387, 0.00225))
    s1.autoTrimCurve(curve1=g[83], point1=(-0.0523294275484085, 
        -0.0461229070982933))
    s1.autoTrimCurve(curve1=g[78], point1=(-0.051957755335331, 
        -0.0469513446054459))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.313531, 
        farPlane=0.323973, width=0.0306378, height=0.0138802, cameraPosition=(
        0.0835564, 0.0971887, -0.316502), cameraTarget=(0.0835564, 0.0971887, 
        0.00225))
    s1.autoTrimCurve(curve1=g[82], point1=(-0.0551858832917213, 
        -0.0350044429264069))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315129, 
        farPlane=0.322375, width=0.0141613, height=0.00641566, cameraPosition=(
        0.0489779, 0.0956377, -0.316502), cameraTarget=(0.0489779, 0.0956377, 
        0.00225))
    s1.autoTrimCurve(curve1=g[80], point1=(-0.0458320295295715, 
        -0.000179743762969968))
    s1.autoTrimCurve(curve1=g[81], point1=(-0.0459715043983459, 
        -0.000439884509801862))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315447, 
        farPlane=0.322057, width=0.0108767, height=0.00492759, cameraPosition=(
        0.0102814, 0.0456035, -0.316502), cameraTarget=(0.0102814, 0.0456035, 
        0.00225))
    s1.autoTrimCurve(curve1=g[79], point1=(0.00572970604085922, 
        0.0386099578850865))
    s1.autoTrimCurve(curve1=g[85], point1=(0.00593681355500221, 
        0.0386099578850865))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315867, 
        farPlane=0.321637, width=0.00654902, height=0.00296697, 
        cameraPosition=(0.0011521, -0.000222049, -0.316502), cameraTarget=(
        0.0011521, -0.000222049, 0.00225))
    s1.autoTrimCurve(curve1=g[84], point1=(0.0551338954243539, 0.0469297437035441))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306383, 
        farPlane=0.331121, width=0.104365, height=0.0472816, cameraPosition=(
        0.0818617, 0.0734005, -0.316502), cameraTarget=(0.0818617, 0.0734005, 
        0.00225))
    s1.autoTrimCurve(curve1=g[41], point1=(-0.0502388393363953, 
        -0.0465133324227333))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316121, 
        farPlane=0.321383, width=0.00392945, height=0.0017802, cameraPosition=(
        0.0901977, 0.0989139, -0.316502), cameraTarget=(0.0901977, 0.0989139, 
        0.00225))
    s1.autoTrimCurve(curve1=g[86], point1=(-0.0442764302573204, 
        -0.0433506429157257))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.300697, 
        farPlane=0.336807, width=0.163006, height=0.0738484, cameraPosition=(
        0.0362842, 0.00164869, -0.316502), cameraTarget=(0.0362842, 0.00164869, 
        0.00225))
    s1.autoTrimCurve(curve1=g[48], point1=(0.0548181919290647, 0.0183161698319912))
    s1.autoTrimCurve(curve1=g[87], point1=(0.0550322471096143, 0.0174606345632076))
    s1.Line(point1=(0.055129, 0.0468525827063729), point2=(0.055129, -0.003046))
    s1.VerticalConstraint(entity=g[88], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306253, 
        farPlane=0.331251, width=0.105706, height=0.0478891, cameraPosition=(
        0.0767109, 0.0820312, -0.316502), cameraTarget=(0.0767109, 0.0820312, 
        0.00225))
    s1.Line(point1=(0.055129, -0.003046), point2=(-0.0439060516870957, 
        -0.0431899848258994))
    s1.Line(point1=(-0.0439060516870957, -0.0431899848258994), point2=(
        -0.0518784522011478, -0.0469109648040314))
    s1.autoTrimCurve(curve1=g[89], point1=(-0.0333222960910797, 
        -0.0388763904533386))
    p = mdb.models['Model-1'].parts['Spiral']
    e, d2 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d2[9], sketchUpEdge=e[205], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s1, depth=0.0001, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.227598, 
        farPlane=0.367864, width=0.0213686, height=0.00928857, 
        viewOffsetX=0.204447, viewOffsetY=0.000846529)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-2'].setValues(depth=0.00025)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209079, 
        farPlane=0.386382, width=0.239025, height=0.1039, viewOffsetX=0.213172, 
        viewOffsetY=0.00558869)
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255751, 
        farPlane=0.381753, width=0.0243425, height=0.0105813, 
        viewOffsetX=0.00259201, viewOffsetY=0.00028371)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-2'].setValues(flipExtrudeDirection=True)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250957, 
        farPlane=0.386547, width=0.0833509, height=0.0362312, 
        viewOffsetX=0.028024, viewOffsetY=0.00158027)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255031, 
        farPlane=0.382473, width=0.035912, height=0.0156103, 
        viewOffsetX=0.0090453, viewOffsetY=-0.00103179)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254367, 
        farPlane=0.383138, width=0.0436558, height=0.0189764, 
        viewOffsetX=0.00621722, viewOffsetY=-0.00221955)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.255087, 
        farPlane=0.382418, width=0.0353156, height=0.0153511, 
        viewOffsetX=-0.0318112, viewOffsetY=-0.00125397)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.246183, 
        farPlane=0.383451, width=0.0340829, height=0.0148152, cameraPosition=(
        0.0777396, -0.257847, 0.0166931), cameraUpVector=(-0.014802, 0.0427594, 
        0.998976), cameraTarget=(0.0467379, 0.0590842, 0.00266811), 
        viewOffsetX=-0.0307009, viewOffsetY=-0.0012102)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.215666, 
        farPlane=0.38375, width=0.0806839, height=0.0350719, cameraPosition=(
        0.180951, -0.212371, 0.0207411), cameraUpVector=(-0.0103765, 0.080629, 
        0.99669), cameraTarget=(0.0412546, 0.0730856, -0.00380574), 
        viewOffsetX=-0.025866, viewOffsetY=-0.000865004)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.215373, 
        farPlane=0.382394, width=0.0805743, height=0.0350242, cameraPosition=(
        0.180141, -0.206423, 0.0588843), cameraUpVector=(-0.0755114, 0.189131, 
        0.979044), cameraTarget=(0.0411495, 0.0730364, -0.00582146), 
        viewOffsetX=-0.0258309, viewOffsetY=-0.000863829)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.214346, 
        farPlane=0.38342, width=0.0867631, height=0.0377144, 
        viewOffsetX=-0.00277448, viewOffsetY=0.00192577)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[9], sketchUpEdge=e1[179], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.046954, 
        0.055129, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286263, 
        farPlane=0.351241, width=0.352958, height=0.159904, cameraPosition=(
        0.0484759, -0.00336643, -0.316502), cameraTarget=(0.0484759, 
        -0.00336643, 0.00225))
    p = mdb.models['Model-1'].parts['Spiral']
    e, p2 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s, edges=(e[0], e[1], e[2], e[3], e[4], e[5], 
        e[6], e[7], e[8], e[9], e[10], e[11], e[12], e[13], e[14], e[15], 
        e[16], e[17], e[18], e[19], e[20], e[21], e[22], e[23], e[24], e[25], 
        e[26], e[27], e[28], e[29], e[30], e[31], e[32], e[33], e[34], e[35], 
        e[36], e[37], e[38], e[39], e[40], e[41], e[42], e[43], e[44], e[45], 
        e[46], e[47], e[48], e[49], e[50], e[51], e[52], e[53], e[54], e[55], 
        e[56], e[57], e[58], e[59], e[60], e[61], e[62], e[63], e[64], e[65], 
        e[66], e[67], e[68], e[69], e[70], e[71], e[72], e[73], e[74], e[75], 
        e[76], e[77], e[78], e[79], e[80], e[81], e[82], e[83], e[84], e[85], 
        e[86], e[87], e[88], e[89], e[90], e[91], e[92], e[93], e[94], e[95], 
        e[96], e[97], e[98], e[99], e[100], e[101], e[102], e[103], e[104], 
        e[105], e[106], e[107], e[108], e[109], e[110], e[111], e[112], e[113], 
        e[114], e[115], e[116], e[117], e[118], e[119], e[120], e[121], e[122], 
        e[123], e[124], e[125], e[126], e[127], e[128], e[129], e[130], e[131], 
        e[132], e[133], e[134], e[135], e[136], e[137], e[138], e[139], e[140], 
        e[141], e[142], e[143], e[144], e[145], e[146], e[147], e[148], e[149], 
        e[150], e[151], e[152], e[153], e[154], e[155], e[156], e[157], e[158], 
        e[159], e[160], e[161], e[162], e[163], e[164], e[165], e[166], e[167], 
        e[168], e[169], e[170], e[171], e[172], e[173], e[174], e[175], e[176], 
        e[177], e[178], e[179], e[180], e[181], e[182], e[183], e[184], e[185], 
        e[186], e[187], e[188], e[189], e[190], e[191], e[192], e[193], e[194], 
        e[195], e[196], e[197], e[198], e[199], e[200], e[201], e[202], e[203], 
        e[204], e[205], e[206], e[207], e[208], e[209], e[210], e[211], e[212], 
        e[213], e[214], e[215], e[216], e[217], e[218], e[219], e[220], e[221], 
        e[222], e[223], e[224], e[225], e[226], e[227], e[228], e[229], e[230], 
        e[231], e[232], e[233], e[234]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.292893, 
        farPlane=0.344611, width=0.243495, height=0.110313, cameraPosition=(
        0.0590231, 0.0265795, -0.316502), cameraTarget=(0.0590231, 0.0265795, 
        0.00225))
    s.Line(point1=(-0.0550284794411846, -0.0355059687185598), point2=(
        -0.0433253806470771, -0.0343069010184524))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.30717, 
        farPlane=0.330335, width=0.0962516, height=0.0436058, cameraPosition=(
        0.0762985, 0.0739043, -0.316502), cameraTarget=(0.0762985, 0.0739043, 
        0.00225))
    s.autoTrimCurve(curve1=g[19], point1=(-0.0486366366825104, 
        -0.0367011412940025))
    s.autoTrimCurve(curve1=g[16], point1=(-0.0520493602237702, 
        -0.0395427480301857))
    s.autoTrimCurve(curve1=g[17], point1=(-0.0485734408578873, 
        -0.0427632391414642))
    s.autoTrimCurve(curve1=g[18], point1=(-0.0458558937392235, 
        -0.0404268041214943))
    s.autoTrimCurve(curve1=g[2], point1=(-0.0534397354207039, -0.0409319832882881))
    s.autoTrimCurve(curve1=g[14], point1=(-0.0435807471952439, 
        -0.0404268041214943))
    s.autoTrimCurve(curve1=g[15], point1=(-0.0450975140414238, 
        -0.0439630284867287))
    s.autoTrimCurve(curve1=g[46], point1=(-0.0533133363208771, 
        -0.0416897445878982))
    s.autoTrimCurve(curve1=g[41], point1=(-0.0499006127796173, 
        -0.0458574354610443))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.297489, 
        farPlane=0.340015, width=0.196098, height=0.0888401, cameraPosition=(
        0.0518691, 0.0450956, -0.316502), cameraTarget=(0.0518691, 0.0450956, 
        0.00225))
    s.autoTrimCurve(curve1=g[39], point1=(-0.0474568148932457, 
        -0.0253064021430015))
    s.autoTrimCurve(curve1=g[36], point1=(-0.0513195386013985, 
        -0.0271075278482437))
    s.autoTrimCurve(curve1=g[37], point1=(-0.0499032055816651, 
        -0.0318676516375542))
    s.autoTrimCurve(curve1=g[38], point1=(-0.0441091200194359, 
        -0.0291659593544006))
    s.autoTrimCurve(curve1=g[33], point1=(-0.0446241563043595, 
        -0.0215755015573501))
    s.autoTrimCurve(curve1=g[32], point1=(-0.0469417860589027, 
        -0.0157861620149612))
    s.autoTrimCurve(curve1=g[35], point1=(-0.0393450921258926, 
        -0.0102541319987774))
    s.autoTrimCurve(curve1=g[34], point1=(-0.035739890285492, -0.0163007736167908))
    s.autoTrimCurve(curve1=g[29], point1=(-0.034452310749054, 
        -0.00369288995480536))
    s.autoTrimCurve(curve1=g[31], point1=(-0.0274994065842629, 
        0.00634195804977418))
    s.autoTrimCurve(curve1=g[28], point1=(-0.0295595293722153, 
        0.00351161659145356))
    s.autoTrimCurve(curve1=g[30], point1=(-0.0204177489361763, 
        -0.00382153912997245))
    s.autoTrimCurve(curve1=g[27], point1=(-0.0210615387043953, 
        0.00981556028509141))
    s.autoTrimCurve(curve1=g[26], point1=(-0.0112759685001373, 0.0202363595404625))
    s.autoTrimCurve(curve1=g[25], point1=(-0.00316425318336486, 
        0.0212655827441216))
    s.autoTrimCurve(curve1=g[24], point1=(0.0036598974981308, 0.0038975715675354))
    s.autoTrimCurve(curve1=g[23], point1=(0.0160206118741036, 0.0174060180821419))
    s.autoTrimCurve(curve1=g[21], point1=(0.0362355271496773, 0.0121312975921631))
    s.autoTrimCurve(curve1=g[20], point1=(0.0304414415874481, 0.00775712877893447))
    s.autoTrimCurve(curve1=g[22], point1=(0.0269649932303429, 0.0276981756129265))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.297489, 
        farPlane=0.340015, width=0.196098, height=0.0888401, cameraPosition=(
        0.0468435, 0.0383168, -0.316502), cameraTarget=(0.0468435, 0.0383168, 
        0.00225))
    s.autoTrimCurve(curve1=g[8], point1=(0.0556326108195782, 0.0108529716768265))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.296109, 
        farPlane=0.341395, width=0.210325, height=0.0952856, cameraPosition=(
        0.0439848, 0.0445707, -0.316502), cameraTarget=(0.0439848, 0.0445707, 
        0.00225))
    s.autoTrimCurve(curve1=g[3], point1=(-0.05483163798666, -0.0270427226982116))
    s.autoTrimCurve(curve1=g[13], point1=(-0.0414360230646134, 
        -0.0303543865642548))
    s.Line(point1=(-0.0540014512844366, -0.0197522889216965), point2=(
        -0.0387048511405319, -0.0233738994243129))
    s.Line(point1=(-0.0387048511405319, -0.0233738994243129), point2=(
        -0.0458062832677608, -0.000351609085874033))
    s.Line(point1=(-0.0458062832677608, -0.000351609085874033), point2=(
        -0.028099072955139, -0.01162801235993))
    s.Line(point1=(-0.028099072955139, -0.01162801235993), point2=(
        -0.0270466640105573, 0.0205811843152886))
    s.Line(point1=(-0.0270466640105573, 0.0205811843152886), point2=(
        -0.00959965253964115, -0.00147888277828301))
    s.Line(point1=(-0.00959965253964115, -0.00147888277828301), point2=(
        0.00582774356550126, 0.0386241672297821))
    s.Line(point1=(0.00582774356550126, 0.0386241672297821), point2=(
        0.0181418117651448, 0.00320327466191974))
    s.autoTrimCurve(curve1=g[4], point1=(-0.0508267646512985, -0.0140720553658008))
    s.autoTrimCurve(curve1=g[12], point1=(-0.033564380355835, -0.0171077460012436))
    s.autoTrimCurve(curve1=g[50], point1=(-0.0406074290952683, 
        -0.0162798300347328))
    s.autoTrimCurve(curve1=g[45], point1=(-0.0544173410019875, 
        -0.0259388372263908))
    s.autoTrimCurve(curve1=g[44], point1=(-0.050136274643898, -0.0122782386801243))
    s.autoTrimCurve(curve1=g[5], point1=(-0.0404693400344849, 0.00634984821462633))
    s.autoTrimCurve(curve1=g[52], point1=(-0.0281785195550919, 
        0.00124437511348725))
    s.autoTrimCurve(curve1=g[11], point1=(-0.0182353844723702, 
        -0.0066208191177845))
    s.autoTrimCurve(curve1=g[10], point1=(-0.000144406207561495, 
        0.000554443899631503))
    s.autoTrimCurve(curve1=g[54], point1=(-0.00580646748161316, 
        0.00897157714152336))
    s.autoTrimCurve(curve1=g[6], point1=(-0.0139543181142807, 0.0270477213003635))
    s.autoTrimCurve(curve1=g[7], point1=(0.0125607038059235, 0.0391904763915539))
    s.autoTrimCurve(curve1=g[40], point1=(0.0555095160522461, 0.0331190951206684))
    s.autoTrimCurve(curve1=g[9], point1=(0.0334136719026566, 0.000554443899631489))
    s.autoTrimCurve(curve1=g[47], point1=(0.0222276458659172, 0.0416742242910862))
    s.autoTrimCurve(curve1=g[42], point1=(-0.00939704383230208, 
        0.0313252858855724))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286821, 
        farPlane=0.350683, width=0.34645, height=0.156956, cameraPosition=(
        0.062388, 0.0225544, -0.316502), cameraTarget=(0.062388, 0.0225544, 
        0.00225))
    s.autoTrimCurve(curve1=g[43], point1=(-0.0325980698547363, 0.0142276041247845))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.310537, 
        farPlane=0.326967, width=0.0615168, height=0.0278696, cameraPosition=(
        0.0735186, 0.0865825, -0.316502), cameraTarget=(0.0735186, 0.0865825, 
        0.00225))
    s.offset(distance=5e-05, objectList=(g[48], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315146, 
        farPlane=0.322359, width=0.0139906, height=0.00633829, cameraPosition=(
        0.0806026, 0.10432, -0.316502), cameraTarget=(0.0806026, 0.10432, 
        0.00225))
    s.offset(distance=5e-05, objectList=(g[48], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315887, 
        farPlane=0.321617, width=0.00633968, height=0.00287213, 
        cameraPosition=(0.0817294, 0.10807, -0.316502), cameraTarget=(
        0.0817294, 0.10807, 0.00225))
    s.Line(point1=(-0.0550335756265558, -0.0354562291076379), point2=(
        -0.0555358864658047, -0.0355076945106703))
    s.Line(point1=(-0.0555358864658047, -0.0355076945106703), point2=(
        -0.055524906883889, -0.0356148570447559))
    s.PerpendicularConstraint(entity1=g[62], entity2=g[63], addUndoState=False)
    s.Line(point1=(-0.055524906883889, -0.0356148570447559), point2=(
        -0.0550233832558133, -0.0355557083294817))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316283, 
        farPlane=0.321221, width=0.00226129, height=0.00102446, 
        cameraPosition=(0.0811657, 0.0985739, -0.316502), cameraTarget=(
        0.0811657, 0.0985739, 0.00225))
    s.Line(point1=(-0.0433304768324483, -0.0342571614075305), point2=(
        -0.0427454574971762, -0.0341972219162017))
    s.ParallelConstraint(entity1=g[60], entity2=g[65], addUndoState=False)
    s.Line(point1=(-0.0427454574971762, -0.0341972219162017), point2=(
        -0.0427349260941803, -0.0343000101488542))
    s.PerpendicularConstraint(entity1=g[65], entity2=g[66], addUndoState=False)
    s.Line(point1=(-0.0427349260941803, -0.0343000101488542), point2=(
        -0.0433202844617059, -0.0343566406293743))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315695, 
        farPlane=0.321809, width=0.00942301, height=0.004269, cameraPosition=(
        0.080835, 0.0982239, -0.316502), cameraTarget=(0.080835, 0.0982239, 
        0.00225))
    s.autoTrimCurve(curve1=g[48], point1=(-0.0465442603311539, 
        -0.0346259832344055))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314559, 
        farPlane=0.322945, width=0.0200435, height=0.00908053, cameraPosition=(
        0.0800012, 0.0986079, -0.316502), cameraTarget=(0.0800012, 0.0986079, 
        0.00225))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31611, 
        farPlane=0.321394, width=0.00404431, height=0.00183224, 
        cameraPosition=(0.0811548, 0.0999797, -0.316502), cameraTarget=(
        0.0811548, 0.0999797, 0.00225))
    s.setAsConstruction(objectList=(g[48], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315036, 
        farPlane=0.322468, width=0.0151195, height=0.00684973, cameraPosition=(
        0.0682425, 0.0990108, -0.316502), cameraTarget=(0.0682425, 0.0990108, 
        0.00225))
    s.offset(distance=5e-05, objectList=(g[49], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316385, 
        farPlane=0.321119, width=0.00120594, height=0.000546338, 
        cameraPosition=(0.0702493, 0.0943586, -0.316502), cameraTarget=(
        0.0702493, 0.0943586, 0.00225))
    s.offset(distance=5e-05, objectList=(g[49], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316204, 
        farPlane=0.3213, width=0.00348095, height=0.00157701, cameraPosition=(
        0.0700831, 0.0941213, -0.316502), cameraTarget=(0.0700831, 0.0941213, 
        0.00225))
    s.Line(point1=(-0.0386933316418049, -0.0233252445052494), point2=(
        -0.0383348505090453, -0.0234101182041968))
    s.ParallelConstraint(entity1=g[69], entity2=g[70], addUndoState=False)
    s.Line(point1=(-0.0383348505090453, -0.0234101182041968), point2=(
        -0.038361652041603, -0.023523319865852))
    s.PerpendicularConstraint(entity1=g[70], entity2=g[71], addUndoState=False)
    s.Line(point1=(-0.038361652041603, -0.023523319865852), point2=(
        -0.0387163706392588, -0.0234225543433765))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316115, 
        farPlane=0.321389, width=0.00399012, height=0.00180769, 
        cameraPosition=(0.0669556, 0.108305, -0.316502), cameraTarget=(
        0.0669556, 0.108305, 0.00225))
    s.Line(point1=(-0.0539899317857096, -0.019703634002633), point2=(
        -0.0544012249156367, -0.01960625657739))
    s.Line(point1=(-0.0544012249156367, -0.01960625657739), point2=(
        -0.0544347230417461, -0.0197477426466719))
    s.PerpendicularConstraint(entity1=g[73], entity2=g[74], addUndoState=False)
    s.Line(point1=(-0.0544347230417461, -0.0197477426466719), point2=(
        -0.0540129707831635, -0.01980094384076))
    s.dragEntity(entity=v[62], points=((-0.0544347230417461, -0.0197477426466719), 
        (-0.0544347230417461, -0.0197477426466719), (-0.0544374650201798, 
        -0.0197020307145118), (-0.0544374650201798, -0.0196994155607223), (
        -0.0544348424158096, -0.0197151064834594)))
    s.setAsConstruction(objectList=(g[49], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316098, 
        farPlane=0.321406, width=0.00416655, height=0.00188761, 
        cameraPosition=(0.0686681, 0.100609, -0.316502), cameraTarget=(
        0.0686681, 0.100609, 0.00225))
    s.DistanceDimension(entity1=g[49], entity2=g[68], textPoint=(
        -0.0461705839118958, -0.0212343916258812), value=5.00000000000008e-05)
    s.DistanceDimension(entity1=g[69], entity2=g[49], textPoint=(
        -0.0456398418030739, -0.0213929325304031), value=4.99999999999976e-05)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316194, 
        farPlane=0.32131, width=0.00317229, height=0.00143718, cameraPosition=(
        0.0809918, 0.099366, -0.316502), cameraTarget=(0.0809918, 0.099366, 
        0.00225))
    s.DistanceDimension(entity1=g[61], entity2=g[48], textPoint=(
        -0.0438880687437058, -0.0345217272601128), value=5.00000000000004e-05)
    s.DistanceDimension(entity1=g[60], entity2=g[48], textPoint=(
        -0.0443233987174034, -0.0339972585401535), value=5.00000000000004e-05)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286301, 
        farPlane=0.351203, width=0.311482, height=0.141114, cameraPosition=(
        0.0624285, -0.00765936, -0.316502), cameraTarget=(0.0624285, 
        -0.00765936, 0.00225))
    s.setAsConstruction(objectList=(g[51], g[53], g[55], g[56], g[57], g[58], 
        g[59]))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, d2 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d2[9], sketchUpEdge=e1[179], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s, depth=0.00199, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.216316, 
        farPlane=0.381451, width=0.0748347, height=0.0325294, 
        viewOffsetX=0.0074493, viewOffsetY=0.00195755)
    p = mdb.models['Model-1'].parts['Spiral']
    s1 = p.features['Cut extrude-3'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-3'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-3'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s1 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1, 
        upToFeature=p.features['Cut extrude-3'], filter=COPLANAR_EDGES)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Spiral']
    s = p.features['Cut extrude-3'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-3'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.220238, 
        farPlane=0.377528, width=0.0258021, height=0.0112157, 
        viewOffsetX=0.0322466, viewOffsetY=0.00565769)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.220385, 
        farPlane=0.377381, width=0.0258193, height=0.0112232, cameraPosition=(
        0.180024, -0.206364, 0.0593885), cameraUpVector=(-0.0649931, 0.194303, 
        0.978786), cameraTarget=(0.0410327, 0.0730951, -0.00531724), 
        viewOffsetX=0.0322681, viewOffsetY=0.00566146)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251964, 
        farPlane=0.401833, width=0.029519, height=0.0128314, cameraPosition=(
        0.334656, -0.0936259, 0.047259), cameraUpVector=(-0.0813048, 0.17135, 
        0.98185), cameraTarget=(0.0516428, 0.0450701, -0.000381503), 
        viewOffsetX=0.0368918, viewOffsetY=0.0064727)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.246574, 
        farPlane=0.407223, width=0.0902191, height=0.0392167, 
        viewOffsetX=0.0303124, viewOffsetY=0.00633326)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24611, 
        farPlane=0.407687, width=0.0900494, height=0.0391429, cameraPosition=(
        0.334849, -0.0935987, 0.0461885), cameraUpVector=(-0.0932774, 0.147864, 
        0.984599), cameraTarget=(0.0518363, 0.0450973, -0.00145196), 
        viewOffsetX=0.0302554, viewOffsetY=0.00632135)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275654, 
        farPlane=0.421912, width=0.100859, height=0.0438417, cameraPosition=(
        0.387005, 0.126838, 0.0361291), cameraUpVector=(-0.139211, 0.0754459, 
        0.987385), cameraTarget=(0.0803748, 0.0481294, -0.00108855), 
        viewOffsetX=0.0338873, viewOffsetY=0.00708018)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.283114, 
        farPlane=0.414452, width=0.00770339, height=0.00334853, 
        viewOffsetX=0.050718, viewOffsetY=0.00578842)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280361, 
        farPlane=0.389928, width=0.00762847, height=0.00331596, 
        cameraPosition=(0.379785, 0.0244215, 0.0321732), cameraUpVector=(
        -0.0908088, 0.15195, 0.984208), cameraTarget=(0.0628456, 0.0375885, 
        0.000897528), viewOffsetX=0.0502248, viewOffsetY=0.00573213)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.274773, 
        farPlane=0.395515, width=0.0733163, height=0.0318693, 
        viewOffsetX=0.0395185, viewOffsetY=0.00529413)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.274825, 
        farPlane=0.40657, width=0.0733302, height=0.0318753, cameraPosition=(
        0.386133, 0.0827678, 0.0262324), cameraUpVector=(-0.0977606, 0.161095, 
        0.982085), cameraTarget=(0.0711043, 0.0408172, 0.00175438), 
        viewOffsetX=0.039526, viewOffsetY=0.00529513)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263248, 
        farPlane=0.418147, width=0.212186, height=0.0922337, 
        viewOffsetX=0.000745624, viewOffsetY=-0.00604698)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25779, 
        farPlane=0.44377, width=0.207787, height=0.0903215, cameraPosition=(
        -0.0963561, -0.24562, 0.112538), cameraUpVector=(-0.114224, 0.414886, 
        0.902675), cameraTarget=(0.0389869, 0.0227164, 0.00633125), 
        viewOffsetX=0.000730165, viewOffsetY=-0.00592161)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25779, 
        farPlane=0.450475, width=0.207787, height=0.0903215, cameraPosition=(
        -0.108052, -0.262161, 0.0306371), cameraUpVector=(-0.264751, 0.240635, 
        0.93381), cameraTarget=(0.0368599, 0.0199781, -0.00098348), 
        viewOffsetX=0.000730165, viewOffsetY=-0.00592161)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.272535, 
        farPlane=0.435729, width=0.0435246, height=0.0189194, 
        viewOffsetX=-0.0168546, viewOffsetY=0.00508327)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.257084, 
        farPlane=0.421632, width=0.041057, height=0.0178468, cameraPosition=(
        0.248711, -0.214123, 0.0506202), cameraUpVector=(-0.00632048, 0.218844, 
        0.975739), cameraTarget=(0.0705495, 0.0435321, -0.00832283), 
        viewOffsetX=-0.015899, viewOffsetY=0.00479508)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253167, 
        farPlane=0.425549, width=0.0815041, height=0.0354284, 
        viewOffsetX=-0.00656001, viewOffsetY=0.0110561)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Cut extrude-3']
    p = mdb.models['Model-1'].parts['Spiral']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[76], sketchUpEdge=e[45], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.034901, 
        0.04875, 0.0045))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.318, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.249012, 
        farPlane=0.334806, width=0.419219, height=0.189923, cameraPosition=(
        0.0610378, 0.0667961, 0.294159), cameraTarget=(0.0610378, 0.0667961, 
        0.0045))
    p = mdb.models['Model-1'].parts['Spiral']
    e1, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s, edges=(e1[6], e1[19], e1[43], e1[45], 
        e1[47], e1[72], e1[112], e1[179], e1[189], e1[193], e1[196], e1[199], 
        e1[202], e1[204], e1[206], e1[208], e1[210], e1[212], e1[214], 
        e1[215]))
    s.autoTrimCurve(curve1=g[41], point1=(-0.00125148091411591, 
        -0.0392983573675156))
    s.autoTrimCurve(curve1=g[40], point1=(-0.00620614681339264, 
        -0.0478243920207024))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.277063, 
        farPlane=0.306755, width=0.12991, height=0.0588546, cameraPosition=(
        0.0451643, 0.0183691, 0.294159), cameraTarget=(0.0451643, 0.0183691, 
        0.0045))
    s.autoTrimCurve(curve1=g[42], point1=(0.00732052382135391, 
        -0.0483216121047735))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.261272, 
        farPlane=0.322546, width=0.331339, height=0.15011, cameraPosition=(
        0.0501623, 0.0642637, 0.294159), cameraTarget=(0.0501623, 0.0642637, 
        0.0045))
    s.Line(point1=(-0.0265711672297821, 0.000551256434498749), point2=(
        0.00884972533808025, -0.0117628117651448))
    s.Line(point1=(0.00884972533808025, -0.0117628117651448), point2=(
        -0.00852818431528861, 0.0334256640105573))
    s.Line(point1=(-0.00852818431528861, 0.0334256640105573), point2=(
        0.013531882778283, 0.0159786525396411))
    s.Line(point1=(0.013531882778283, 0.0159786525396411), point2=(
        0.0123501408113617, 0.0522708307475496))
    s.Line(point1=(0.0123501408113617, 0.0522708307475496), point2=(
        0.02368101235993, 0.034478072955139))
    s.Line(point1=(0.02368101235993, 0.034478072955139), point2=(
        0.0317819324061809, 0.0604791408857608))
    s.Line(point1=(0.0317819324061809, 0.0604791408857608), point2=(
        0.0354268994243129, 0.0450838511405319))
    s.Line(point1=(0.0354268994243129, 0.0450838511405319), point2=(
        0.0475693142727197, 0.0615083661783491))
    s.Line(point1=(0.0475693142727197, 0.0615083661783491), point2=(
        0.0463599010184524, 0.0497043806470771))
    s.autoTrimCurve(curve1=g[54], point1=(-0.0314046138892174, 
        -0.0239404122531414))
    s.autoTrimCurve(curve1=g[53], point1=(0.0125418087472916, -0.0256794410943985))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268741, 
        farPlane=0.315077, width=0.215745, height=0.0977411, cameraPosition=(
        0.0423219, 0.0771052, 0.294159), cameraTarget=(0.0423219, 0.0771052, 
        0.0045))
    s.autoTrimCurve(curve1=g[56], point1=(-0.00313261840438843, 
        0.0193673205375671))
    s.autoTrimCurve(curve1=g[65], point1=(-0.00624908450937271, 
        0.0264444035291672))
    s.autoTrimCurve(curve1=g[43], point1=(-0.013898603058815, 0.0248874408006668))
    s.autoTrimCurve(curve1=g[52], point1=(0.0113164788117409, 0.00450545370578766))
    s.autoTrimCurve(curve1=g[64], point1=(0.0060751443734169, 
        -0.00582708224654198))
    s.autoTrimCurve(curve1=g[44], point1=(-0.00242432150936127, 
        0.0405985620617866))
    s.autoTrimCurve(curve1=g[58], point1=(0.0128747081389427, 0.0374846440553665))
    s.autoTrimCurve(curve1=g[67], point1=(0.0127330502500534, 0.0448448118567467))
    s.autoTrimCurve(curve1=g[66], point1=(0.0135830050339699, 0.0217735302448273))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286182, 
        farPlane=0.297636, width=0.0358631, height=0.0162474, cameraPosition=(
        0.0467789, 0.0673108, 0.294159), cameraTarget=(0.0467789, 0.0673108, 
        0.0045))
    s.autoTrimCurve(curve1=g[51], point1=(0.0140795713295937, 0.0169725847244263))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.276538, 
        farPlane=0.30728, width=0.135324, height=0.0613072, cameraPosition=(
        0.0572385, 0.0853312, 0.294159), cameraTarget=(0.0572385, 0.0853312, 
        0.0045))
    s.autoTrimCurve(curve1=g[45], point1=(0.0203382937242985, 0.0560685527324676))
    s.autoTrimCurve(curve1=g[60], point1=(0.0302898814907074, 0.05704514503479))
    s.autoTrimCurve(curve1=g[68], point1=(0.0294013550510406, 0.0527836737036705))
    s.autoTrimCurve(curve1=g[69], point1=(0.0245144112040997, 0.0371582788228989))
    s.autoTrimCurve(curve1=g[50], point1=(0.0274465797474384, 0.0390226674079895))
    s.autoTrimCurve(curve1=g[46], point1=(0.0359765073289871, 0.0607739296555519))
    s.autoTrimCurve(curve1=g[62], point1=(0.0404191842308044, 0.0510080587863922))
    s.autoTrimCurve(curve1=g[70], point1=(0.0386421164503098, 0.0487885457277298))
    s.autoTrimCurve(curve1=g[49], point1=(0.0394418021669388, 0.0475456100702286))
    s.autoTrimCurve(curve1=g[71], point1=(0.0452172687282562, 0.0585544091463089))
    s.autoTrimCurve(curve1=g[47], point1=(0.0507261982192993, 0.0608627107739449))
    s.autoTrimCurve(curve1=g[48], point1=(0.0512593170633316, 0.0494100061058998))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289086, 
        farPlane=0.294732, width=0.00590927, height=0.00267713, 
        cameraPosition=(0.0426705, 0.0378858, 0.294159), cameraTarget=(
        0.0426705, 0.0378858, 0.0045))
    s.offset(distance=5e-05, objectList=(g[55], ), side=LEFT)
    s.offset(distance=5e-05, objectList=(g[55], ), side=RIGHT)
    s.Line(point1=(0.00886614394444873, -0.0117155843433973), point2=(
        0.00929096535764984, -0.0118632734465791))
    s.ParallelConstraint(entity1=g[72], entity2=g[74], addUndoState=False)
    s.Line(point1=(0.00929096535764984, -0.0118632734465791), point2=(
        0.00925310928468193, -0.0119721648276752))
    s.PerpendicularConstraint(entity1=g[74], entity2=g[75], addUndoState=False)
    s.Line(point1=(0.00925310928468193, -0.0119721648276752), point2=(
        0.00884972533808025, -0.0117628117651448))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289331, 
        farPlane=0.294487, width=0.00338598, height=0.00153398, 
        cameraPosition=(0.0431355, 0.0374641, 0.294159), cameraTarget=(
        0.0431355, 0.0374641, 0.0045))
    s.undo()
    s.Line(point1=(0.00883330673171176, -0.0118100391868923), point2=(
        0.00946993157685938, -0.0120313617226202))
    s.ParallelConstraint(entity1=g[73], entity2=g[76], addUndoState=False)
    s.autoTrimCurve(curve1=g[76], point1=(0.00934277158284187, 
        -0.0119912232458591))
    s.autoTrimCurve(curve1=g[75], point1=(0.00925828572416305, 
        -0.0119712296128273))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289064, 
        farPlane=0.294754, width=0.00613397, height=0.00277894, 
        cameraPosition=(0.0430619, 0.0375776, 0.294159), cameraTarget=(
        0.0430619, 0.0375776, 0.0045))
    s.dragEntity(entity=g[78], points=((0.00927615659441767, -0.0119058702231133), 
        (0.00929059889221191, -0.0119104067981243), (0.00986250918412208, 
        -0.0121235530078411), (0.0102249911060333, -0.0121878999471664), (
        0.0107928780844212, -0.0123125705122948), (0.0112278541555405, 
        -0.0123970228433609), (0.0112278541555405, -0.0124653893709183), (
        0.0111271632840633, -0.0124533268809319), (0.0105512222280502, 
        -0.01225), (0.0112278541555405, -0.0125136505067348), (
        0.0112278541555405, -0.012537779211998)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.28682, 
        farPlane=0.296998, width=0.0331422, height=0.0150148, cameraPosition=(
        0.0358391, 0.0401466, 0.294159), cameraTarget=(0.0358391, 0.0401466, 
        0.0045))
    s.dragEntity(entity=v[70], points=((0.0111953725927574, -0.0126312110435198), (
        0.0111953725927574, -0.0126312110435198), (0.0134181311359406, 
        -0.0135685074329376), (0.014, -0.014), (0.01575, -0.0144593994319439), 
        (0.0162688462069035, -0.0146549585461617), (0.0163341281940937, 
        -0.0146766881644726), (0.0151155075063705, -0.0146766881644726), (
        0.014810849540472, -0.0148722510039806), (0.0148326089611053, 
        -0.0149591657519341)))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289008, 
        farPlane=0.29481, width=0.00759924, height=0.00344276, cameraPosition=(
        0.00842644, 0.0491095, 0.294159), cameraTarget=(0.00842644, 0.0491095, 
        0.0045))
    s.Line(point1=(-0.0265547486234136, 0.000598483856246255), point2=(
        -0.0290877953957533, 0.00147909719817108))
    s.Line(point1=(-0.0265875858361506, 0.000504029012751244), point2=(
        -0.0290969231136842, 0.00137639974855119))
    s.Line(point1=(-0.0290969231136842, 0.00137639974855119), point2=(
        -0.0290877953957533, 0.00147909719817108))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289179, 
        farPlane=0.294639, width=0.00494809, height=0.00224169, 
        cameraPosition=(0.0093154, 0.0488903, 0.294159), cameraTarget=(
        0.0093154, 0.0488903, 0.0045))
    s.setAsConstruction(objectList=(g[55], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289091, 
        farPlane=0.294727, width=0.00585343, height=0.00265184, 
        cameraPosition=(0.0277307, 0.0819109, 0.294159), cameraTarget=(
        0.0277307, 0.0819109, 0.0045))
    s.offset(distance=5e-05, objectList=(g[57], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289178, 
        farPlane=0.29464, width=0.00561569, height=0.00254413, cameraPosition=(
        0.0277983, 0.0819514, 0.294159), cameraTarget=(0.0277983, 0.0819514, 
        0.0045))
    s.offset(distance=5e-05, objectList=(g[57], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289305, 
        farPlane=0.294514, width=0.00365655, height=0.00165656, 
        cameraPosition=(0.0271455, 0.0822714, 0.294159), cameraTarget=(
        0.0271455, 0.0822714, 0.0045))
    s.Line(point1=(-0.00849716797738979, 0.0334648811851539), point2=(
        -0.00935671050683595, 0.0341446818492841))
    s.Line(point1=(-0.00855920065318744, 0.0333864468359606), point2=(
        -0.00942694355035201, 0.034072733062203))
    s.Line(point1=(-0.00942694355035201, 0.034072733062203), point2=(
        -0.00935671050683595, 0.0341446818492841))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288547, 
        farPlane=0.295271, width=0.0129763, height=0.00587878, cameraPosition=(
        0.0515466, 0.0648962, 0.294159), cameraTarget=(0.0515466, 0.0648962, 
        0.0045))
    s.Line(point1=(0.0135628991161818, 0.0160178697142378), point2=(
        0.015418091664742, 0.0145506227863734))
    s.ParallelConstraint(entity1=g[83], entity2=g[87], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288597, 
        farPlane=0.295221, width=0.0109554, height=0.00496322, cameraPosition=(
        0.050928, 0.0642589, 0.294159), cameraTarget=(0.050928, 0.0642589, 
        0.0045))
    s.Line(point1=(0.0135008664403842, 0.0159394353650445), point2=(
        0.0153527386605674, 0.0144748144407458))
    s.ParallelConstraint(entity1=g[82], entity2=g[88], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289288, 
        farPlane=0.29453, width=0.00382649, height=0.00173355, cameraPosition=(
        0.0504661, 0.0636956, 0.294159), cameraTarget=(0.0504661, 0.0636956, 
        0.0045))
    s.Line(point1=(0.0153527386605674, 0.0144748144407458), point2=(
        0.015418091664742, 0.0145506227863734))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289528, 
        farPlane=0.29429, width=0.00134747, height=0.000610459, 
        cameraPosition=(0.0487977, 0.0646553, 0.294159), cameraTarget=(
        0.0487977, 0.0646553, 0.0045))
    s.setAsConstruction(objectList=(g[57], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289219, 
        farPlane=0.294599, width=0.00453706, height=0.00205547, 
        cameraPosition=(0.047906, 0.101199, 0.294159), cameraTarget=(0.047906, 
        0.101199, 0.0045))
    s.offset(distance=5e-05, objectList=(g[59], ), side=LEFT)
    s.offset(distance=5e-05, objectList=(g[59], ), side=RIGHT)
    s.Line(point1=(0.0123079665508897, 0.0522439731275202), point2=(
        0.0116629492695211, 0.0532568374910625))
    s.Line(point1=(0.0123923150718336, 0.052297688367579), point2=(
        0.0117510193231283, 0.0533047088538297))
    s.Line(point1=(0.0117510193231283, 0.0533047088538297), point2=(
        0.0116629492695211, 0.0532568374910625))
    s.setAsConstruction(objectList=(g[59], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289186, 
        farPlane=0.294632, width=0.00487502, height=0.00220858, 
        cameraPosition=(0.0600218, 0.0826023, 0.294159), cameraTarget=(
        0.0600218, 0.0826023, 0.0045))
    s.Line(point1=(0.023638838099458, 0.0344512153351096), point2=(
        0.024610368308231, 0.0329256308627919))
    s.ParallelConstraint(entity1=g[91], entity2=g[95], addUndoState=False)
    s.Line(point1=(0.023723186620402, 0.0345049305751683), point2=(
        0.0246992695438166, 0.0329721970192622))
    s.ParallelConstraint(entity1=g[90], entity2=g[96], addUndoState=False)
    s.Line(point1=(0.0246992695438166, 0.0329721970192622), point2=(
        0.024610368308231, 0.0329256308627919))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289363, 
        farPlane=0.294456, width=0.00305781, height=0.00138531, 
        cameraPosition=(0.0668029, 0.109439, 0.294159), cameraTarget=(
        0.0668029, 0.109439, 0.0045))
    s.offset(distance=5e-05, objectList=(g[61], ), side=RIGHT)
    s.offset(distance=5e-05, objectList=(g[61], ), side=LEFT)
    s.setAsConstruction(objectList=(g[61], ))
    s.Line(point1=(0.0317332774806318, 0.060467621414427), point2=(
        0.031565910387144, 0.0611745317728492))
    s.Line(point1=(0.031565910387144, 0.0611745317728492), point2=(
        0.0316775777628777, 0.0612009699822949))
    s.PerpendicularConstraint(entity1=g[100], entity2=g[101], addUndoState=False)
    s.Line(point1=(0.0316775777628777, 0.0612009699822949), point2=(
        0.03183058733173, 0.0604906603570947))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.28719, 
        farPlane=0.296628, width=0.0254613, height=0.011535, cameraPosition=(
        0.0725592, 0.0936532, 0.294159), cameraTarget=(0.0725592, 0.0936532, 
        0.0045))
    s.Line(point1=(0.0353782444987638, 0.045072331669198), point2=(
        0.0363800948089761, 0.0408408048190267))
    s.ParallelConstraint(entity1=g[98], entity2=g[103], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289094, 
        farPlane=0.294724, width=0.00582476, height=0.00263885, 
        cameraPosition=(0.0717846, 0.0902496, 0.294159), cameraTarget=(
        0.0717846, 0.0902496, 0.0045))
    s.Line(point1=(0.035475554349862, 0.0450953706118657), point2=(
        0.0364772081360343, 0.0408646738221705))
    s.ParallelConstraint(entity1=g[99], entity2=g[104], addUndoState=False)
    s.Line(point1=(0.0364772081360343, 0.0408646738221705), point2=(
        0.0363800948089761, 0.0408408048190267))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289394, 
        farPlane=0.294424, width=0.00272863, height=0.00123618, 
        cameraPosition=(0.0813437, 0.0984369, 0.294159), cameraTarget=(
        0.0813437, 0.0984369, 0.0045))
    s.offset(distance=5e-05, objectList=(g[63], ), side=LEFT)
    s.offset(distance=5e-05, objectList=(g[63], ), side=RIGHT)
    s.Line(point1=(0.0463101614113644, 0.0497094768698668), point2=(
        0.0462520195688398, 0.0491420070945878))
    s.ParallelConstraint(entity1=g[107], entity2=g[108], addUndoState=False)
    s.Line(point1=(0.0462520195688398, 0.0491420070945878), point2=(
        0.0463718402909876, 0.049129730497909))
    s.PerpendicularConstraint(entity1=g[108], entity2=g[109], addUndoState=False)
    s.Line(point1=(0.0463718402909876, 0.049129730497909), point2=(
        0.0464096406255405, 0.0496992844242873))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289249, 
        farPlane=0.294569, width=0.00478154, height=0.00216623, 
        cameraPosition=(0.0816507, 0.0985178, 0.294159), cameraTarget=(
        0.0816507, 0.0985178, 0.0045))
    s.setAsConstruction(objectList=(g[63], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289304, 
        farPlane=0.294514, width=0.00365753, height=0.00165701, 
        cameraPosition=(0.0828574, 0.110927, 0.294159), cameraTarget=(
        0.0828574, 0.110927, 0.0045))
    s.Line(point1=(0.0476190538798078, 0.0615032699555593), point2=(
        0.0477596161745169, 0.0628751710173674))
    s.Line(point1=(0.0477596161745169, 0.0628751710173674), point2=(
        0.0476506189097847, 0.0628863386635423))
    s.PerpendicularConstraint(entity1=g[111], entity2=g[112], addUndoState=False)
    s.Line(point1=(0.0476506189097847, 0.0628863386635423), point2=(
        0.0475195746656316, 0.0615134624011388))
    p = mdb.models['Model-1'].parts['Spiral']
    f1, e, d2 = p.faces, p.edges, p.datums
    p.CutExtrude(sketchPlane=f1[76], sketchUpEdge=e[45], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s, depth=0.002, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.258946, 
        farPlane=0.41977, width=0.024597, height=0.0106919, 
        viewOffsetX=-0.0174907, viewOffsetY=0.00872449)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.26959, 
        farPlane=0.425755, width=0.025608, height=0.0111313, cameraPosition=(
        -0.226463, -0.155709, 0.0513031), cameraUpVector=(0.290792, -0.091341, 
        0.952416), cameraTarget=(0.031626, 0.0208247, -0.0105671), 
        viewOffsetX=-0.0182097, viewOffsetY=0.0090831)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.264282, 
        farPlane=0.431063, width=0.087958, height=0.0382338, 
        viewOffsetX=-0.0124389, viewOffsetY=0.00632754)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.270353, 
        farPlane=0.433425, width=0.0899783, height=0.039112, cameraPosition=(
        -0.0498387, -0.284166, -0.00245879), cameraUpVector=(0.601874, 
        -0.148927, 0.784582), cameraTarget=(0.0473702, 0.018922, -0.0195002), 
        viewOffsetX=-0.0127246, viewOffsetY=0.00647288)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275336, 
        farPlane=0.422352, width=0.0916367, height=0.0398329, cameraPosition=(
        -0.285392, -0.0528715, 0.00629376), cameraUpVector=(-0.126998, 
        0.561535, 0.817649), cameraTarget=(0.022965, 0.0275309, -0.00103067), 
        viewOffsetX=-0.0129591, viewOffsetY=0.00659218)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280736, 
        farPlane=0.416951, width=0.028836, height=0.0125345, 
        viewOffsetX=-0.0153075, viewOffsetY=0.0135677)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290906, 
        farPlane=0.408413, width=0.0298805, height=0.0129885, cameraPosition=(
        -0.300018, 0.00789126, 0.0110648), cameraUpVector=(-0.0300797, 
        0.670084, 0.741676), cameraTarget=(0.0176987, 0.031963, 0.00220107), 
        viewOffsetX=-0.015862, viewOffsetY=0.0140592)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286161, 
        farPlane=0.413157, width=0.0859386, height=0.037356, 
        viewOffsetX=-0.0182488, viewOffsetY=0.00902698)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.279318, 
        farPlane=0.421704, width=0.0838835, height=0.0364627, cameraPosition=(
        -0.298814, 0.11287, 0.0198191), cameraUpVector=(0.202697, 0.873686, 
        0.442252), cameraTarget=(0.0125562, 0.0453047, 0.0105844), 
        viewOffsetX=-0.0178124, viewOffsetY=0.00881111)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.28442, 
        farPlane=0.416601, width=0.028044, height=0.0121902, 
        viewOffsetX=-0.0108106, viewOffsetY=0.0028044)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286438, 
        farPlane=0.420024, width=0.028243, height=0.0122767, cameraPosition=(
        -0.234152, -0.0790615, 0.169586), cameraUpVector=(-0.192163, 0.918193, 
        0.346404), cameraTarget=(0.0270287, 0.0307069, 0.0235126), 
        viewOffsetX=-0.0108873, viewOffsetY=0.0028243)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.27891, 
        farPlane=0.427553, width=0.104254, height=0.0453176, 
        viewOffsetX=-0.0157521, viewOffsetY=0.0264473)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275342, 
        farPlane=0.453646, width=0.102921, height=0.0447378, cameraPosition=(
        0.236569, 0.369426, 0.0419574), cameraUpVector=(0.756126, -0.643903, 
        0.116886), cameraTarget=(0.0322261, 0.125683, 0.0210958), 
        viewOffsetX=-0.0155505, viewOffsetY=0.026109)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275451, 
        farPlane=0.418835, width=0.102962, height=0.0447556, cameraPosition=(
        0.384924, 0.0120049, 0.0830428), cameraUpVector=(-0.078342, -0.77978, 
        -0.621133), cameraTarget=(0.0745772, 0.0737593, 0.0446596), 
        viewOffsetX=-0.0155566, viewOffsetY=0.0261193)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331341, 
        farPlane=0.367546, width=0.123853, height=0.0538369, cameraPosition=(
        0.0143896, 0.0149701, 0.34953), cameraUpVector=(0.988476, -0.150123, 
        -0.0194686), cameraTarget=(0.0131592, 0.0479873, 0.0324965), 
        viewOffsetX=-0.0187131, viewOffsetY=0.031419)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.329501, 
        farPlane=0.369386, width=0.123166, height=0.053538, cameraPosition=(
        0.0673885, -0.00489786, 0.347255), cameraUpVector=(0.0731494, 0.991985, 
        0.103028), cameraTarget=(0.0661581, 0.0281193, 0.0302217), 
        viewOffsetX=-0.0186092, viewOffsetY=0.0312446)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321467, 
        farPlane=0.377419, width=0.224009, height=0.0973729, 
        viewOffsetX=-0.00246374, viewOffsetY=0.0244728)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.298741, 
        farPlane=0.431503, width=0.208172, height=0.0904889, cameraPosition=(
        0.366551, 0.0402983, 0.180715), cameraUpVector=(-0.177549, 0.953169, 
        0.244838), cameraTarget=(0.0973155, 0.033945, 0.0102051), 
        viewOffsetX=-0.00228956, viewOffsetY=0.0227426)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316777, 
        farPlane=0.413466, width=0.023795, height=0.0103433, 
        viewOffsetX=-0.00703359, viewOffsetY=0.0313582)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-3'].setValues(depth=0.0019)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.318949, 
        farPlane=0.411295, width=0.00139102, height=0.000604653, 
        viewOffsetX=-0.00926935, viewOffsetY=0.032119)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309197, 
        farPlane=0.421047, width=0.11496, height=0.0499709, 
        viewOffsetX=0.000856988, viewOffsetY=0.00341749)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.257966, 
        farPlane=0.379539, width=0.106431, height=0.0462639, 
        viewOffsetX=-0.000414788, viewOffsetY=0.019139)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2474, 
        farPlane=0.405755, width=0.151831, height=0.0659982, 
        viewOffsetX=0.000788497, viewOffsetY=0.0140509)
    p = mdb.models['Model-1'].parts['Spiral']
    f, e1, d1 = p.faces, p.edges, p.datums
    p.Mirror(mirrorPlane=d1[9], keepOriginal=ON)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Mirror-1'].setValues(keepInternalBoundaries=True)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.26002, 
        farPlane=0.393136, width=0.00440942, height=0.0019167, 
        viewOffsetX=0.0205166, viewOffsetY=0.0279274)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Mirror-1'].setValues(keepInternalBoundaries=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2596, 
        farPlane=0.393555, width=0.00988079, height=0.00429501, 
        viewOffsetX=0.0219862, viewOffsetY=0.0273018)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25667, 
        farPlane=0.396485, width=0.0440463, height=0.0191462, 
        viewOffsetX=0.0190699, viewOffsetY=0.0219721)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253896, 
        farPlane=0.399259, width=0.0763506, height=0.0331883, 
        viewOffsetX=0.0133645, viewOffsetY=0.0180703)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    f1, e, d2 = p.faces, p.edges, p.datums
    p.Mirror(mirrorPlane=d2[9], keepOriginal=ON)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    p = mdb.models['Model-1'].parts['Spiral']
    f, e1, d1 = p.faces, p.edges, p.datums
    p.Mirror(mirrorPlane=d1[9], keepOriginal=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25428, 
        farPlane=0.398875, width=0.0718782, height=0.0312442, 
        viewOffsetX=0.0137926, viewOffsetY=0.0181606)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    p = mdb.models['Model-1'].parts['Spiral']
    f1, e, d2 = p.faces, p.edges, p.datums
    p.Mirror(mirrorPlane=d2[9], keepOriginal=ON)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250434, 
        farPlane=0.402722, width=0.116608, height=0.0506874, 
        viewOffsetX=0.033424, viewOffsetY=0.013335)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.261392, 
        farPlane=0.428153, width=0.12171, height=0.0529053, cameraPosition=(
        0.348778, 0.200475, 0.0867328), cameraUpVector=(-0.762405, 0.64708, 
        0.00506449), cameraTarget=(0.074049, 0.0456794, 0.00179089), 
        viewOffsetX=0.0348865, viewOffsetY=0.0139185)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262808, 
        farPlane=0.340365, width=0.122369, height=0.0531919, cameraPosition=(
        0.00466247, 0.133477, 0.291559), cameraUpVector=(-0.660916, 0.460171, 
        -0.592817), cameraTarget=(0.0384065, 0.0243588, -0.014394), 
        viewOffsetX=0.0350755, viewOffsetY=0.0139939)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.257894, 
        farPlane=0.345279, width=0.185932, height=0.0808214, 
        viewOffsetX=0.0751064, viewOffsetY=0.0188263)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(width=0.197063, height=0.08566, 
        viewOffsetX=0.067288, viewOffsetY=0.0158003)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.260286, 
        farPlane=0.389999, width=0.199635, height=0.0867777, cameraPosition=(
        0.0777705, 0.248335, 0.264314), cameraUpVector=(-0.844311, 0.1671, 
        -0.509134), cameraTarget=(0.049732, 0.0281735, 0.0247406), 
        viewOffsetX=0.068166, viewOffsetY=0.0160065)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.276302, 
        farPlane=0.442396, width=0.211919, height=0.0921174, cameraPosition=(
        0.394989, 0.138772, 0.0585986), cameraUpVector=(-0.553679, 0.826339, 
        0.10297), cameraTarget=(0.0783193, 0.0594523, 0.0495732), 
        viewOffsetX=0.0723603, viewOffsetY=0.0169914)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288616, 
        farPlane=0.430082, width=0.068318, height=0.0296966, 
        viewOffsetX=0.0587109, viewOffsetY=0.0284579)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.291432, 
        farPlane=0.427266, width=0.0355019, height=0.015432, 
        viewOffsetX=0.0558339, viewOffsetY=0.0368227)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Mirror-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289181, 
        farPlane=0.429517, width=0.0617314, height=0.0268336, 
        viewOffsetX=0.0562452, viewOffsetY=0.035348)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.292859, 
        farPlane=0.440143, width=0.0625165, height=0.0271748, cameraPosition=(
        0.3976, 0.171839, -0.00558126), cameraUpVector=(-0.600371, 0.785714, 
        0.149027), cameraTarget=(0.0920599, 0.0675761, 0.0436846), 
        viewOffsetX=0.0569605, viewOffsetY=0.0357975)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.294903, 
        farPlane=0.435122, width=0.0629527, height=0.0273645, cameraPosition=(
        0.401295, 0.141153, -0.043439), cameraUpVector=(-0.508822, 0.816783, 
        0.271968), cameraTarget=(0.0949829, 0.0580073, 0.0334518), 
        viewOffsetX=0.057358, viewOffsetY=0.0360473)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.285912, 
        farPlane=0.444112, width=0.170919, height=0.0742957, 
        viewOffsetX=0.0721857, viewOffsetY=0.0290782)
    p = mdb.models['Model-1'].parts['Spiral']
    f, e1, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[98], sketchUpEdge=e1[177], 
        sketchPlaneSide=SIDE1, sketchOrientation=BOTTOM, origin=(0.034901, 
        0.04875, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.289, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Spiral']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250808, 
        farPlane=0.33301, width=0.400695, height=0.181531, cameraPosition=(
        0.0525577, 0.0502934, -0.289659), cameraTarget=(0.0525577, 0.0502934, 
        0))
    s1.Line(point1=(-0.0122215737409919, -0.00820454230747737), point2=(
        0.025278771669811, -0.00820454230747739))
    s1.HorizontalConstraint(entity=g[40], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.267398, 
        farPlane=0.31642, width=0.229596, height=0.104016, cameraPosition=(
        0.0405096, 0.0613108, -0.289659), cameraTarget=(0.0405096, 0.0613108, 
        0))
    s1.Line(point1=(-0.0075345745732125, 0.0195361043841517), point2=(
        0.0190313395478631, 0.028771740602128))
    s1.Line(point1=(-0.0110462249987198, 0.0403423942567704), point2=(
        0.00549897771716873, 0.0534277733876822))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.276903, 
        farPlane=0.306915, width=0.131558, height=0.0596008, cameraPosition=(
        0.0672917, 0.0883776, -0.289659), cameraTarget=(0.0672917, 0.0883776, 
        0))
    s1.Line(point1=(-0.0186581422973349, 0.0542170873663868), point2=(
        -0.0101599103597998, 0.06756177862691))
    s1.Line(point1=(-0.0274676387387477, 0.0621714942724387), point2=(
        -0.024733888294929, 0.0737180679353483))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.284919, 
        farPlane=0.298899, width=0.0488834, height=0.0221461, cameraPosition=(
        0.076229, 0.100138, -0.289659), cameraTarget=(0.076229, 0.100138, 0))
    s1.offset(distance=5e-05, objectList=(g[44], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289179, 
        farPlane=0.294639, width=0.00495327, height=0.00224403, 
        cameraPosition=(0.0806909, 0.0989593, -0.289659), cameraTarget=(
        0.0806909, 0.0989593, 0))
    s1.offset(distance=5e-05, objectList=(g[44], ), side=LEFT)
    s1.Line(point1=(-0.0275162936642969, 0.0621830137437726), point2=(
        -0.0276749928270874, 0.061512714237324))
    s1.ParallelConstraint(entity1=g[46], entity2=g[47], addUndoState=False)
    s1.Line(point1=(-0.0276749928270874, 0.061512714237324), point2=(
        -0.027537011823398, 0.0614800460501108))
    s1.PerpendicularConstraint(entity1=g[47], entity2=g[48], addUndoState=False)
    s1.Line(point1=(-0.027537011823398, 0.0614800460501108), point2=(
        -0.0274189838131986, 0.0621599748011049))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289393, 
        farPlane=0.294425, width=0.00274684, height=0.00124443, 
        cameraPosition=(0.0820582, 0.110682, -0.289659), cameraTarget=(
        0.0820582, 0.110682, 0))
    s1.Line(point1=(-0.0247825432204781, 0.0737295874066821), point2=(
        -0.0246018067858245, 0.0744929659954323))
    s1.ParallelConstraint(entity1=g[46], entity2=g[50], addUndoState=False)
    s1.Line(point1=(-0.0246018067858245, 0.0744929659954323), point2=(
        -0.0245002285186047, 0.074468916468593))
    s1.PerpendicularConstraint(entity1=g[50], entity2=g[51], addUndoState=False)
    s1.Line(point1=(-0.0245002285186047, 0.074468916468593), point2=(
        -0.0246852333693799, 0.0737065484640145))
    s1.setAsConstruction(objectList=(g[44], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289066, 
        farPlane=0.294752, width=0.00611818, height=0.00277178, 
        cameraPosition=(0.0698275, 0.0949744, -0.289659), cameraTarget=(
        0.0698275, 0.0949744, 0))
    s1.offset(distance=5e-05, objectList=(g[43], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289452, 
        farPlane=0.294366, width=0.00213696, height=0.000968128, 
        cameraPosition=(0.0701306, 0.0942236, -0.289659), cameraTarget=(
        0.0701306, 0.0942236, 0))
    s1.offset(distance=5e-05, objectList=(g[43], ), side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289222, 
        farPlane=0.294596, width=0.00450853, height=0.00204255, 
        cameraPosition=(0.0695596, 0.0941595, -0.289659), cameraTarget=(
        0.0695596, 0.0941595, 0))
    s1.Line(point1=(-0.0187003165578068, 0.0542439449864162), point2=(
        -0.0192686598597699, 0.0535876520873307))
    s1.Line(point1=(-0.0192686598597699, 0.0535876520873307), point2=(
        -0.0191691471924713, 0.0535014750800826))
    s1.PerpendicularConstraint(entity1=g[55], entity2=g[56], addUndoState=False)
    s1.Line(point1=(-0.0191691471924713, 0.0535014750800826), point2=(
        -0.0186159680368629, 0.0541902297463575))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289145, 
        farPlane=0.294673, width=0.00529648, height=0.00239952, 
        cameraPosition=(0.0658543, 0.109464, -0.289659), cameraTarget=(
        0.0658543, 0.109464, 0))
    s1.Line(point1=(-0.0102020846202718, 0.0675886362469394), point2=(
        -0.00951701390044946, 0.0686643961601021))
    s1.ParallelConstraint(entity1=g[53], entity2=g[58], addUndoState=False)
    s1.Line(point1=(-0.00951701390044946, 0.0686643961601021), point2=(
        -0.00935851390619291, 0.0685634594139941))
    s1.Line(point1=(-0.00935851390619291, 0.0685634594139941), point2=(
        -0.0101177360993279, 0.0675349210068806))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289526, 
        farPlane=0.294292, width=0.00136882, height=0.000620131, 
        cameraPosition=(0.0664244, 0.109208, -0.289659), cameraTarget=(
        0.0664244, 0.109208, 0))
    s1.setAsConstruction(objectList=(g[43], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289485, 
        farPlane=0.294333, width=0.00179866, height=0.000814866, 
        cameraPosition=(0.0583191, 0.083319, -0.289659), cameraTarget=(
        0.0583191, 0.083319, 0))
    s1.offset(distance=5e-05, objectList=(g[42], ), side=RIGHT)
    s1.offset(distance=5e-05, objectList=(g[42], ), side=LEFT)
    s1.Line(point1=(-0.0110772413366186, 0.0403816114313671), point2=(
        -0.0113454476959305, 0.0401694906176999))
    s1.Line(point1=(-0.0113454476959305, 0.0401694906176999), point2=(
        -0.0112919709485588, 0.0401018744160027))
    s1.PerpendicularConstraint(entity1=g[63], entity2=g[64], addUndoState=False)
    s1.Line(point1=(-0.0112919709485588, 0.0401018744160027), point2=(
        -0.0110152086608209, 0.0403031770821737))
    s1.setAsConstruction(objectList=(g[42], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289492, 
        farPlane=0.294326, width=0.0017265, height=0.000782175, 
        cameraPosition=(0.0467575, 0.10125, -0.289659), cameraTarget=(
        0.0467575, 0.10125, 0))
    s1.Line(point1=(0.0054679613792699, 0.0534669905622789), point2=(
        0.00591676718181589, 0.0538219450577344))
    s1.ParallelConstraint(entity1=g[62], entity2=g[66], addUndoState=False)
    s1.Line(point1=(0.00591676718181589, 0.0538219450577344), point2=(
        0.0059963217902137, 0.0537213559108949))
    s1.PerpendicularConstraint(entity1=g[66], entity2=g[67], addUndoState=False)
    s1.Line(point1=(0.0059963217902137, 0.0537213559108949), point2=(
        0.00552999405506756, 0.0533885562130856))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288727, 
        farPlane=0.295091, width=0.00960936, height=0.00435343, 
        cameraPosition=(0.0456795, 0.0665456, -0.289659), cameraTarget=(
        0.0456795, 0.0665456, 0))
    s1.offset(distance=5e-05, objectList=(g[41], ), side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289353, 
        farPlane=0.294465, width=0.00315498, height=0.00142933, 
        cameraPosition=(0.0474354, 0.0653145, -0.289659), cameraTarget=(
        0.0474354, 0.0653145, 0))
    s1.offset(distance=5e-05, objectList=(g[41], ), side=RIGHT)
    s1.Line(point1=(-0.00755099317958099, 0.0195833318058992), point2=(
        -0.00790106067142915, 0.0194616308872355))
    s1.Line(point1=(-0.00790106067142915, 0.0194616308872355), point2=(
        -0.00785729732667129, 0.0193357474961928))
    s1.PerpendicularConstraint(entity1=g[71], entity2=g[72], addUndoState=False)
    s1.Line(point1=(-0.00785729732667129, 0.0193357474961928), point2=(
        -0.00751815596684402, 0.0194888769624042))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289462, 
        farPlane=0.294356, width=0.002028, height=0.000918767, cameraPosition=(
        0.0255801, 0.0824795, -0.289659), cameraTarget=(0.0255801, 0.0824795, 
        0))
    s1.Line(point1=(0.0190149209414947, 0.0288189680238755), point2=(
        0.0194231433019922, 0.028960886468667))
    s1.ParallelConstraint(entity1=g[69], entity2=g[74], addUndoState=False)
    s1.Line(point1=(0.0194231433019922, 0.028960886468667), point2=(
        0.0194541795249172, 0.0288716120956138))
    s1.PerpendicularConstraint(entity1=g[74], entity2=g[75], addUndoState=False)
    s1.Line(point1=(0.0194541795249172, 0.0288716120956138), point2=(
        0.0190477581542316, 0.0287245131803805))
    s1.setAsConstruction(objectList=(g[41], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289066, 
        farPlane=0.294752, width=0.00611937, height=0.00277232, 
        cameraPosition=(0.0421374, 0.0379096, -0.289659), cameraTarget=(
        0.0421374, 0.0379096, 0))
    s1.offset(distance=5e-05, objectList=(g[40], ), side=RIGHT)
    s1.offset(distance=5e-05, objectList=(g[40], ), side=LEFT)
    s1.Line(point1=(-0.0122215737409919, -0.00815454230747737), point2=(
        -0.013064808677882, -0.00815454230747737))
    s1.HorizontalConstraint(entity=g[79], addUndoState=False)
    s1.ParallelConstraint(entity1=g[78], entity2=g[79], addUndoState=False)
    s1.Line(point1=(-0.013064808677882, -0.00815454230747737), point2=(
        -0.013064808677882, -0.00833079521544278))
    s1.VerticalConstraint(entity=g[80], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[79], entity2=g[80], addUndoState=False)
    s1.Line(point1=(-0.013064808677882, -0.00833079521544278), point2=(
        -0.0122215737409919, -0.00825454230747737))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289382, 
        farPlane=0.294436, width=0.00285497, height=0.00129341, 
        cameraPosition=(0.00801166, 0.0493833, -0.289659), cameraTarget=(
        0.00801166, 0.0493833, 0))
    s1.Line(point1=(0.025278771669811, -0.00815454230747739), point2=(
        0.0260720809455961, -0.00815454230747739))
    s1.HorizontalConstraint(entity=g[82], addUndoState=False)
    s1.ParallelConstraint(entity1=g[78], entity2=g[82], addUndoState=False)
    s1.Line(point1=(0.0260720809455961, -0.00815454230747739), point2=(
        0.0260720809455961, -0.00822870177216828))
    s1.VerticalConstraint(entity=g[83], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[82], entity2=g[83], addUndoState=False)
    s1.Line(point1=(0.0260720809455961, -0.00822870177216828), point2=(
        0.025278771669811, -0.00825454230747739))
    s1.setAsConstruction(objectList=(g[40], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251684, 
        farPlane=0.332134, width=0.39166, height=0.177438, cameraPosition=(
        -0.0121142, 0.0621539, -0.289659), cameraTarget=(-0.0121142, 0.0621539, 
        0))
    p = mdb.models['Model-1'].parts['Spiral']
    f1, e, d2 = p.faces, p.edges, p.datums
    p.CutExtrude(sketchPlane=f1[98], sketchUpEdge=e[177], sketchPlaneSide=SIDE1, 
        sketchOrientation=BOTTOM, sketch=s1, depth=0.0019, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.294979, 
        farPlane=0.435045, width=0.0655231, height=0.0284818, 
        viewOffsetX=0.0528868, viewOffsetY=0.0391004)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.294634, 
        farPlane=0.43539, width=0.0654465, height=0.0284485, cameraPosition=(
        0.401291, 0.139752, -0.0449709), cameraUpVector=(-0.502087, 0.813039, 
        0.294749), cameraTarget=(0.0949787, 0.0566062, 0.0319199), 
        viewOffsetX=0.052825, viewOffsetY=0.0390547)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.291636, 
        farPlane=0.449013, width=0.0647806, height=0.028159, cameraPosition=(
        0.372703, 0.215526, 0.0924113), cameraUpVector=(-0.707897, 0.705268, 
        -0.0384561), cameraTarget=(0.080063, 0.0743503, 0.0594937), 
        viewOffsetX=0.0522875, viewOffsetY=0.0386573)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.29419, 
        farPlane=0.446458, width=0.0351974, height=0.0152997, 
        viewOffsetX=0.0553142, viewOffsetY=0.0333424)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.292508, 
        farPlane=0.426211, width=0.0349962, height=0.0152122, cameraPosition=(
        0.361279, 0.144816, 0.161766), cameraUpVector=(-0.554598, 0.82503, 
        -0.10838), cameraTarget=(0.0604434, 0.0618841, 0.0654723), 
        viewOffsetX=0.0549979, viewOffsetY=0.0331518)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286714, 
        farPlane=0.432005, width=0.104907, height=0.0456012, 
        viewOffsetX=0.0574256, viewOffsetY=0.0312044)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312759, 
        farPlane=0.384585, width=0.114437, height=0.0497436, cameraPosition=(
        0.0797539, 0.11245, 0.352751), cameraUpVector=(-0.10456, 0.883799, 
        -0.456033), cameraTarget=(-0.0180135, 0.0651355, 0.0447652), 
        viewOffsetX=0.062642, viewOffsetY=0.034039)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.320526, 
        farPlane=0.376818, width=0.0183255, height=0.00796577, 
        viewOffsetX=0.096983, viewOffsetY=0.037991)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.320631, 
        farPlane=0.376713, width=0.0183315, height=0.00796839, cameraPosition=(
        0.0822117, 0.106432, 0.352895), cameraUpVector=(-0.156151, 0.884439, 
        -0.439754), cameraTarget=(-0.0155557, 0.0591178, 0.0449095), 
        viewOffsetX=0.0970149, viewOffsetY=0.0380035)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.298027, 
        farPlane=0.367741, width=0.0170392, height=0.00740664, cameraPosition=(
        0.0802788, -0.00639733, 0.337666), cameraUpVector=(0.129824, 0.980026, 
        -0.150648), cameraTarget=(-0.0239114, 0.0724746, 0.0383734), 
        viewOffsetX=0.0901756, viewOffsetY=0.0353244)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.298145, 
        farPlane=0.367624, width=0.0170459, height=0.00740958, cameraPosition=(
        0.110344, -0.0673487, 0.311137), cameraUpVector=(-0.471052, 0.881504, 
        0.0325667), cameraTarget=(0.00615367, 0.0115232, 0.0118447), 
        viewOffsetX=0.0902113, viewOffsetY=0.0353384)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.299165, 
        farPlane=0.366603, width=0.00549877, height=0.00239022, 
        viewOffsetX=0.087138, viewOffsetY=0.0370739)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290935, 
        farPlane=0.373199, width=0.0053475, height=0.00232446, cameraPosition=(
        0.141714, -0.0952035, 0.288999), cameraUpVector=(-0.549972, 0.821183, 
        0.152279), cameraTarget=(0.0147457, 0.00493861, 0.00526835), 
        viewOffsetX=0.0847408, viewOffsetY=0.036054)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290151, 
        farPlane=0.373984, width=0.0132651, height=0.00576612, 
        viewOffsetX=0.0272404, viewOffsetY=-0.0173044)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, v1 = p.edges, p.vertices
    p.DatumPlaneByLinePoint(line=e1[82], point=v1[184])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.273309, 
        farPlane=0.390826, width=0.210848, height=0.0916519, 
        viewOffsetX=0.0656416, viewOffsetY=0.00949515)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Datum plane-1'].suppress()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.284632, 
        farPlane=0.379504, width=0.120218, height=0.0522566, 
        viewOffsetX=0.0613842, viewOffsetY=0.0175005)
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Datum plane-1'].resume()
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Datum plane-1'].suppress()
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Cut extrude-1'].resume()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290156, 
        farPlane=0.373979, width=0.0132105, height=0.00574239, 
        viewOffsetX=0.0414024, viewOffsetY=0.00981024)
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Datum plane-1'].suppress()
    p = mdb.models['Model-1'].parts['Spiral']
    p.features['Datum plane-2'].resume()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.281789, 
        farPlane=0.382346, width=0.099716, height=0.0433448, 
        viewOffsetX=0.0391792, viewOffsetY=-0.00816151)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Datum plane-2']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.291204, 
        farPlane=0.372931, width=0.00240397, height=0.00104497, 
        viewOffsetX=0.0315098, viewOffsetY=-0.005325)
    p = mdb.models['Model-1'].parts['Spiral']
    e = p.edges
    p.DatumPlaneByLinePoint(line=e[238], point=p.InterestingPoint(edge=e[239], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290635, 
        farPlane=0.3735, width=0.00826986, height=0.00359477, 
        viewOffsetX=0.00839121, viewOffsetY=-0.00933662)
    p = mdb.models['Model-1'].parts['Spiral']
    e1 = p.edges
    p.DatumPlaneByLinePoint(line=e1[300], point=p.InterestingPoint(edge=e1[269], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290489, 
        farPlane=0.373647, width=0.00978366, height=0.00425279, 
        viewOffsetX=-0.00858173, viewOffsetY=0.0019971)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290545, 
        farPlane=0.37359, width=0.00978556, height=0.00425361, cameraPosition=(
        0.141787, -0.0954737, 0.288871), cameraUpVector=(-0.526538, 0.837264, 
        0.147468), cameraTarget=(0.014819, 0.00466837, 0.00514018), 
        viewOffsetX=-0.0085834, viewOffsetY=0.00199749)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.320786, 
        farPlane=0.45178, width=0.0108041, height=0.00469635, cameraPosition=(
        -0.27316, -0.107024, 0.150349), cameraUpVector=(-0.0446459, 0.992942, 
        -0.109878), cameraTarget=(0.00375088, -7.63452e-07, 0.0142655), 
        viewOffsetX=-0.0094768, viewOffsetY=0.0022054)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.301103, 
        farPlane=0.471463, width=0.238242, height=0.103559, 
        viewOffsetX=0.0249805, viewOffsetY=0.0264158)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311306, 
        farPlane=0.481423, width=0.246314, height=0.107068, cameraPosition=(
        0.105361, 0.406979, 0.177979), cameraUpVector=(0.849258, -0.497067, 
        -0.178001), cameraTarget=(0.03778, 0.128793, 0.020823), 
        viewOffsetX=0.0258269, viewOffsetY=0.0273109)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.322347, 
        farPlane=0.470383, width=0.123382, height=0.053632, 
        viewOffsetX=0.0309278, viewOffsetY=0.00825687)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337087, 
        farPlane=0.489108, width=0.129024, height=0.0560844, cameraPosition=(
        -0.210856, 0.286518, 0.231124), cameraUpVector=(0.805536, 0.500657, 
        -0.316946), cameraTarget=(-0.0344318, 0.0951935, 0.0338377), 
        viewOffsetX=0.032342, viewOffsetY=0.00863443)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347501, 
        farPlane=0.478693, width=0.00833137, height=0.0036215, 
        viewOffsetX=0.000420969, viewOffsetY=0.00642733)
    p = mdb.models['Model-1'].parts['Spiral']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[9], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337249, 
        farPlane=0.488946, width=0.128851, height=0.0560095, 
        viewOffsetX=0.0451818, viewOffsetY=0.0100109)
    p = mdb.models['Model-1'].parts['Spiral']
    del p.features['Partition cell-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346891, 
        farPlane=0.479303, width=0.0146225, height=0.00635616, 
        viewOffsetX=-0.0121472, viewOffsetY=0.0382975)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:3 #fffffff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[26], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347895, 
        farPlane=0.478299, width=0.0042688, height=0.00185557, 
        viewOffsetX=-0.0145912, viewOffsetY=0.0387948)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:4 #f ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[27], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.342541, 
        farPlane=0.483653, width=0.0672508, height=0.0292328, 
        viewOffsetX=0.0253927, viewOffsetY=0.030896)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.354104, 
        farPlane=0.478767, width=0.0695208, height=0.0302195, cameraPosition=(
        0.385273, -0.0476465, 0.225883), cameraUpVector=(-0.118101, 0.986425, 
        -0.114092), cameraTarget=(0.105538, 0.0109409, 0.0678696), 
        viewOffsetX=0.0262499, viewOffsetY=0.0319389)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359489, 
        farPlane=0.473382, width=0.00760804, height=0.00330708, 
        viewOffsetX=0.0239078, viewOffsetY=0.0337642)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.340528, 
        farPlane=0.487889, width=0.00720675, height=0.00313265, 
        cameraPosition=(0.405382, -0.15623, 0.00669519), cameraUpVector=(
        0.113355, 0.982826, 0.145617), cameraTarget=(0.111895, -0.0136413, 
        0.0203345), viewOffsetX=0.0226468, viewOffsetY=0.0319833)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.339315, 
        farPlane=0.489102, width=0.0222449, height=0.00966949, 
        viewOffsetX=0.023252, viewOffsetY=0.0317852)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359552, 
        farPlane=0.477895, width=0.0235717, height=0.0102462, cameraPosition=(
        0.354268, 0.168751, 0.267126), cameraUpVector=(0.111988, 0.357762, 
        -0.927073), cameraTarget=(0.0927776, 0.0903747, 0.0878723), 
        viewOffsetX=0.0246388, viewOffsetY=0.033681)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.351261, 
        farPlane=0.486185, width=0.120222, height=0.0522586, 
        viewOffsetX=0.0279157, viewOffsetY=0.0411688)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.348897, 
        farPlane=0.48464, width=0.119413, height=0.0519069, cameraPosition=(
        0.257713, 0.231189, 0.319166), cameraUpVector=(0.231225, 0.374305, 
        -0.898015), cameraTarget=(0.0637985, 0.0981471, 0.092562), 
        viewOffsetX=0.0277278, viewOffsetY=0.0408917)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327443, 
        farPlane=0.496428, width=0.112071, height=0.0487151, cameraPosition=(
        -0.2908, 0.254855, 0.137046), cameraUpVector=(0.596622, 0.553441, 
        -0.581159), cameraTarget=(-0.0490109, 0.0687074, 0.0206879), 
        viewOffsetX=0.0260228, viewOffsetY=0.0383772)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.328864, 
        farPlane=0.495006, width=0.110277, height=0.0479353, 
        viewOffsetX=0.0317428, viewOffsetY=0.0442818)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.337301, 
        farPlane=0.476579, width=0.113106, height=0.0491651, cameraPosition=(
        -0.247158, 0.163416, 0.266029), cameraUpVector=(0.0967602, 0.603506, 
        -0.791466), cameraTarget=(-0.0222018, 0.0415462, 0.0630646), 
        viewOffsetX=0.0325572, viewOffsetY=0.0454179)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346501, 
        farPlane=0.467379, width=0.00859392, height=0.00373563, 
        viewOffsetX=-0.000479209, viewOffsetY=0.0355141)
    p = mdb.models['Model-1'].parts['Spiral']
    e, v2 = p.edges, p.vertices
    p.DatumPlaneByLinePoint(line=e[237], point=v2[73])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333202, 
        farPlane=0.472427, width=0.00770461, height=0.00334906, 
        viewOffsetX=-0.00132815, viewOffsetY=0.0345334)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, v1 = p.edges, p.vertices
    p.DatumPlaneByLinePoint(line=e1[235], point=v1[82])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.33277, 
        farPlane=0.472882, width=0.0121599, height=0.00528572, 
        viewOffsetX=0.024996, viewOffsetY=0.0532945)
    p = mdb.models['Model-1'].parts['Spiral']
    e, v2 = p.edges, p.vertices
    p.DatumPlaneByLinePoint(line=e[188], point=v2[68])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.33374, 
        farPlane=0.477159, width=0.00215663, height=0.000937448, 
        viewOffsetX=0.0224441, viewOffsetY=0.0549168)
    p = mdb.models['Model-1'].parts['Spiral']
    e1, v1 = p.edges, p.vertices
    p.DatumPlaneByLinePoint(line=e1[189], point=v1[61])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.319726, 
        farPlane=0.491173, width=0.147087, height=0.0639362, 
        viewOffsetX=0.088585, viewOffsetY=0.0498512)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.320509, 
        farPlane=0.49039, width=0.147447, height=0.0640928, cameraPosition=(
        -0.24573, 0.162188, 0.268349), cameraUpVector=(0.0812552, 0.592067, 
        -0.801782), cameraTarget=(-0.0207738, 0.0403184, 0.0653846), 
        viewOffsetX=0.0888019, viewOffsetY=0.0499732)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408706, 
        farPlane=0.551412, width=0.188022, height=0.0817298, cameraPosition=(
        0.107935, 0.335253, 0.394888), cameraUpVector=(-0.148227, 0.523163, 
        -0.839243), cameraTarget=(0.0202368, 0.132559, 0.154313), 
        viewOffsetX=0.113238, viewOffsetY=0.0637247)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.420567, 
        farPlane=0.539551, width=0.0162835, height=0.00707814, 
        viewOffsetX=0.0982942, viewOffsetY=0.0713711)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.419423, 
        farPlane=0.544299, width=0.0162392, height=0.00705889, cameraPosition=(
        0.148111, 0.319545, 0.399318), cameraUpVector=(-0.191524, 0.55565, 
        -0.809056), cameraTarget=(0.0361132, 0.127976, 0.159714), 
        viewOffsetX=0.0980269, viewOffsetY=0.071177)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.416066, 
        farPlane=0.547657, width=0.0564755, height=0.0245489, 
        viewOffsetX=0.104521, viewOffsetY=0.0704754)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.417977, 
        farPlane=0.582487, width=0.0567349, height=0.0246617, cameraPosition=(
        0.299061, 0.325992, 0.34683), cameraUpVector=(-0.540721, 0.532996, 
        -0.650796), cameraTarget=(0.117108, 0.124293, 0.165549), 
        viewOffsetX=0.105001, viewOffsetY=0.070799)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.422382, 
        farPlane=0.578081, width=0.00760702, height=0.00330664, 
        viewOffsetX=0.0817823, viewOffsetY=0.0772976)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[56], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.421299, 
        farPlane=0.582899, width=0.00869286, height=0.00377864, 
        viewOffsetX=0.0818289, viewOffsetY=0.0769772)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.421349, 
        farPlane=0.582848, width=0.0086939, height=0.00377909, cameraPosition=(
        0.30166, 0.323972, 0.346469), cameraUpVector=(-0.557868, 0.534314, 
        -0.635053), cameraTarget=(0.119707, 0.122273, 0.165188), 
        viewOffsetX=0.0818386, viewOffsetY=0.0769864)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.422998, 
        farPlane=0.573612, width=0.00872794, height=0.00379388, 
        cameraPosition=(0.247165, 0.325767, 0.374783), cameraUpVector=(
        -0.518034, 0.521667, -0.677868), cameraTarget=(0.0958478, 0.119885, 
        0.171392), viewOffsetX=0.082159, viewOffsetY=0.0772878)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.419488, 
        farPlane=0.577121, width=0.0501592, height=0.0218033, 
        viewOffsetX=0.0814873, viewOffsetY=0.0780602)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.433133, 
        farPlane=0.536592, width=0.0517908, height=0.0225126, cameraPosition=(
        0.0354323, 0.292227, 0.431665), cameraUpVector=(-0.276569, 0.545994, 
        -0.790823), cameraTarget=(0.00491424, 0.0982185, 0.17074), 
        viewOffsetX=0.0841379, viewOffsetY=0.0805994)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.423417, 
        farPlane=0.546308, width=0.16607, height=0.0721877, 
        viewOffsetX=0.0934938, viewOffsetY=0.0736381)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.40815, 
        farPlane=0.523671, width=0.160082, height=0.0695847, cameraPosition=(
        -0.126627, 0.167984, 0.429088), cameraUpVector=(-0.0986515, 0.710468, 
        -0.69678), cameraTarget=(-0.0518431, 0.0443563, 0.136213), 
        viewOffsetX=0.0901225, viewOffsetY=0.0709828)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.42278, 
        farPlane=0.509039, width=0.00553914, height=0.00240777, 
        viewOffsetX=0.119911, viewOffsetY=0.0837847)
    p = mdb.models['Model-1'].parts['Spiral']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[55], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.422764, 
        farPlane=0.509059, width=0.0050596, height=0.00219932, 
        viewOffsetX=0.108446, viewOffsetY=0.0860686)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[52], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.417378, 
        farPlane=0.509114, width=0.00562656, height=0.00244577, 
        viewOffsetX=0.0881756, viewOffsetY=0.0819214)
    p = mdb.models['Model-1'].parts['Spiral']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[58], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.407161, 
        farPlane=0.517954, width=0.0969308, height=0.0421341, 
        viewOffsetX=0.101336, viewOffsetY=0.0754502)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.403209, 
        farPlane=0.589279, width=0.09599, height=0.0417252, cameraPosition=(
        0.425908, 0.228487, 0.299321), cameraUpVector=(-0.342355, 0.671349, 
        -0.65733), cameraTarget=(0.140895, 0.125842, 0.177322), 
        viewOffsetX=0.100353, viewOffsetY=0.0747179)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.401688, 
        farPlane=0.598918, width=0.0956279, height=0.0415678, cameraPosition=(
        0.306933, 0.350277, 0.338461), cameraUpVector=(-0.408639, 0.508066, 
        -0.75821), cameraTarget=(0.0898168, 0.16073, 0.18489), 
        viewOffsetX=0.0999744, viewOffsetY=0.074436)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.409591, 
        farPlane=0.591013, width=0.00873038, height=0.00379495, 
        viewOffsetX=0.0992794, viewOffsetY=0.0730779)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[53], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.410146, 
        farPlane=0.590458, width=0.00300944, height=0.00130815, 
        viewOffsetX=0.0865278, viewOffsetY=0.0686214)
    p = mdb.models['Model-1'].parts['Spiral']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[59], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.410284, 
        farPlane=0.590321, width=0.00159118, height=0.000691658, 
        viewOffsetX=0.0679536, viewOffsetY=0.0375069)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:4 #fff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[31], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.410018, 
        farPlane=0.590586, width=0.00433198, height=0.00188304, 
        viewOffsetX=0.0680619, viewOffsetY=0.0377214)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:4 #1fffff ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[32], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.410264, 
        farPlane=0.59034, width=0.00179213, height=0.000779006, 
        viewOffsetX=0.0741235, viewOffsetY=0.0571089)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:4 #1fffffff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[34], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408785, 
        farPlane=0.591819, width=0.0192909, height=0.00838542, 
        viewOffsetX=0.0798541, viewOffsetY=0.0577161)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.388675, 
        farPlane=0.420112, width=0.136875, height=0.0594972, 
        viewOffsetX=-0.0112507, viewOffsetY=0.0143739)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.379013, 
        farPlane=0.427527, width=0.133472, height=0.0580181, cameraPosition=(
        0.0917327, 0.0673659, 0.402728), cameraUpVector=(0.0282301, 0.999399, 
        -0.0201369), cameraTarget=(0.0442825, 0.0606156, 0.00118401), 
        viewOffsetX=-0.010971, viewOffsetY=0.0140166)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330194, 
        farPlane=0.475074, width=0.11628, height=0.050545, cameraPosition=(
        0.255509, 0.182739, 0.323003), cameraUpVector=(-0.109551, 0.951211, 
        -0.288439), cameraTarget=(0.0441636, 0.0606284, 0.000579476), 
        viewOffsetX=-0.00955786, viewOffsetY=0.0122112)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.307737, 
        farPlane=0.497532, width=0.399069, height=0.173468, 
        viewOffsetX=0.0873861, viewOffsetY=-0.0120706)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330193, 
        farPlane=0.499035, width=0.00545683, height=0.00237199, 
        viewOffsetX=-0.00155295, viewOffsetY=0.000689875)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:5 #3f ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[33], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.302098, 
        farPlane=0.52713, width=0.332533, height=0.144546, viewOffsetX=0.05565, 
        viewOffsetY=-0.00736239)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['User-2'])
    session.viewports['Viewport: 1'].view.setValues(session.views['User-3'])
    session.viewports['Viewport: 1'].view.setValues(session.views['User-3'])
    session.viewports['Viewport: 1'].view.setValues(session.views['User-4'])
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330512, 
        farPlane=0.498716, width=0.00216796, height=0.000942374, 
        viewOffsetX=-0.00398231, viewOffsetY=0.0261585)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:5 #3fff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[40], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330469, 
        farPlane=0.498759, width=0.00261253, height=0.00113562, 
        viewOffsetX=-0.00360491, viewOffsetY=0.0265375)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:5 #7fffff ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[38], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.32993, 
        farPlane=0.499298, width=0.00817402, height=0.0035531, 
        viewOffsetX=0.00897466, viewOffsetY=0.0280732)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:5 #7fffffff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[39], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330064, 
        farPlane=0.499164, width=0.00768579, height=0.00334088, 
        viewOffsetX=0.00912338, viewOffsetY=0.0282471)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:6 #ff ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[37], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.329985, 
        farPlane=0.499243, width=0.00760223, height=0.00330456, 
        viewOffsetX=0.0195929, viewOffsetY=0.0226077)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:6 #ffff ]', ), )
    d2 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d2[35], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330038, 
        farPlane=0.49919, width=0.00705982, height=0.00306878, 
        viewOffsetX=0.0208934, viewOffsetY=0.0230676)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#ffffffff:6 #1ffffff ]', ), )
    d1 = p.datums
    p.PartitionFaceByDatumPlane(datumPlane=d1[36], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.326265, 
        farPlane=0.502963, width=0.051981, height=0.0225953, 
        viewOffsetX=0.0206543, viewOffsetY=0.020684)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.31343, 
        farPlane=0.498759, width=0.0499361, height=0.0217064, cameraPosition=(
        0.41896, -0.0927658, 0.0727879), cameraUpVector=(-0.606209, 0.135918, 
        0.783605), cameraTarget=(0.0555099, 0.0577997, -0.0581283), 
        viewOffsetX=0.0198418, viewOffsetY=0.0198703)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.312942, 
        farPlane=0.499248, width=0.0539142, height=0.0234356, 
        viewOffsetX=0.036625, viewOffsetY=0.0323557)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.29564, 
        farPlane=0.501163, width=0.0509335, height=0.0221399, cameraPosition=(
        0.385056, -0.158481, 0.00308227), cameraUpVector=(-0.618807, 
        -0.0462354, 0.784181), cameraTarget=(0.0521793, 0.0778272, -0.0694213), 
        viewOffsetX=0.0346001, viewOffsetY=0.0305669)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286604, 
        farPlane=0.5102, width=0.161962, height=0.0704019, 
        viewOffsetX=0.0215206, viewOffsetY=0.0162907)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.285839, 
        farPlane=0.510964, width=0.16153, height=0.0702141, cameraPosition=(
        0.404063, -0.13211, 0.00176785), cameraUpVector=(-0.829694, -0.533929, 
        0.162877), cameraTarget=(0.0711865, 0.104199, -0.0707357), 
        viewOffsetX=0.0214632, viewOffsetY=0.0162473)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.297848, 
        farPlane=0.498955, width=0.0279791, height=0.012162, 
        viewOffsetX=0.0483737, viewOffsetY=0.0100666)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280507, 
        farPlane=0.481454, width=0.0263502, height=0.011454, cameraPosition=(
        0.300106, -0.193277, 0.154687), cameraUpVector=(0.575678, 0.701851, 
        -0.419522), cameraTarget=(0.0675928, 0.135669, 0.0565141), 
        viewOffsetX=0.0455574, viewOffsetY=0.0094805)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.329782, 
        farPlane=0.506438, width=0.0309791, height=0.0134661, cameraPosition=(
        0.0992265, 0.473569, 0.0517436), cameraUpVector=(0.154762, -0.249534, 
        -0.955919), cameraTarget=(0.0173751, 0.0705338, -0.000876486), 
        viewOffsetX=0.0535603, viewOffsetY=0.0111459)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331115, 
        farPlane=0.505106, width=0.0124978, height=0.00543255, 
        viewOffsetX=0.0509087, viewOffsetY=0.0127333)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333009, 
        farPlane=0.496308, width=0.0125692, height=0.00546363, cameraPosition=(
        0.0570895, 0.475454, 0.0306173), cameraUpVector=(0.103636, -0.284077, 
        -0.953184), cameraTarget=(0.0163685, 0.0637088, 0.00391035), 
        viewOffsetX=0.0511999, viewOffsetY=0.0128062)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332878, 
        farPlane=0.496158, width=0.0125643, height=0.00546148, cameraPosition=(
        0.0588862, 0.472733, 0.0559957), cameraUpVector=(0.101259, -0.226008, 
        -0.968848), cameraTarget=(0.016403, 0.063545, 0.00436146), 
        viewOffsetX=0.0511797, viewOffsetY=0.0128012)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.321681, 
        farPlane=0.507356, width=0.143753, height=0.0624867, 
        viewOffsetX=0.0593529, viewOffsetY=0.000686815)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.28116, 
        farPlane=0.453141, width=0.125645, height=0.0546156, cameraPosition=(
        -0.314689, -0.0443943, -0.0376241), cameraUpVector=(0.397985, 0.228489, 
        -0.888482), cameraTarget=(0.0976862, -0.019975, -0.00217629), 
        viewOffsetX=0.0518765, viewOffsetY=0.0006003)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.266813, 
        farPlane=0.490657, width=0.119233, height=0.0518287, cameraPosition=(
        -0.189643, -0.246718, 0.0125063), cameraUpVector=(-0.037539, 0.439855, 
        -0.897284), cameraTarget=(0.121006, 0.025838, -0.0209062), 
        viewOffsetX=0.0492293, viewOffsetY=0.000569667)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268981, 
        farPlane=0.488489, width=0.108907, height=0.0473401, 
        viewOffsetX=0.0535232, viewOffsetY=-0.00248542)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.275729, 
        farPlane=0.494741, width=0.111639, height=0.0485277, cameraPosition=(
        0.384027, -0.138938, -0.00567002), cameraUpVector=(-0.0250934, 0.66346, 
        -0.747791), cameraTarget=(0.0704079, 0.125473, 0.0546301), 
        viewOffsetX=0.054866, viewOffsetY=-0.00254777)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268416, 
        farPlane=0.502054, width=0.200328, height=0.0870793, 
        viewOffsetX=0.0805663, viewOffsetY=-0.0115472)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.313221, 
        farPlane=0.528481, width=0.233768, height=0.101615, cameraPosition=(
        -0.330238, -0.145997, -0.0949206), cameraUpVector=(0.0448047, 0.852233, 
        -0.52124), cameraTarget=(0.0608359, -0.00843415, -0.101533), 
        viewOffsetX=0.0940147, viewOffsetY=-0.0134747)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332769, 
        farPlane=0.532175, width=0.248358, height=0.107957, cameraPosition=(
        -0.300988, -0.0859849, 0.243382), cameraUpVector=(0.294072, 0.864442, 
        0.407753), cameraTarget=(-0.0515283, 0.113664, -0.0208455), 
        viewOffsetX=0.0998821, viewOffsetY=-0.0143157)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.342576, 
        farPlane=0.512781, width=0.255678, height=0.111139, cameraPosition=(
        -0.333507, -0.0213077, 0.218051), cameraUpVector=(0.0536156, 0.983314, 
        -0.173835), cameraTarget=(-0.0458794, 0.0524, -0.071334), 
        viewOffsetX=0.102826, viewOffsetY=-0.0147376)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.386207, 
        farPlane=0.477575, width=0.288242, height=0.125294, cameraPosition=(
        -0.171471, 0.0904199, 0.39239), cameraUpVector=(0.124697, 0.926131, 
        -0.355993), cameraTarget=(-0.0708165, 0.0716579, -0.00938446), 
        viewOffsetX=0.115922, viewOffsetY=-0.0166146)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='plywood')
    mdb.models['Model-1'].materials['plywood'].Elastic(table=((7000000000.0, 0.13), 
        ))
    mdb.models['Model-1'].Material(name='tape')
    mdb.models['Model-1'].materials['tape'].Elastic(table=((500000000.0, 0.34), ))


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.393529, 
        farPlane=0.484541, width=0.0506293, height=0.0220077, 
        viewOffsetX=0.0896581, viewOffsetY=-0.0181222)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.396729, 
        farPlane=0.481341, width=0.0132992, height=0.00578093, 
        viewOffsetX=0.0809797, viewOffsetY=-0.0184742)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#0:4 #20000 ]', ), )
    p.Set(faces=faces, name='tape_1')
    p1 = mdb.models['Model-1'].parts['Spiral']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.394287, 
        farPlane=0.483783, width=0.0417878, height=0.0181644, 
        viewOffsetX=0.084324, viewOffsetY=-0.0164347)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#0:4 #20000 ]', ), )
    p.Set(faces=faces, name='tape_1')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397, 
        farPlane=0.481069, width=0.00895829, height=0.00389401, 
        viewOffsetX=0.0794251, viewOffsetY=-0.0179032)
    p1 = mdb.models['Model-1'].parts['Spiral']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397565, 
        farPlane=0.480505, width=0.0031334, height=0.00136203, 
        viewOffsetX=0.0784168, viewOffsetY=-0.0181116)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=HIDDEN)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397427, 
        farPlane=0.480643, width=0.00515959, height=0.00224278, 
        viewOffsetX=0.0789825, viewOffsetY=-0.0180686)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
    del mdb.models['Model-1'].parts['Spiral'].sets['tape_1']
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397391, 
        farPlane=0.480679, width=0.00492943, height=0.00214274, 
        viewOffsetX=0.0788895, viewOffsetY=-0.0183594)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.39768, 
        farPlane=0.48039, width=0.00194998, height=0.000847621, 
        viewOffsetX=0.0780853, viewOffsetY=-0.0182451)
    session.viewports['Viewport: 1'].setColor(translucency=0.45)
    session.viewports['Viewport: 1'].setColor(translucency=0.35)
    session.viewports['Viewport: 1'].setColor(translucency=0.3)
    session.viewports['Viewport: 1'].setColor(translucency=0.25)
    session.viewports['Viewport: 1'].setColor(translucency=0.15)
    session.viewports['Viewport: 1'].setColor(translucency=0)
    session.viewports['Viewport: 1'].setColor(translucency=0.05)
    session.viewports['Viewport: 1'].setColor(translucency=0.1)
    session.viewports['Viewport: 1'].setColor(translucency=0.25)
    session.viewports['Viewport: 1'].setColor(translucency=0.3)
    session.viewports['Viewport: 1'].setColor(translucency=0.5)
    session.viewports['Viewport: 1'].setColor(translucency=0.55)
    session.viewports['Viewport: 1'].setColor(translucency=0.7)
    session.viewports['Viewport: 1'].setColor(translucency=0.75)
    session.viewports['Viewport: 1'].setColor(translucency=0.8)
    session.viewports['Viewport: 1'].setColor(translucency=0.9)
    session.viewports['Viewport: 1'].setColor(translucency=0.95)
    session.viewports['Viewport: 1'].setColor(translucency=1)
    session.viewports['Viewport: 1'].setColor(translucency=0.95)
    session.viewports['Viewport: 1'].setColor(translucency=0.65)
    session.viewports['Viewport: 1'].setColor(translucency=0.6)
    session.viewports['Viewport: 1'].setColor(translucency=0.55)
    session.viewports['Viewport: 1'].setColor(translucency=0.5)
    session.viewports['Viewport: 1'].setColor(translucency=0.45)
    session.viewports['Viewport: 1'].setColor(translucency=0.4)
    session.viewports['Viewport: 1'].setColor(translucency=0.35)
    session.viewports['Viewport: 1'].setColor(translucency=0.3)
    session.viewports['Viewport: 1'].setColor(translucency=0.35)
    session.viewports['Viewport: 1'].setColor(translucency=0.35)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397189, 
        farPlane=0.480881, width=0.00793361, height=0.0034486, 
        viewOffsetX=0.0793799, viewOffsetY=-0.0187837)
    p = mdb.models['Model-1'].parts['Spiral']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(cells=cells, name='Set-1')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Spiral']
    region = p.sets['Set-1']
    p = mdb.models['Model-1'].parts['Spiral']
    p.SectionAssignment(region=region, sectionName='plywood_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    del mdb.models['Model-1'].parts['Spiral'].sectionAssignments[0]
    del mdb.models['Model-1'].parts['Spiral'].sets['Set-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.394887, 
        farPlane=0.483183, width=0.0307704, height=0.0133754, 
        viewOffsetX=0.0893155, viewOffsetY=-0.0197836)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397338, 
        farPlane=0.480732, width=0.00547521, height=0.00237998, 
        viewOffsetX=0.0792293, viewOffsetY=-0.0184313)
    p = mdb.models['Model-1'].parts['Spiral']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#0 #20000000 ]', ), )
    p.Set(faces=faces, name='Set-1')
    p1 = mdb.models['Model-1'].parts['Spiral']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['Spiral'].sets['Set-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.396414, 
        farPlane=0.481656, width=0.0169806, height=0.00738118, 
        viewOffsetX=0.0824469, viewOffsetY=-0.0179774)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.416311, 
        farPlane=0.445748, width=0.0178329, height=0.00775166, cameraPosition=(
        -0.114886, 0.0903692, 0.417167), cameraUpVector=(0.0935962, 0.926963, 
        -0.363289), cameraTarget=(-0.0684972, 0.0734419, 0.00550199), 
        viewOffsetX=0.0865852, viewOffsetY=-0.0188797)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.414535, 
        farPlane=0.447524, width=0.0361009, height=0.0156924, 
        viewOffsetX=0.0838482, viewOffsetY=-0.0192316)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.414568, 
        farPlane=0.447491, width=0.0361038, height=0.0156937, cameraPosition=(
        -0.114395, 0.0919969, 0.417155), cameraUpVector=(0.111362, 0.925799, 
        -0.361239), cameraTarget=(-0.0680058, 0.0750696, 0.00549043), 
        viewOffsetX=0.0838548, viewOffsetY=-0.0192332)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.323195, 
        farPlane=0.497558, width=0.0281463, height=0.0122347, cameraPosition=(
        0.402965, -0.013627, 0.205442), cameraUpVector=(0.0871515, 0.853149, 
        -0.514336), cameraTarget=(0.0294443, 0.104853, 0.0699753), 
        viewOffsetX=0.0653727, viewOffsetY=-0.0149941)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.323914, 
        farPlane=0.496839, width=0.028209, height=0.0122619, cameraPosition=(
        0.399032, -0.0200759, 0.210647), cameraUpVector=(0.0707304, 0.901653, 
        -0.426636), cameraTarget=(0.025511, 0.0984041, 0.0751803), 
        viewOffsetX=0.0655182, viewOffsetY=-0.0150275)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.343053, 
        farPlane=0.499512, width=0.0298758, height=0.0129865, cameraPosition=(
        -0.379229, 0.0689481, 0.0522271), cameraUpVector=(0.386058, 0.716049, 
        0.581578), cameraTarget=(0.0232745, 0.1161, -0.0353778), 
        viewOffsetX=0.0693895, viewOffsetY=-0.0159154)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336771, 
        farPlane=0.505795, width=0.103182, height=0.0448512, 
        viewOffsetX=0.0693374, viewOffsetY=-0.0163082)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333204, 
        farPlane=0.501644, width=0.102088, height=0.0443761, cameraPosition=(
        -0.381232, 0.0695402, 0.0199249), cameraUpVector=(0.321118, 0.81914, 
        -0.475282), cameraTarget=(0.0202423, 0.0262768, -0.0741708), 
        viewOffsetX=0.0686029, viewOffsetY=-0.0161355)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341829, 
        farPlane=0.49357, width=0.104731, height=0.0455248, cameraPosition=(
        -0.289079, 0.172433, 0.241562), cameraUpVector=(0.379093, 0.81981, 
        -0.429186), cameraTarget=(-0.0171435, 0.0619602, -0.0512755), 
        viewOffsetX=0.0703787, viewOffsetY=-0.0165532)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.350355, 
        farPlane=0.485043, width=0.00804806, height=0.00349835, 
        viewOffsetX=0.0503529, viewOffsetY=-0.0167582)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    p = mdb.models['Model-1'].parts['Spiral']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34462, 
        farPlane=0.490778, width=0.0758761, height=0.0343749, 
        viewOffsetX=0.0496555, viewOffsetY=-0.0146349)
    mdb.save()
    mdb.save()
    mdb.save()
    mdb.save()


