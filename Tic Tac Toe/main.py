from error import PlaceError

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def display_board(self):
        for space in self.board:
            print(space)
        
    def get_play(self):
        player_choice = input("Choose line and column (in this order) ").split(" ")
        return int(player_choice[0]) - 1, int(player_choice[1]) - 1
    
    def is_empty(self, line, column):
        return self.board[line][column] == " "
    
    def update_board(self):
        line, column = self.get_play()
        if not self.is_empty(line, column):
            raise PlaceError("This place is already ocuppied")
        else:
            self.board[line][column] = self.player
        self.display_board()
        self.change_player()
    
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

class PlayGame():
    def __init__(self):
        self.game = TicTacToe()
    
    def run_game(self):
        while True:
            self.game.update_board()
            if self.game.check_victory():
                self.game.change_player()
                print(f"Game over {self.game.player} won.") 
                break
            elif self.game.check_draw():
                print("The game was a tie")
                break

def main():
    game = PlayGame()
    game.run_game()

if __name__ == "__main__":
    main()