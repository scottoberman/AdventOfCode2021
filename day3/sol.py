import os
import string
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines


def RangerDangerBits(nums):
    lenBits = len(nums[0])
    countZero = 0
    countOne = 0
    gamma = []
    eps = []
    gammaBin = 0
    epsBin = 0
    for x in range(lenBits):
        for y in nums:
            if y[x] == "0":
                countZero += 1
            elif y[x] == "1":
                countOne += 1
        
        if countZero > countOne:
            gamma.append("0")
            eps.append("1")
        else:
            gamma.append("1")
            eps.append("0")
        countZero = 0
        countOne = 0

        gammaBin = int(''.join(x for x in gamma), 2)
        epsBin = int(''.join(x for x in eps), 2)
        print("blah")

    prod = int(gammaBin * epsBin)

    return prod

def theGoods():
    RangerDangerBits(readInputFile("input.txt"))

theGoods()