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
        if (lineIndex, eleIndex - 1) in pointsToCheck and (eleIndex > 0  and grid[lineIndex][eleIndex - 1] != 9):
            pointsToCheck.remove((lineIndex, eleIndex - 1))
            basinInd.append((lineIndex, eleIndex - 1))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving right
        if (lineIndex, eleIndex + 1) in pointsToCheck and (eleIndex < len(grid[0]) - 1  and grid[lineIndex][eleIndex + 1] != 9):
            pointsToCheck.remove((lineIndex, eleIndex + 1))
            basinInd.append((lineIndex, eleIndex + 1))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving down
        if lineIndex > 0 and grid[lineIndex - 1][eleIndex] != 9:
            pointsToCheck.remove((lineIndex - 1, eleIndex))
            basinInd.append((lineIndex - 1, eleIndex))
            DFSBasin(basinInd, pointsToCheck, grid, basinNum, basinData)
        # Moving up
        if lineIndex < len(grid) - 1 and grid[lineIndex + 1][eleIndex] != 9:
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
        basinNum += 1

def daGoods():
    print(GetLowPointsRiskScore(readInputFile("exinput.txt")))
    print(GetLowPointsRiskScore(readInputFile("input.txt")))


daGoods()