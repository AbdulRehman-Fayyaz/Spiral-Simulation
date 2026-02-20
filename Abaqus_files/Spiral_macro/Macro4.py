# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro4():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.245058, 
        farPlane=0.393802, width=0.0371781, height=0.0166841, cameraPosition=(
        0.252581, 0.20878, 0.196553), cameraTarget=(0.0681576, 0.0243566, 
        0.0121303))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[55], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.24334, 
        farPlane=0.395521, width=0.0705007, height=0.031638, cameraPosition=(
        0.249097, 0.204319, 0.204499), cameraTarget=(0.0646735, 0.0198955, 
        0.0200756))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237597, 
        farPlane=0.374383, cameraPosition=(0.269574, 0.131304, -0.198189), 
        cameraUpVector=(-0.865338, 0.496091, -0.071301), cameraTarget=(
        0.0646735, 0.0198955, 0.0200756))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2466, 
        farPlane=0.365379, width=0.0147851, height=0.00663499, cameraPosition=(
        0.256805, 0.114545, -0.21873), cameraTarget=(0.0519046, 0.00313651, 
        -0.000465776))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[71], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.172216, 
        farPlane=0.439764, width=0.358586, height=0.16092, cameraPosition=(
        0.246981, 0.138553, -0.215698), cameraTarget=(0.0420807, 0.0271447, 
        0.00256634))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.190436, 
        farPlane=0.431864, cameraPosition=(0.242106, -0.091832, 0.197592), 
        cameraUpVector=(-0.264528, 0.91557, 0.302915), cameraTarget=(0.0422949, 
        0.0372642, -0.0155871))
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.252883, 
        farPlane=0.385977, width=0.00101046, height=0.000453458, 
        cameraPosition=(0.234866, 0.227482, 0.195565), cameraTarget=(0.0504432, 
        0.0430593, 0.011142))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[46], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.246284, 
        farPlane=0.399742, width=0.0196056, height=0.00879825, cameraPosition=(
        0.238234, 0.228528, 0.191151), cameraTarget=(0.0538114, 0.0441049, 
        0.00672813))
    session.viewports['Viewport: 1'].view.setValues(cameraUpVector=(-0.596022, 
        0.577043, -0.558372))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262951, 
        farPlane=0.381968, cameraPosition=(-0.133997, -0.0465363, 0.253643), 
        cameraUpVector=(-0.348313, 0.852912, -0.38887), cameraTarget=(
        0.0496827, 0.0410539, 0.00742131))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.244769, 
        farPlane=0.40015, width=0.155812, height=0.0699223, cameraPosition=(
        -0.129758, -0.0181445, 0.266905), cameraTarget=(0.0539217, 0.0694457, 
        0.0206836))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[47], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.257506, 
        farPlane=0.387508, width=0.0638205, height=0.0286402, cameraPosition=(
        -0.138879, -0.013269, 0.261835), cameraTarget=(0.0448002, 0.0743212, 
        0.0156134))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[34], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.251615, 
        farPlane=0.397233, width=0.106367, height=0.0477337, cameraPosition=(
        -0.135629, -0.00826024, 0.266042), cameraTarget=(0.048051, 0.0793299, 
        0.0198203))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.296016, 
        farPlane=0.396934, cameraPosition=(0.100588, 0.184128, 0.319429), 
        cameraUpVector=(-0.573762, 0.658563, -0.486921), cameraTarget=(
        0.0516875, 0.0822918, 0.0206422))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.311338, 
        farPlane=0.381612, width=0.0223069, height=0.0100105, cameraPosition=(
        0.0975364, 0.173949, 0.323398), cameraTarget=(0.0486359, 0.072113, 
        0.0246109))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[33], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.306705, 
        farPlane=0.386245, width=0.0743563, height=0.0333683, cameraPosition=(
        0.108082, 0.194736, 0.314587), cameraTarget=(0.0591816, 0.0928996, 
        0.0158002))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[42], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.278762, 
        farPlane=0.383157, cameraPosition=(-0.119775, 0.0949258, 0.288502), 
        cameraUpVector=(-0.1915, 0.826935, -0.528684), cameraTarget=(0.0433003, 
        0.085943, 0.0139821))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288934, 
        farPlane=0.372986, width=0.0124749, height=0.00559827, cameraPosition=(
        -0.116201, 0.100746, 0.290435), cameraTarget=(0.0468745, 0.0917635, 
        0.0159149))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[43], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288677, 
        farPlane=0.373235, width=0.013626, height=0.00611481, cameraPosition=(
        -0.104894, 0.116468, 0.296637), cameraTarget=(0.0581814, 0.107485, 
        0.0221171))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[37], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.319641, 
        farPlane=0.39238, cameraPosition=(0.117925, 0.202657, 0.324486), 
        cameraUpVector=(-0.475352, 0.728051, -0.493946), cameraTarget=(
        0.0659571, 0.110493, 0.023089))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315447, 
        farPlane=0.396573, width=0.0473123, height=0.021232, cameraPosition=(
        0.122225, 0.204131, 0.323294), cameraTarget=(0.0702568, 0.111967, 
        0.0218968))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.299298, 
        farPlane=0.434407, cameraPosition=(0.219635, 0.23825, 0.277021), 
        cameraUpVector=(-0.562423, 0.700624, -0.439099), cameraTarget=(
        0.0802659, 0.115473, 0.0171422))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.287494, 
        farPlane=0.446211, width=0.0924069, height=0.0414687, cameraPosition=(
        0.218354, 0.238277, 0.277695), cameraTarget=(0.0789848, 0.1155, 
        0.0178165))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.286235, 
        farPlane=0.459085, cameraPosition=(0.25171, 0.264302, 0.24243), 
        cameraUpVector=(-0.603883, 0.6634, -0.441843), cameraTarget=(0.0832967, 
        0.118864, 0.0132577))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.293495, 
        farPlane=0.451826, width=0.0630832, height=0.0283093, cameraPosition=(
        0.246173, 0.263491, 0.247013), cameraTarget=(0.0777598, 0.118053, 
        0.017841))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[36], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.288978, 
        farPlane=0.456388, width=0.0956995, height=0.0429463, cameraPosition=(
        0.242251, 0.245193, 0.261508), cameraTarget=(0.073838, 0.0997547, 
        0.0323359))
    p = mdb.models['Model-1'].parts['Part-1']
    f1 = p.faces
    p.DatumPlaneByOffset(plane=f1[39], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.295445, 
        farPlane=0.453618, width=0.0313588, height=0.0140726, cameraPosition=(
        0.253214, 0.255115, 0.247155), cameraTarget=(0.0848008, 0.109677, 
        0.0179829))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.320172, 
        farPlane=0.406714, cameraPosition=(0.090545, 0.230263, 0.321732), 
        cameraUpVector=(-0.544417, 0.615631, -0.569744), cameraTarget=(
        0.0608686, 0.10602, 0.0289548))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.27168, 
        farPlane=0.455208, width=0.389403, height=0.174749, cameraPosition=(
        0.107683, 0.200927, 0.332444), cameraTarget=(0.0780068, 0.0766835, 
        0.0396669))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.225291, 
        farPlane=0.466587, cameraPosition=(-0.115204, 0.133635, 0.300719), 
        cameraUpVector=(-0.368111, 0.530781, -0.763391), cameraTarget=(
        0.0510148, 0.0685344, 0.0358249))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.269134, 
        farPlane=0.422745, width=0.226844, height=0.101799, cameraPosition=(
        -0.0874731, 0.160946, 0.311408), cameraTarget=(0.0787457, 0.0958454, 
        0.0465138))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.DatumPlaneByOffset(plane=f[40], flip=SIDE1, offset=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.216005, 
        farPlane=0.475888, width=0.553817, height=0.248532, cameraPosition=(
        -0.0497711, 0.165008, 0.334067), cameraTarget=(0.116448, 0.0999075, 
        0.0691732))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263816, 
        farPlane=0.589732, cameraPosition=(0.238874, 0.295433, 0.307004), 
        cameraUpVector=(-0.39555, 0.570581, -0.719707), cameraTarget=(0.138572, 
        0.109904, 0.0670988))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.281614, 
        farPlane=0.596613, cameraPosition=(0.312504, 0.195924, 0.328547), 
        cameraUpVector=(-0.304446, 0.767599, -0.564007), cameraTarget=(
        0.157092, 0.0848751, 0.0725173))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.374774, 
        farPlane=0.503452, width=0.0124709, height=0.00559645, cameraPosition=(
        0.22776, 0.201422, 0.377602), cameraTarget=(0.0723481, 0.0903735, 
        0.121573))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[8], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.375314, 
        farPlane=0.502912, width=0.0099767, height=0.00447716, cameraPosition=(
        0.226691, 0.205642, 0.376421), cameraTarget=(0.0712795, 0.0945927, 
        0.120391))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[7], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332799, 
        farPlane=0.545427, width=0.206478, height=0.0926597, cameraPosition=(
        0.275567, 0.22132, 0.339953), cameraTarget=(0.120155, 0.110271, 
        0.0839234))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341734, 
        cameraPosition=(0.275567, 0.22132, 0.339953), cameraUpVector=(
        -0.136897, 0.743064, -0.655069), cameraTarget=(0.120155, 0.110271, 
        0.0839234))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.325168, 
        farPlane=0.510572, cameraPosition=(-0.249071, 0.105821, 0.295762), 
        cameraUpVector=(0.117976, 0.878753, -0.462466), cameraTarget=(
        -0.0228379, 0.0787912, 0.071879))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.336509, 
        farPlane=0.49923, width=0.176195, height=0.0790696, cameraPosition=(
        -0.224942, 0.0892504, 0.322145), cameraTarget=(0.00129134, 0.0622206, 
        0.0982621))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.330409, 
        farPlane=0.505329, cameraPosition=(-0.224942, 0.0892504, 0.322145), 
        cameraUpVector=(0.156047, 0.891393, -0.425522), cameraTarget=(
        0.00129133, 0.0622206, 0.0982621))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.396408, 
        farPlane=0.502674, cameraPosition=(0.145423, 0.00974896, 0.438082), 
        cameraUpVector=(0.107448, 0.960538, -0.256558), cameraTarget=(
        0.0885398, 0.0434921, 0.125574))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.36734, 
        farPlane=0.531742, width=0.275305, height=0.123546, cameraPosition=(
        0.119405, -0.0117359, 0.440498), cameraTarget=(0.062522, 0.0220072, 
        0.12799))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.332905, 
        farPlane=0.540834, cameraPosition=(0.200601, 0.212305, 0.381375), 
        cameraUpVector=(-0.0871336, 0.718562, -0.689983), cameraTarget=(
        0.0860226, 0.0868516, 0.110878))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.379824, 
        farPlane=0.493915, width=0.00338566, height=0.00151935, 
        cameraPosition=(0.157665, 0.246457, 0.383723), cameraTarget=(0.0430869, 
        0.121004, 0.113226))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#5 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[7], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.338165, 
        farPlane=0.535574, width=0.19593, height=0.0879257, cameraPosition=(
        0.169995, 0.225076, 0.388416), cameraTarget=(0.0554169, 0.0996225, 
        0.117919))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331244, 
        farPlane=0.594022, cameraPosition=(-0.341265, 0.291973, 0.109434), 
        cameraUpVector=(0.651073, 0.554895, -0.517876), cameraTarget=(
        -0.0820207, 0.117606, 0.0429228))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.362243, 
        farPlane=0.563022, width=0.0134642, height=0.00604222, cameraPosition=(
        -0.351105, 0.283466, 0.0933829), cameraTarget=(-0.0918605, 0.109099, 
        0.0268717))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#5 ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[7], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.29656, 
        farPlane=0.628705, width=0.495389, height=0.222312, cameraPosition=(
        -0.272195, 0.33219, 0.273218), cameraTarget=(-0.0129509, 0.157823, 
        0.206706))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.279411, 
        farPlane=0.645854, cameraPosition=(-0.272195, 0.33219, 0.273218), 
        cameraUpVector=(0.615379, 0.527649, -0.585572), cameraTarget=(
        -0.0129509, 0.157823, 0.206706))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.545976, 
        farPlane=0.731473, cameraPosition=(0.108694, 0.102607, 0.638919), 
        cameraUpVector=(0.219918, 0.898054, -0.380966), cameraTarget=(0.104949, 
        0.086758, 0.319905))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.518745, 
        farPlane=0.764234, cameraPosition=(0.0877601, 0.354709, 0.573082), 
        cameraUpVector=(0.235117, 0.673517, -0.700782), cameraTarget=(
        0.0944843, 0.212783, 0.286994))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.510577, 
        farPlane=0.732253, cameraPosition=(-0.0904275, 0.0877109, 0.610462), 
        cameraUpVector=(0.147506, 0.93214, -0.330693), cameraTarget=(
        0.00502487, 0.0787361, 0.305761))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.514137, 
        farPlane=0.815637, cameraPosition=(0.444003, 0.272283, 0.49069), 
        cameraUpVector=(-0.670857, 0.700771, -0.242634), cameraTarget=(0.26474, 
        0.168432, 0.247556))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.512971, 
        farPlane=0.842118, cameraPosition=(0.631516, 0.228657, 0.297625), 
        cameraUpVector=(-0.498928, 0.823971, -0.268594), cameraTarget=(
        0.362167, 0.145765, 0.147244))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.557332, 
        farPlane=0.797757, width=0.298868, height=0.134121, cameraPosition=(
        0.629473, 0.248102, 0.290566), cameraTarget=(0.360124, 0.16521, 
        0.140185))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#7 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[9], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.59726, 
        farPlane=0.757828, width=0.00672992, height=0.00302013, 
        cameraPosition=(0.607327, 0.234737, 0.337598), cameraTarget=(0.337979, 
        0.151845, 0.187216))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#2f ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[10], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.595481, 
        farPlane=0.759608, width=0.0149554, height=0.00671141, cameraPosition=(
        0.605254, 0.262481, 0.326018), cameraTarget=(0.335906, 0.179589, 
        0.175637))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#83 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[12], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.596949, 
        farPlane=0.758139, width=0.00816764, height=0.00366533, 
        cameraPosition=(0.604602, 0.262775, 0.327026), cameraTarget=(0.335253, 
        0.179883, 0.176644))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3d ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[11], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.595771, 
        farPlane=0.759318, width=0.0136127, height=0.00610888, cameraPosition=(
        0.607737, 0.274729, 0.31482), cameraTarget=(0.338388, 0.191837, 
        0.164439))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#83 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[13], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.596887, 
        farPlane=0.758203, width=0.00845867, height=0.00379593, 
        cameraPosition=(0.607181, 0.27579, 0.315231), cameraTarget=(0.337832, 
        0.192898, 0.16485))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3d ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[14], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.593951, 
        farPlane=0.761138, width=0.0344185, height=0.0154457, cameraPosition=(
        0.612287, 0.277611, 0.305082), cameraTarget=(0.342939, 0.194719, 
        0.1547))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#83 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[16], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.594378, 
        farPlane=0.76071, width=0.0200502, height=0.00899778, cameraPosition=(
        0.610833, 0.279065, 0.306886), cameraTarget=(0.341484, 0.196173, 
        0.156504))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3d ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[15], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.585478, 
        farPlane=0.769611, width=0.095607, height=0.0429048, cameraPosition=(
        0.622289, 0.265388, 0.293905), cameraTarget=(0.35294, 0.182496, 
        0.143523))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#83 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[17], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.597423, 
        farPlane=0.757666, width=0.0093441, height=0.00419328, cameraPosition=(
        0.615118, 0.276498, 0.300625), cameraTarget=(0.34577, 0.193606, 
        0.150243))
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3d ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[18], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.528982, 
        farPlane=0.826107, width=0.50361, height=0.226001, cameraPosition=(
        0.674787, 0.233402, 0.217508), cameraTarget=(0.405438, 0.15051, 
        0.0671264))
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Cell']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.554086, 
        farPlane=0.801003, width=0.206279, height=0.09257, cameraPosition=(
        0.638662, 0.244713, 0.275975), cameraTarget=(0.369313, 0.161821, 
        0.125594))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.573199, 
        farPlane=0.690901, cameraPosition=(-0.0152579, 0.180078, 0.620234), 
        cameraUpVector=(-0.746191, 0.432637, -0.505988), cameraTarget=(
        0.023684, 0.127658, 0.307551))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.524505, 
        farPlane=0.711403, cameraPosition=(-0.419958, 0.0465162, 0.409589), 
        cameraUpVector=(-0.194995, 0.691068, -0.69599), cameraTarget=(
        -0.176487, 0.0615964, 0.203363))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.519638, 
        farPlane=0.726813, cameraPosition=(-0.38036, 0.224229, 0.427391), 
        cameraUpVector=(0.0497506, 0.714825, -0.697532), cameraTarget=(
        -0.157358, 0.147447, 0.211963))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.554874, 
        farPlane=0.691577, width=0.00216472, height=0.000971446, 
        cameraPosition=(-0.395426, 0.22793, 0.410476), cameraTarget=(-0.172424, 
        0.151148, 0.195049))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.548072, 
        farPlane=0.698379, width=0.0525015, height=0.0235607, cameraPosition=(
        -0.386393, 0.22882, 0.41951), cameraTarget=(-0.163391, 0.152038, 
        0.204082))
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].setColor(translucency=0.45)
    session.viewports['Viewport: 1'].setColor(translucency=0.4)
    session.viewports['Viewport: 1'].setColor(translucency=0.35)
    session.viewports['Viewport: 1'].setColor(translucency=0.3)
    session.viewports['Viewport: 1'].setColor(translucency=0.25)
    session.viewports['Viewport: 1'].setColor(translucency=0.2)
    session.viewports['Viewport: 1'].setColor(translucency=0.15)
    session.viewports['Viewport: 1'].setColor(translucency=0.1)
    session.viewports['Viewport: 1'].setColor(translucency=0.05)
    session.viewports['Viewport: 1'].setColor(translucency=0)
    session.viewports['Viewport: 1'].setColor(translucency=0)
    session.viewports['Viewport: 1'].setColor(translucency=0.05)
    session.viewports['Viewport: 1'].setColor(translucency=0.05)
    session.viewports['Viewport: 1'].setColor(translucency=0.1)
    session.viewports['Viewport: 1'].setColor(translucency=0.1)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.533156, 
        farPlane=0.713295, width=0.160222, height=0.0719015, cameraPosition=(
        -0.395701, 0.209267, 0.416843), cameraTarget=(-0.172699, 0.132485, 
        0.201415))
    session.viewports['Viewport: 1'].setColor(globalTranslucency=False)

Macro4()