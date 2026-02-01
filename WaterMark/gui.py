from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.setWindowTitle("Watermark Inserter")

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
