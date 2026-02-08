# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from widgets import (btn_browse, color_box, drop_area, filename_label,
    font_box, generate_btn, pos_button, slider,
    slider_opacity_value, slider_size_value, text_watermark_radio)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 545)
        MainWindow.setMinimumSize(QSize(743, 545))
        MainWindow.setMaximumSize(QSize(743, 545))
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #e0e0e0;\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.title_layout = QWidget(self.centralwidget)
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setGeometry(QRect(20, 10, 701, 71))
        self.title_layout.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 5px;")
        self.layoutWidget = QWidget(self.title_layout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 711, 58))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.water_icon = QLabel(self.layoutWidget)
        self.water_icon.setObjectName(u"water_icon")
        self.water_icon.setMinimumSize(QSize(40, 40))
        self.water_icon.setMaximumSize(QSize(40, 40))
        self.water_icon.setPixmap(QPixmap(u":/Resources/droplet.svg"))
        self.water_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.water_icon)

        self.title_label = QLabel(self.layoutWidget)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setKerning(True)
        self.title_label.setFont(font1)

        self.horizontalLayout.addWidget(self.title_label)

        self.horizontalSpacer_3 = QSpacerItem(488, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.main_layout_2 = QWidget(self.centralwidget)
        self.main_layout_2.setObjectName(u"main_layout_2")
        self.main_layout_2.setGeometry(QRect(400, 90, 321, 361))
        self.main_layout_2.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 5px;")
        self.layoutWidget1 = QWidget(self.main_layout_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 281, 343))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        font2.setPointSize(12)
        font2.setWeight(QFont.DemiBold)
        self.label.setFont(font2)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.text_watermark_button = text_watermark_radio(self.layoutWidget1)
        self.text_watermark_button.setObjectName(u"text_watermark_button")
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setBold(False)
        self.text_watermark_button.setFont(font3)
        self.text_watermark_button.setStyleSheet(u"QRadioButton {\n"
"    color: #2C3E50;\n"
"    font-family: \"Montserrat\";\n"
"    spacing: 8px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 2px solid #BDC3C7;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #2ABB9B; \n"
"    border: 2px solid #27AE60;\n"
"}")
        self.text_watermark_button.setChecked(False)

        self.horizontalLayout_6.addWidget(self.text_watermark_button)

        self.horizontalSpacer_18 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Sans Serif Collection"])
        font4.setBold(False)
        self.label_2.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.font_box = font_box(self.layoutWidget1)
        self.font_box.setObjectName(u"font_box")
        self.font_box.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #CBD5E1;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"    background-color: white;\n"
"    color: #334155;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #2ABB9B;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px; \n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\":/icons/down_arrow.png\"); /* Se tiver \u00edcone */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #CBD5E1;\n"
"    border-radius: 8px;\n"
"    background-color: white;\n"
"    selection-background-color: #2ABB9B;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    height: 35px;\n"
"    padding-left: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.font_box)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.slider_size = slider(self.layoutWidget1)
        self.slider_size.setObjectName(u"slider_size")
        self.slider_size.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #D1D5DB;\n"
