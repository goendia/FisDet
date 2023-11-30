# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_v4.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(438, 996)
        MainWindow.setMinimumSize(QSize(345, 731))
        MainWindow.setBaseSize(QSize(299, 632))
        MainWindow.setStyleSheet(u"/*QMainWindow{\n"
"	background-color: rgb(85, 255, 0);\n"
"	background-color:rgb(165, 165, 165);\n"
"	/*color:white;*/\n"
"\n"
"\n"
"QGroupBox {\n"
"	/*background-color:rgb(200, 200, 200);*/\n"
"     border: 1px solid gray;\n"
"     border-radius: 2px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
"	font: bold;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; /* position at the top center */\n"
"     padding: 0 7px;\n"
" }\n"
"\n"
" QGroupBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"	border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearG"
                        "radient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:on\n"
"{\n"
"    border: 2px solid;\n"
"	background-color: rgb(118, 214, 255);\n"
"	text-color: black\n"
"}\n"
"\n"
"/*\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"*/")
        self.action_Laden = QAction(MainWindow)
        self.action_Laden.setObjectName(u"action_Laden")
        icon = QIcon()
        icon.addFile(u":/images/images/database_go.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Laden.setIcon(icon)
        self.actionAnzeigen = QAction(MainWindow)
        self.actionAnzeigen.setObjectName(u"actionAnzeigen")
        self.actionAls_Excel_exportieren = QAction(MainWindow)
        self.actionAls_Excel_exportieren.setObjectName(u"actionAls_Excel_exportieren")
        self.action_Oeffnen = QAction(MainWindow)
        self.action_Oeffnen.setObjectName(u"action_Oeffnen")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/table_edit_small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Oeffnen.setIcon(icon1)
        self.action_Zuletzt_verwendet = QAction(MainWindow)
        self.action_Zuletzt_verwendet.setObjectName(u"action_Zuletzt_verwendet")
        self.action_Schliessen = QAction(MainWindow)
        self.action_Schliessen.setObjectName(u"action_Schliessen")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/door_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Schliessen.setIcon(icon2)
        self.actionServer_DB = QAction(MainWindow)
        self.actionServer_DB.setObjectName(u"actionServer_DB")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/database_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionServer_DB.setIcon(icon3)
        self.actionSub_DB = QAction(MainWindow)
        self.actionSub_DB.setObjectName(u"actionSub_DB")
        self.actionSub_DB.setIcon(icon3)
        self.actionManuelleEingabe = QAction(MainWindow)
        self.actionManuelleEingabe.setObjectName(u"actionManuelleEingabe")
        self.actionManuelleEingabe.setCheckable(True)
        self.actionManuelleEingabe.setChecked(True)
        self.actionTruebungTurbulenz = QAction(MainWindow)
        self.actionTruebungTurbulenz.setObjectName(u"actionTruebungTurbulenz")
        self.actionTruebungTurbulenz.setCheckable(True)
        self.actionTruebungTurbulenz.setChecked(True)
        self.actionBodenplatteButtons = QAction(MainWindow)
        self.actionBodenplatteButtons.setObjectName(u"actionBodenplatteButtons")
        self.actionBodenplatteButtons.setCheckable(True)
        self.actionBodenplatteButtons.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QSize(91, 61))
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinbox = QSpinBox(self.groupBox_5)
        self.spinbox.setObjectName(u"spinbox")
        font = QFont()
        font.setPointSize(14)
        self.spinbox.setFont(font)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(99999)
        self.spinbox.setValue(1)

        self.verticalLayout.addWidget(self.spinbox)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QSize(90, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.editProtokollant = QLineEdit(self.groupBox_7)
        self.editProtokollant.setObjectName(u"editProtokollant")
        sizePolicy.setHeightForWidth(self.editProtokollant.sizePolicy().hasHeightForWidth())
        self.editProtokollant.setSizePolicy(sizePolicy)
        self.editProtokollant.setMinimumSize(QSize(10, 0))
        self.editProtokollant.setMaximumSize(QSize(16777215, 31))
        self.editProtokollant.setBaseSize(QSize(30, 0))
        font1 = QFont()
        font1.setFamilies([u"Abyssinica SIL"])
        font1.setPointSize(14)
        self.editProtokollant.setFont(font1)
        self.editProtokollant.setMaxLength(100)

        self.verticalLayout_2.addWidget(self.editProtokollant)


        self.horizontalLayout_2.addWidget(self.groupBox_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBoxArtLaenge = QGroupBox(self.centralwidget)
        self.groupBoxArtLaenge.setObjectName(u"groupBoxArtLaenge")
        sizePolicy.setHeightForWidth(self.groupBoxArtLaenge.sizePolicy().hasHeightForWidth())
        self.groupBoxArtLaenge.setSizePolicy(sizePolicy)
        self.groupBoxArtLaenge.setMinimumSize(QSize(221, 191))
        palette = QPalette()
        self.groupBoxArtLaenge.setPalette(palette)
        self.groupBoxArtLaenge.setLayoutDirection(Qt.LeftToRight)
        self.groupBoxArtLaenge.setAutoFillBackground(False)
        self.groupBoxArtLaenge.setCheckable(True)
        self.groupBoxArtLaenge.setChecked(True)
        self.gridLayout = QGridLayout(self.groupBoxArtLaenge)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBab10 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab10.setObjectName(u"buttonBab10")
        sizePolicy.setHeightForWidth(self.buttonBab10.sizePolicy().hasHeightForWidth())
        self.buttonBab10.setSizePolicy(sizePolicy)
        self.buttonBab10.setMinimumSize(QSize(51, 22))
        self.buttonBab10.setCheckable(True)
        self.buttonBab10.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab10, 3, 5, 1, 1)

        self.buttonRot20 = QPushButton(self.groupBoxArtLaenge)
        self.buttonRot20.setObjectName(u"buttonRot20")
        sizePolicy.setHeightForWidth(self.buttonRot20.sizePolicy().hasHeightForWidth())
        self.buttonRot20.setSizePolicy(sizePolicy)
        self.buttonRot20.setMinimumSize(QSize(51, 22))
        self.buttonRot20.setCheckable(True)
        self.buttonRot20.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonRot20, 5, 1, 1, 1)

        self.buttonRot10 = QPushButton(self.groupBoxArtLaenge)
        self.buttonRot10.setObjectName(u"buttonRot10")
        sizePolicy.setHeightForWidth(self.buttonRot10.sizePolicy().hasHeightForWidth())
        self.buttonRot10.setSizePolicy(sizePolicy)
        self.buttonRot10.setMinimumSize(QSize(51, 22))
        self.buttonRot10.setCheckable(True)
        self.buttonRot10.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonRot10, 5, 2, 1, 1)

        self.buttonLac60 = QPushButton(self.groupBoxArtLaenge)
        self.buttonLac60.setObjectName(u"buttonLac60")
        sizePolicy.setHeightForWidth(self.buttonLac60.sizePolicy().hasHeightForWidth())
        self.buttonLac60.setSizePolicy(sizePolicy)
        self.buttonLac60.setMinimumSize(QSize(51, 22))
        self.buttonLac60.setCheckable(True)
        self.buttonLac60.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonLac60, 10, 2, 1, 1)

        self.buttonLac50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonLac50.setObjectName(u"buttonLac50")
        sizePolicy.setHeightForWidth(self.buttonLac50.sizePolicy().hasHeightForWidth())
        self.buttonLac50.setSizePolicy(sizePolicy)
        self.buttonLac50.setMinimumSize(QSize(51, 22))
        self.buttonLac50.setCheckable(True)
        self.buttonLac50.setAutoExclusive(True)
        self.buttonLac50.setFlat(False)

        self.gridLayout.addWidget(self.buttonLac50, 10, 3, 1, 1)

        self.buttonRot30 = QPushButton(self.groupBoxArtLaenge)
        self.buttonRot30.setObjectName(u"buttonRot30")
        sizePolicy.setHeightForWidth(self.buttonRot30.sizePolicy().hasHeightForWidth())
        self.buttonRot30.setSizePolicy(sizePolicy)
        self.buttonRot30.setMinimumSize(QSize(51, 22))
        self.buttonRot30.setCheckable(True)
        self.buttonRot30.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonRot30, 5, 0, 1, 1)

        self.buttonAal30 = QPushButton(self.groupBoxArtLaenge)
        self.buttonAal30.setObjectName(u"buttonAal30")
        sizePolicy.setHeightForWidth(self.buttonAal30.sizePolicy().hasHeightForWidth())
        self.buttonAal30.setSizePolicy(sizePolicy)
        self.buttonAal30.setMinimumSize(QSize(51, 22))
        self.buttonAal30.setCheckable(True)
        self.buttonAal30.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonAal30, 2, 2, 1, 1)

        self.buttonMai40 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMai40.setObjectName(u"buttonMai40")
        sizePolicy.setHeightForWidth(self.buttonMai40.sizePolicy().hasHeightForWidth())
        self.buttonMai40.setSizePolicy(sizePolicy)
        self.buttonMai40.setMinimumSize(QSize(51, 22))
        self.buttonMai40.setCheckable(True)
        self.buttonMai40.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMai40, 8, 1, 1, 1)

        self.buttonLac80 = QPushButton(self.groupBoxArtLaenge)
        self.buttonLac80.setObjectName(u"buttonLac80")
        sizePolicy.setHeightForWidth(self.buttonLac80.sizePolicy().hasHeightForWidth())
        self.buttonLac80.setSizePolicy(sizePolicy)
        self.buttonLac80.setMinimumSize(QSize(51, 22))
        self.buttonLac80.setCheckable(True)
        self.buttonLac80.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonLac80, 10, 0, 1, 1)

        self.buttonRot0 = QPushButton(self.groupBoxArtLaenge)
        self.buttonRot0.setObjectName(u"buttonRot0")
        sizePolicy.setHeightForWidth(self.buttonRot0.sizePolicy().hasHeightForWidth())
        self.buttonRot0.setSizePolicy(sizePolicy)
        self.buttonRot0.setMinimumSize(QSize(51, 22))
        self.buttonRot0.setCheckable(True)
        self.buttonRot0.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonRot0, 5, 3, 1, 1)

        self.buttonNas40 = QPushButton(self.groupBoxArtLaenge)
        self.buttonNas40.setObjectName(u"buttonNas40")
        sizePolicy.setHeightForWidth(self.buttonNas40.sizePolicy().hasHeightForWidth())
        self.buttonNas40.setSizePolicy(sizePolicy)
        self.buttonNas40.setMinimumSize(QSize(51, 22))
        self.buttonNas40.setCheckable(True)
        self.buttonNas40.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonNas40, 1, 1, 1, 1)

        self.buttonAal40 = QPushButton(self.groupBoxArtLaenge)
        self.buttonAal40.setObjectName(u"buttonAal40")
        sizePolicy.setHeightForWidth(self.buttonAal40.sizePolicy().hasHeightForWidth())
        self.buttonAal40.setSizePolicy(sizePolicy)
        self.buttonAal40.setMinimumSize(QSize(51, 22))
        self.buttonAal40.setCheckable(True)
        self.buttonAal40.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonAal40, 2, 1, 1, 1)

        self.buttonBab50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab50.setObjectName(u"buttonBab50")
        sizePolicy.setHeightForWidth(self.buttonBab50.sizePolicy().hasHeightForWidth())
        self.buttonBab50.setSizePolicy(sizePolicy)
        self.buttonBab50.setMinimumSize(QSize(51, 22))
        self.buttonBab50.setCheckable(True)
        self.buttonBab50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab50, 3, 1, 1, 1)

        self.buttonBra50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBra50.setObjectName(u"buttonBra50")
        sizePolicy.setHeightForWidth(self.buttonBra50.sizePolicy().hasHeightForWidth())
        self.buttonBra50.setSizePolicy(sizePolicy)
        self.buttonBra50.setMinimumSize(QSize(51, 22))
        self.buttonBra50.setCheckable(True)
        self.buttonBra50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBra50, 4, 1, 1, 1)

        self.buttonBra30 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBra30.setObjectName(u"buttonBra30")
        sizePolicy.setHeightForWidth(self.buttonBra30.sizePolicy().hasHeightForWidth())
        self.buttonBra30.setSizePolicy(sizePolicy)
        self.buttonBra30.setMinimumSize(QSize(51, 22))
        self.buttonBra30.setCheckable(True)
        self.buttonBra30.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBra30, 4, 3, 1, 1)

        self.buttonMen90 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMen90.setObjectName(u"buttonMen90")
        sizePolicy.setHeightForWidth(self.buttonMen90.sizePolicy().hasHeightForWidth())
        self.buttonMen90.setSizePolicy(sizePolicy)
        self.buttonMen90.setMinimumSize(QSize(51, 22))
        self.buttonMen90.setCheckable(True)
        self.buttonMen90.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMen90, 9, 0, 1, 1)

        self.buttonMai50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMai50.setObjectName(u"buttonMai50")
        sizePolicy.setHeightForWidth(self.buttonMai50.sizePolicy().hasHeightForWidth())
        self.buttonMai50.setSizePolicy(sizePolicy)
        self.buttonMai50.setMinimumSize(QSize(51, 22))
        self.buttonMai50.setCheckable(True)
        self.buttonMai50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMai50, 8, 0, 1, 1)

        self.buttonBra60 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBra60.setObjectName(u"buttonBra60")
        sizePolicy.setHeightForWidth(self.buttonBra60.sizePolicy().hasHeightForWidth())
        self.buttonBra60.setSizePolicy(sizePolicy)
        self.buttonBra60.setMinimumSize(QSize(51, 22))
        self.buttonBra60.setCheckable(True)
        self.buttonBra60.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBra60, 4, 0, 1, 1)

        self.buttonAal50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonAal50.setObjectName(u"buttonAal50")
        sizePolicy.setHeightForWidth(self.buttonAal50.sizePolicy().hasHeightForWidth())
        self.buttonAal50.setSizePolicy(sizePolicy)
        self.buttonAal50.setMinimumSize(QSize(51, 22))
        self.buttonAal50.setCheckable(True)
        self.buttonAal50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonAal50, 2, 0, 1, 1)

        self.buttonNas30 = QPushButton(self.groupBoxArtLaenge)
        self.buttonNas30.setObjectName(u"buttonNas30")
        sizePolicy.setHeightForWidth(self.buttonNas30.sizePolicy().hasHeightForWidth())
        self.buttonNas30.setSizePolicy(sizePolicy)
        self.buttonNas30.setMinimumSize(QSize(51, 22))
        self.buttonNas30.setCheckable(True)
        self.buttonNas30.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonNas30, 1, 2, 1, 1)

        self.buttonMee70 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMee70.setObjectName(u"buttonMee70")
        sizePolicy.setHeightForWidth(self.buttonMee70.sizePolicy().hasHeightForWidth())
        self.buttonMee70.setSizePolicy(sizePolicy)
        self.buttonMee70.setMinimumSize(QSize(51, 22))
        self.buttonMee70.setCheckable(True)
        self.buttonMee70.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMee70, 6, 0, 1, 1)

        self.buttonBab40 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab40.setObjectName(u"buttonBab40")
        sizePolicy.setHeightForWidth(self.buttonBab40.sizePolicy().hasHeightForWidth())
        self.buttonBab40.setSizePolicy(sizePolicy)
        self.buttonBab40.setMinimumSize(QSize(51, 22))
        self.buttonBab40.setCheckable(True)
        self.buttonBab40.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab40, 3, 2, 1, 1)

        self.buttonBra40 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBra40.setObjectName(u"buttonBra40")
        sizePolicy.setHeightForWidth(self.buttonBra40.sizePolicy().hasHeightForWidth())
        self.buttonBra40.setSizePolicy(sizePolicy)
        self.buttonBra40.setMinimumSize(QSize(51, 22))
        self.buttonBra40.setCheckable(True)
        self.buttonBra40.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBra40, 4, 2, 1, 1)

        self.buttonNas50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonNas50.setObjectName(u"buttonNas50")
        sizePolicy.setHeightForWidth(self.buttonNas50.sizePolicy().hasHeightForWidth())
        self.buttonNas50.setSizePolicy(sizePolicy)
        self.buttonNas50.setMinimumSize(QSize(51, 22))
        self.buttonNas50.setCheckable(True)
        self.buttonNas50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonNas50, 1, 0, 1, 1)

        self.buttonUke10 = QPushButton(self.groupBoxArtLaenge)
        self.buttonUke10.setObjectName(u"buttonUke10")
        sizePolicy.setHeightForWidth(self.buttonUke10.sizePolicy().hasHeightForWidth())
        self.buttonUke10.setSizePolicy(sizePolicy)
        self.buttonUke10.setMinimumSize(QSize(51, 22))
        self.buttonUke10.setCheckable(True)
        self.buttonUke10.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonUke10, 0, 0, 1, 1)

        self.buttonMee50 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMee50.setObjectName(u"buttonMee50")
        sizePolicy.setHeightForWidth(self.buttonMee50.sizePolicy().hasHeightForWidth())
        self.buttonMee50.setSizePolicy(sizePolicy)
        self.buttonMee50.setMinimumSize(QSize(51, 22))
        self.buttonMee50.setCheckable(True)
        self.buttonMee50.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMee50, 6, 2, 1, 1)

        self.buttonMen70 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMen70.setObjectName(u"buttonMen70")
        sizePolicy.setHeightForWidth(self.buttonMen70.sizePolicy().hasHeightForWidth())
        self.buttonMen70.setSizePolicy(sizePolicy)
        self.buttonMen70.setMinimumSize(QSize(51, 22))
        self.buttonMen70.setCheckable(True)
        self.buttonMen70.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMen70, 9, 2, 1, 1)

        self.buttonMen80 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMen80.setObjectName(u"buttonMen80")
        sizePolicy.setHeightForWidth(self.buttonMen80.sizePolicy().hasHeightForWidth())
        self.buttonMen80.setSizePolicy(sizePolicy)
        self.buttonMen80.setMinimumSize(QSize(51, 22))
        self.buttonMen80.setCheckable(True)
        self.buttonMen80.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMen80, 9, 1, 1, 1)

        self.buttonNas20 = QPushButton(self.groupBoxArtLaenge)
        self.buttonNas20.setObjectName(u"buttonNas20")
        sizePolicy.setHeightForWidth(self.buttonNas20.sizePolicy().hasHeightForWidth())
        self.buttonNas20.setSizePolicy(sizePolicy)
        self.buttonNas20.setMinimumSize(QSize(51, 22))
        self.buttonNas20.setCheckable(True)
        self.buttonNas20.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonNas20, 1, 3, 1, 1)

        self.buttonBab60 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab60.setObjectName(u"buttonBab60")
        sizePolicy.setHeightForWidth(self.buttonBab60.sizePolicy().hasHeightForWidth())
        self.buttonBab60.setSizePolicy(sizePolicy)
        self.buttonBab60.setMinimumSize(QSize(51, 22))
        self.buttonBab60.setCheckable(True)
        self.buttonBab60.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab60, 3, 0, 1, 1)

        self.buttonBab30 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab30.setObjectName(u"buttonBab30")
        sizePolicy.setHeightForWidth(self.buttonBab30.sizePolicy().hasHeightForWidth())
        self.buttonBab30.setSizePolicy(sizePolicy)
        self.buttonBab30.setMinimumSize(QSize(51, 22))
        self.buttonBab30.setCheckable(True)
        self.buttonBab30.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab30, 3, 3, 1, 1)

        self.buttonUke0 = QPushButton(self.groupBoxArtLaenge)
        self.buttonUke0.setObjectName(u"buttonUke0")
        sizePolicy.setHeightForWidth(self.buttonUke0.sizePolicy().hasHeightForWidth())
        self.buttonUke0.setSizePolicy(sizePolicy)
        self.buttonUke0.setMinimumSize(QSize(51, 22))
        self.buttonUke0.setCheckable(True)
        self.buttonUke0.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonUke0, 0, 1, 1, 1)

        self.buttonMee60 = QPushButton(self.groupBoxArtLaenge)
        self.buttonMee60.setObjectName(u"buttonMee60")
        sizePolicy.setHeightForWidth(self.buttonMee60.sizePolicy().hasHeightForWidth())
        self.buttonMee60.setSizePolicy(sizePolicy)
        self.buttonMee60.setMinimumSize(QSize(51, 22))
        self.buttonMee60.setCheckable(True)
        self.buttonMee60.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonMee60, 6, 1, 1, 1)

        self.buttonBab20 = QPushButton(self.groupBoxArtLaenge)
        self.buttonBab20.setObjectName(u"buttonBab20")
        sizePolicy.setHeightForWidth(self.buttonBab20.sizePolicy().hasHeightForWidth())
        self.buttonBab20.setSizePolicy(sizePolicy)
        self.buttonBab20.setMinimumSize(QSize(51, 22))
        self.buttonBab20.setCheckable(True)
        self.buttonBab20.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonBab20, 3, 4, 1, 1)

        self.buttonAal20 = QPushButton(self.groupBoxArtLaenge)
        self.buttonAal20.setObjectName(u"buttonAal20")
        sizePolicy.setHeightForWidth(self.buttonAal20.sizePolicy().hasHeightForWidth())
        self.buttonAal20.setSizePolicy(sizePolicy)
        self.buttonAal20.setMinimumSize(QSize(51, 22))
        self.buttonAal20.setCheckable(True)
        self.buttonAal20.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonAal20, 2, 3, 1, 1)

        self.buttonLac70 = QPushButton(self.groupBoxArtLaenge)
        self.buttonLac70.setObjectName(u"buttonLac70")
        sizePolicy.setHeightForWidth(self.buttonLac70.sizePolicy().hasHeightForWidth())
        self.buttonLac70.setSizePolicy(sizePolicy)
        self.buttonLac70.setMinimumSize(QSize(51, 22))
        self.buttonLac70.setCheckable(True)
        self.buttonLac70.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonLac70, 10, 1, 1, 1)

        self.buttonUk10 = QPushButton(self.groupBoxArtLaenge)
        self.buttonUk10.setObjectName(u"buttonUk10")
        sizePolicy.setHeightForWidth(self.buttonUk10.sizePolicy().hasHeightForWidth())
        self.buttonUk10.setSizePolicy(sizePolicy)
        self.buttonUk10.setMinimumSize(QSize(51, 22))
        self.buttonUk10.setCheckable(True)
        self.buttonUk10.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonUk10, 11, 0, 1, 1)

        self.buttonUk0 = QPushButton(self.groupBoxArtLaenge)
        self.buttonUk0.setObjectName(u"buttonUk0")
        sizePolicy.setHeightForWidth(self.buttonUk0.sizePolicy().hasHeightForWidth())
        self.buttonUk0.setSizePolicy(sizePolicy)
        self.buttonUk0.setMinimumSize(QSize(51, 22))
        self.buttonUk0.setCheckable(True)
        self.buttonUk0.setAutoExclusive(True)

        self.gridLayout.addWidget(self.buttonUk0, 11, 1, 1, 1)

        self.buttonUncheckAllFishButtons = QPushButton(self.groupBoxArtLaenge)
        self.buttonUncheckAllFishButtons.setObjectName(u"buttonUncheckAllFishButtons")
        self.buttonUncheckAllFishButtons.setEnabled(True)
        sizePolicy.setHeightForWidth(self.buttonUncheckAllFishButtons.sizePolicy().hasHeightForWidth())
        self.buttonUncheckAllFishButtons.setSizePolicy(sizePolicy)
        self.buttonUncheckAllFishButtons.setMinimumSize(QSize(51, 22))
        self.buttonUncheckAllFishButtons.setCheckable(True)
        self.buttonUncheckAllFishButtons.setAutoExclusive(True)
        self.buttonUncheckAllFishButtons.setAutoDefault(False)
        self.buttonUncheckAllFishButtons.setFlat(False)

        self.gridLayout.addWidget(self.buttonUncheckAllFishButtons, 11, 5, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBoxArtLaenge)

        self.groupBoxManuell = QGroupBox(self.centralwidget)
        self.groupBoxManuell.setObjectName(u"groupBoxManuell")
        sizePolicy.setHeightForWidth(self.groupBoxManuell.sizePolicy().hasHeightForWidth())
        self.groupBoxManuell.setSizePolicy(sizePolicy)
        self.groupBoxManuell.setMinimumSize(QSize(281, 64))
        self.groupBoxManuell.setCheckable(True)
        self.groupBoxManuell.setChecked(False)
        self.horizontalLayout = QHBoxLayout(self.groupBoxManuell)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_art = QLabel(self.groupBoxManuell)
        self.label_art.setObjectName(u"label_art")
        self.label_art.setMinimumSize(QSize(1, 30))
        self.label_art.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_art)

        self.comboBoxArt = QComboBox(self.groupBoxManuell)
        self.comboBoxArt.setObjectName(u"comboBoxArt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxArt.sizePolicy().hasHeightForWidth())
        self.comboBoxArt.setSizePolicy(sizePolicy1)
        self.comboBoxArt.setMinimumSize(QSize(170, 27))
        self.comboBoxArt.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.comboBoxArt)

        self.label_laenge = QLabel(self.groupBoxManuell)
        self.label_laenge.setObjectName(u"label_laenge")
        self.label_laenge.setMinimumSize(QSize(1, 30))
        self.label_laenge.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_laenge)

        self.spinBoxLaenge = QSpinBox(self.groupBoxManuell)
        self.spinBoxLaenge.setObjectName(u"spinBoxLaenge")
        sizePolicy1.setHeightForWidth(self.spinBoxLaenge.sizePolicy().hasHeightForWidth())
        self.spinBoxLaenge.setSizePolicy(sizePolicy1)
        self.spinBoxLaenge.setMinimumSize(QSize(70, 27))
        self.spinBoxLaenge.setMaximumSize(QSize(16777215, 30))
        self.spinBoxLaenge.setWrapping(False)
        self.spinBoxLaenge.setReadOnly(False)
        self.spinBoxLaenge.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxLaenge.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.spinBoxLaenge.setKeyboardTracking(True)
        self.spinBoxLaenge.setMaximum(150)
        self.spinBoxLaenge.setSingleStep(10)

        self.horizontalLayout.addWidget(self.spinBoxLaenge)


        self.verticalLayout_3.addWidget(self.groupBoxManuell)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(281, 81))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edit_bem = QTextEdit(self.groupBox_2)
        self.edit_bem.setObjectName(u"edit_bem")
        self.edit_bem.setMaximumSize(QSize(9999, 20))
        self.edit_bem.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.edit_bem, 0, 0, 1, 6)

        self.check_bem = QCheckBox(self.groupBox_2)
        self.check_bem.setObjectName(u"check_bem")

        self.gridLayout_2.addWidget(self.check_bem, 0, 6, 1, 1)

        self.rbtn_blau = QRadioButton(self.groupBox_2)
        self.rbtn_blau.setObjectName(u"rbtn_blau")
        self.rbtn_blau.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(0, 0, 255);\n"
