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
    insAndOuts = []
    storage1478 = []

    len1 = 2
    len4 = 4
    len7 = 3
    len8 = 7

    for line in lines:
        insAndOuts.append((line.split(' | ')[0].split(), line.split(' | ')[1].split()))

    for entry in insAndOuts:
        for out in entry[1]:
            if len(out) == len1 or len(out) == len4 or \
            len(out) == len7 or len(out) == len8:
                storage1478.append(out)
            # Seems like python match doesn't support fall throughs
            # match len(out):
            #     case 1:
            #         storage1478.append(out)
            #     case 4:
            #         storage1478.append(out)
            #     case 7:
            #         storage1478.append(out)
            #     case 8:
            #         storage1478.append(out)

    return len(storage1478)
                
                    
def daGoods():
    print(Count1478(readInputFile('exinput.txt')))
    print(Count1478(readInputFile('input.txt')))

daGoods()