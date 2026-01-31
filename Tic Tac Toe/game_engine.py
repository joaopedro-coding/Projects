from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import os

DIR = os.path.dirname(os.path.abspath(__file__))

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def is_empty(self, line, column):
        return self.board[line][column] == " "
    
    def update_board(self, row, column, button):
        button.setIcon(QIcon(os.path.join(DIR, f"Resources/{self.player}.svg")))
        button.setIconSize(QSize(70, 70))
        button.setEnabled(False)
        self.board[row][column] = self.player
    
    def check_victory(self):
        for i in range(3):
            # Checking horizontal and vertical lines
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
 
        # Checking diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        
        return False
    
    def change_player(self):
        self.player = "X" if self.player == "O" else "O"
    
    def check_draw(self):
        return all(space != " " for row in self.board for space in row)