"    }")

        self.gridLayout_2.addWidget(self.rbtn_blau, 1, 0, 1, 1)

        self.rbtn_rot = QRadioButton(self.groupBox_2)
        self.rbtn_rot.setObjectName(u"rbtn_rot")
        self.rbtn_rot.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(255, 0, 0);\n"
"    }")

        self.gridLayout_2.addWidget(self.rbtn_rot, 1, 1, 1, 1)

        self.rbtn_gruen = QRadioButton(self.groupBox_2)
        self.rbtn_gruen.setObjectName(u"rbtn_gruen")
        self.rbtn_gruen.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(0, 255, 0);\n"
"    }")

        self.gridLayout_2.addWidget(self.rbtn_gruen, 1, 2, 1, 1)

        self.rbtn_gelb = QRadioButton(self.groupBox_2)
        self.rbtn_gelb.setObjectName(u"rbtn_gelb")
        self.rbtn_gelb.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(255, 255, 0);\n"
"    }")

        self.gridLayout_2.addWidget(self.rbtn_gelb, 1, 3, 1, 1)

        self.rbtn_pink = QRadioButton(self.groupBox_2)
        self.rbtn_pink.setObjectName(u"rbtn_pink")
        self.rbtn_pink.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(255, 0, 255);\n"
"    }")

        self.gridLayout_2.addWidget(self.rbtn_pink, 1, 4, 1, 1)

        self.rbtn_def = QRadioButton(self.groupBox_2)
        self.rbtn_def.setObjectName(u"rbtn_def")
        self.rbtn_def.setStyleSheet(u"    QRadioButton{\n"
"    background:rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"    }")
        self.rbtn_def.setChecked(True)

        self.gridLayout_2.addWidget(self.rbtn_def, 1, 5, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBoxTruebungTurbulenz = QGroupBox(self.centralwidget)
        self.groupBoxTruebungTurbulenz.setObjectName(u"groupBoxTruebungTurbulenz")
        self.groupBoxTruebungTurbulenz.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxTruebungTurbulenz)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.combo_trueb = QComboBox(self.groupBoxTruebungTurbulenz)
        self.combo_trueb.setObjectName(u"combo_trueb")

        self.horizontalLayout_3.addWidget(self.combo_trueb)

        self.combo_turb = QComboBox(self.groupBoxTruebungTurbulenz)
        self.combo_turb.setObjectName(u"combo_turb")

        self.horizontalLayout_3.addWidget(self.combo_turb)


        self.verticalLayout_3.addWidget(self.groupBoxTruebungTurbulenz)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(241, 65))
        self.groupBox_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonAufstieg = QPushButton(self.groupBox_4)
        self.buttonAufstieg.setObjectName(u"buttonAufstieg")
        self.buttonAufstieg.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonAufstieg, 0, 0, 1, 1)

        self.buttonAbstieg = QPushButton(self.groupBox_4)
        self.buttonAbstieg.setObjectName(u"buttonAbstieg")
        self.buttonAbstieg.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonAbstieg, 0, 1, 1, 1)

        self.buttonKvogno = QPushButton(self.groupBox_4)
        self.buttonKvogno.setObjectName(u"buttonKvogno")
        self.buttonKvogno.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonKvogno, 0, 2, 1, 1)

        self.buttonUnklar = QPushButton(self.groupBox_4)
        self.buttonUnklar.setObjectName(u"buttonUnklar")
        self.buttonUnklar.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonUnklar, 0, 4, 1, 1)

        self.buttonKvugnu = QPushButton(self.groupBox_4)
        self.buttonKvugnu.setObjectName(u"buttonKvugnu")
        self.buttonKvugnu.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonKvugnu, 0, 3, 1, 1)

        self.buttonVonUntenInBox = QPushButton(self.groupBox_4)
        self.buttonVonUntenInBox.setObjectName(u"buttonVonUntenInBox")
        self.buttonVonUntenInBox.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonVonUntenInBox, 1, 0, 1, 1)

        self.buttonVonObenInBox = QPushButton(self.groupBox_4)
        self.buttonVonObenInBox.setObjectName(u"buttonVonObenInBox")
        self.buttonVonObenInBox.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonVonObenInBox, 1, 1, 1, 1)

        self.buttonVonBoxInBox = QPushButton(self.groupBox_4)
        self.buttonVonBoxInBox.setObjectName(u"buttonVonBoxInBox")
        self.buttonVonBoxInBox.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonVonBoxInBox, 1, 2, 1, 1)

        self.buttonVonBoxAuf = QPushButton(self.groupBox_4)
        self.buttonVonBoxAuf.setObjectName(u"buttonVonBoxAuf")
        self.buttonVonBoxAuf.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonVonBoxAuf, 1, 3, 1, 1)

        self.buttonVonBoxAb = QPushButton(self.groupBox_4)
        self.buttonVonBoxAb.setObjectName(u"buttonVonBoxAb")
        self.buttonVonBoxAb.setMinimumSize(QSize(51, 25))

        self.gridLayout_3.addWidget(self.buttonVonBoxAb, 1, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(141, 51))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_con = QLabel(self.groupBox)
        self.label_con.setObjectName(u"label_con")

        self.gridLayout_4.addWidget(self.label_con, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 438, 24))
        self.menu_Menue = QMenu(self.menubar)
        self.menu_Menue.setObjectName(u"menu_Menue")
        self.menu_Menue.setTitle(u"&Datenbank")
        self.menu_Neu = QMenu(self.menu_Menue)
        self.menu_Neu.setObjectName(u"menu_Neu")
        self.menu_Editor = QMenu(self.menubar)
        self.menu_Editor.setObjectName(u"menu_Editor")
        self.menu_Editor.setTitle(u"&Editor")
        self.menu_Ueber = QMenu(self.menubar)
        self.menu_Ueber.setObjectName(u"menu_Ueber")
        self.menuOptionen = QMenu(self.menubar)
        self.menuOptionen.setObjectName(u"menuOptionen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.spinbox, self.buttonUke10)
        QWidget.setTabOrder(self.buttonUke10, self.buttonUke0)
        QWidget.setTabOrder(self.buttonUke0, self.buttonNas50)
        QWidget.setTabOrder(self.buttonNas50, self.buttonNas40)
        QWidget.setTabOrder(self.buttonNas40, self.buttonNas30)
        QWidget.setTabOrder(self.buttonNas30, self.buttonNas20)
        QWidget.setTabOrder(self.buttonNas20, self.buttonAal50)
        QWidget.setTabOrder(self.buttonAal50, self.buttonAal40)
        QWidget.setTabOrder(self.buttonAal40, self.buttonBab60)
        QWidget.setTabOrder(self.buttonBab60, self.buttonBab50)
        QWidget.setTabOrder(self.buttonBab50, self.buttonBab40)
        QWidget.setTabOrder(self.buttonBab40, self.buttonBab30)
        QWidget.setTabOrder(self.buttonBab30, self.buttonBra60)
        QWidget.setTabOrder(self.buttonBra60, self.buttonBra50)
        QWidget.setTabOrder(self.buttonBra50, self.buttonBra40)
        QWidget.setTabOrder(self.buttonBra40, self.buttonBra30)
        QWidget.setTabOrder(self.buttonBra30, self.buttonMee70)
        QWidget.setTabOrder(self.buttonMee70, self.buttonMee60)
        QWidget.setTabOrder(self.buttonMee60, self.buttonMee50)
        QWidget.setTabOrder(self.buttonMee50, self.buttonMai50)
        QWidget.setTabOrder(self.buttonMai50, self.buttonMen90)
        QWidget.setTabOrder(self.buttonMen90, self.buttonMen80)
        QWidget.setTabOrder(self.buttonMen80, self.buttonMen70)
        QWidget.setTabOrder(self.buttonMen70, self.edit_bem)
        QWidget.setTabOrder(self.edit_bem, self.rbtn_blau)
        QWidget.setTabOrder(self.rbtn_blau, self.rbtn_rot)
        QWidget.setTabOrder(self.rbtn_rot, self.rbtn_gruen)
        QWidget.setTabOrder(self.rbtn_gruen, self.rbtn_def)
        QWidget.setTabOrder(self.rbtn_def, self.buttonAufstieg)
        QWidget.setTabOrder(self.buttonAufstieg, self.buttonAbstieg)
        QWidget.setTabOrder(self.buttonAbstieg, self.buttonKvogno)
        QWidget.setTabOrder(self.buttonKvogno, self.buttonUnklar)

        self.menubar.addAction(self.menu_Menue.menuAction())
        self.menubar.addAction(self.menu_Editor.menuAction())
        self.menubar.addAction(self.menuOptionen.menuAction())
        self.menubar.addAction(self.menu_Ueber.menuAction())
        self.menu_Menue.addAction(self.menu_Neu.menuAction())
        self.menu_Menue.addAction(self.action_Laden)
        self.menu_Menue.addSeparator()
        self.menu_Menue.addAction(self.action_Zuletzt_verwendet)
        self.menu_Menue.addSeparator()
        self.menu_Menue.addAction(self.action_Schliessen)
        self.menu_Neu.addAction(self.actionServer_DB)
        self.menu_Neu.addAction(self.actionSub_DB)
        self.menu_Editor.addAction(self.action_Oeffnen)
        self.menuOptionen.addAction(self.actionManuelleEingabe)
        self.menuOptionen.addAction(self.actionTruebungTurbulenz)
        self.menuOptionen.addAction(self.actionBodenplatteButtons)

        self.retranslateUi(MainWindow)

        self.buttonUncheckAllFishButtons.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fisdet", None))
        self.action_Laden.setText(QCoreApplication.translate("MainWindow", u"&Laden", None))
#if QT_CONFIG(statustip)
        self.action_Laden.setStatusTip(QCoreApplication.translate("MainWindow", u"Datenbank laden.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Laden.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionAnzeigen.setText(QCoreApplication.translate("MainWindow", u"&Anzeigen", None))
        self.actionAls_Excel_exportieren.setText(QCoreApplication.translate("MainWindow", u"als Excel exportieren", None))
        self.action_Oeffnen.setText(QCoreApplication.translate("MainWindow", u"&\u00d6ffnen", None))
#if QT_CONFIG(statustip)
        self.action_Oeffnen.setStatusTip(QCoreApplication.translate("MainWindow", u"Editor \u00f6ffnen.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Oeffnen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_Zuletzt_verwendet.setText(QCoreApplication.translate("MainWindow", u"Zuletzt &verwendet", None))
        self.action_Schliessen.setText(QCoreApplication.translate("MainWindow", u"&Schlie\u00dfen", None))
#if QT_CONFIG(statustip)
        self.action_Schliessen.setStatusTip(QCoreApplication.translate("MainWindow", u"Programm schlie\u00dfen.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Schliessen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionServer_DB.setText(QCoreApplication.translate("MainWindow", u"server-DB", None))
#if QT_CONFIG(tooltip)
        self.actionServer_DB.setToolTip(QCoreApplication.translate("MainWindow", u"Erstellt eine neue Server-Datenbank. (Administratoren vorbehalten)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionServer_DB.setStatusTip(QCoreApplication.translate("MainWindow", u"Erstellt eine neue Server-Datenbank. (Administratoren vorbehalten)", None))
#endif // QT_CONFIG(statustip)
        self.actionSub_DB.setText(QCoreApplication.translate("MainWindow", u"sub-DB", None))
#if QT_CONFIG(tooltip)
        self.actionSub_DB.setToolTip(QCoreApplication.translate("MainWindow", u"Erstellt eine neue Unterdatenbank.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionSub_DB.setStatusTip(QCoreApplication.translate("MainWindow", u"Erstellt eine neue Unterdatenbank.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSub_DB.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionManuelleEingabe.setText(QCoreApplication.translate("MainWindow", u"Manuelle Eingabe", None))
        self.actionTruebungTurbulenz.setText(QCoreApplication.translate("MainWindow", u"Tr\u00fcbung/Turbulenz", None))
        self.actionBodenplatteButtons.setText(QCoreApplication.translate("MainWindow", u"Bodenplatte", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Multiplikator", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Protokollant", None))
        self.groupBoxArtLaenge.setTitle(QCoreApplication.translate("MainWindow", u"Art und Laenge", None))
        self.buttonBab10.setText(QCoreApplication.translate("MainWindow", u"BAB 10", None))
        self.buttonRot20.setText(QCoreApplication.translate("MainWindow", u"ROT 20", None))
        self.buttonRot10.setText(QCoreApplication.translate("MainWindow", u"ROT 10", None))
        self.buttonLac60.setText(QCoreApplication.translate("MainWindow", u"LAC 60", None))
        self.buttonLac50.setText(QCoreApplication.translate("MainWindow", u"LAC 50", None))
        self.buttonRot30.setText(QCoreApplication.translate("MainWindow", u"ROT 30", None))
        self.buttonAal30.setText(QCoreApplication.translate("MainWindow", u"AAL 30", None))
        self.buttonMai40.setText(QCoreApplication.translate("MainWindow", u"MAI 40", None))
        self.buttonLac80.setText(QCoreApplication.translate("MainWindow", u"LAC 80", None))
        self.buttonRot0.setText(QCoreApplication.translate("MainWindow", u"ROT 0", None))
        self.buttonNas40.setText(QCoreApplication.translate("MainWindow", u"NAS 40", None))
        self.buttonAal40.setText(QCoreApplication.translate("MainWindow", u"AAL 40", None))
        self.buttonBab50.setText(QCoreApplication.translate("MainWindow", u"BAB 50", None))
        self.buttonBra50.setText(QCoreApplication.translate("MainWindow", u"BRA 50", None))
        self.buttonBra30.setText(QCoreApplication.translate("MainWindow", u"BRA 30", None))
        self.buttonMen90.setText(QCoreApplication.translate("MainWindow", u"MEN 90", None))
        self.buttonMai50.setText(QCoreApplication.translate("MainWindow", u"MAI 50", None))
        self.buttonBra60.setText(QCoreApplication.translate("MainWindow", u"BRA 60", None))
        self.buttonAal50.setText(QCoreApplication.translate("MainWindow", u"AAL 50", None))
        self.buttonNas30.setText(QCoreApplication.translate("MainWindow", u"NAS 30", None))
        self.buttonMee70.setText(QCoreApplication.translate("MainWindow", u"MEE 70", None))
        self.buttonBab40.setText(QCoreApplication.translate("MainWindow", u"BAB 40", None))
        self.buttonBra40.setText(QCoreApplication.translate("MainWindow", u"BRA 40", None))
        self.buttonNas50.setText(QCoreApplication.translate("MainWindow", u"NAS 50", None))
        self.buttonUke10.setText(QCoreApplication.translate("MainWindow", u"UKE 10", None))
        self.buttonMee50.setText(QCoreApplication.translate("MainWindow", u"MEE 50", None))
        self.buttonMen70.setText(QCoreApplication.translate("MainWindow", u"MEN 70", None))
        self.buttonMen80.setText(QCoreApplication.translate("MainWindow", u"MEN 80", None))
        self.buttonNas20.setText(QCoreApplication.translate("MainWindow", u"NAS 20", None))
        self.buttonBab60.setText(QCoreApplication.translate("MainWindow", u"BAB 60", None))
        self.buttonBab30.setText(QCoreApplication.translate("MainWindow", u"BAB 30", None))
        self.buttonUke0.setText(QCoreApplication.translate("MainWindow", u"UKE 0", None))
        self.buttonMee60.setText(QCoreApplication.translate("MainWindow", u"MEE 60", None))
        self.buttonBab20.setText(QCoreApplication.translate("MainWindow", u"BAB 20", None))
        self.buttonAal20.setText(QCoreApplication.translate("MainWindow", u"AAL 20", None))
        self.buttonLac70.setText(QCoreApplication.translate("MainWindow", u"LAC 70", None))
        self.buttonUk10.setText(QCoreApplication.translate("MainWindow", u"uK 10", None))
        self.buttonUk0.setText(QCoreApplication.translate("MainWindow", u"uK 0", None))
        self.buttonUncheckAllFishButtons.setText(QCoreApplication.translate("MainWindow", u"uncheck", None))
        self.groupBoxManuell.setTitle(QCoreApplication.translate("MainWindow", u"manuelle Eingabe:", None))
        self.label_art.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"left\">Art:</p></body></html>", None))
        self.label_laenge.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">L\u00e4nge:</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Text und Farbe der Bemerkung", None))
#if QT_CONFIG(tooltip)
        self.check_bem.setToolTip(QCoreApplication.translate("MainWindow", u"Bemerkung und Farbe f\u00fcr weitere Eingaben fixieren. ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.check_bem.setStatusTip(QCoreApplication.translate("MainWindow", u"Bemerkung und Farbe f\u00fcr weitere Eingaben fixieren. ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.check_bem.setWhatsThis(QCoreApplication.translate("MainWindow", u"Bemerkung stehen lassen.", None))
#endif // QT_CONFIG(whatsthis)
        self.check_bem.setText(QCoreApplication.translate("MainWindow", u"fix", None))
        self.rbtn_blau.setText("")
        self.rbtn_rot.setText("")
        self.rbtn_gruen.setText("")
        self.rbtn_gelb.setText("")
        self.rbtn_pink.setText("")
        self.rbtn_def.setText(QCoreApplication.translate("MainWindow", u"default", None))
        self.groupBoxTruebungTurbulenz.setTitle(QCoreApplication.translate("MainWindow", u"Tr\u00fcbung / Turbulenz", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Verhalten", None))
        self.buttonAufstieg.setText(QCoreApplication.translate("MainWindow", u"auf", None))
        self.buttonAbstieg.setText(QCoreApplication.translate("MainWindow", u"ab", None))
        self.buttonKvogno.setText(QCoreApplication.translate("MainWindow", u"kvogno", None))
        self.buttonUnklar.setText(QCoreApplication.translate("MainWindow", u"unklar", None))
        self.buttonKvugnu.setText(QCoreApplication.translate("MainWindow", u"kvugnu", None))
        self.buttonVonUntenInBox.setText(QCoreApplication.translate("MainWindow", u"vuiBox", None))
        self.buttonVonObenInBox.setText(QCoreApplication.translate("MainWindow", u"voiBox", None))
        self.buttonVonBoxInBox.setText(QCoreApplication.translate("MainWindow", u"BiB", None))
        self.buttonVonBoxAuf.setText(QCoreApplication.translate("MainWindow", u"Boxauf", None))
        self.buttonVonBoxAb.setText(QCoreApplication.translate("MainWindow", u"Boxab", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Zusammenfassung", None))
        self.label_con.setText("")
        self.menu_Neu.setTitle(QCoreApplication.translate("MainWindow", u"&Neu", None))
        self.menu_Ueber.setTitle(QCoreApplication.translate("MainWindow", u"\u00dc&ber", None))
        self.menuOptionen.setTitle(QCoreApplication.translate("MainWindow", u"Ansicht", None))
    # retranslateUi

