# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QDialog

# import the class for the export dialog
from exportdialog import ExportDialog
from ui_welcome import Ui_Welcome

#from mainwindow import MyWindow


class Welcome(QMainWindow, Ui_Welcome):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent, Qt.WindowStaysOnTopHint)
        self.dialog = QDialog(parent)
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

