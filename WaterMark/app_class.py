import sys
import os
from PySide6.QtWidgets import QMainWindow, QFileDialog, QColorDialog
from PySide6.QtGui import QIcon, QColor
from interface import Ui_MainWindow
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager

class WatermarkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Watermark App")
        self.setWindowIcon(QIcon(":/Resources/droplet.svg"))
        self.selected_color = QColor(255, 255, 255)
        self.file_location = ""

        # Configuring the widgets
        self.ui.drop_area.file_dropped.connect(self.process_image)
        self.ui.drop_area.error.connect(self.show_error)
        self.ui.btn_browse.clicked.connect(self.open_explorer)
        self.ui.text_watermark_button.click()
        self.ui.text_watermark_button.toggled.connect(self.check_radio)
        self.check_radio()
        self.ui.slider_size_value.setText("10")
        self.ui.slider_size.valueChanged.connect(self._slider_size_value_)
        self.ui.slider_opacity_value.setText("10")
        self.ui.slider_opacity.valueChanged.connect(self._slider_opacity_value_)
        self.ui.color_box.clicked.connect(self.choose_color)
        self.ui.pos_top_left.click()
        self.ui.generate_btn.clicked.connect(self.add_watermark)
        self.ui.filename_label.setText("Filename")
    
    def process_image(self, path):
        name = os.path.basename(path)
        self.ui.filename_label.setStyleSheet("color: black;")
        self.ui.filename_label.setText(f"Filename: {name}")
        self.file_location = path
    
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
        if color.isValid():
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

    def get_font(self):
        font_name = self.ui.font_box.currentFont().family()
        font_path = font_manager.findfont(font_manager.FontProperties(family=font_name))
        return font_path

    def _calculate_position_(self, text_bbox, base_image):
        w_text, h_text = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        w_img, h_img = base_image.size
        margin = 20
        pos_key = self._get_pos_()
        x = y = margin

        # Calculating x
        if "left" in pos_key:
            x = margin
        elif "right" in pos_key:
            x = w_img - w_text - margin
        else:
            x = (w_img - w_text) // 2
        
        # Calculating y
        if "top" in pos_key:
            y = margin
        elif "bottom" in pos_key:
            y = h_img - h_text - margin
        else:
            y = (h_img - h_text) // 2
        
        return x, y
    
    def _save_image_(self, output_img):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Watermarked Image", os.path.join(os.path.dirname(self.file_location), "watermarked_image.png"), "PNG Image (*.png);;JPEG Image (*.jpg);;All Files (*.*)")

        if save_path:
            if save_path.lower().endswith((".jpg", ".jpeg")):
                final_img = output_img.convert("RGB")
                final_img.save(save_path, "JPEG", quality=100)
            else:
                output_img.save(save_path, "PNG")
        else:
            return

        output_img.show()
        self.ui.filename_label.setStyleSheet("color: green")
        self.ui.filename_label.setText("Image Saved Succesfully!")
        self.file_location = ""

    def add_watermark(self):
        img_path = self.file_location
        font_size = self.ui.slider_size.value()

        # Convert opacity value into percentage and into the pillow scale
        opacity_value = int((int(self.ui.slider_opacity.value()) / 100) * 255)

        # Color divided into RGBA
        color_rgb = (self.selected_color.red(), self.selected_color.green(), self.selected_color.blue(), opacity_value)
        
        if not img_path:
            self.show_error("No image selected")
            return
        else:
            with Image.open(img_path).convert("RGBA") as base:
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                fnt = ImageFont.truetype(self.get_font(), font_size)
                d = ImageDraw.Draw(txt)
                
                # Getting positions
                text_bbox = d.textbbox((0, 0), "WATERMARK PRO", font=fnt)

                # Drawing
                d.text(self._calculate_position_(text_bbox, base), "WATERMARK PRO", font=fnt, fill=color_rgb)

                out = Image.alpha_composite(base, txt)
                self._save_image_(out)
                