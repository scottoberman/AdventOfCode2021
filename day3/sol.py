# Hideous code challenge

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

    prod = int(gammaBin * epsBin)

    return prod
def RangerDangerPart2Outie(nums):
    return RangerDangerPart2Innie(nums, "oxy") * RangerDangerPart2Innie(nums, "c02")

def RangerDangerPart2Innie(nums, targetType):
    lenBits = len(nums[0])
    countZero = 0
    countOne = 0
    gamma = []
    eps = []
    gammaBin = 0
    epsBin = 0
    leadingNum = ""
    for x in range(lenBits):
        y = 0
        if len(nums) == 1:
            break
        for y in nums:
            if y[x] == "0":
                countZero += 1
            elif y[x] == "1":
                countOne += 1
        
        if countZero > countOne:
            leadingNum = "0"
        else:
            leadingNum = "1"

        if targetType == "oxy":
            if countZero > countOne:
                numsNew = [z for z in nums if z[x] == "0"]
            else:
                numsNew = [z for z in nums if z[x] == "1"]
        elif targetType == "c02":
            if countZero > countOne:
                numsNew = [z for z in nums if z[x] == "1"]
            else:
                numsNew = [z for z in nums if z[x] == "0"]
        else:
            assert(False)

        nums = numsNew

        countZero = 0
        countOne = 0

        print("blah")

    return int(nums[0], 2)

def theGoods():
    RangerDangerBits(readInputFile("input.txt"))
    print(RangerDangerPart2Outie(readInputFile("input.txt")))
    

theGoods()