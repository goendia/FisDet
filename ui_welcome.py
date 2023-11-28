# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Manuel\Documents\Fischprojekt\STRUKTURIERT\welcome.ui'
#
# Created: Thu Jan 29 15:39:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore, QtGui

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(316, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Welcome)
        self.buttonBox.setGeometry(QtCore.QRect(220, 220, 81, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_7 = QtGui.QGroupBox(Welcome)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 191, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QtCore.QSize(90, 0))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editProtokollant_2 = QtGui.QLineEdit(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editProtokollant_2.sizePolicy().hasHeightForWidth())
        self.editProtokollant_2.setSizePolicy(sizePolicy)
        self.editProtokollant_2.setMinimumSize(QtCore.QSize(10, 0))
        self.editProtokollant_2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.editProtokollant_2.setBaseSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(14)
        self.editProtokollant_2.setFont(font)
        self.editProtokollant_2.setMaxLength(100)
        self.editProtokollant_2.setObjectName("editProtokollant_2")
        self.verticalLayout_2.addWidget(self.editProtokollant_2)
        self.listWidget = QtGui.QListWidget(Welcome)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 191, 192))
        self.listWidget.setObjectName("listWidget")
        self.findDb = QtGui.QPushButton(Welcome)
        self.findDb.setGeometry(QtCore.QRect(220, 100, 81, 23))
        self.findDb.setObjectName("findDb")
        self.createDb = QtGui.QPushButton(Welcome)
        self.createDb.setGeometry(QtCore.QRect(220, 130, 81, 23))
        self.createDb.setObjectName("createDb")

        self.retranslateUi(Welcome)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Welcome.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Welcome.reject)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QtGui.QApplication.translate("Welcome", "Willkommen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Welcome", "Protokollant", None, QtGui.QApplication.UnicodeUTF8))
        self.findDb.setText(QtGui.QApplication.translate("Welcome", "find db", None, QtGui.QApplication.UnicodeUTF8))
        self.createDb.setText(QtGui.QApplication.translate("Welcome", "create db", None, QtGui.QApplication.UnicodeUTF8))

