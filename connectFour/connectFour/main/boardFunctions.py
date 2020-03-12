from copy import deepcopy


def printState(state):
    print()
    r = " "
    for row in state:
        for l in row:
            r = r + " " + str(l)
            #print(str(l), end = " ")
        print(r)
        r = " "


def generateMoves(state):
    moveList = []
    for ii in range(len(state[0])):
        if state[0][ii] == 0:
            moveList.append(ii)
    return moveList



def makeMove(state, m, player):
    mVs = []
    for i in list(reversed(range(6))): #the len of the rows
        #could add handeling for out of index handeling
        if state[i][m] == 0:
            state[i][m] = player
            break
##        else:
##            print("Didnt make move")
##            print(state, "move", m, "State", state[i][m])
    
    if len(mVs) == 6:
        print("Col is full!")
        print()

    return state


def makeChildren(stateStruct, player):
    state = stateStruct[0]
    parentMove = stateStruct[1]
    moveList = generateMoves(state)
    children = []
    for move in moveList:
        child = deepcopy(state)
        child = makeMove(child, move, player)
        if parentMove == None:
            child = [child, move]
        else:
            child = [child, parentMove]
        
        children.append(child)
    return children
        
        
def isTerminal(state):
    for ii in range(len(state[0])):
        if state[0][ii] == 0:
            return False
    return True

def switchPlayer(player):
        if player == 2:
            return 1
        elif player == 1:
            return 2

#Helper function for the lastMoveWon function
def checkAdjacent(state, row, column, deltaROW, deltaCOL, player):
        count = 0
        indsList = []
        for i in range(4):
                current = state[row][column]
                if current == player:
                        indsList.append([row, column])
                        count += 1
                row += deltaROW
                column += deltaCOL
        return count, indsList


def lastMoveWon(state, player):
        cnt = 0
        for row in range(len(state) - 3):
            for column in range(len(state[0])):
               cnt,iL = checkAdjacent(state, row, column, 1, 0, player)
               if cnt == 4:
                    #print("Vertical Win!")
                    #showWinner(iL)
                    return True,iL
        for row in range(len(state)):
                for column in range(len(state[0]) - 3):
                        cnt,iL = checkAdjacent(state, row, column, 0, 1, player)
                        if cnt == 4:
                            #print("Horizontal Win!")
                            #showWinner(iL)
                            return True,iL
        for row in range(len(state)-3):
                for column in range(len(state[0]) - 3):
                        cnt,iL = checkAdjacent(state, row, column, 1, 1, player)
                        if cnt == 4:
                            #print("Forward Slash Win!")
                            #showWinner(iL)
                            return True,iL
        for row in range(3, len(state)):
                for column in range(len(state[0]) - 3):
                        cnt,iL = checkAdjacent(state, row, column, -1, 1, player)
                        if cnt == 4:
                            #print("Backslash Win!")
                            #showWinner(iL)
                            return True,iL
        return False, iL

#Takes a state, and checks if its children have a win
#next move win?
def isForcedWin(state, player):
    
    children = bf.makeChildren(state, player)
    for child in children:
        if lastMoveWon(child, player)[0] == True:
            return True
    return False
            
