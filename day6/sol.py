import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def fishCalc(fishesInit, dayTarget, daysRep1stGen, daysRep2ndGen):

    assert(daysRep1stGen > daysRep2ndGen)

    class fish:
        def __init_(self, daysToRep):
            self.daysToRep = daysToRep
            self.genOne = True

    fishCount = Counter()

    for day in range(daysRep1stGen + 1):
        fishCount[day] = 0

    for fish in fishesInit:
        fishCount[int(fish)] += 1

    for day in range(dayTarget):
        fishCountNew = Counter()
        for fish in fishCount:
            if  fish != daysRep1stGen:
                fishCountNew[fish] = fishCount[fish + 1]
            else:
                fishCountNew[daysRep1stGen] += fishCount[0]

            if fish == daysRep2ndGen:
                fishCountNew[daysRep2ndGen] += fishCount[0]

        fishCount = fishCountNew

    totalFishCount = 0

    for count in fishCount:
        totalFishCount += fishCount[count]



    return totalFishCount   

def daGoods():
    # Part 1 Example == 5934
    fishCalc(readInputFile("exinput.txt")[0].split(','), 80, 8, 6)

    # Part 1 Actual
    fishCalc(readInputFile("input.txt")[0].split(','), 80, 8, 6)

    # Part 2 Example == 5934
    ans = fishCalc(readInputFile("exinput.txt")[0].split(','), 256, 8, 6)

    assert(26984457539 == ans)

    # Part 2 Actual
    ans = fishCalc(readInputFile("input.txt")[0].split(','), 256, 8, 6)

    print(ans)

daGoods()