import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from game_engine import TicTacToe

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
        self.header = self.create_header()
        self.main_layout.addLayout(self.header)


        self.central_widget.setLayout(self.main_layout)
    
    def create_header(self):
        header_layout = QVBoxLayout()

        self.title_label = QLabel("TIC-TAC-TOE")
        self.current_player = QLabel(f"Current Player: {self.engine.player}")
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.current_player)
        header_layout.addStretch()   

        return header_layout

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()