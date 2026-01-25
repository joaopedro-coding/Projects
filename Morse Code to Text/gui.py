import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy, QPushButton
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
        morse_input = self.create_input_box()
        morse_result = self.create_result_box()
        mode_selector = self.create_mode_selector()
        footer = self.create_footer()

        self.main_layout.addLayout(header)
        self.main_layout.addLayout(morse_input)
        self.main_layout.addLayout(mode_selector)
        self.main_layout.addLayout(morse_result)
        self.main_layout.addLayout(footer)
        self.adjustSize()
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

    def create_mode_selector(self):
        mode_layout = QHBoxLayout()

        self.text_to_morse_button = QPushButton("TEXT - MORSE")
        self.text_to_morse_button.setIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/arrow-white.svg")))
        self.text_to_morse_button.setLayoutDirection(Qt.RightToLeft)

        self.morse_to_text_button = QPushButton("MORSE - TEXT")
        self.morse_to_text_button.setIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/arrow-up-white.svg")))
        self.morse_to_text_button.setLayoutDirection(Qt.RightToLeft)


        mode_layout.addStretch()
        mode_layout.addWidget(self.text_to_morse_button)
        mode_layout.addSpacing(20)
        mode_layout.addWidget(self.morse_to_text_button)
        mode_layout.addStretch()

        return mode_layout        

    def create_input_box(self):
        input_layout = QVBoxLayout()

        self.input_label = QLabel("INPUT TEXT")
        self.input_box = QTextEdit(placeholderText="Type your message here...")
        self.input_box.setReadOnly(False)
        self.input_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.input_box.setFixedHeight(80)

        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_box)

        return input_layout
    
    def create_result_box(self):
        result_layout = QVBoxLayout()

        self.result_label = QLabel("MORSE CODE RESULT")
        self.result_box = QTextEdit(placeholderText="Here are your results...")
        self.result_box.setReadOnly(True)
        self.result_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.result_box.setFixedHeight(80)

        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_box)

        return result_layout

    def create_footer(self):
        footer_layout = QHBoxLayout()

        self.play_button = QPushButton("Play")
        self.play_button.setIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/play-white.svg")))

        self.copy_button = QPushButton("Copy")
        self.copy_button.setIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/copy-white.svg")))

        self.clear_button = QPushButton("Clear")
        self.clear_button.setIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/clear.svg")))

        footer_layout.addStretch()
        footer_layout.addWidget(self.play_button)
        footer_layout.addSpacing(20)
        footer_layout.addWidget(self.copy_button)
        footer_layout.addSpacing(20)
        footer_layout.addWidget(self.clear_button)
        footer_layout.addStretch()
        
        return footer_layout

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/morse-icon.png")))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()