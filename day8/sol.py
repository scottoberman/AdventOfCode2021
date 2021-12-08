import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines


def CalcScore(lines):
    # General formation rules:
    #  * 1 -> 7 -> 4 -> (2, 3, 5)  -> (0, 6, 9) -> 8
    # EZ Digits: 1, 7, 4, 8
            
    ins = []
    outs = []
    outsTotal = []

    len1 = 2
    len7 = 3
    len4 = 4
    len8 = 7

    chars1 = {}

    # Parse Input
    for line in lines:
        outsResolved = []
        ins = line.split(' | ')[0].split()
        outs = line.split(' | ')[1].split()

        for entry in ins:
                match len(entry):
                    case 2:
                        chars1[1] = (set([char for char in entry]))
                    case 3:
                        chars1[7] = (set([char for char in entry]))
                    case 4:
                        chars1[4] = (set([char for char in entry]))
                    case 7:
                        chars1[8] = (set([char for char in entry]))

        for entry in outs:
            if len(entry) == len1:
                outsResolved.append('1')
            elif len(entry) == len7:
                outsResolved.append('7')
            elif len(entry) == len4:
                outsResolved.append('4')
            elif len(entry) == len8:
                outsResolved.append('8')
            elif len(chars1[8].intersection(set(entry))) == 6:
                if len(chars1[1].intersection(set(entry))) == 2 and \
                len(chars1[4].intersection(set(entry))) != 3:
                    outsResolved.append('9')
                elif len(chars1[1].intersection(set(entry))) == 1:
                    outsResolved.append('6')
                elif len(chars1[4].intersection(set(entry))) == 3:
                    outsResolved.append('0')
                else:
                    assert(False)
            elif len(chars1[7].intersection(set(entry))) == 3:
                outsResolved.append('3')
            elif len(chars1[4].intersection(set(entry))) == 2:
                outsResolved.append('2')
            elif len(chars1[4].intersection(set(entry))) == 3:
                outsResolved.append('5')
            else:
                assert(False)
        
        outsTotal.append(int(''.join(outsResolved)))

    return sum(outsTotal)
    
                
                    
def daGoods():
    print(CalcScore(readInputFile('exinput.txt')))
    print(CalcScore(readInputFile('input.txt')))

daGoods()