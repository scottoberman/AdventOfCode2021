import os
from collections import Counter, OrderedDict

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

def GenerateGrid(inputFile):

    coords, folds = ParseLines(readInputFile(inputFile))

    maxX, maxY = PreProcessCoords(coords)

    grid = [[0 for x in range(maxX)] for y in range(maxY)]

    # Prefill grid with dots
    charFill = '.'
    for x in range(maxX):
        for y in range(maxY):
            grid[y][x] = charFill

    charMark = '#'
    for coord in coords:
        grid[coord[1]][coord[0]] = charMark

    for fold in folds:
        ExecFold(fold, grid)

    someThing = 4

def ExecFold(fold, grid):
    if fold[0] == 'y':
        foldedPart = [tuple(ele) for ele in grid[fold[1]:-1]]

        # Shrink the grid
        grid = grid[:fold[1]]

        # fold may extend over top of original grid
        # but check this case later
        assert(len(foldedPart) > len(grid))
        # if len(foldedPart) > len(grid):


    elif fold[1] == 'y':
    else:
        assert(False)

def FoldOnGrid(foldedPart, grid):
    # Measure from the bottom
    
    
def ParseLines(lines):
    coords = []
    folds = []
    inCoordSec = True

    # X and Y are swapped compared
    # to what is normally done
    for line in lines:
        if line != "":
            if inCoordSec:
                coords.append((int(line.split(',')[0]), int(line.split(',')[1])))
            else:
                folds.append((line.split('=')[0][-1], int(line.split('=')[1])))
        else:
            inCoordSec = False

    return coords, folds

# Need to find max value in each dimension
def PreProcessCoords(coords):
    maxX = 0
    maxY = 0
    for coord in coords:
        if coord[0] > maxX:
            maxX = coord[0]
        if coord[1] > maxY:
            maxY = coord[1]
    
    return maxX + 1, maxY + 1

def iBeni():
    print(GenerateGrid("exinput.txt"))

iBeni()