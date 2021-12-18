import os
from collections import Counter, OrderedDict

charFill = '.'
charMark = '#'

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines
    
def ResolveChem(lines, runs):
    startChem = lines[0]
    rules = {}

    for line in lines[2:]:
        chars = line.split(' -> ')[0]
        insert = line.split(' -> ')[1]
        pairs = Counter(map(str.__add__, startChem, startChem[1:]))
        cntr = Counter(startChem)

        rules[chars] = insert

    for run in range(runs):
        for (a,b), c in pairs.copy().items():
            x = rules[a+b]
            pairs[a+b] -= c
            pairs[a+x] += c
            pairs[x+b] += c
            cntr[x] += c

    return max(cntr.values())-min(cntr.values())

def oOloa():
    # print(ResolveChem(readInputFile("exinput.txt"), 10))
    print(ResolveChem(readInputFile("input.txt"), 40))

oOloa()