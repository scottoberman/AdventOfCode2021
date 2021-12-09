import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def DFSBasin(basinInd, pointsToCheck: set, grid, basinNum, basinData: dict):
        lineIndex, eleIndex = basinInd.pop()
        basinData[(lineIndex, eleIndex)] = basinNum
        # Moving left
        if (lineIndex, eleIndex - 1) in pointsToCheck:
            pointsToCheck.remove((lineIndex, eleIndex - 1))
            basinInd.append((lineIndex, eleIndex - 1))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving right
        if (lineIndex, eleIndex + 1) in pointsToCheck:
            pointsToCheck.remove((lineIndex, eleIndex + 1))
            basinInd.append((lineIndex, eleIndex + 1))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving down
        if (lineIndex - 1, eleIndex) in pointsToCheck:
            pointsToCheck.remove((lineIndex - 1, eleIndex))
            basinInd.append((lineIndex - 1, eleIndex))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving up
        if (lineIndex + 1, eleIndex) in pointsToCheck:
            pointsToCheck.remove((lineIndex + 1, eleIndex))
            basinInd.append((lineIndex + 1, eleIndex))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)


def GetLowPointsRiskScore(lines):
    grid = [[int(ele) for ele in line] for line in lines]

    basinData = []
    basinInd = []

    pointsToCheck = set()
    basinData = dict() # Coord then basin number
    coordFirst = 0
    getFirstPoint = True

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != 9:
                pointsToCheck.add((x,y))
                if getFirstPoint:
                    # Pretty random start point for checking basins
                    basinInd = [(x,y)]
                    coordFirst = (x,y)
                    getFirstPoint = False

    basinNum = 0

    pointsToCheck.remove(coordFirst)
    # Have to jump between basins.
    while len(pointsToCheck) > 0:
        DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        if len(pointsToCheck) > 0:
            assert(len(basinInd) == 0)
            basinInd.append(next(iter(pointsToCheck)))
        basinNum += 1

    basinProd = 1
    basinCount = Counter()
    for basin in basinData:
        basinCount[basinData[basin]] += 1

    for count in basinCount.most_common(3):
        basinProd *= count[1]
    
    return basinProd

def daGoods():
    print(GetLowPointsRiskScore(readInputFile("exinput.txt")))
    print(GetLowPointsRiskScore(readInputFile("input.txt")))


daGoods()