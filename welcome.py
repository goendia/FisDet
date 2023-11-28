# -*- coding: utf-8 -*-

import sys
import xlwt
# import win32gui
import re
from PySide6 import QtCore, QtGui, QtSql

from PySide6.QtCore import Qt
from PySide6.QtGui import QMainWindow, qApp, QMessageBox, QApplication, QColor, QFileDialog
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

# import the class for the export dialog
from exportdialog import ExportDialog

from ui_welcome import Ui_Welcome

#from mainwindow import MyWindow


class Welcome(QtGui.QMainWindow, Ui_Welcome):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.dialog = QtGui.QDialog(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.createDb.clicked.connect(self.createNewDatabase)
        self.findDb.clicked.connect(self.openDatabase)

        # this will activate the window
        self.activateWindow()

    def createNewDatabase(self):
        # Inherit createNewDatabase function from MyWindow class
        super(Welcome, self).createNewDatabase()
        #MyWindow.createNewDatabase()

    def openDatabase(self):
        # Inherit openDatabase function from MyWindow class
        super(Welcome, self).openDatabase()
        #MyWindow.openDatabase()

    def accept(self):
        print("STOP")

    def reject(self):
        print('jshdkhd')

