import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

class Dumbos:
    def __init__(self, lines) -> None:
        self.__energyMax = 9
        self.__grid = [] # Values of this list undergo transformation
        self.__legalRange = set()
        self.__flashesCount = 0
        self.__hardZeroBoys = set()
        self.__burstingBoys = set()
        for x, line in enumerate(lines):
            self.__grid.append([])
            for y, energy in enumerate(line):
                self.__grid[x].append(int(energy))
                self.__legalRange.add((x,y))

    def runScenario(self, steps):
        for step in range(steps):
            self.__runStep()

        return self.__flashesCount

    def __runStep(self):
        self.__hardZeroBoys = set()
        self.__burstingBoys = set()
        for x, line in enumerate(self.__grid):
            for y, energy in enumerate(line):
                self.__grid[x][y] += 1
                if self.__grid[x][y] > self.__energyMax:
                    self.__burstingBoys.add((x,y))
                    self.__hardZeroBoys.add((x,y))
                    self.__grid[x][y] = 0
                    self.__flashesCount += 1

        # Now have to see if any have become greater than 9
        self.__resolveFlashes()
        
    def __resolveFlashes(self):

        while len(self.__burstingBoys) > 0:
            coordCur = self.__burstingBoys.pop()
            self.__hardZeroBoys.add(coordCur)
            for xOff in range(-1, 1 + 1):
                for yOff in range(-1, 1 + 1):
                    if xOff != 0 or yOff != 0:
                        coordExam = (coordCur[0] + xOff, coordCur[1] + yOff)
                        if coordExam in self.__legalRange and \
                        coordExam not in self.__hardZeroBoys and \
                        coordExam not in self.__burstingBoys:
                            self.__grid[coordExam[0]][coordExam[1]] += 1

                            if self.__grid[coordExam[0]][coordExam[1]] > self.__energyMax:
                                self.__burstingBoys.add(coordExam)
                                self.__grid[coordExam[0]][coordExam[1]] = 0
                                self.__flashesCount += 1

def daGoodies():
    ex1 = Dumbos(readInputFile("exinput.txt"))
    print(ex1.runScenario(100))
    part1 = Dumbos(readInputFile("input.txt"))
    print(part1.runScenario(100))

daGoodies()