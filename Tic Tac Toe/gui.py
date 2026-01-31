import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from game_engine import TicTacToe

DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300 ,500, 500)
        self.setWindowTitle("TIC TAC TOE")
        self.engine = TicTacToe()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()

        # Creating the parts
        ## Header
        self.header = self.create_header()
        self.main_layout.addLayout(self.header)

        ## Grid
        self.grid = self.create_board()
        self.main_layout.addLayout(self.grid)

        ## Footer
        self.footer = self.create_footer()
        self.main_layout.addLayout(self.footer)
        self.main_layout.addStretch()

        self.central_widget.setLayout(self.main_layout)
    
    def create_header(self):
        header_layout = QVBoxLayout()

        self.title_label = QLabel("TIC-TAC-TOE")
        self.current_player = QLabel(f"Current Player: {self.engine.player}")
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.current_player)

        return header_layout
    
    def create_board(self):
        grid_layout = QGridLayout()
        for r in range(3):
            for c in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                grid_layout.addWidget(button, r, c)

        return grid_layout  
    
    def create_footer(self):
        footer_layout = QHBoxLayout()

        self.reset_button = QPushButton("Reset")
        self.reset_button.setIcon(QIcon(os.path.join(DIR, "Resources/recycle.svg")))
        self.new_game_button = QPushButton("New Game")

        footer_layout.addStretch()
        footer_layout.addWidget(self.reset_button)
        footer_layout.addWidget(self.new_game_button)
        footer_layout.addStretch()

        return footer_layout

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()