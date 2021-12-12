import os
from collections import Counter, OrderedDict

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

class CaveGraph:
    def __init__(self, lines) -> None:
        self.graph = OrderedDict()
        for line in lines:
            nodeFrom = line.split('-')[0]
            nodeTo = line.split('-')[1]
            if nodeFrom not in self.graph:
                self.graph[nodeFrom] = []
            self.graph[nodeFrom].append(nodeTo)

    def __canBeTraversed(self, node, pathCur):
        # These nodes can only be traversed once
        if node == node.lower():
            if node not in pathCur or pathCur[node] == 0:
                return True
            else:
                return False
        # These nodes can be traversed any number of times
        else:
            return True
            
    def search(self, pathCur, nodeCur, pathsFound):
        # Can halt pretty quickly if at a dead end
        if nodeCur in self.graph:
            # Search each connected node
            for nextNode in self.graph[nodeCur]:
                if self.__canBeTraversed(nextNode, pathCur):
                    if nextNode == "end":
                        # This should probably be done at the start of next recursion
                        # but maybe not.
                        pathCur[nextNode] += 1
                        pathsFound.append(Counter(pathCur))
                    else:
                        pathCur[nextNode] += 1
                        self.search(pathCur, nextNode, pathsFound)

                    pathCur[nextNode] -= 1
                    assert (pathCur[nextNode] >= 0)




    def getPaths(self):
        nodeCur = "start"
        pathCur = Counter()
        pathCur[nodeCur] += 1
        pathsFound = []
        self.search(pathCur, nodeCur, pathsFound)

        return len(pathsFound)


def losGoods():
    ex1 = CaveGraph(readInputFile("exinput1.txt"))
    print(ex1.getPaths())

losGoods()