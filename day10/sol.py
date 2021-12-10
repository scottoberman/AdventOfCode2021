import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

# Assuming all chunks at least start (so never looking for a '(', '[', etc as an error only cosing symbols).
def TotalErrorScore(lines):
    symbStack = []

    symbPairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    charErrorScore = {')': 3, ']': 57, '}': 1197, '>': 25137}

    totalErrorScore = 0

    for line in lines:
        for char in line:
            if char in symbPairs:
                symbStack.append(symbPairs[char])
            else:
                if symbStack[-1] == char:
                    symbStack.pop()
                else:
                    totalErrorScore += charErrorScore[char]
                    break

    return totalErrorScore

def daGoods():
    print(TotalErrorScore(readInputFile("exinput.txt")))
    print(TotalErrorScore(readInputFile("input.txt")))

daGoods()