
import board
import boardFunctions as bf
import search as s


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






