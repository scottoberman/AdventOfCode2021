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
    def charMatchCount(chars1: set, chars2: set):

        if len(chars1) >= len(chars2):
            source = chars1
            target = chars2
        else:
            source = chars2
            target = chars2

        matchCount = 0
        for char in source:
            if char in target:
                matchCount += 1
                
        return matchCount
            

    ins = []
    outs = []
    outsResolved = []
    outsTotal = []

    len1 = 2
    len7 = 3
    len4 = 4
    len8 = 7

    len235 = 5
    len069 = 6

    chars1 = {}
    numStuff = {}


    # Parse Input
    for line in lines:
        ins = line.split(' | ')[0].split()
        outs = line.split(' | ')[1].split()

    for entry in ins:
            match len(entry):
                case 2:
                    chars1[1] = (set([char for char in entry]))
                case 3:
                    chars1[7] = (set([char for char in entry]))
                case 4:
                    chars1[4] = (set([char for char in entry]))
                case 7:
                    chars1[8] = (set([char for char in entry]))

    for entry in outs:
        if charMatchCount(chars1[8], set(entry)) == 6:
            # 9
            if charMatchCount(chars1[1], set(entry)) == 2:
                outsResolved.append('9')
            # 6
            elif charMatchCount(chars1[1], set(entry)) == 1:
                outsResolved.append('6')
            # 0
            elif charMatchCount(chars1[4], set(entry)) == 3:
                outsResolved.append('0')
        # 3
        elif charMatchCount(chars1[7], set(entry)) == 3:
            outsResolved.append('3')
        # 2
        elif charMatchCount(chars1[4], set(entry)) == 2:
            outsResolved.append('2')
        # 5
        elif charMatchCount(chars1[4], set(entry)) == 3:
            outsResolved.append('5')
        elif len(entry) == len1:
            outsResolved.append('1')
        elif len(entry) == len7:
            outsResolved.append('7')
        elif len(entry) == len4:
            outsResolved.append('4')
        elif len(entry) == len8:
            outsResolved.append('8')
        else:
            assert(False)
        
    outsResolved = outsResolved.join()
    outsTotal.append(outsResolved)

    return outsResolved
    
                
                    
def daGoods():
    print(Count1478(readInputFile('exinput.txt')))
    print(Count1478(readInputFile('input.txt')))

daGoods()