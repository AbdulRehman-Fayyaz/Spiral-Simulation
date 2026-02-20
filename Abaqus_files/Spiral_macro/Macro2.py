# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.218952, 
        farPlane=0.361879, width=0.0510583, height=0.022913, cameraPosition=(
        0.231543, 0.190236, 0.18588), cameraTarget=(0.0638712, 0.022565, 
        0.0182083))
    p = mdb.models['Model-1'].parts['Part-1']
    v1 = p.vertices
    p.DatumPlaneByTwoPoint(point1=v1[24], point2=v1[25])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.210278, 
        farPlane=0.370552, width=0.0638229, height=0.0286413, cameraPosition=(
        0.210309, 0.213717, 0.183632), cameraTarget=(0.0426382, 0.0460454, 
        0.0159609))
    p = mdb.models['Model-1'].parts['Part-1']
    e1, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e1[100], 
        sketchPlaneSide=SIDE1, sketchOrientation=LEFT, origin=(0.047738, 
        0.054657, 0.00225))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.319, gridSpacing=0.007, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=4)
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209558, 
        farPlane=0.429303, width=0.497423, height=0.223225, cameraPosition=(
        0.0602971, 0.0518161, -0.31718), cameraTarget=(0.0602971, 0.0518161, 
        0.00225))
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-1'].parts['Part-1']
    e, p2 = p.edges, p.elemEdges
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
        e[105], e[106], e[107], e[108], e[109], e[110], e[111], e[112], 
        e[113]))
    s1.autoTrimCurve(curve1=g[14], point1=(-0.0236723987798583, 
        0.0594685465602193))
    s1.autoTrimCurve(curve1=g[13], point1=(0.00816289926264276, 
        0.0461323516004927))
    s1.autoTrimCurve(curve1=g[32], point1=(-0.00897916956819048, 
        0.0453158538274648))
    s1.autoTrimCurve(curve1=g[33], point1=(-0.00489772811105517, 
        0.0390560034488664))
    s1.autoTrimCurve(curve1=g[35], point1=(-0.0255770802860366, 
        0.0409611760981447))
    s1.autoTrimCurve(curve1=g[34], point1=(-0.0220398281486942, 
        0.0249033077814235))
    s1.autoTrimCurve(curve1=g[28], point1=(-0.0239444941390181, 
        0.00938977144468201))
    s1.autoTrimCurve(curve1=g[31], point1=(-0.0285701270154423, 
        0.000136085358501181))
    s1.autoTrimCurve(curve1=g[29], point1=(-0.00653029836217278, 
        0.00367426141563459))
    s1.autoTrimCurve(curve1=g[12], point1=(-0.00136047389538622, 
        0.00639593269857805))
    s1.autoTrimCurve(curve1=g[30], point1=(-0.00925127984783169, 
        -0.0077567630701758))
    s1.autoTrimCurve(curve1=g[24], point1=(-0.0100675654441623, 
        -0.0180991194462727))
    s1.autoTrimCurve(curve1=g[27], point1=(-0.0141490093090648, 
        -0.0287136442460574))
    s1.autoTrimCurve(curve1=g[26], point1=(-0.00217675932214143, 
        -0.0322518181636864))
    s1.autoTrimCurve(curve1=g[25], point1=(-0.00244885533429993, 
        -0.0208207945465428))
    s1.autoTrimCurve(curve1=g[11], point1=(0.00326517372900262, 
        -0.0172826219252611))
    s1.autoTrimCurve(curve1=g[10], point1=(0.0106117723588225, 
        -0.0347013225673352))
    s1.autoTrimCurve(curve1=g[21], point1=(0.00897919928007768, 
        -0.038511663193755))
    s1.autoTrimCurve(curve1=g[20], point1=(0.00190468275561478, 
        -0.0385116648690549))
    s1.autoTrimCurve(curve1=g[23], point1=(0.00544193429908228, 
        -0.0483096823108551))
    s1.autoTrimCurve(curve1=g[22], point1=(0.0108838807989075, 
        -0.0458601823376748))
    s1.autoTrimCurve(curve1=g[16], point1=(0.0185025756643694, 
        -0.0493983527020821))
    s1.autoTrimCurve(curve1=g[9], point1=(0.0201351656218154, -0.0477653500564224))
    s1.autoTrimCurve(curve1=g[17], point1=(0.0214956357320046, -0.048037511599276))
    s1.autoTrimCurve(curve1=g[18], point1=(0.0236724151379232, 
        -0.0515756936619682))
    s1.autoTrimCurve(curve1=g[19], point1=(0.0179583866261017, 
        -0.0542973685366291))
    s1.autoTrimCurve(curve1=g[36], point1=(0.0282980654768523, 
        -0.0534808596738485))
    s1.autoTrimCurve(curve1=g[38], point1=(0.0315632077320519, 
        -0.0551138652831258))
    s1.autoTrimCurve(curve1=g[8], point1=(0.0310190299425339, -0.0507591954967977))
    s1.autoTrimCurve(curve1=g[37], point1=(0.0310190339210386, 
        -0.0521200259019937))
    s1.autoTrimCurve(curve1=g[39], point1=(0.031563205467059, -0.0548416989538382))
    s1.autoTrimCurve(curve1=g[7], point1=(0.0345562678788981, -0.0518478550113307))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10278, 
        farPlane=1.10818, width=0.00208121, height=0.000933967, 
        cameraPosition=(0.0235614, 0.0770568, -1.10323), cameraTarget=(
        0.0235614, 0.0770568, 0.00225))
    s1.offset(distance=0.0001, objectList=(g[2], g[3], g[4], g[5], g[6], g[15]), 
        side=LEFT)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10308, 
        farPlane=1.10789, width=0.000727436, height=0.000326446, 
        cameraPosition=(0.0840382, 0.109274, -1.10323), cameraTarget=(
        0.0840382, 0.109274, 0.00225))
    s1.autoTrimCurve(curve1=g[6], point1=(0.0266028320915286, -0.0599178552058238))
    s1.autoTrimCurve(curve1=g[5], point1=(0.0265627125477536, -0.0599184590803262))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10286, 
        farPlane=1.10811, width=0.00172429, height=0.000773797, 
        cameraPosition=(0.068122, 0.108728, -1.10323), cameraTarget=(0.068122, 
        0.108728, 0.00225))
    s1.autoTrimCurve(curve1=g[4], point1=(0.01079575199631, -0.0566712162675432))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10299, 
        farPlane=1.10798, width=0.00114287, height=0.000512876, 
        cameraPosition=(0.0266779, 0.0822086, -1.10323), cameraTarget=(
        0.0266779, 0.0822086, 0.00225))
    s1.autoTrimCurve(curve1=g[3], point1=(-0.0253003298369921, -0.023661364803308))
    s1.autoTrimCurve(curve1=g[2], point1=(-0.0253596013062029, 
        -0.0235813726680728))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10286, 
        farPlane=1.10811, width=0.00173378, height=0.000778053, 
        cameraPosition=(0.00319217, 0.0173431, -1.10323), cameraTarget=(
        0.00319217, 0.0173431, 0.00225))
    s1.autoTrimCurve(curve1=g[15], point1=(-0.0379638336557693, 
        0.0442486295483322))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.45736, 
        farPlane=17.1524, width=42.2133, height=18.9437, cameraPosition=(
        8.92967, 4.14288, -11.3026), cameraTarget=(8.92967, 4.14288, 0.00225))
    s1.Arc3Points(point1=(-0.037865194198966, 0.0618461665945012), point2=(
        0.0385591667656759, -0.0581480930245183), point3=(7.035, 1.63275))
    p = mdb.models['Model-1'].parts['Part-1']
    e1, d2 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=e1[100], sketchPlaneSide=SIDE1, 
        sketchOrientation=LEFT, sketch=s1, depth=0.00025, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.212304, 
        farPlane=0.368527, width=0.0544623, height=0.0244406, cameraPosition=(
        0.218505, 0.208883, 0.180271), cameraTarget=(0.050834, 0.0412112, 
        0.0125993))
    p = mdb.models['Model-1'].parts['Part-1']
    e, d1 = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e[224], 
        sketchPlaneSide=SIDE1, sketchOrientation=LEFT, origin=(0.047738, 
        0.054657, 0.00225))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.319, gridSpacing=0.007, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=4)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.14902, 
        farPlane=0.48984, width=1.21441, height=0.544982, cameraPosition=(
        0.372351, 0.0528102, -0.31718), cameraTarget=(0.372351, 0.0528102, 
        0.00225))
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-1'].parts['Part-1']
    e1, p1 = p.edges, p.elemEdges
    p.projectEdgesOntoSketch(sketch=s, edges=(e1[0], e1[1], e1[2], e1[3], e1[4], 
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
    s.autoTrimCurve(curve1=g[41], point1=(-0.012110097980779, 0.0571832439162714))
    s.autoTrimCurve(curve1=g[58], point1=(-0.0146812319373838, 0.0491820655522466))
    s.autoTrimCurve(curve1=g[61], point1=(-0.0258228457643505, 0.042895431812091))
    s.autoTrimCurve(curve1=g[60], point1=(-0.0192521497723647, 0.0254642850674077))
    s.autoTrimCurve(curve1=g[59], point1=(-0.00582508707291233, 
        0.0348942344960436))
    s.autoTrimCurve(curve1=g[53], point1=(0.0064592508517405, 0.0394663484510574))
    s.autoTrimCurve(curve1=g[78], point1=(0.00274537664828772, 0.0543256922783124))
    s.autoTrimCurve(curve1=g[62], point1=(-0.0172523682330446, 0.0111764564575756))
    s.autoTrimCurve(curve1=g[63], point1=(-0.00611075560665012, 
        0.00831889944295634))
    s.autoTrimCurve(curve1=g[65], point1=(-0.0249657913643044, 
        -0.000539548371812387))
    s.autoTrimCurve(curve1=g[64], point1=(-0.00982464930422701, 
        -0.0113982913750283))
    s.autoTrimCurve(curve1=g[52], point1=(0.000174239569609415, 
        0.00517557957071989))
    s.autoTrimCurve(curve1=g[51], point1=(0.00131696436034303, 
        -0.0162561575745643))
    s.autoTrimCurve(curve1=g[66], point1=(-0.00839622228955719, 
        -0.0199709931520564))
    s.autoTrimCurve(curve1=g[67], point1=(-0.00353962154677501, 
        -0.0216855327030216))
    s.autoTrimCurve(curve1=g[69], point1=(-0.0121100954541515, 
        -0.0299724623505062))
    s.autoTrimCurve(curve1=g[68], point1=(-0.00411098954783844, 
        -0.0331157852518652))
    s.autoTrimCurve(curve1=g[70], point1=(0.0013169644834359, -0.0416884819081335))
    s.autoTrimCurve(curve1=g[50], point1=(0.00731629068704377, -0.030543976509971))
    s.autoTrimCurve(curve1=g[49], point1=(0.0187435923411964, -0.0451175530456231))
    s.autoTrimCurve(curve1=g[48], point1=(0.0284567883118323, -0.0474036082905826))
    s.autoTrimCurve(curve1=g[47], point1=(0.0370272495209001, -0.0496896574459819))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.316616, 
        farPlane=0.360482, width=0.0909738, height=0.0408256, cameraPosition=(
        0.0748129, 0.0899852, -0.336299), cameraTarget=(0.0748129, 0.0899852, 
        0.00225))
    s.autoTrimCurve(curve1=g[54], point1=(0.029423298640907, -0.0538400838610772))
    s.autoTrimCurve(curve1=g[55], point1=(0.0309211028372269, -0.0506189855505761))
    s.autoTrimCurve(curve1=g[57], point1=(0.0323440060411988, -0.0569862771191178))
    s.autoTrimCurve(curve1=g[56], point1=(0.0350400481710876, -0.0544393550632115))
    s.autoTrimCurve(curve1=g[76], point1=(0.0237316665450682, -0.0516677118416644))
    s.autoTrimCurve(curve1=g[75], point1=(0.0205114022357582, -0.0479971489034124))
    s.autoTrimCurve(curve1=g[74], point1=(0.0177404764629404, -0.0486713373093024))
    s.autoTrimCurve(curve1=g[77], point1=(0.0181898116574742, -0.0553382675785301))
    s.autoTrimCurve(curve1=g[72], point1=(0.0106259348300712, -0.0486713392081681))
    s.autoTrimCurve(curve1=g[73], point1=(0.00598275682191638, -0.050993530009268))
    s.autoTrimCurve(curve1=g[71], point1=(0.00927791626955813, 
        -0.0370603888832348))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.285041, 
        farPlane=0.392057, width=0.370174, height=0.16612, cameraPosition=(
        0.143274, 0.0886111, -0.336299), cameraTarget=(0.143274, 0.0886111, 
        0.00225))
    s.autoTrimCurve(curve1=g[84], point1=(0.0391785421513981, -0.0532057007404868))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23538, 
        farPlane=1.2401, width=0.000488804, height=0.000219357, 
        cameraPosition=(0.000157707, 7.11838e-05, -1.23549), cameraTarget=(
        0.000157707, 7.11838e-05, 0.00225))
    s.autoTrimCurve(curve1=g[86], point1=(-0.0379474967921643, 0.0618428804600977))
    s.autoTrimCurve(curve1=g[85], point1=(-0.0379668112618338, 0.0618227559907935))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23536, 
        farPlane=1.24012, width=0.000593228, height=0.000266218, 
        cameraPosition=(0.00841886, 0.049198, -1.23549), cameraTarget=(
        0.00841886, 0.049198, 0.00225))
    s.autoTrimCurve(curve1=g[79], point1=(-0.0379656938282663, 0.0118361871362137))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23528, 
        farPlane=1.2402, width=0.000967169, height=0.000434029, 
        cameraPosition=(0.0478325, 0.100755, -1.23549), cameraTarget=(
        0.0478325, 0.100755, 0.00225))
    s.autoTrimCurve(curve1=g[81], point1=(-0.0074136973241407, 
        -0.0456168057578095))
    s.autoTrimCurve(curve1=g[80], point1=(-0.00743280342698754, 
        -0.0456016690970707))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23514, 
        farPlane=1.24034, width=0.00161195, height=0.000723382, 
        cameraPosition=(0.0835209, 0.109259, -1.23549), cameraTarget=(
        0.0835209, 0.109259, 0.00225))
    s.autoTrimCurve(curve1=g[83], point1=(0.0266560182111327, -0.0599141092580194))
    s.autoTrimCurve(curve1=g[82], point1=(0.0265193368020324, -0.0599154374299281))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.682214, 
        farPlane=1.79327, width=3.99563, height=1.79309, cameraPosition=(
        0.338143, 0.2808, -1.23549), cameraTarget=(0.338143, 0.2808, 0.00225))
    s.Arc3Points(point1=(-0.037865194198966, 0.0618292708125828), point2=(
        0.0385417035329429, -0.0581505317831723), point3=(1.1305, 0.385))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23542, 
        farPlane=1.24006, width=0.000339911, height=0.000152539, 
        cameraPosition=(0.095503, 0.105675, -1.23549), cameraTarget=(0.095503, 
        0.105675, 0.00225))
    s.autoTrimCurve(curve1=g[87], point1=(0.0385639350423906, -0.0582180549722982))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01546, 
        farPlane=1.46002, width=1.58899, height=0.71308, cameraPosition=(
        0.195148, 0.0665575, -1.23549), cameraTarget=(0.195148, 0.0665575, 
        0.00225))
    p = mdb.models['Model-1'].parts['Part-1']
    e, d2 = p.edges, p.datums
    p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=e[224], sketchPlaneSide=SIDE1, 
        sketchOrientation=LEFT, sketch=s, depth=0.00025, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-1']
    s1 = p.features['Cut extrude-2'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Cut extrude-2'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Part-1']
    p.features['Cut extrude-2'].setValues(flipExtrudeDirection=True)
    p = mdb.models['Model-1'].parts['Part-1']
    p.regenerate()

Macro2()