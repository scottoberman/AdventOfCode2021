import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def GetLowPointsRiskScore(lines):
    grid = [[int(ele) for ele in line] for line in lines]
    lowPoints = [] # Coordinates then val

    for lineIndex, line in enumerate(grid):
        for eleIndex, ele in enumerate(line):
            lowLeft  = False
            lowRight = False
            lowUp    = False
            lowDown  = False
            if eleIndex == 0  or ele < grid[lineIndex][eleIndex - 1]:
                lowLeft = True
            if eleIndex == len(line) - 1  or ele < grid[lineIndex][eleIndex + 1]:
                lowRight = True
            if lineIndex == 0 or ele < grid[lineIndex - 1][eleIndex]:
                lowUp = True
            if lineIndex == len(grid) - 1 or ele < grid[lineIndex + 1][eleIndex]:
                lowDown = True
            
            if lowLeft and lowRight and lowUp and lowDown:
                lowPoints.append(((lineIndex, eleIndex), ele))

    riskScore = 0
    for ele in lowPoints:
        riskScore += ele[1] + 1
    return riskScore

def daGoods():
    print(GetLowPointsRiskScore(readInputFile("exinput.txt")))
    print(GetLowPointsRiskScore(readInputFile("input.txt")))


daGoods()