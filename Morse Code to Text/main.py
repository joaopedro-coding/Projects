from converter import Converter
from morse_code_exception import MorseTranslationError
from gui import MainWindow
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
convert = Converter()
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(SCRIPT_DIR, "Resources/morse-icon.png")))
window = MainWindow()
window.show()
sys.exit(app.exec())

