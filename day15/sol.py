import os
import heapq
from collections import Counter, OrderedDict

charFill = '.'
charMark = '#'

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

class DaGame:
    class DaPath:
        def __init__(self, nodes = []) -> None:
            self.score = 0
            self.nodes = list(nodes)
        def addNode(self, node, score):
            self.nodes.append((score, node))
            self.score += score
        def pop(self):
            nodeRemoved = self.nodes.pop()
            self.score -= nodeRemoved[0]
            
    def __init__(self, lines) -> None:
        for indexLine, line in enumerate(lines):
            for indexRisk, risk in enumerate(line):
                self.board[indexLine][indexRisk] = risk

    def __isInRange((x,y)):
        return x < len(self.board) and y < len(self.board[0])

    def PlayGame(self):
        pathCur = DaGame.DaPath()
        nodesExplored = set()

        self.Search(pathCur, nodesExplored)

    def Search(self, pathCur, nodesExplored):
        for xOff in range(-1, 2):
            for yOff in range(-1, 2):
                nodeNew = (xOff,yOff) + nodeCur
                if (xOff == 0 or yOff == 0) and\
                (abs(xOff) != abs(yOff)) and \
                (xOff,yOff) not in nodesExplored and \
                self.__isInRange(nodeNew):
                    nodeCur = pathCur.nodes[-1][-1]
                    
                    pathCur.addNode(nodeNew, self.board[x][y])
                    # Node is encountered 1st on the shortest
                    # path.
                    nodesExplored.add(nodeNew)
                    if nodeNew[0] == len(self.board) - 1 and nodeNew[0][0] == len(self.board[0]) - 1:
                        print(pathCur.score)
                    else:
                        pathCur.pop()

            
        

        

