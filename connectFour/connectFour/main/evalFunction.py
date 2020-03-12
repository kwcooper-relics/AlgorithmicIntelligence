#import board

# this accepts a 7x6 2D array representation of the board and returns an integer evaluation of the board
def evalFunction(board): # with Black as max.  If you want to switch max and min, multiply this value by -1
    seen = []  # List of board positions that have already contributed to the current eval
    eval = 0
    # Vertical cumulative score
    for row in range(5):
        for col in range(7):
            if (row,col) not in seen:
                color = board[row][col]
                if color == 1:
                    if board[row+1][col] != 1:
                        eval += 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval += 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col))
                        if row <= 3 and board[row+2][col] == 1:
                            eval += 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col))
                            if row <= 2 and board[row+3][col] == 1:
                                eval += 10000 # Found goal state
                                return eval
                elif color == 2:
                    if board[row+1][col] != 2:
                        eval -= 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval -= 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col))
                        if row <= 3 and board[row+2][col] == 2:
                            eval -= 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col))
                            if row <= 2 and board[row+3][col] == 2:
                                eval -= 10000 # Found goal state
                                return eval
              
    # Horizontal cumulative score
    seen.clear()
    for row in range(6):
        for col in range(6):
            if (row,col) not in seen:
                color = board[row][col]
                if color == 1:
                    if board[row][col+1] != 1:
                        eval += 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval += 1 # 2 in a row adds a value of 1
                        seen.append((row,col+1))
                        if col <= 4 and board[row][col+2] == 1:
                            eval += 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row,col+2))
                            if col <= 3 and board[row][col+3] == 1:
                                eval += 10000 # Found goal state
                                return eval
                elif color == 2:
                    if board[row][col+1] != 2:
                        eval -= 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval -= 1 # 2 in a row adds a value of 1
                        seen.append((row,col+1))
                        if col <= 4 and board[row][col+2] == 2:
                            eval -= 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row,col+2))
                            if col <= 3 and board[row][col+3] == 2:
                                eval -= 10000 # Found goal state
                                return eval
                            
    # Diagonal cumulative score (positive slope)
    seen.clear()
    for row in range(5):
        for col in range(1,7):
            if (row, col) not in seen:
                color = board[row][col]
                if color == 1:
                    if board[row+1][col-1] != 1:
                        eval += 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval += 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col-1))
                        if (row <= 3 and col >= 2) and board[row+2][col-2] == 1:
                            eval += 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col-2))
                            if (row <= 2 and col >= 3) and board[row+3][col-3] == 1:
                                eval += 10000 # Found goal state
                                return eval
                elif color == 2:
                    if board[row+1][col-1] != 2:
                        eval -= 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval -= 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col-1))
                        if (row <= 3 and col >= 2) and board[row+2][col-2] == 2:
                            eval -= 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col-2))
                            if (row <= 2 and col >= 3) and board[row+3][col-3] == 2:
                                eval -= 10000 # Found goal state
                                return eval
    # Diagonal cumulative score (negative slope)
    seen.clear()
    for row in range(5):
        for col in range(6):
            if (row, col) not in seen:
                color = board[row][col]
                if color == 1:
                    if board[row+1][col+1] != 1:
                        eval += 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval += 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col+1))
                        if (row <= 3 and col <= 4) and board[row+2][col+2] == 1:
                            eval += 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col+2))
                            if (row <= 2 and col <= 3) and board[row+3][col+3] == 1:
                                eval += 10000 # Found goal state
                                return eval
                elif color == 2:
                    if board[row+1][col+1] != 2:
                        eval -= 0 # 1 token alone adds nothing to the value of the board
                    else:
                        eval -= 1 # 2 in a row adds a value of 1
                        seen.append((row+1,col+1))
                        if (row <= 3 and col <= 4) and board[row+2][col+2] == 2:
                            eval -= 3 # 3 in a row adds a total value of 4 to the board state
                            seen.append((row+2,col+2))
                            if (row <= 2 and col <= 3) and board[row+3][col+3] == 2:
                                eval -= 10000 # Found goal state
                                return eval 
    return eval


