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

def Parse(packet):
    def __parseLiteral(literal):
        blockStart = 0
        blockEnd = 5
        moreBlocks = True
        blocksAll = ""
        while moreBlocks:
            block = literal[blockStart:blockEnd]
            if block[0] == '1':
                blocksAll += block
            else:
                moreBlocks = False
        
        blocksAll = int(blocksAll, 2)

        return blocksAll

    typeLiteral = 2
    lengthType15 = 0
    lengthType11 = 1

    # Get version
    vers = int(packet[:3], 2)

    # Get type
    type = int(packet[3:6], 2)

    if type == typeLiteral:
        return __parseLiteral(packet[6:])
    else:
        lengthType = int(packet[6:7], 2)
        # Parse operator
        if lengthType == lengthType15:
            # Next 15 bits will contain
            # total length of all sub packets
            # thereafter
            length = int(packet[7:22], 2)
        if lengthType == lengthType11:
            # Next 11 bits will contain
            # number of sub packets immediately
            # contained within
            packetCount = int(packet[7:18], 2)