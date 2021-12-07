import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def getMinCost(crabsLine):

    crabsStrs = crabsLine.split(',')

    crabs = [int(x) for x in crabsStrs]

    crabs.sort()

    locMin = crabs[0]
    locMax = crabs[-1]

    costMin = len(crabs) * locMax

    for loc in range (locMin, locMax + 1):
        costCur = 0
        for crab in crabs:
            costCur += abs(crab - loc)

            # else:
            #     break
        if costCur <= costMin:
            costMin = costCur

    return costMin

def daGoods():
    print(getMinCost(readInputFile('exinput.txt')[0]))
    print(getMinCost(readInputFile('input.txt')[0]))

daGoods()