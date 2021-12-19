import os
import heapq
from collections import Counter, OrderedDict

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]
    
    return inputLines

class Node:
    def __init__(self, coord: tuple, value, prev) -> None:
        self.coord = coord
        self.value = value
        self.prev = prev

    def __lt__(self, rhs):
        return self.value < rhs.value
class DaGame:
    def __init__(self, lines) -> None:
        self.board = []
        for indexLine, line in enumerate(lines):
            self.board.append([])
            for indexRisk, risk in enumerate(line):
                self.board[indexLine].append(int(risk))
        
        self.__Part2Board(5)
    
    def __Part2Board(self, n):
        boardNew = [row[:] for row in self.board]
        # Generate first row with n duplicate first blocks
        for x in range(len(self.board)):
            for y in range(0, len(self.board[x]) - 1 + (n - 2) * (len(self.board[x])) + 1):
                boardNew[x].append(self.__incRisk(boardNew[x][y]))
        
        # Duplicate first row downwards
        for x in range(0, len(self.board) - 1 + (n - 2) * (len(self.board)) + 1):
            boardNew.append([])
            for y in range(len(boardNew[0])):
                boardNew[-1].append(self.__incRisk(boardNew[x][y]))

        self.board = boardNew
        

    def __incRisk(self, risk):
        if risk > 8:
            return 1
        else:
            return risk + 1

    def __isInRange(self, coord):
        return coord[0] < len(self.board) and coord[1] < len(self.board[0])

    def PlayGame(self):
        coordsExplored = set()
        coordsToVisit = set()                
        nodesPotential = []

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if x != 0 or y != 0:
                    coordsToVisit.add((x,y))
                    heapq.heappush(nodesPotential, Node((x,y), 9999999, None))

        nodeCur = Node((0, 0), 0, None)
        heapq.heappush(nodesPotential, nodeCur)

        while True:
            for xOff in range(-1, 2):
                for yOff in range(-1, 2):
                    coordNew = (xOff + nodeCur.coord[0], yOff + nodeCur.coord[1])
                    if (xOff == 0 or yOff == 0) and\
                    (abs(xOff) != abs(yOff)) and \
                    coordNew in coordsToVisit and \
                    self.__isInRange(coordNew):
                        nodeNew = Node(coordNew, nodeCur.value + self.board[coordNew[0]][coordNew[1]], nodeCur)   
                        coordsToVisit.remove(coordNew)
                        heapq.heappush(nodesPotential, nodeNew) # Gonna have a bunch of duplicates currently
                        if coordNew[0] == len(self.board) - 1 and coordNew[1] == len(self.board[0]) - 1:
                            return (nodeNew.value)
            nodeCur = heapq.heappop(nodesPotential)

            
def dieGuter():
    ex = DaGame(readInputFile("exinput.txt"))
    print(ex.PlayGame())

    actual = DaGame(readInputFile("input.txt"))
    print(actual.PlayGame())

dieGuter()
