from PySide6.QtWidgets import QLabel, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
import os

class QDragnDrop(QLabel):
    def __init__(self):
        super().__init__()
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources/cloud.svg")
        self.setText(f"<img src='{icon_path}' width='50' height='50'><br><br>Drag & Drop Here")
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #95A5A6;
                border-radius: 10px;
                background-color: rgb(214, 228, 237);
                color: #34495E;
            }
        """)
    
    def mousePressEvent(self, event):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.process_file(file_path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            self.process_file(files[0])
    
    def process_file(self, path):
        print(f"Arquivo recebido: {path}")
        self.setText(f"Selected: {path.split('/')[-1]}")