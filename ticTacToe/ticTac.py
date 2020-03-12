board = [[0,0,0], [0,0,0], [0,0,0]]

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
                

def isWinner(state):
    for i in range(len(state)):
        

def evaluation(state):
    pass

def makeChilden(state):
    pass

def minimax(state, depth, player):
    if depth == 0: #TD: or is terminal
        return evaluation(state)

    if player == 1:
        bestVal = float("-inf")
        children = makeChildren(state)
        for child in children:
            val = minimax(child, depth-1, 2)
            bestVal = max(bestVal, val)
    return bestVal

    elif player == 2:
        bestVal = float("inf")
        children = makeChildren(state)
        for child in children:
            val = minimax(child, depth-1, 1)
            bestVal = min(bestVal, val)
    return bestVal


print(availableMoves(board))
makeMoves(board, [0,0], 1)