"    height: 6px;\n"
"    background: #E5E7EB;\n"
"    margin: 2px 0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2ABB9B;\n"
"    border: 1px solid #27AE60;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #27AE60;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #2ABB9B;\n"
"    border-radius: 3px;\n"
"}")
        self.slider_size.setMinimum(10)
        self.slider_size.setMaximum(100)
        self.slider_size.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_8.addWidget(self.slider_size)

        self.slider_size_value = slider_size_value(self.layoutWidget1)
        self.slider_size_value.setObjectName(u"slider_size_value")
        font5 = QFont()
        font5.setFamilies([u"Sans Serif Collection"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.slider_size_value.setFont(font5)

        self.horizontalLayout_8.addWidget(self.slider_size_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.slider_opacity = slider(self.layoutWidget1)
        self.slider_opacity.setObjectName(u"slider_opacity")
        self.slider_opacity.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #D1D5DB;\n"
"    height: 6px;\n"
"    background: #E5E7EB;\n"
"    margin: 2px 0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2ABB9B;\n"
"    border: 1px solid #27AE60;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #27AE60;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #2ABB9B;\n"
"    border-radius: 3px;\n"
"}")
        self.slider_opacity.setMinimum(10)
        self.slider_opacity.setMaximum(100)
        self.slider_opacity.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_9.addWidget(self.slider_opacity)

        self.slider_opacity_value = slider_opacity_value(self.layoutWidget1)
        self.slider_opacity_value.setObjectName(u"slider_opacity_value")
        self.slider_opacity_value.setFont(font5)

        self.horizontalLayout_9.addWidget(self.slider_opacity_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.color_box = color_box(self.layoutWidget1)
        self.color_box.setObjectName(u"color_box")
        self.color_box.setMinimumSize(QSize(32, 32))
        self.color_box.setMaximumSize(QSize(32, 32))
        self.color_box.setStyleSheet(u"background-color: #000000; \n"
"border: 2px solid #34495E;\n"
"border-radius: 5px;")

        self.horizontalLayout_10.addWidget(self.color_box)

        self.horizontalSpacer_16 = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.position_box = QFrame(self.layoutWidget1)
        self.position_box.setObjectName(u"position_box")
        self.position_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.position_box.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.position_box)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.pos_bottom_mid = pos_button(self.position_box)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pos_bottom_mid)
        self.pos_bottom_mid.setObjectName(u"pos_bottom_mid")
        self.pos_bottom_mid.setMinimumSize(QSize(30, 30))
        self.pos_bottom_mid.setMaximumSize(QSize(30, 30))
        self.pos_bottom_mid.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_bottom_mid.setCheckable(True)

        self.gridLayout.addWidget(self.pos_bottom_mid, 2, 1, 1, 1)

        self.pos_mid = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_mid)
        self.pos_mid.setObjectName(u"pos_mid")
        self.pos_mid.setMinimumSize(QSize(30, 30))
        self.pos_mid.setMaximumSize(QSize(30, 30))
        self.pos_mid.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_mid.setCheckable(True)

        self.gridLayout.addWidget(self.pos_mid, 1, 1, 1, 1)

        self.pos_mid_left = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_mid_left)
        self.pos_mid_left.setObjectName(u"pos_mid_left")
        self.pos_mid_left.setMinimumSize(QSize(30, 30))
        self.pos_mid_left.setMaximumSize(QSize(30, 30))
        self.pos_mid_left.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_mid_left.setCheckable(True)

        self.gridLayout.addWidget(self.pos_mid_left, 1, 0, 1, 1)

        self.pos_top_left = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_top_left)
        self.pos_top_left.setObjectName(u"pos_top_left")
        self.pos_top_left.setMinimumSize(QSize(30, 30))
        self.pos_top_left.setMaximumSize(QSize(30, 30))
        self.pos_top_left.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_top_left.setCheckable(True)

        self.gridLayout.addWidget(self.pos_top_left, 0, 0, 1, 1)

        self.pos_bottom_right = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_bottom_right)
        self.pos_bottom_right.setObjectName(u"pos_bottom_right")
        self.pos_bottom_right.setMinimumSize(QSize(30, 30))
        self.pos_bottom_right.setMaximumSize(QSize(30, 30))
        self.pos_bottom_right.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_bottom_right.setCheckable(True)

        self.gridLayout.addWidget(self.pos_bottom_right, 2, 2, 1, 1)

        self.pos_bottom_left = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_bottom_left)
        self.pos_bottom_left.setObjectName(u"pos_bottom_left")
        self.pos_bottom_left.setMinimumSize(QSize(30, 30))
        self.pos_bottom_left.setMaximumSize(QSize(30, 30))
        self.pos_bottom_left.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_bottom_left.setCheckable(True)

        self.gridLayout.addWidget(self.pos_bottom_left, 2, 0, 1, 1)

        self.pos_top_right = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_top_right)
        self.pos_top_right.setObjectName(u"pos_top_right")
        self.pos_top_right.setMinimumSize(QSize(30, 30))
        self.pos_top_right.setMaximumSize(QSize(30, 30))
        self.pos_top_right.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_top_right.setCheckable(True)

        self.gridLayout.addWidget(self.pos_top_right, 0, 2, 1, 1)

        self.pos_top_mid = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_top_mid)
        self.pos_top_mid.setObjectName(u"pos_top_mid")
        self.pos_top_mid.setMinimumSize(QSize(30, 30))
        self.pos_top_mid.setMaximumSize(QSize(30, 30))
        self.pos_top_mid.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_top_mid.setCheckable(True)

        self.gridLayout.addWidget(self.pos_top_mid, 0, 1, 1, 1)

        self.pos_mid_right = pos_button(self.position_box)
        self.buttonGroup.addButton(self.pos_mid_right)
        self.pos_mid_right.setObjectName(u"pos_mid_right")
        self.pos_mid_right.setMinimumSize(QSize(30, 30))
        self.pos_mid_right.setMaximumSize(QSize(30, 30))
        self.pos_mid_right.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: 2px solid #24a085;\n"
