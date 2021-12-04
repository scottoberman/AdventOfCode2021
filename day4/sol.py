import os
from collections import Counter

def readInputFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\' + fileName
    inputFile = open(__location__, 'r')
    inputLines = inputFile.readlines()
    inputLines = [x.strip('\n') for x in inputLines ]

    return inputLines

class Game:
    def __init__(self, lines) -> None:
        self.winningsNumbers = lines[0].split(',')
        self.boards = []
        self.__curStep = 0
        self.__genBoards(lines[2:])
        self.__winningBoards = []

    def __genBoards(self, lines):
        curBoard = []
        for line in lines:
            if(len(line) == 0):
                self.boards.append(curBoard)
                curBoard = []
            else:
                curBoard.append(line.split())

        self.boards.append(curBoard)
    
    def __doStep(self):
        winningBoard = self.__checkWinAll()

        if winningBoard != False:
            self.__winningBoards.append(winningBoard)
        else:
            return 0
        

    def PlayGame(self):
        self.__curStep = 0

        winningBoardProd = self.__doStep()

        while self.__curStep < len(self.winningsNumbers):
            self.__curStep += 1
            winningBoardProd = self.__doStep()
           # assert(self._curStep < len(self.winningsNumbers))


        return self.__calcPart1Answer(self.__winningBoards[-1])

    # Check all boards for a win in a current step.
    # Returns first board with a win.
    def __checkWinAll(self):
        for board in self.boards:
            win = self.__checkOneBoardForWin(board)
            if win:
                return board

        return False

    def __checkOneBoardForWin(self, board):
        # Horizonal
        matchCount = 0
        for row in board:
            for num in row:
                if num in self.winningsNumbers[:self.__curStep]:
                    matchCount += 1
                    if matchCount == len(row):
                        return True
                else:
                    matchCount = 0
                    break
        # Vertical
        for colPos in range(len(board)):
            for rowPos in range(len(board)):
                if board[rowPos][colPos] in self.winningsNumbers[:self.__curStep]:
                    matchCount += 1
                    if matchCount == len(row):
                        return True
                else:
                    matchCount = 0
                    break
        
        return False

    def __calcPart1Answer(self, board):
        sum = 0
        for row in board:
            for num in row:
                if not num in self.winningsNumbers[:self.__curStep]:
                    sum += int(num)
        
        prod = sum * int(self.winningsNumbers[self.__curStep - 1])

        return prod

def theGoods():

    exinput = readInputFile("exinput.txt")
    exGame = Game(exinput)
    solEx = exGame.PlayGame()

    assert (solEx == 4512)

    
    input = readInputFile("input.txt")
    ILostTheGame = Game(input)
    solPart1 = ILostTheGame.PlayGame()

    print(solPart1)

theGoods()
