from PySide6.QtWidgets import QFrame, QPushButton, QLabel, QSlider, QFontComboBox, QRadioButton
from PySide6.QtCore import Signal
import os

class drop_area(QFrame):
    file_dropped = Signal(str)
    error = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if os.path.isfile(file_path):
                extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
                
                if file_path.lower().endswith(extensions):
                    self.file_dropped.emit(file_path)
                else:
                    self.error.emit("Not an image")
            else:
                self.error.emit("Place only image files")

class btn_browse(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

class filename_label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

class pos_button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

class color_box(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

class slider(QSlider):
    def __init__(self, parent=None):
        super().__init__(parent)

class font_box(QFontComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

class text_watermark_radio(QRadioButton):
    def __init__(self, parent=None):
        super().__init__(parent)

class generate_btn(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

class slider_opacity_value(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

class slider_size_value(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)