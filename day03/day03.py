from util import Util
l1 = 'R992,U221,L822,U805,R667,D397,L969,U433,R918,D517,L494,U909,L224,D738,R247,D312,L803,D656,L571,D968,L392,D332,L581,U487,R522,D780,L74,D561,L246,U380,L125,U11,R735,D761,R482,D208,R985,D991,L352,U140,L586,D492,L777,U96,R682,D969,R775,U279,R671,D423,R838,U907,L486,D702,L432,D625,R463,U559,R12,D531,R510,D347,R147,U949,R175,U160,L975,D627,L537,D343,L406,D237,R953,U725,L996,D740,L703,D996,R157,U356,R247,D541,L592,D345,R580,U656,R50,D423,L158,U502,L86,U729,L720,D464,R901,D739,L20,U21,R497,D14,L580,U610,L114,D858,R853,U550,L354,D433,L507,U144,R9,U422,R674,U604,R107,D999,L420,U675,R538,D491,R84,D158,R303,D450,L616,U938,L162,U102,L160,U275,L281,D164,L254,U103,R60,D707,R655,U128,L907,U225,L292,U919,R517,D276,R308,D113,L455,U584,R899,U321,L417,U449,L780,U387,L579,U224,L192,D325,L626,U145,R178,D162,L18,D469,R169,U694,R162,D806,L10,U979,L944,D304,R719,D253,L343,D711,R429,D933,R445,D772,R230,D407,R335,U883,L900,D377,R413,D44,R805,D378,R421,D860,L597,U63,L583,D561,R235,D502,L37,U29,L381,U803,R588,D972,R678,D223,L440,U835,R88,D16,R529,D867,R742,U25,R353,D952,R31,D202,R737,D744,R765,U154,L969,U851,L22,U165,L12,D457,R635,U829,L996,D871,L397,U995,R215,D505,R93,U12,R183,D920,L442,D393,L919,D803,R22,D806,R776,U558,R263,D222,R111,D530,L908,D640,R351,D172,R315,U731,R25,U718,L172,D145,L606,U803,R837,U310,L607,D523,R271,U927,R3,U518,R754,D322,L924,D256,L997,U153,L904,D745,L475,U346,L979,D658,R208,U924,L484,U961,R94,D283,L79,U927,R122,D513,L806,D480,L971,U340,R328,D427,L494'
l2 = 'L998,U308,R889,D471,R719,U326,L6,U802,L608,U149,R454,U6,R837,U255,L720,D60,L426,D525,L190,U995,R676,U172,R910,U645,R249,D725,R355,U668,L988,U253,L820,D266,R836,D750,R998,U113,L502,U634,L620,U903,L542,D426,L497,D766,R930,U415,R655,D676,L694,D548,L280,U895,L899,U235,R912,D257,R161,D834,R88,D379,L723,U508,L604,D1,R706,D321,R725,U986,R52,D741,L738,D810,R595,U352,L835,D712,R797,D332,L451,D145,L608,U940,R886,D945,R929,D4,R332,D303,L877,D927,R686,U762,L588,D496,R352,D516,R355,D299,L459,D831,R9,U322,R635,U895,L127,U27,R996,D491,L360,U921,L146,U833,L420,D60,R32,D936,R815,D451,R715,U570,R889,D35,R135,U814,L559,D141,L470,U410,L711,D668,L196,U42,R989,U448,L875,U417,R554,U61,R259,D111,L177,D147,L925,D427,R911,U667,L209,U641,L516,U521,R373,D165,L91,U594,R968,U536,L694,U270,R602,U92,L158,U321,R422,D851,L73,D492,L698,D950,L988,U48,L184,D99,R67,D168,R269,D918,L645,D736,L597,U104,L427,U72,R568,D749,R16,U190,L146,D911,L820,D275,R12,U402,R461,D595,L103,D326,R948,U288,L1,D786,R698,D286,L557,U283,R278,U327,R457,D136,L878,D23,L371,U836,R987,U695,R904,U395,R869,U276,R310,D843,L994,D209,R554,U653,L924,U659,R695,U779,L427,U504,R711,D679,R191,D775,R816,D293,L415,D323,R505,U154,R966,U446,R837,U707,L591,D593,L696,U168,R35,U905,R141,U708,L772,D898,R254,U612,R934,U114,R912,D576,L721,D965,R731,U737,R494,D760,R909,D244,R662,D863,L23,D298,L234,D476,L571,D786,L48,U960,L377,U134,R335,D453,R203,D120,L27,U365,R254,U446,R738,D919,L42,U529,R31,D104,R583,U272,R867,U834,L43,D220,R424'

