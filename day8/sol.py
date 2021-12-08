# Probably easier with linear algebra shenanigans

import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def Count1478(lines):
    # General formation rules:
    #  * 1 -> 7 -> 4 -> (2, 3, 5)  -> (0, 6, 9) -> 8
    # EZ Digits: 1, 7, 4, 8

    insAndOuts = []
    storage1478 = []

    len1 = 2
    len7 = 3
    len4 = 4
    len8 = 7

    len235 = 5
    len069 = 6

    chars1 = {}
    numStuff = {}

    # Get the non overlapping char between two strings
    def Get1NonOverlap(strLong, strShort):
        strPrcs = str(strLong)
        for x in strLong:
            if x in strShort:
                strPrcs.replace(x, '')
        
        assert(len(strPrcs) == 1)
        return strPrcs[0]
    
    

    # Parse Input
    for line in lines:
        insAndOuts.append((line.split(' | ')[0].split(), line.split(' | ')[1].split()))

    for entry in insAndOuts:
        for inSig in entry[0]:
            match len(inSig):
                case 1:
                    chars1[1] = (set([char for char in inSig]))
                case 7:
                    chars1[7] = (set([char for char in inSig]))
                case 4:
                    chars1[4] = (set([char for char in inSig]))
                case 8:
                    chars1[8] = (set([char for char in inSig]))

    chars1[9].update(chars1[4])
    chars1[9].update(chars1[7])

    chars1[3].update(chars1[7])

    chars1[0].update(chars1[7])

    # 1   1   1
    # 2       3
    # 2       3
    # 2       3
    # 4   4   4
    # 5       6
    # 5       6
    # 5       6
    # 7   7   7
    if chars1.has_key(1):
        if chars1.has_key(7):
            numStuff[1] = Get1NonOverlap(chars1[7], chars1[1])
    elif chars1.has_key(8):
        if chars1.has_key(9):
            numStuff[5] = Get1NonOverlap(chars1[8], chars1[9])
        if chars1.has_key(0):
            numStuff[4] = Get1NonOverlap(chars1[8], chars1[0])
    elif chars1.has_key(6):
        if chars1.has_key(5):
            numStuff[5] = Get1NonOverlap(chars1[6], chars1[5])
        if chars1.has_key(8):
            numStuff[3] = Get1NonOverlap(chars1[8], chars1[6])
        if chars1.has_key(7):
            numStuff[3] = Get1NonOverlap(chars1[6], chars1[7])
    elif chars1.has_key(5):
        if chars1.has_key(7):
            numStuff[3] = Get1NonOverlap(chars1[5], chars1[7])
    

        

    return len(storage1478)
    
                
                    
def daGoods():
    print(Count1478(readInputFile('exinput.txt')))
    print(Count1478(readInputFile('input.txt')))

daGoods()