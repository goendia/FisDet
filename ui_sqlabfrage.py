# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqlabfrage.ui'
#
# Created: Wed Oct 15 10:27:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 416)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.exportButton = QtGui.QPushButton(Dialog)
        self.exportButton.setObjectName("exportButton")
        self.verticalLayout.addWidget(self.exportButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "SQL-Abfrage", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("Dialog", "Als Excel-Datei speichern", None, QtGui.QApplication.UnicodeUTF8))

