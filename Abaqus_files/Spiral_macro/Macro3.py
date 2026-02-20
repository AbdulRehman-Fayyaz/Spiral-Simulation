# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro3():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.19679, 
        farPlane=0.384041, width=0.131465, height=0.0589965, 
        viewOffsetX=0.0271409, viewOffsetY=0.0119905)
    p = mdb.models['Model-1'].parts['Part-1']
    f1, e1 = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f1[76], sketchUpEdge=e1[215], 
        sketchPlaneSide=SIDE1, sketchOrientation=LEFT, origin=(0.035232, 
        0.048748, 0.0045))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.29, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=4)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.264628, 
        farPlane=0.320424, width=0.118542, height=0.0531973, cameraPosition=(
        0.0225591, 0.0507062, 0.294776), cameraTarget=(0.0225591, 0.0507062, 
        0.0045))
    s1.Line(point1=(-0.03675, -0.00175), point2=(-0.0266183835763536, 
        -0.00393628633658523))
    s1.Line(point1=(-0.0266183835763536, -0.00393628633658523), point2=(
        0.0104624276316472, -0.0104746338191126))
    s1.Line(point1=(0.0104624276316472, -0.0104746338191126), point2=(
        0.0264052773354706, -0.0132857883712632))
    s1.ParallelConstraint(entity1=g[41], entity2=g[42], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240182, 
        farPlane=0.344869, width=0.231528, height=0.103901, cameraPosition=(
        0.0361585, 0.0878754, 0.294776), cameraTarget=(0.0361585, 0.0878754, 
        0.0045))
    s1.Line(point1=(-0.02975, 0.04375), point2=(-0.0139938695315414, 
        0.0315370584842518))
    s1.Line(point1=(-0.0139938695315414, 0.0315370584842518), point2=(
        0.0106628693203534, 0.0175357729503602))
    s1.Line(point1=(0.0106628693203534, 0.0175357729503602), point2=(0.03325, 
        0.00470971075520188))
    s1.ParallelConstraint(entity1=g[44], entity2=g[45], addUndoState=False)
    s1.Line(point1=(-0.007, 0.063), point2=(0.00391948006474348, 
        0.0535166552424587))
    s1.Line(point1=(0.00391948006474348, 0.0535166552424587), point2=(
        0.0178774315363945, 0.0373576197301838))
    s1.Line(point1=(0.0178774315363945, 0.0373576197301838), point2=(
        0.0367500000002192, 0.0155089620214446))
    s1.ParallelConstraint(entity1=g[47], entity2=g[48], addUndoState=False)
    s1.Line(point1=(0.01575, 0.0805), point2=(0.0221780431667136, 
        0.0645875048676366))
    s1.Line(point1=(0.0221780431667136, 0.0645875048676366), point2=(
        0.0280007482621347, 0.0495989570058417))
    s1.Line(point1=(0.0280007482621347, 0.0495989570058417), point2=(
        0.0368768678821425, 0.0267504456055576))
    s1.ParallelConstraint(entity1=g[50], entity2=g[51], addUndoState=False)
    s1.Line(point1=(0.03675, 0.08225), point2=(0.0379271711953188, 
        0.0678317964655298))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.273861, 
        farPlane=0.31119, width=0.0758671, height=0.0340463, cameraPosition=(
        0.0662774, 0.0932508, 0.294776), cameraTarget=(0.0662774, 0.0932508, 
        0.0045))
    s1.Line(point1=(0.0379271711953188, 0.0678317964655298), point2=(
        0.0382737250482658, 0.0557277414871095))
    s1.Line(point1=(0.0382737250482658, 0.0557277414871095), point2=(
        0.0387861102982114, 0.0378317083518596))
    s1.ParallelConstraint(entity1=g[53], entity2=g[54], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.227659, 
        farPlane=0.357393, width=0.28941, height=0.129876, cameraPosition=(
        0.0575227, 0.0597899, 0.294776), cameraTarget=(0.0575227, 0.0597899, 
        0.0045))
    s1.dragEntity(entity=v[40], points=((-0.02975, 0.04375), (-0.02975, 0.04375), (
        -0.03325, 0.0385), (-0.0315, 0.042), (-0.0315, 0.042)))
    s1.dragEntity(entity=v[42], points=((-0.007, 0.063), (-0.007, 0.063), (-0.007, 
        0.06825)))
    s1.dragEntity(entity=v[42], points=((-0.007, 0.06825), (-0.007, 0.06825), (
        -0.0105, 0.06475), (-0.0105, 0.06475), (-0.00875, 0.0665), (-0.00875, 
        0.0665)))
    session.viewports['Viewport: 1'].view.setValues(farPlane=0.344869, 
        width=0.231528, height=0.103901, cameraPosition=(0.0694062, 0.0840689, 
        0.294776), cameraTarget=(0.0694062, 0.0840689, 0.0045))
    s1.dragEntity(entity=v[45], points=((0.0368768678821425, 0.0267504456055576), (
        0.03675, 0.02625), (0.035, 0.03325), (0.03325, 0.03675), (0.03325, 
        0.0385), (0.03325, 0.042), (0.0315, 0.04375), (0.03325, 0.04025), (
        0.03325, 0.04025)))
    s1.dragEntity(entity=v[47], points=((0.0387861102982114, 0.0378317083518596), (
        0.0385, 0.0385), (0.04025, 0.04375), (0.04025, 0.0455), (0.04025, 
        0.04725), (0.0385, 0.049), (0.0385, 0.04725), (0.0385, 0.04375), (
        0.04025, 0.042), (0.04025, 0.0385), (0.04025, 0.03675), (0.04025, 
        0.035)))
    s1.dragEntity(entity=v[45], points=((0.0318446846254298, 0.0397040673941442), (
        0.0315, 0.04025), (0.035, 0.035), (0.03675, 0.03325), (0.03675, 
        0.0315), (0.03675, 0.02975)))
    s1.dragEntity(entity=v[47], points=((0.0388683181902628, 0.0349604407650523), (
        0.0385, 0.035), (0.0385, 0.0315), (0.0385, 0.0315)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.223485, 
        farPlane=0.361567, width=0.482351, height=0.216461, cameraPosition=(
        0.0790215, 0.099644, 0.294776), cameraTarget=(0.0790215, 0.099644, 
        0.0045))
    s1.dragEntity(entity=v[39], points=((0.0264052773354706, -0.0132857883712632), 
        (0.02625, -0.014), (0.035, -0.01575), (0.0385, -0.0175), (0.042, 
        -0.01925)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.26839, 
        farPlane=0.316662, width=0.101156, height=0.0453951, cameraPosition=(
        0.0225289, 0.0628718, 0.294776), cameraTarget=(0.0225289, 0.0628718, 
        0.0045))
    s1.dragEntity(entity=v[38], points=((-0.03675, -0.00175), (-0.03675, -0.00175), 
        (-0.0385, -0.00175), (-0.04025, -0.00175), (-0.042, -0.00175), (
        -0.04375, -0.00175), (-0.0455, -0.00175), (-0.0455, 0.0), (-0.0455, 
        0.0), (-0.0455, 0.0), (-0.04725, 0.0)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239907, 
        farPlane=0.345145, width=0.232803, height=0.104473, cameraPosition=(
        0.0865959, 0.0746718, 0.294776), cameraTarget=(0.0865959, 0.0746718, 
        0.0045))
    s1.offset(distance=0.00025, objectList=(g[40], g[41], g[42], g[43], g[44], 
        g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], g[53], g[54]), 
        side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.287714, 
        farPlane=0.297338, width=0.0118427, height=0.00531457, cameraPosition=(
        0.0439374, 0.0372643, 0.294776), cameraTarget=(0.0439374, 0.0372643, 
        0.0045))
    s1.offset(distance=0.00025, objectList=(g[40], g[41], g[42], g[43], g[44], 
        g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], g[53], g[54]), 
        side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.289188, 
        farPlane=0.295863, width=0.00502603, height=0.00225549, 
        cameraPosition=(0.0439529, 0.0367428, 0.294776), cameraTarget=(
        0.0439529, 0.0367428, 0.0045))
    s1.setAsConstruction(objectList=(g[40], g[41], g[42], g[45], g[44], g[47], 
        g[48], g[50], g[51], g[53], g[54], g[52], g[49], g[46], g[43]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250266, 
        farPlane=0.334786, width=0.288942, height=0.129666, cameraPosition=(
        0.0847388, 0.0342242, 0.294776), cameraTarget=(0.0847388, 0.0342242, 
        0.0045))
    s1.EllipseByCenterPerimeter(center=(0.0945, 0.014), axisPoint1=(
        0.0178675610176696, 0.0137320962571392), axisPoint2=(0.028, -0.0315))
    s1.CoincidentConstraint(entity1=v[88], entity2=g[75], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.192596, 
        farPlane=0.392456, width=0.451471, height=0.202603, cameraPosition=(
        0.0995961, 0.0228446, 0.294776), cameraTarget=(0.0995961, 0.0228446, 
        0.0045))
    s1.EllipseByCenterPerimeter(center=(0.0875, -0.04375), axisPoint1=(
        -0.00383552764332209, 0.0611058204781062), axisPoint2=(-0.0525, 
        -0.0385))
    s1.CoincidentConstraint(entity1=v[91], entity2=g[61], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.258268, 
        farPlane=0.326784, width=0.147938, height=0.066389, cameraPosition=(
        0.0915215, 0.0384299, 0.294776), cameraTarget=(0.0915215, 0.0384299, 
        0.0045))
    s1.autoTrimCurve(curve1=g[85], point1=(0.0490624055815442, 
        -0.0222965761146848))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.277165, 
        farPlane=0.307886, width=0.0605955, height=0.0271929, cameraPosition=(
        0.0767999, 0.0327845, 0.294776), cameraTarget=(0.0767999, 0.0327845, 
        0.0045))
    s1.autoTrimCurve(curve1=g[42], point1=(0.0384087724252112, 
        -0.0156759056375779))
    s1.autoTrimCurve(curve1=g[57], point1=(0.0379598243784804, 
        -0.0150272669833252))
    s1.autoTrimCurve(curve1=g[72], point1=(0.038059591005002, -0.0149773712468698))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286839, 
        farPlane=0.298213, width=0.0158847, height=0.00712847, cameraPosition=(
        0.0700838, 0.0290094, 0.294776), cameraTarget=(0.0700838, 0.0290094, 
        0.0045))
    s1.autoTrimCurve(curve1=g[89], point1=(0.0337955912044055, 
        -0.0137808051983119))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262962, 
        farPlane=0.322089, width=0.126241, height=0.056652, cameraPosition=(
        0.0893018, 0.0424107, 0.294776), cameraTarget=(0.0893018, 0.0424107, 
        0.0045))
    s1.autoTrimCurve(curve1=g[45], point1=(0.0289091787786799, 
        0.00655324145919386))
    s1.autoTrimCurve(curve1=g[60], point1=(0.0291170267542765, 
        0.00821641671766752))
    s1.autoTrimCurve(curve1=g[75], point1=(0.0283895727783333, 
        0.00780062269585104))
    s1.autoTrimCurve(curve1=g[48], point1=(0.0342091820657595, 0.019754704867549))
    s1.autoTrimCurve(curve1=g[63], point1=(0.0331699644075061, 0.0191310169418076))
    s1.autoTrimCurve(curve1=g[78], point1=(0.0337934935088839, 0.0200665566918603))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.253858, 
        farPlane=0.331194, width=0.168321, height=0.075536, cameraPosition=(
        0.122322, 0.0604036, 0.294776), cameraTarget=(0.122322, 0.0604036, 
        0.0045))
    s1.autoTrimCurve(curve1=g[51], point1=(0.0350188830230138, 0.032307911226127))
    s1.autoTrimCurve(curve1=g[66], point1=(0.0334947004613207, 0.0330009028630977))
    s1.autoTrimCurve(curve1=g[81], point1=(0.0341875145264069, 0.0338324940012838))
    s1.autoTrimCurve(curve1=g[54], point1=(0.0373744403116903, 0.0382676328334867))
    s1.autoTrimCurve(curve1=g[69], point1=(0.0391757472102656, 0.0386834313324649))
    s1.autoTrimCurve(curve1=g[84], point1=(0.0391757508236072, 0.0396536148708542))
    s1.autoTrimCurve(curve1=g[90], point1=(0.0359888179956847, 0.0432571668571626))
    s1.autoTrimCurve(curve1=g[109], point1=(0.028922151236561, 0.0371588463280391))
    s1.autoTrimCurve(curve1=g[111], point1=(0.0213012243098908, 
        0.0227446401009388))
    s1.autoTrimCurve(curve1=g[108], point1=(0.054833277684687, 0.0522660444437944))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229579, 
        farPlane=0.355472, width=0.438336, height=0.196708, cameraPosition=(
        0.134813, 0.0243873, 0.294776), cameraTarget=(0.134813, 0.0243873, 
        0.0045))
    s1.autoTrimCurve(curve1=g[87], point1=(0.140496793322745, 0.0447244616065779))
    s1.autoTrimCurve(curve1=g[113], point1=(0.145909364698848, 0.0468900567901485))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.142091, 
        farPlane=0.442961, width=1.07016, height=0.480245, cameraPosition=(
        0.0849757, -0.0429063, 0.294776), cameraTarget=(0.0849757, -0.0429063, 
        0.0045))
    s1.autoTrimCurve(curve1=g[115], point1=(0.198222960996508, 
        -0.0578538244918543))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.259199, 
        farPlane=0.325852, width=0.143634, height=0.0644574, cameraPosition=(
        0.0171092, -0.00551995, 0.294776), cameraTarget=(0.0171092, 
        -0.00551995, 0.0045))
    s1.autoTrimCurve(curve1=g[117], point1=(-0.0250275226032587, 
        -0.0503195541678775))
    s1.autoTrimCurve(curve1=g[118], point1=(-0.0285747176183624, 
        -0.0379011494243326))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.195438, 
        farPlane=0.389614, width=0.438336, height=0.196709, cameraPosition=(
        0.100675, 0.0251448, 0.294776), cameraTarget=(0.100675, 0.0251448, 
        0.0045))
    s1.autoTrimCurve(curve1=g[116], point1=(0.0767601905336036, 
        0.0765993129269069))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.259199, 
        farPlane=0.325852, width=0.143634, height=0.0644575, cameraPosition=(
        0.0929726, 0.100006, 0.294776), cameraTarget=(0.0929726, 0.100006, 
        0.0045))
    s1.autoTrimCurve(curve1=g[52], point1=(0.0372796375741131, 0.0773696725163843))
    s1.autoTrimCurve(curve1=g[67], point1=(0.0373978785867516, 0.0798533569487264))
    s1.autoTrimCurve(curve1=g[82], point1=(0.0370431562106492, 0.0783158360465395))
    s1.autoTrimCurve(curve1=g[120], point1=(0.0379890766293556, 
        0.0802081672309377))
    s1.autoTrimCurve(curve1=g[121], point1=(0.0371613982263812, 
        0.0816274132033789))
    s1.autoTrimCurve(curve1=g[123], point1=(0.0370431563291905, 
        0.0810360674150699))
    s1.autoTrimCurve(curve1=g[122], point1=(0.0366884353644372, 
        0.0800899007352613))
    s1.undo()
    s1.undo()
    s1.undo()
    s1.undo()
    s1.undo()
    s1.undo()
    s1.undo()
    s1.undo()
    s1.autoTrimCurve(curve1=g[116], point1=(0.0505224936472461, 
        0.0810360599316716))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.283759, 
        farPlane=0.301293, width=0.0301222, height=0.0135177, cameraPosition=(
        0.0860265, 0.11829, 0.294776), cameraTarget=(0.0860265, 0.11829, 
        0.0045))
    s1.autoTrimCurve(curve1=g[52], point1=(0.0371106385463085, 0.0813107187208102))
    s1.autoTrimCurve(curve1=g[67], point1=(0.036788282070166, 0.0812859120691147))
    s1.autoTrimCurve(curve1=g[82], point1=(0.036937065761268, 0.0813107177652967))
    s1.autoTrimCurve(curve1=g[120], point1=(0.0351764972844648, 
        0.0793512672234158))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.274365, 
        farPlane=0.310687, width=0.114907, height=0.051566, cameraPosition=(
        0.0878624, 0.101752, 0.294776), cameraTarget=(0.0878624, 0.101752, 
        0.0045))
    s1.autoTrimCurve(curve1=g[49], point1=(0.0165788853056846, 0.0787717176467772))
    s1.autoTrimCurve(curve1=g[64], point1=(0.0163896985316078, 0.0783932494441089))
    s1.autoTrimCurve(curve1=g[79], point1=(0.0162951080439753, 0.0782986305054731))
    s1.autoTrimCurve(curve1=g[46], point1=(-0.00697450179263844, 
        0.0644846336164151))
    s1.autoTrimCurve(curve1=g[61], point1=(-0.00593399279063713, 
        0.0647684815260305))
    s1.autoTrimCurve(curve1=g[76], point1=(-0.00669072357854804, 
        0.0637276961691597))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.259199, 
        farPlane=0.325852, width=0.143634, height=0.0644575, cameraPosition=(
        0.0456517, 0.0469206, 0.294776), cameraTarget=(0.0456517, 0.0469206, 
        0.0045))
    s1.autoTrimCurve(curve1=g[40], point1=(-0.0395552004308252, 
        -0.0014261073174827))
    s1.autoTrimCurve(curve1=g[55], point1=(-0.0405011145835144, 
        -0.000953025285597639))
    s1.autoTrimCurve(curve1=g[70], point1=(-0.040619354032242, 
        -0.000834754946928515))
    session.viewports['Viewport: 1'].view.setValues(width=0.114907, 
        height=0.051566, cameraPosition=(0.0512311, 0.0746208, 0.294776), 
        cameraTarget=(0.0512311, 0.0746208, 0.0045))
    s1.autoTrimCurve(curve1=g[43], point1=(-0.0285472255230522, 
        0.0408079723611392))
    s1.autoTrimCurve(curve1=g[58], point1=(-0.0284526359875885, 
        0.0400510401930658))
    s1.autoTrimCurve(curve1=g[73], point1=(-0.0275067193777696, 
        0.0406187426458957))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.277547, 
        farPlane=0.307505, width=0.0588325, height=0.0264018, cameraPosition=(
        0.0480711, 0.0991319, 0.294776), cameraTarget=(0.0480711, 0.0991319, 
        0.0045))
    s1.autoTrimCurve(curve1=g[119], point1=(-0.00900422083241131, 
        0.0558637534667659))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238481, 
        farPlane=0.34657, width=0.374047, height=0.167858, cameraPosition=(
        0.123745, 0.049099, 0.294776), cameraTarget=(0.123745, 0.049099, 
        0.0045))
    s1.autoTrimCurve(curve1=g[125], point1=(0.00808254940977881, 
        0.0694533645214507))
    s1.autoTrimCurve(curve1=g[138], point1=(-0.030714943965221, 
        0.0164779532191229))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254069, 
        farPlane=0.330983, width=0.261478, height=0.117341, cameraPosition=(
        0.0850817, 0.0625, 0.294776), cameraTarget=(0.0850817, 0.0625, 0.0045))
    p = mdb.models['Model-1'].parts['Part-1']
    f, e = p.faces, p.edges
    p.CutExtrude(sketchPlane=f[76], sketchUpEdge=e[215], sketchPlaneSide=SIDE1, 
        sketchOrientation=LEFT, sketch=s1, depth=0.0019, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.200175, 
        farPlane=0.380656, width=0.113452, height=0.0509129, 
        viewOffsetX=0.0122061, viewOffsetY=0.0158297)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.218335, 
        farPlane=0.3855, width=0.123744, height=0.0555318, cameraPosition=(
        0.32216, 0.122338, -0.106105), cameraUpVector=(-0.605499, 0.793752, 
        0.0576927), cameraTarget=(0.0678128, 0.041927, 0.00871275), 
        viewOffsetX=0.0133135, viewOffsetY=0.0172657)
    p = mdb.models['Model-1'].parts['Part-1']
    f1, e1 = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f1[99], sketchUpEdge=e1[86], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.035232, 
        0.048748, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.29, 
        gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=4)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250201, 
        farPlane=0.334851, width=0.185222, height=0.0831208, cameraPosition=(
        0.0354022, 0.0458337, -0.290276), cameraTarget=(0.0354022, 0.0458337, 
        0))
    s.Line(point1=(0.063, 0.00175), point2=(0.0266183835763536, 
        -0.00393628633658523))
    s.Line(point1=(0.0266183835763536, -0.00393628633658523), point2=(
        -0.0104624276316472, -0.0104746338191126))
    s.Line(point1=(-0.0104624276316472, -0.0104746338191126), point2=(-0.042, 
        -0.0160355587337895))
    s.ParallelConstraint(entity1=g[41], entity2=g[42], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24753, 
        farPlane=0.337522, width=0.197571, height=0.0886622, cameraPosition=(
        0.0252358, 0.0755737, -0.290276), cameraTarget=(0.0252358, 0.0755737, 
        0))
    s.Line(point1=(0.04375, 0.0455), point2=(0.0139938695315414, 
        0.0315370584842518))
    s.Line(point1=(0.0139938695315414, 0.0315370584842518), point2=(
        -0.0106628693203534, 0.0175357729503602))
    s.Line(point1=(-0.0106628693203534, 0.0175357729503602), point2=(
        -0.0341687913587521, 0.00418797670795357))
    s.ParallelConstraint(entity1=g[44], entity2=g[45], addUndoState=False)
    s.Line(point1=(-0.035, 0.021), point2=(-0.0178774315363945, 
        0.0373576197301838))
    s.Line(point1=(-0.0178774315363945, 0.0373576197301838), point2=(
        -0.00391948006474348, 0.0535166552424587))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.223485, 
        farPlane=0.361567, width=0.48235, height=0.21646, cameraPosition=(
        0.0120645, 0.024327, -0.290276), cameraTarget=(0.0120645, 0.024327, 0))
    s.Line(point1=(-0.00391948006474348, 0.0535166552424587), point2=(
        0.0157500000002401, 0.0762878926643371))
    s.ParallelConstraint(entity1=g[47], entity2=g[48], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24753, 
        farPlane=0.337522, width=0.197571, height=0.0886622, cameraPosition=(
        0.049787, 0.0988517, -0.290276), cameraTarget=(0.049787, 0.0988517, 0))
    s.Line(point1=(-0.01575, 0.08575), point2=(-0.0221780431667136, 
        0.0645875048676366))
    s.Line(point1=(-0.0221780431667136, 0.0645875048676366), point2=(
        -0.0245667396394956, 0.0501539149679164))
    s.undo()
    s.Line(point1=(-0.0221780431667136, 0.0645875048676366), point2=(
        -0.0280007482621347, 0.0495989570058417))
    s.Line(point1=(-0.0280007482621347, 0.0495989570058417), point2=(
        -0.0343519409285233, 0.03325))
    s.ParallelConstraint(entity1=g[50], entity2=g[51], addUndoState=False)
    s.Line(point1=(-0.03675, 0.091), point2=(-0.0379271711953188, 
        0.0678317964655298))
    s.Line(point1=(-0.0379271711953188, 0.0678317964655298), point2=(
        -0.0382737250482658, 0.0557277414871095))
    s.Line(point1=(-0.0382737250482658, 0.0557277414871095), point2=(
        -0.0388288900113025, 0.036337545194101))
    s.ParallelConstraint(entity1=g[53], entity2=g[54], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.287338, 
        farPlane=0.297713, width=0.013577, height=0.00609282, cameraPosition=(
        0.0387342, 0.0389915, -0.290276), cameraTarget=(0.0387342, 0.0389915, 
        0))
    s.offset(distance=0.00025, objectList=(g[40], g[41], g[42], g[43], g[44], 
        g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], g[53], g[54]), 
        side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.283153, 
        farPlane=0.301899, width=0.0514417, height=0.0230851, cameraPosition=(
        0.0337428, 0.0359147, -0.290276), cameraTarget=(0.0337428, 0.0359147, 
        0))
    s.offset(distance=0.00025, objectList=(g[40], g[41], g[42], g[43], g[44], 
        g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], g[53], g[54]), 
        side=RIGHT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.223936, 
        farPlane=0.361115, width=0.306616, height=0.137598, cameraPosition=(
        -0.00471686, 0.0460104, -0.290276), cameraTarget=(-0.00471686, 
        0.0460104, 0))
    s.EllipseByCenterPerimeter(center=(-0.07525, -0.00875), axisPoint1=(
        -0.0237451585917939, 0.0314062865705068), axisPoint2=(
        -0.0171310045555331, -0.0296457227703292))
    s.CoincidentConstraint(entity1=v[88], entity2=g[76], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.117517, 
        farPlane=0.467535, width=1.24763, height=0.559887, cameraPosition=(
        -0.210249, 0.0961889, -0.290276), cameraTarget=(-0.210249, 0.0961889, 
        0))
    s.EllipseByCenterPerimeter(center=(-0.0945, -0.0315), axisPoint1=(0.03675, 
        0.049), axisPoint2=(0.0595, -0.042))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.172339, 
        farPlane=0.412713, width=0.545096, height=0.244618, cameraPosition=(
        -0.0380006, 0.115823, -0.290276), cameraTarget=(-0.0380006, 0.115823, 
        0))
    s.autoTrimCurve(curve1=g[85], point1=(-0.0979009751488572, 0.0393504550303793))
    s.autoTrimCurve(curve1=g[87], point1=(-0.0938624373437932, 0.0689739670807116))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.265543, 
        farPlane=0.319509, width=0.114315, height=0.0513002, cameraPosition=(
        0.044575, 0.0750705, -0.290276), cameraTarget=(0.044575, 0.0750705, 0))
    s.autoTrimCurve(curve1=g[54], point1=(-0.0380460612026655, 0.0392302489598503))
    s.autoTrimCurve(curve1=g[69], point1=(-0.038987104453256, 0.03941850309335))
    s.autoTrimCurve(curve1=g[84], point1=(-0.0394576211640795, 0.0395126368859387))
    s.autoTrimCurve(curve1=g[89], point1=(-0.0355993423421533, 0.0411128237880468))
    s.autoTrimCurve(curve1=g[66], point1=(-0.0326821065177791, 0.0334883912743712))
    s.autoTrimCurve(curve1=g[51], point1=(-0.0341877816275174, 0.0357474860057752))
    s.autoTrimCurve(curve1=g[81], point1=(-0.0329644212870162, 0.0364063800336397))
    s.autoTrimCurve(curve1=g[96], point1=(-0.0292943478146098, 0.0364063825493107))
    s.autoTrimCurve(curve1=g[46], point1=(-0.0283533046389369, 0.0263345957564484))
    s.autoTrimCurve(curve1=g[61], point1=(-0.028635616895281, 0.0273700154347796))
    s.autoTrimCurve(curve1=g[76], point1=(-0.028447411181314, 0.0271817584026679))
    s.autoTrimCurve(curve1=g[90], point1=(-0.0216718951580354, 0.0272758852492093))
    s.autoTrimCurve(curve1=g[45], point1=(-0.023271669002028, 0.0111798548722526))
    s.autoTrimCurve(curve1=g[60], point1=(-0.0228952480791886, 0.0107092119043989))
    s.autoTrimCurve(curve1=g[75], point1=(-0.0228011480064765, 0.0116504992644299))
    s.autoTrimCurve(curve1=g[106], point1=(-0.0150845816392806, 
        0.00957966726706534))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241969, 
        farPlane=0.343083, width=0.223272, height=0.100196, cameraPosition=(
        0.00637563, 0.0472215, -0.290276), cameraTarget=(0.00637563, 0.0472215, 
        0))
    s.autoTrimCurve(curve1=g[42], point1=(-0.0319030639828395, 
        -0.0122875314237858))
    s.autoTrimCurve(curve1=g[57], point1=(-0.0302488878947018, 
        -0.0143098251219965))
    s.autoTrimCurve(curve1=g[72], point1=(-0.0302488806680046, 
        -0.0122875307468843))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.256507, 
        farPlane=0.328545, width=0.243872, height=0.109441, cameraPosition=(
        -0.0189173, 0.0230803, -0.290276), cameraTarget=(-0.0189173, 0.0230803, 
        0))
    s.autoTrimCurve(curve1=g[92], point1=(0.033055940528457, -0.0259964953911641))
    s.autoTrimCurve(curve1=g[115], point1=(0.0236203970835836, 
        -0.0404546992881354))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.272986, 
        farPlane=0.312066, width=0.0799121, height=0.0358615, cameraPosition=(
        -0.0185318, 0.0526071, -0.290276), cameraTarget=(-0.0185318, 0.0526071, 
        0))
    s.autoTrimCurve(curve1=g[116], point1=(0.0445772320926064, 
        0.00665951039650424))
    s.autoTrimCurve(curve1=g[40], point1=(0.0495110231138949, 
        -0.00117079868144522))
    s.autoTrimCurve(curve1=g[55], point1=(0.0497083706623248, 
        7.94181720907491e-05))
    s.autoTrimCurve(curve1=g[70], point1=(0.0497083706623248, 
        7.94181720907491e-05))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.283194, 
        farPlane=0.301858, width=0.032732, height=0.0146889, cameraPosition=(
        -0.00106358, 0.0973937, -0.290276), cameraTarget=(-0.00106358, 
        0.0973937, 0))
    s.autoTrimCurve(curve1=g[118], point1=(0.0390424623158069, 0.0450321636716497))
    s.autoTrimCurve(curve1=g[73], point1=(0.0413058469479964, 0.0448165421957524))
    s.autoTrimCurve(curve1=g[43], point1=(0.0416291882385927, 0.0445739739171002))
    s.autoTrimCurve(curve1=g[58], point1=(0.0418178038720282, 0.0443044565018653))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.281423, 
        farPlane=0.303628, width=0.0639297, height=0.0286892, cameraPosition=(
        0.000169045, 0.0989584, -0.290276), cameraTarget=(0.000169045, 
        0.0989584, 0))
    s.autoTrimCurve(curve1=g[91], point1=(0.0346227630235922, 0.0520109391337287))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.271833, 
        farPlane=0.313218, width=0.0852396, height=0.0382523, cameraPosition=(
        0.052524, 0.115863, -0.290276), cameraTarget=(0.052524, 0.115863, 0))
    s.autoTrimCurve(curve1=g[52], point1=(-0.0374455908147642, 0.0829194561091654))
    s.autoTrimCurve(curve1=g[67], point1=(-0.0373052500021123, 0.0829194557155736))
    s.autoTrimCurve(curve1=g[82], point1=(-0.0370947391564638, 0.082989644518282))
    s.autoTrimCurve(curve1=g[126], point1=(-0.030428638886609, 0.079831196457813))
    s.autoTrimCurve(curve1=g[49], point1=(-0.0172367736137307, 0.0822877695852472))
    s.autoTrimCurve(curve1=g[64], point1=(-0.0171666094338762, 0.0820772024504048))
    s.autoTrimCurve(curve1=g[79], point1=(-0.0169560925537677, 0.0819368297996637))
    s.autoTrimCurve(curve1=g[130], point1=(-0.0121144002543618, 
        0.0782168759544743))
    s.autoTrimCurve(curve1=g[48], point1=(0.0123747543911599, 0.0734441148734557))
    s.autoTrimCurve(curve1=g[63], point1=(0.0132869584616965, 0.0730229857854758))
    s.autoTrimCurve(curve1=g[78], point1=(0.0133571284946931, 0.0730931749817759))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24528, 
        farPlane=0.339772, width=0.324952, height=0.145826, cameraPosition=(
        -0.0175862, 0.0793553, -0.290276), cameraTarget=(-0.0175862, 0.0793553, 
        0))
    s.setAsConstruction(objectList=(g[127], g[53], g[93], g[50], g[99], g[132], 
        g[137], g[47], g[103], g[107], g[44], g[112], g[41], g[119], g[124]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254279, 
        farPlane=0.330773, width=0.259962, height=0.116661, cameraPosition=(
        -0.00641411, 0.0744215, -0.290276), cameraTarget=(-0.00641411, 
        0.0744215, 0))
    p = mdb.models['Model-1'].parts['Part-1']
    f, e = p.faces, p.edges
    p.CutExtrude(sketchPlane=f[99], sketchUpEdge=e[86], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s, depth=0.0019, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.210278, 
        farPlane=0.393558, width=0.19863, height=0.0891377, 
        viewOffsetX=0.0469373, viewOffsetY=0.0015024)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.148787, 
        farPlane=0.363485, width=0.140546, height=0.0630716, cameraPosition=(
        0.245779, 0.173315, 0.122551), cameraUpVector=(-0.905168, 0.371987, 
        0.205662), cameraTarget=(0.0418721, -0.00189533, 0.0127113), 
        viewOffsetX=0.0332117, viewOffsetY=0.00106306)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.174227, 
        farPlane=0.308566, width=0.164577, height=0.0738557, cameraPosition=(
        0.0909524, -0.10416, 0.188675), cameraUpVector=(-0.720942, 0.673416, 
        0.163563), cameraTarget=(0.0187428, 0.0232029, -0.062135), 
        viewOffsetX=0.0388902, viewOffsetY=0.00124482)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])

Macro3()