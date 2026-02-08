import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from interface import Ui_MainWindow

class WatermarkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Watermark App")
        self.setWindowIcon(QIcon(":/Resources/droplet.svg"))

        # Configuring the widgets
        self.ui.drop_area.file_dropped.connect(self.process_image)
        self.ui.drop_area.error.connect(self.show_error)
        self.ui.btn_browse.clicked.connect(self.open_explorer)
        self.ui.text_watermark_button.toggled.connect(self.check_radio)
        self.check_radio()
    
    def process_image(self, path):
        name = os.path.basename(path)
        self.ui.filename_label.setStyleSheet("color: black;")
        self.ui.filename_label.setText(f"Filename: {name}")
    
    def show_error(self, error_msg):
        self.ui.filename_label.setStyleSheet("color: #FF5555;")
        self.ui.filename_label.setText(error_msg)
    
    def open_explorer(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)"
        )
        if file_path:
            self.process_image(file_path)
    
    def check_radio(self):
        is_text_mode = self.ui.text_watermark_button.isChecked()
        
        self.ui.font_box.setEnabled(is_text_mode)
        self.ui.slider_size.setEnabled(is_text_mode)
        self.ui.slider_opacity.setEnabled(is_text_mode)
        self.ui.color_box.setEnabled(is_text_mode)
        self.ui.position_box.setEnabled(is_text_mode)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WatermarkApp()
    window.show()
    sys.exit(app.exec())