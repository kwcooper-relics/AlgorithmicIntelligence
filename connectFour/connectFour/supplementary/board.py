#import search
import numpy as np
import evalFunction as ef

class Board:
    def __init__(self, board, aP):

        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]

##        self.board = [[0,0,0,0,0,0,0],
##                      [0,0,1,0,0,0,0],
##                      [0,0,1,1,2,0,0],
##                      [0,0,1,1,1,2,2],
##                      [0,0,0,2,2,1,1],
##                      [0,0,2,1,2,2,2]]

##        self.board = [[0,0,0,0,0,0,0],
##                      [0,0,0,0,0,2,0],
##                      [0,0,0,0,2,2,0],
##                      [0,0,1,2,2,1,0],
##                      [0,0,2,2,1,2,0],
##                      [0,0,1,1,2,1,0]]


        self.board = board
        self.activePlayer = aP #1 or 2
        self.moveList = []
        self.madeMoves = []

    def switchPlayer(self):
        if self.activePlayer == 2:
                self.activePlayer = 1
        elif self.activePlayer == 1:
            self.activePlayer = 2
            
    #a random list of possible moves (1-6)
    def generateRandMoves(self, n):
        self.moveList = np.random.randint(0,6,n)

    def generateMoves(self, board):
        moveList = []
        for ii in range(len(board[0])):
            if board[0][ii] == 0:
                moveList.append(ii)
        #self.moveList = moveList
        return moveList
            
    def make_move(self, m, prnt=False):
        mVs = []
        for i in list(reversed(range(6))): #the len of the rows
            #could add handeling for out of index handeling
            if self.board[i][m] == 0:
                self.board[i][m] = self.activePlayer
                self.madeMoves.append(m)
                break
            else:
                mVs.append(self.board[i][m])
        
        if len(mVs) == 6:
            print("Col is full!")
            print()
        if prnt:
            self.printBoard()
        #self.switchPlayer()
                  
    def unmake_last_move(self, prnt=False):
        mVs = []
        if len(self.madeMoves) > 0:
            m = self.madeMoves.pop()
        
            for i in list(range(6)): #the len of the rows
                #could add handeling for out of index handeling
                if self.board[i][m] == 1 or self.board[i][m] == 2:
                    self.board[i][m] = 0
                    break
                else:
                    mVs.append(self.board[i][m])
            if len(mVs) == 6:
                print("No tile found!")
                print()
            if prnt:
                self.printBoard()
            #self.switchPlayer()
        else:
            print("No move to take back!")

    #Helper function for the lastMoveWon function
    def checkAdjacent(self, row, column, deltaROW, deltaCOL):
            count = 0
            indsList = []
            for i in range(4):
                    current = self.board[row][column]
                    if current == self.activePlayer:
                            indsList.append([row, column])
                            count += 1
                    row += deltaROW
                    column += deltaCOL
            return count, indsList

    def isTerminal(self):
        pass

    def showWinner(self, il):
        b = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

        #could make the star the winners number
        for i in range(len(il)):
            b[il[i][0]][il[i][1]] = "*"

        r = " "
        for row in b:
            for l in row:
                if l == 0:
                    l = "."
                r = r + " " + str(l)
                #print(str(l), end = " ")
            print(r)
            r = " "
                          
    def last_move_won(self):
        cnt = 0
        for row in range(len(self.board) - 3):
            for column in range(len(self.board[0])):
               cnt,iL = self.checkAdjacent(row, column, 1, 0)
               if cnt == 4:
                    print("Vertical Win!")
                    self.showWinner(iL)
                    return True,iL
        for row in range(len(self.board)):
                for column in range(len(self.board[0]) - 3):
                        cnt,iL = self.checkAdjacent(row, column, 0, 1)
                        if cnt == 4:
                            print("Horizontal Win!")
                            self.showWinner(iL)
                            return True,iL
        for row in range(len(self.board)-3):
                for column in range(len(self.board[0]) - 3):
                        cnt,iL = self.checkAdjacent(row, column, 1, 1)
                        if cnt == 4:
                            print("Forward Slash Win!")
                            self.showWinner(iL)
                            return True,iL
        for row in range(3, len(self.board)):
                for column in range(len(self.board[0]) - 3):
                        cnt,iL = self.checkAdjacent(row, column, -1, 1)
                        if cnt == 4:
                            print("Backslash Win!")
                            self.showWinner(iL)
                            return True,iL
        return False, iL

    def makeRandBoard(self, moves):
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        
        self.generateRandMoves(moves)
        for m in self.moveList:
            self.make_move(m)
            self.switchPlayer()

    def getBoard(self):
        return self.board
    
    def printBoard(self):
        r = " "
        for row in self.board:
            for l in row:
                r = r + " " + str(l)
                #print(str(l), end = " ")
            print(r)
            r = " "
    
    def __str__(self):
        return str(np.matrix(self.board))

board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0],
         [0,1,0,2,0,0,0],
         [0,1,0,2,2,0,0],
         [1,1,1,2,1,0,0]]

##b = Board(board, 2)
##print()
##b.printBoard()
##print()
###b.generateRandMoves(5)
###print(b.moveList)
###w,il = b.last_move_won()
###print("il:", il)
##
###b.makeRandBoard(20)
##b.printBoard()
##print()
##print("eval:", ef.evalFunction(b.board))
##
##b.generate_moves()
##print(b.moveList)
##
##brd = b.getBoard()
##print(brd)
