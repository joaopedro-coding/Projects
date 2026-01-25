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

        text_to_morse_layout = QHBoxLayout()
        self.text_to_morse = QPushButton("TEXT - MORSE")
        self.arrow_down = QLabel()
        arrow_down_image = QPixmap(os.path.join(SCRIPT_DIR, "Resources/arrow-white.svg"))
        self.arrow_down.setPixmap(arrow_down_image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        text_to_morse_layout.addWidget(self.text_to_morse)
        text_to_morse_layout.addWidget(self.arrow_down)

        morse_to_text_layout = QHBoxLayout()
        self.morse_to_text = QPushButton("MORSE - TEXT")
        self.arrow_up = QLabel()
        arrow_up_image = QPixmap(os.path.join(SCRIPT_DIR, "Resources/arrow-up-white.svg"))
        self.arrow_up.setPixmap(arrow_up_image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        morse_to_text_layout.addWidget(self.morse_to_text)
        morse_to_text_layout.addWidget(self.arrow_up)

        mode_layout.addStretch()
        mode_layout.addLayout(text_to_morse_layout)
        mode_layout.addSpacing(20)
        mode_layout.addLayout(morse_to_text_layout)
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

        play_layout = QHBoxLayout()
        self.play_button = QPushButton("Play")
        self.play = QLabel()
        play_image = QPixmap(os.path.join(SCRIPT_DIR, "Resources/play-white.svg"))
        self.play.setPixmap(play_image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        play_layout.addWidget(self.play)
        play_layout.addWidget(self.play_button)

        copy_layout = QHBoxLayout()
        self.copy_button = QPushButton("Copy")
        self.copy = QLabel()
        copy_image = QPixmap(os.path.join(SCRIPT_DIR, "Resources/copy-white.svg"))
        self.copy.setPixmap(copy_image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        copy_layout.addWidget(self.copy)
        copy_layout.addWidget(self.copy_button)

        clear_layout = QHBoxLayout()
        self.clear_button = QPushButton("Clear")
        self.clear = QLabel()
        clear_image = QPixmap(os.path.join(SCRIPT_DIR, "Resources/clear.svg"))
        self.clear.setPixmap(clear_image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        clear_layout.addWidget(self.clear)
        clear_layout.addWidget(self.clear_button)

        footer_layout.addStretch()
        footer_layout.addLayout(play_layout)
        footer_layout.addSpacing(20)
        footer_layout.addLayout(copy_layout)
        footer_layout.addSpacing(20)
        footer_layout.addLayout(clear_layout)
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