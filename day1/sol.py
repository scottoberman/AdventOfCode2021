import os
import string
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()

    return inputLines

def RangerDangerIntegers(depths):
    count = 0
    for x in range (1, len(depths)):
        if int(depths[x]) > int(depths[x - 1]):
            count += 1
    return count

def RangerDangerThreeIntegers(depths):
    depth = 3
    depthsInts = [int(x) for x in depths]
    count = 0
    for x in range (len(depthsInts) - depth):

        sum1 = sum(depthsInts[x:x+depth])
        sum2 = sum(depthsInts[x + 1:x+depth+1])
        if sum2 > sum1 :
            count += 1
    return count    

def main():
    input = readInputFile("input.txt")
    print(RangerDangerIntegers(input))
    print(RangerDangerThreeIntegers(input))


main()