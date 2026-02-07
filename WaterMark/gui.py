from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from drag_drop import QDragnDrop
import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.setWindowTitle("Watermark Inserter")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # set window background color
        self.central_widget.setStyleSheet("background-color: #F4F7F9;")
        self.main_layout = QVBoxLayout()

        self.header = self.create_header()
        self.body = self.create_body()

        self.main_layout.addLayout(self.header)
        self.main_layout.addLayout(self.body)
        self.main_layout.addStretch()

        self.central_widget.setLayout(self.main_layout)
    
    def create_header(self):
        header_layout = QHBoxLayout()

        self.logo_icon = QLabel()
        water_droplet = QPixmap(os.path.join(DIR, "Resources/droplet.svg"))
        self.logo_icon.setPixmap(water_droplet.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.title_label = QLabel("WATERMARK PRO")

        header_layout.addWidget(self.logo_icon)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        return header_layout
    
    def create_body(self):
        body_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        drag_drop = QDragnDrop()
        cloud_icon = QIcon(os.path.join(DIR, "Resources/cloud.svg"))
        body_layout.addWidget(drag_drop)
        return body_layout

        

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
