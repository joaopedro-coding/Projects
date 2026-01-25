import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtCore import Qt

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Morse Code Translator")
        self.setWindowIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/morse-icon.png")))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()

        header = self.create_header()
        morse_input = self.create_input()

        self.main_layout.addLayout(header)
        self.main_layout.addLayout(morse_input)
        self.main_layout.addStretch()
        self.central_widget.setLayout(self.main_layout)

    
    def create_header(self):
        header_layout = QHBoxLayout()

        self.logo_icon = QLabel()
        pixmap = QPixmap(os.path.join(SCRIPT_DIR, "Resources/circle-white.svg"))
        self.logo_icon.setPixmap(pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.title_label = QLabel("Morse Code Translator")

        header_layout.addWidget(self.logo_icon)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        return header_layout

    def create_input(self):
        input_layout = QVBoxLayout()

        self.input_label = QLabel("INPUT TEXT")
        self.input_box = QTextEdit(placeholderText="Type your message here...")
        self.input_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.input_box.setMaximumHeight(80)

        self.result_label = QLabel("MORSE CODE RESULT")
        self.result_box = QTextEdit(placeholderText="Here are your results...")
        self.result_box.setReadOnly(True)
        self.result_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.result_box.setMaximumHeight(80)

        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.result_label)
        input_layout.addWidget(self.result_box)

        return input_layout


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/morse-icon.png")))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()