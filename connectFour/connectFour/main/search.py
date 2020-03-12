import boardFunctions as bf
import evalFunction as ef
import numpy as np

#where True is max and false is min
def minmax(board,depth,isMax, player):
    
    if depth == 0 or bf.isTerminal(board[0]): 
        hOfx = ef.evalFunction(board[0])
        if not isMax:
            hOfx = hOfx * -1
        #returns a struct of the evaluation and the parent move
        return [hOfx, board[1]] 
    
    if isMax == True:
        maxValS = [float("-inf"), None] #init to worst case
        #makeChildren, will return child structs with the parent move
        #currently assumes player 1 is max
        children = bf.makeChildren(board, player)
        for child in children:
            valS = minmax(child, depth - 1, False, player)
            if maxValS[0] < valS[0]:
                maxValS = valS
        return maxValS            


    elif isMax == False:
        minValS = [float("inf"), None] #init to worst case
        player = bf.switchPlayer(player)
        children = bf.makeChildren(board, player)
        player = bf.switchPlayer(player)
        for child in children:
            valS = minmax(child, depth - 1, True, player)
            if minValS[0] > valS[0]:
                minValS = valS
        return minValS        


#Where alpha and beta are structs: [value, move]
def alphabeta_minimax(board,depth,a,b,isMax, player):
    if depth == 0 or bf.isTerminal(board[0]): #TD: or is terminal?
        hOfx = ef.evalFunction(board[0])
        if not isMax:
            hOfx = hOfx * -1
        #returns a struct of the evaluation and the parent move
        return [hOfx, board[1]] #TD: adjust for player (* -1?)

    if isMax == True:
        maxValS = [float("-inf"), None]
        children = bf.makeChildren(board, player)
        #print("len child", len(children))
        for child in children:
            #print(child[1])
            valS = alphabeta_minimax(child, depth - 1, a, b, False, player)
            
            if maxValS[0] < valS[0]:
                maxValS = valS
            if a[0] < valS[0]:
                a = valS
            #prune
            if a[0] >= b[0]:
                #print("Prune")
                break
        return a

    if isMax == False:
        minValS = [float("inf"), None]
        player = bf.switchPlayer(player)
        children = bf.makeChildren(board, player)
        player = bf.switchPlayer(player)
        for child in children:
            #print(child[1])
            valS = alphabeta_minimax(child, depth - 1, a, b, False, player)
            
            if minValS[0] > valS[0]:
                minValS = valS
            if b[0] > valS[0]:
                b = valS
            #prune
            if a[0] >= b[0]:
                break
        return b



# code for testing

##board = [[[0,0,0,0,0,0,0],
##          [0,0,0,0,0,0,0],
##          [0,0,0,0,0,0,0],
##          [1,1,0,0,0,0,0],
##          [2,1,1,0,2,0,2],
##          [2,1,1,0,2,0,1]], None]
##
##mm = minmax(board,5,True,1)
##a = [float("-inf"), None]
##b = [float("inf"), None]
##mm = alphabeta_minimax(board,5,a,b,True, 1)
##print(mm)
####mvs = bf.generateMoves(board[0])
##bf.printState(board[0])
##boardd = bf.makeMove(board[0], 2, 2)
##children = bf.makeChildren(board, 1)
##for c in children:
##    bf.printState(c[0])
##    print("pMove", c[1])


