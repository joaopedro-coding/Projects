import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from PySide6.QtGui import QIcon, QColor
from interface import Ui_MainWindow

class WatermarkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Watermark App")
        self.setWindowIcon(QIcon(":/Resources/droplet.svg"))
        self.selected_color = QColor(255, 255, 255)

        # Configuring the widgets
        self.ui.drop_area.file_dropped.connect(self.process_image)
        self.ui.drop_area.error.connect(self.show_error)
        self.ui.btn_browse.clicked.connect(self.open_explorer)
        self.ui.text_watermark_button.click()
        self.ui.text_watermark_button.toggled.connect(self.check_radio)
        self.check_radio()
        self.ui.generate_btn.clicked.connect(self.add_watermark)
        self.ui.slider_size_value.setText("10")
        self.ui.slider_size.valueChanged.connect(self._slider_size_value_)
        self.ui.slider_opacity_value.setText("10")
        self.ui.slider_opacity.valueChanged.connect(self._slider_opacity_value_)
        self.ui.color_box.clicked.connect(self.choose_color)
    
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
    
    def _slider_size_value_(self, value):
        self.ui.slider_size_value.setText(f"{value}")
    
    def _slider_opacity_value_(self, value):
        self.ui.slider_opacity_value.setText(f"{value}")
    
    def choose_color(self):
        color = QColorDialog.getColor(self.selected_color, self, "Choose a font color")
        if color:
            self.selected_color = color
            self.ui.color_box.setStyleSheet(f"background-color: {color.name()}; border-radius: 5px;")

    def _get_pos_(self):
        position_buttons = {
            "top_left": self.ui.pos_top_left,
            "top_center": self.ui.pos_top_mid,
            "top_right": self.ui.pos_top_right,
            "middle_left": self.ui.pos_mid_left,
            "center": self.ui.pos_mid,
            "middle_right": self.ui.pos_mid_right,
            "bottom_left": self.ui.pos_bottom_left,
            "bottom_center": self.ui.pos_bottom_mid,
            "bottom_right": self.ui.pos_bottom_right,
        }
        for name, btn in position_buttons.items():
            if btn.isChecked():
                return name

    def add_watermark(self):
        font = self.ui.font_box.font().family()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WatermarkApp()
    window.show()
    sys.exit(app.exec())