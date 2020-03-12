#by keiland Cooper

import boardFunctions as bf
import search as s
import random
import matplotlib.pyplot as plt
import time

class Player:
    def __init__(self, board):
        self.name = input("Enter Name: ")
        self.board = board
        

    def get_player_move(self, m):
        move = int(input("enter 0-6: "))
        return move
        
    def make_move(self,m):
        self.board[0] = bf.makeMove(self.board[0], m, 1)
    
    def get_move(self):
        computerMove = s.minmax(self.board, 5, True, 2)

    def make_computer_move(self, m):
        self.board[0] = bf.makeMove(self.board[0], m, 2)
    
    def __str__(self):
        for i in self.board:
            for j in i:
                print(str(j), end = "")
            print()




def get_player_move(state):
    move = int(input("enter 0-6: "))
    return move
        
def make_move(stateStruct, m, player):
    state = bf.makeMove(stateStruct[0], m, player)
    return [state, stateStruct[1]]

def get_move(stateStruct, player):
    computerMove = s.minmax(stateStruct, 5, True, player)
    return computerMove[1]

def make_computer_move(stateStruct, m, player):
    state = bf.makeMove(stateStruct[0], m, player)
    return [state, stateStruct[1]]

def get_random_player_move(state):
    moveList = bf.generateMoves(state)
    if len(moveList)- 1 == 0:
        print("ENd")
    n = random.randint(0, len(moveList)-1)
    return moveList[n]

def get_ab_move(stateStruct, player):
    a = [float("-inf"), None]
    b = [float("inf"), None]
    computerMove = s.alphabeta_minimax(board,5,a,b,True, player)
    return computerMove[1]

def plotRuns(data, runs, name):
    labels = "randomPlayer", "Computer"
    sizes = [data[0], data[1]]
    explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    title = "Percent win:"+ name +" (" + str(runs) +" runs)"
    plt.title(title)
    plt.show()

def plotTime(lot):
    plt.plot(lot)
    plt.title("time per run: ")
    plt.show()

def compareTimes(timeListNorm, timeListAB):
    c = 0
    for i in timeListNorm:
        c += i
        
    avgTimeNorm = c/len(timeListNorm)

    c = 0
    for i in timeListAB:
        c += i

    avgTimeAB = c/len(timeListAB)

    print("Without Pruning:", avgTimeNorm, ". With AB:", avgTimeAB)
    
    
    
    



board = [[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,2,1,0,0,0],
        [1,2,2,2,2,0,0],
        [1,2,1,2,1,0,1]], None]

board = [[[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]], None]

##print("PlayingGame!")
##while not (bf.lastMoveWon(board[0], 1))[0]:
##    bf.printState(board[0])
##    playerMove = get_player_move(board[0])
##    board = make_move(board, playerMove)
##
##    bf.printState(board[0])
##    botMove = get_move(board)
##    print("botMove", botMove)
##    board = make_computer_move(board, botMove)
    

print("Playing Random Game!")
print("Please wait while the sim runs!")
tally = [0,0]
runs = 0
printResults = False
timeListNorm = []
while runs < 20:
    start = time.time()
    board = [[[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]], None]
    
    while True:
        #bf.printState(board[0])
        playerMove = get_random_player_move(board[0])
        board = make_move(board, playerMove, 1)
        if (bf.lastMoveWon(board[0], 1))[0]:
            if printResults:
                bf.printState(board[0])
                print("Random Player wins!")
            tally[0] += 1
            break
        
        #bf.printState(board[0])
        botMove = get_move(board, 2)
        #print("botMove", botMove)
        board = make_computer_move(board, botMove, 2)
        if (bf.lastMoveWon(board[0], 2))[0]:
            if printResults:
                bf.printState(board[0])
                print("computer wins!")
            tally[1] += 1
            break
    runs += 1
    end = time.time()
    runTime = end - start
    timeListNorm.append(runTime)


plotRuns(tally,runs, "Norm")
plotTime(timeListNorm)



print("Playing Random AB Game!")
print("Please wait while the sim runs!")
tally = [0,0]
runs = 0
printResults = False
timeListAB = []

while runs < 20:
    start = time.time()
    
    board = [[[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]], None]
    
    while True:
        #bf.printState(board[0])
        playerMove = get_random_player_move(board[0])
        board = make_move(board, playerMove, 1)
        if (bf.lastMoveWon(board[0], 1))[0]:
            if printResults:
                bf.printState(board[0])
                print("Random Player wins!")
            tally[0] += 1
            break
        
        #bf.printState(board[0])
        botMove = get_ab_move(board, 2)
        #print("botMove", botMove)
        board = make_computer_move(board, botMove, 2)
        if (bf.lastMoveWon(board[0], 2))[0]:
            if printResults:
                bf.printState(board[0])
                print("computer wins!")
            tally[1] += 1
            break
    runs += 1
    end = time.time()
    runTime = end - start
    timeListAB.append(runTime)
    
plotRuns(tally,runs, "AB")
plotTime(timeListAB)


compareTimes(timeListNorm, timeListAB)


#1. 7.65 vs 3.0467
#2. 7.56 vs 3.88
#3. 7.45 vs 5.54





