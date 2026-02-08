from PySide6.QtWidgets import QFrame, QPushButton, QLabel, QSlider, QFontComboBox, QRadioButton

class drop_area(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

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