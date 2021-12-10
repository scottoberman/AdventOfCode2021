import os
import math
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

# Assuming all chunks at least start (so never looking for a '(', '[', etc as an error only cosing symbols).
def TotalIncompScore(lines):
    symbStack = []

    symbPairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    charIncompScore = {')': 1, ']': 2, '}': 3, '>': 4}

    linesScores = [0 for x in lines]

    for index, line in enumerate(lines):
        symbStack = []
        lineError = False
        for char in line:
            if char in symbPairs:
                symbStack.append(symbPairs[char])
            else:
                if symbStack[-1] == char:
                    symbStack.pop()
                else:
                    lineError = True
                    break
            
        if not lineError:
            while len(symbStack) > 0:
                charEnd = symbStack.pop()
                linesScores[index] = 5 * linesScores[index] + charIncompScore[charEnd]

    linesScores = list(filter(lambda x: x != 0, linesScores))
    midScore = sorted(linesScores)[math.ceil((len(linesScores) - 1)/2)]

    return midScore

def daGoods():
    print(TotalIncompScore(readInputFile("exinput.txt")))
    print(TotalIncompScore(readInputFile("input.txt")))

daGoods()