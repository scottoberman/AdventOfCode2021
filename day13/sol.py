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

def GenerateGrid(inputFile):

    coords, folds = ParseLines(readInputFile(inputFile))

    maxX, maxY = PreProcessCoords(coords)

    grid = [[0 for x in range(maxX)] for y in range(maxY)]

    # Prefill grid with dots
    for x in range(maxX):
        for y in range(maxY):
            grid[y][x] = charFill

    for coord in coords:
        grid[coord[1]][coord[0]] = charMark

    for fold in folds:
        grid = ExecFold(fold, grid)



    return CalcScore(grid)

def ExecFold(fold, grid):
    foldedPart = []
    if fold[0] == 'y':
        foldedPart = [tuple(ele) for ele in grid[len(grid):fold[1]:-1]]

        grid = grid[:fold[1]]

        # Fold may extend over top/side of original grid.
        # If so, fall on sword.
        assert(len(foldedPart) <= len(grid))


    elif fold[0] == 'x':
        
        for y in range(len(grid)):
            foldedPart.append([])
            for x in range(len(grid[0]) - 1, fold[1], -1):   
                foldedPart[-1].append(grid[y][x])

        # Shrink the grid
        grid = [grid[y][0:fold[1]] for y in range(len(grid))]

    else:
        assert(False)

    for x in range(len(foldedPart[0])):
        for y in range(len(foldedPart)):
            if foldedPart[y][x] == charMark:
                grid[len(grid) - len(foldedPart) + y][len(grid[0]) - len(foldedPart[0]) + x] = charMark

    return grid
    
    
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

def CalcScore(grid):
    score = 0
    for y in grid:
        for ele in y:
            if ele == charMark:
                score += 1

    return score

def iBeni():
    print(GenerateGrid("exinput.txt"))
    print(GenerateGrid("input.txt"))

iBeni()