"}\n"
"QPushButton {\n"
"	background-color: #e0e0e0\n"
"}")
        self.pos_mid_right.setCheckable(True)

        self.gridLayout.addWidget(self.pos_mid_right, 1, 2, 1, 1)


        self.horizontalLayout_11.addWidget(self.position_box)

        self.horizontalSpacer_17 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.main_layout = QWidget(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setGeometry(QRect(20, 90, 361, 361))
        self.main_layout.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 5px;")
        self.drop_area = drop_area(self.main_layout)
        self.drop_area.setObjectName(u"drop_area")
        self.drop_area.setEnabled(True)
        self.drop_area.setGeometry(QRect(30, 10, 301, 181))
        self.drop_area.setStyleSheet(u"#drop_area {\n"
"    border: 2px dashed #CBD5E1;\n"
"	background-color: #e6f2f1;\n"
"	border-radius: 5px\n"
"}\n"
"")
        self.drop_area.setFrameShape(QFrame.Shape.Box)
        self.drop_area.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_area)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.drop_area)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(64, 64))
        self.label_7.setMaximumSize(QSize(64, 64))
        self.label_7.setStyleSheet(u"background-color: transparent")
        self.label_7.setPixmap(QPixmap(u":/Resources/cloud.svg"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.drop_area)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setPointSize(12)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"background-color: transparent")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.filename_label = filename_label(self.main_layout)
        self.filename_label.setObjectName(u"filename_label")
        self.filename_label.setGeometry(QRect(10, 320, 341, 20))
        self.filename_label.setStyleSheet(u"")
        self.filename_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget2 = QWidget(self.main_layout)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 200, 298, 116))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.btn_browse = btn_browse(self.layoutWidget2)
        self.btn_browse.setObjectName(u"btn_browse")
        font7 = QFont()
        font7.setFamilies([u"Montserrat"])
        font7.setWeight(QFont.DemiBold)
        self.btn_browse.setFont(font7)
        self.btn_browse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_browse.setStyleSheet(u"#btn_browse {\n"
"    background-color: #D6DCE2;\n"
"    padding: 10px 20px;\n"
"    border: 1px solid #B0B7BE;\n"
"    border-radius: 6px;\n"
"    color: #475569;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#btn_browse:hover {\n"
"    background-color: #CBD5E1;\n"
"    border: 1px solid #94A3B8;\n"
"    color: #1E293B;\n"
"}\n"
"\n"
"QPushButton#btn_browse:pressed {\n"
"    background-color: #94A3B8;\n"
"    padding-top: 11px; \n"
"    padding-bottom: 9px;\n"
"}\n"
"\n"
"QPushButton#btn_browse:disabled {\n"
"    background-color: #F1F5F9;\n"
"    color: #CBD5E1;\n"
"    border: 1px solid #E2E8F0;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_browse.setIcon(icon)
        self.btn_browse.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btn_browse)

        self.horizontalSpacer_7 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setMinimumSize(QSize(64, 64))
        self.label_9.setMaximumSize(QSize(64, 64))
        self.label_9.setStyleSheet(u"background-color: transparent")
        self.label_9.setPixmap(QPixmap(u":/Resources/image.svg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.footer_layout = QWidget(self.centralwidget)
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_layout.setGeometry(QRect(80, 460, 611, 81))
        self.footer_layout.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 5px;")
        self.verticalLayout_7 = QVBoxLayout(self.footer_layout)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_11 = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)

        self.generate_btn = generate_btn(self.footer_layout)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setStyleSheet(u"QPushButton#generate_btn {\n"
"    background-color: #2ABB9B;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 12px 25px;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#generate_btn:hover {\n"
"    background-color: #34D399;\n"
"}\n"
"\n"
"QPushButton#generate_btn:pressed {\n"
"    background-color: #059669;\n"
"    padding-top: 14px;\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#generate_btn:disabled {\n"
"    background-color: #E2E8F0;\n"
"    color: #94A3B8;\n"
"}")

        self.horizontalLayout_22.addWidget(self.generate_btn)

        self.horizontalSpacer_12 = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.water_icon.setText("")
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"WATERMARK PRO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Customize Watermark", None))
        self.text_watermark_button.setText(QCoreApplication.translate("MainWindow", u"Text Watermark", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Font: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.slider_size_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Opacity:", None))
        self.slider_opacity_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.color_box.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.pos_bottom_mid.setText("")
        self.pos_mid.setText("")
        self.pos_mid_left.setText("")
        self.pos_top_left.setText("")
        self.pos_bottom_right.setText("")
        self.pos_bottom_left.setText("")
        self.pos_top_right.setText("")
        self.pos_top_mid.setText("")
        self.pos_mid_right.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop Image Here or Click to Upload", None))
        self.filename_label.setText(QCoreApplication.translate("MainWindow", u"Uploaded File", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.label_9.setText("")
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"APPLY WATERMARK", None))
    # retranslateUi

