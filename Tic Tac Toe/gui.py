import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt
from game_engine import TicTacToe
from functools import partial

DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300 ,500, 500)
        self.setWindowTitle("TIC TAC TOE")
        self.engine = TicTacToe()
        self.buttons = []

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        # Creating the parts
        ## Header
        self.header = self.create_header()
        self.main_layout.addLayout(self.header)

        ## Grid
        self.grid = self.create_board()
        self.main_layout.addLayout(self.grid)
        self.main_layout.addSpacing(20)

        ## Footer
        self.footer = self.create_footer()
        self.main_layout.addLayout(self.footer)
        self.main_layout.addStretch()

        self.central_widget.setLayout(self.main_layout)
    
    def create_header(self):
        header_layout = QVBoxLayout()

        self.title_label = QLabel("TIC-TAC-TOE")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("QLabel {font-family: Roboto, sans-serif; font-size: 32px}")
        self.current_player = QLabel(f"Current Player: X")
        self.current_player.setAlignment(Qt.AlignCenter)
        self.current_player.setStyleSheet("QLabel {font-family: Roboto, sans-serif; font-size: 16px; color: rgb(133, 232, 39)}")
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.current_player)

        return header_layout
    
    def create_board(self):
        grid_layout = QGridLayout()
        for r in range(3):
            for c in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setStyleSheet("""QPushButton {border: 2px solid white; border-radius: 15px;} QPushButton:hover {background-color: rgb(80, 80, 80)} QPushButton:pressed {background-color: rgb(85, 85, 85)}""")
                button.clicked.connect(partial(self.run_game, r, c, button))
                self.buttons.append(button)
                grid_layout.addWidget(button, r, c)

        return grid_layout  
    
    def create_footer(self):
        footer_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.reset_button = QPushButton("RESET")
        self.reset_button.setIcon(QIcon(os.path.join(DIR, "Resources/recycle.svg")))
        self.reset_button.setFixedSize(120, 30)
        self.reset_button.setIconSize(QSize(20, 20))
        self.reset_button.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 2px; font-family: Roboto, sans-serif; font-size: 12px; padding: 8px 12px 8px 12px; background-color: rgb(65, 65, 65)} QPushButton:hover {background-color: rgb(80, 80, 80)} QPushButton:pressed {background-color: rgb(85, 85, 85)}")
        self.reset_button.clicked.connect(self.restart_game)
        self.new_game_button = QPushButton("NEW GAME")
        self.new_game_button.setFixedSize(120, 30)
        self.new_game_button.setIconSize(QSize(20, 20))
        self.new_game_button.setStyleSheet("QPushButton {border: 1px solid rgb(133, 232, 39); border-radius: 2px; font-family: Roboto, sans-serif; font-size: 12px; padding: 8px 12px 8px 12px; background-color: rgb(60, 77, 44); color: rgb(133, 232, 39)} QPushButton:hover {background-color: rgb(80, 100, 60)} QPushButton:pressed {background-color: rgb(85, 110, 65)}")
        self.new_game_button.clicked.connect(self.restart_game)

        # Creating the status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("QLabel {font-family: Roboto, sans-serif; font-size: 24px;}")
        self.status_label.setAlignment(Qt.AlignCenter)
        
        button_layout.addStretch()
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.new_game_button)
        button_layout.addStretch()
        footer_layout.addWidget(self.status_label)
        footer_layout.addLayout(button_layout)


        return footer_layout

    def run_game(self, r, c, button):
        self.engine.update_board(r, c, button)
        if self.engine.check_victory():
            self.status_label.setText(f"Player {self.engine.player} WON")
            self.disable_enable_all_buttons("disable")
        elif self.engine.check_draw():
            self.status_label.setText(f"TIE")
            self.disable_enable_all_buttons("disable")
        else:
            self.engine.change_player()
            self.change_player_color()
    
    def disable_enable_all_buttons(self, prompt):
        if prompt == "disable":
            for button in self.buttons:
                button.setEnabled(False)
        elif prompt == "enable":
            for button in self.buttons:
                button.setEnabled(True)
    
    def change_player_color(self):
        if self.engine.player == "X":
            self.current_player.setText(f"<span style='color: rgb(133, 232, 39);'>Current Player: X</span>")
        elif self.engine.player == "O":
            self.current_player.setText(f"<span style='color: #75e3ff;'>Current Player: O</span>")

    def restart_game(self):
        self.engine.board = [[" " for _ in range(3)] for _ in range(3)]
        for button in self.buttons:
            button.setIcon(QIcon())
        self.disable_enable_all_buttons("enable")
        self.status_label.setText("")