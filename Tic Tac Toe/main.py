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
    
def main():
    game = TicTacToe()
    game.update_board()
    game.display_board()
    game.update_board()

if __name__ == "__main__":
    main()