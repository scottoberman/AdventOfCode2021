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
            if nodeTo not in self.graph:
                self.graph[nodeTo] = []
            self.graph[nodeFrom].append(nodeTo)
            self.graph[nodeTo].append(nodeFrom)

    def __canBeTraversed(self, node, pathCur, nodeToDouble):
        # These nodes can only be traversed once
        maxVisits = 1
        if node == nodeToDouble:
            maxVisits = 2
        if node == node.lower():
            if node not in pathCur or pathCur[node] < maxVisits:
                return True
            else:
                return False
        # These nodes can be traversed any number of times
        else:
            return True
            
    def search(self, pathCur, nodeCur, pathsFound, pathCurList, nodeToDouble):
        # Search each connected node
        for nextNode in self.graph[nodeCur]:
            if self.__canBeTraversed(nextNode, pathCur, nodeToDouble):
                if nextNode == "end":
                    # This should probably be done at the start of next recursion
                    # but maybe not.
                    pathCur[nextNode] += 1
                    pathCurList.append(nextNode)
                    pathsFound.add(''.join(pathCurList))
                else:
                    pathCur[nextNode] += 1
                    pathCurList.append(nextNode)
                    self.search(pathCur, nextNode, pathsFound, pathCurList, nodeToDouble)

                pathCur[nextNode] -= 1
                pathCurList.pop()
                assert (pathCur[nextNode] >= 0)




    def getPaths(self):
        nodeCur = "start"
        pathCur = Counter()
        pathCur[nodeCur] += 1
        pathCurList = []
        pathCurList.append(nodeCur)
        pathsFound = set()
        nodesDoubled = set()
        for nodeToDouble in self.graph:
            if nodeToDouble != "start" and \
            nodeToDouble != "end" and \
            nodeToDouble != "start":
                nodesDoubled.add(nodeToDouble)
                self.search(pathCur, nodeCur, pathsFound, pathCurList, nodeToDouble)

        return len(pathsFound)


def losGoods():
    ex1 = CaveGraph(readInputFile("exinput1.txt"))
    print(ex1.getPaths())

    ex2 = CaveGraph(readInputFile("exinput2.txt"))
    print(ex2.getPaths())

    ex3 = CaveGraph(readInputFile("exinput3.txt"))
    print(ex3.getPaths())

    actual = CaveGraph(readInputFile("input.txt"))
    print(actual.getPaths())

losGoods()