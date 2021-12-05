import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def ventStuff(lines):
    def generateVentCoords(line):
        x1 = int(line[0])
        x2 = int(line[2])
        y1 = int(line[1])
        y2 = int(line[3])


        # Horiz or Vertical
        if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2):
            incX = 1
            incY = 1

            if x1 > x2:
                incX = -1
            if y1 > y2:
                incY = -1

            for x in range(x1, x2 + incX, incX):
                for y in range(y1, y2 + incY, incY):
                    coordTemp = (x,y)
                    daVents[coordTemp] += 1
        #else:
            # Don't allow diags
            
                
    coords = [x.replace(",", " ").replace(" ->", "").split() for x in lines]
    daVents = Counter()
    
    for coord in coords:
        generateVentCoords(coord)

    dubs = 0
    for vent in daVents:
        if daVents[vent] > 1:
            dubs += 1

    return dubs




    
def daGoods():
    exinput = readInputFile("exinput.txt")
    print(ventStuff(exinput))

    input = readInputFile("input.txt")
    print(ventStuff(input))

daGoods()