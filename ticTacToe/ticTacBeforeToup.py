from copy import deepcopy

def makeMoves(state, move, player):
    state[move[0]][move[1]] = player
    return state

def availableMoves(state):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                moves.append([i,j])
    return moves

def makeChildren(state, player):
    moveList = availableMoves(state)
    children = []
    for move in moveList:
        child = deepcopy(state)
        child[move[0]][move[1]] = player
        children.append(child)
    return children
        
    

#possibly scaleable checking function...
#(the diagionals would need work)
def isWinner(state, player):
    count = 0
    #check row
    for row in range(len(state)):
        for column in range(len(state[0])):
            if state[row][column] == player:
                count += 1
        if count == 3:
            return True
        else:
            count = 0

    #check col
    count = 0
    for row in range(len(state)):
        for column in range(len(state[0])):
            if state[column][row] == player:
                count += 1
        if count == 3:
            return True
        else:
            count = 0

    #check front diag
    count = 0
    for row in range(len(state)):
        if state[row][row] == player:
            count += 1
            
    if count == 3:
        return True
    else:
        count = 0

    #check back diag
    count = 0
    for row in range(len(state)):
        if state[(len(state) - 1 - row)][row] == player:
            count += 1
            
    if count == 3:
        return True
    else:
        count = 0
        
    return False

def countSquares(state, player):
    count = 0
    for row in range(len(state)):
        for column in range(len(state[0])):
            if state[row][column] == player:
                count += 1
    return count 

def isDraw(state, win):
    count = 0
    for row in range(len(state)):
        for column in range(len(state[0])):
            if state[row][column] == 1 or state[row][column] == 2:
                count += 1
    if count == 8 and not win:
        return True
    return False
            
#may be able to take the winner check code and modify it
def evaluation(state, player):
    return countSquares(state, player)


def minimax(state, depth, player):
    #print("depth:", depth)
    if depth == 0: #TD: or is terminal
        return evaluation(state, player)
    else:
        if player == 1:
            bestVal = float("-inf")
            children = makeChildren(state, 1)
            for child in children:
                val = minimax(child, depth-1, 2)
                bestVal = max(bestVal, val)
            return bestVal

        elif player == 2:
            bestVal = float("inf")
            children = makeChildren(state, 2)
            for child in children:
                val = minimax(child, depth-1, 1)
                bestVal = min(bestVal, val)
            return bestVal

board = [[0,0,0], [0,0,0], [0,0,0]]
#board = [[0,0,2], [0,2,0], [2,0,0]]
board = [[2,1,0], [0,2,0], [1,0,0]]


print(board)
print(availableMoves(board))
#makeMoves(board, [0,0], 1)

print(isWinner(board, 2))

val = minimax(board, 5, 1)

print(val)
