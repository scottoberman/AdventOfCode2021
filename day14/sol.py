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
    
def ParseLines(lines):
    startChem = lines[0]
    rules = {}

    for line in lines[2:]:
        chars = line.split(' -> ')[0]
        insert = line.split(' -> ')[1]

        rules[chars] = insert

    return startChem, rules

def ResolveChem(lines, steps):
    chemStatic, rules = ParseLines(lines)

    chemCur = str(chemStatic)

    for step in range(steps):
        for startPos in range(len(chemStatic) - 1, -1, -1):
            if chemStatic[startPos:startPos + 2] in rules:
                pre = chemCur[:startPos + 1]
                post = chemCur[startPos + 1:]
                chemCur = chemCur[:startPos + 1] + rules[chemStatic[startPos:startPos + 2]] + chemCur[startPos + 1:]
            
        chemStatic = chemCur

    return GetChemScore(chemStatic)

def GetChemScore(chem):
    chars = Counter()

    for char in chem:
        chars[char] += 1

    score = chars.most_common(1)[0][1] - chars.most_common()[-1][1]

    return score

def oOloa():
    print(ResolveChem(readInputFile("exinput.txt"), 10))
    print(ResolveChem(readInputFile("input.txt"), 10))

oOloa()