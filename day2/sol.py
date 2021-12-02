import os
import string
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()

    return inputLines

def findPosPart1(lines):
    posX = 0
    posY = 0
    for line in lines:
        dir = line.split()[0]
        val = int(line.split()[1])
    
        if dir == "forward":
            posX += val
        elif dir == "up":
            posY -= val
        elif dir == "down":
            posY += val
    
    return posX * posY

def findPosPart2(lines):
    posX = 0
    posY = 0
    aim = 0

    for line in lines:
        dir = line.split()[0]
        val = int(line.split()[1])
    
        if dir == "forward":
            posX += val
            posY += aim * val
        elif dir == "up":
            aim -= val
        elif dir == "down":
            aim += val
    
    return posX * posY

def theGoods():
    print(findPosPart1(readInputFile("input.txt")))
    print(findPosPart2(readInputFile("input.txt")))
theGoods()