# l1 = 'R8,U5,L5,D3'
# l2 = 'U7,R6,D4,L4'

# l1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# l2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# l1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# l2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

def solveDistance():
    # return findDistance2(l1, l2)
    return findDistance(l1, l2)

def solveBestSteps():
    return bestSteps(l1, l2)

def bestSteps(line1, line2):
    minSteps = Util.maxInt()
    arr1 = createPointsArray(line1)
    arr2 = createPointsArray(line2)

    steps1 = 0
    for point in arr1:
        steps1 += 1
        if point in arr2:
            steps2 = findPointIndex(arr2, point)
            steps = steps1 + steps2
            if steps < minSteps:
                minSteps = steps
    return minSteps

def findPointIndex(arr, point):
    i = 0
    for p in arr:
        i += 1
        if point == p:
            break
    return i

def findDistance(line1, line2):
    minDistance = Util.maxInt()
    arr1 = createPointsArray(line1)
    arr2 = createPointsArray(line2)
    # intersection = [list(filter(lambda x: x in arr1, sublist)) for sublist in arr2]

    i = 0
    for point in arr1:
        i += 1
        if point in arr2:
            dist = abs(point[0]) + abs(point[1])
            if dist < minDistance:
                minDistance = dist
    return minDistance

def createPointsArray(line):
    x = 0
    y = 0
    arr = []
    paths = line.split(',')
    for path in paths:
        direction = path[:1]
        steps = int(path[1:])
        moveTuple = getMoveTuple(direction)
        for i in range(steps):
            x += moveTuple[1]
            y += moveTuple[0]
            arr.append((x, y))
    return arr

def findDistance2(line1, line2):
    m1 = getMatrixSize(line1)
    m2 = getMatrixSize(line2)
    sizeX = max(m1[1], m2[1]) - min(m1[0], m2[0])
    sizeY = max(m1[3], m2[3]) - min(m1[2], m2[2])
    # matrix1 = Util.createZeroMatrix(max(m1[1] - m1[0], m2[1] - m2[0]) + 2, max(m1[3] - m1[2], m2[3] - m2[2]) + 2)
    # matrix2 = Util.createZeroMatrix(max(m1[1] - m1[0], m2[1] - m2[0]) + 2, max(m1[3] - m1[2], m2[3] - m2[2]) + 2)
    matrix1 = Util.createZeroMatrix(sizeX + 2, sizeY + 2)
    matrix2 = Util.createZeroMatrix(sizeX + 2, sizeY + 2)
    start = (max(m1[0], m2[0]), max(m1[2], m2[2]))
    passMatrix(matrix1, line1)
    passMatrix(matrix2, line2)
     
    return minCrossDistance(matrix1, matrix2)

def minCrossDistance(matrix1, matrix2):
    width = len(matrix1[0])
    height = len(matrix1)
    minDistance = width + height
    for x in range(width):
        for y in range(height):
            if matrix1[y][x] == 1 and matrix2[y][x] == 1 and x != 0 and y != 0:
                if minDistance > x + y:
                    minDistance = x + y

    return minDistance

def passMatrix(matrix, line):
    x = 0
    y = 0
    paths = line.split(',')

    for path in paths:
        direction = path[:1]
        steps = int(path[1:])
        if direction == 'R':
            for i in range(steps):
                matrix[y][x + i + 1] = 1
            x += steps
        elif direction == 'L':
            for i in range(steps):
                matrix[y][x - i - 1] = 1
            x -= steps
        elif direction == 'U':
            for i in range(steps):
                matrix[y + i + 1][x] = 1
            y += steps
        elif direction == 'D':
            for i in range(steps):
                matrix[y - i - 1][x] = 1
            y -= steps

def getMoveTuple(direction):
    if direction == 'R':
        return (0, 1)
    elif direction == 'L':
        return (0, -1)
    elif direction == 'U':
        return (1, 0)
    elif direction == 'D':
        return (-1, 0)

def getMatrixSize(line):
    x = 0
    y = 0
    maxx = 0
    maxy = 0
    minx = 0
    miny = 0
    paths = line.split(',')
    for path in paths:
        direction = path[:1]
        if direction == 'R':
            x += int(path[1:])
        elif direction == 'L':
            x -= int(path[1:])
        elif direction == 'U':
            y += int(path[1:])
        elif direction == 'D':
            y -= int(path[1:])
        
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        if x < minx:
            minx = x
        if y > maxy:
            miny = y

    return (minx, maxx, miny, maxy)