# -*- coding: utf-8 -*-

import sys
import xlwt
# import win32gui
import re
from PySide6 import QtCore, QtGui, QtSql

from PySide6.QtCore import Qt
from PySide6.QtGui import QMainWindow, qApp, QMessageBox, QApplication, QColor, QFileDialog
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

from ui_sqlabfrage import Ui_Dialog
from PySide6.QtCore import QSettings

ID, NAME, DATUM, ART, LAENGE, VERHALTEN, BEMERKUNG, ANTWORT, TRUEBUNG, TURBULENZ, FARBE, LOG, ID_SERVER = range(13)
ID, DB_TYPE, BUILD_DATE = range(3)
verhaltenDictionary = {"kvogno":"00-1", "ab":"-100", "unklar":"010", "auf":"100", "kvugnu":"001",
                        "vuiBox": "002", "voiBox":"00-2", "BiB":"020", "Boxauf":"200", "Boxab":"-200"}


class ExportDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, databaseType, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        # Get database type from Editor class (Editor class gets the variable from MainWindow class)
        self.databaseType = databaseType

        self.export_model = QtSql.QSqlTableModel(self)
        print("ExportDialog.__init__(): DB-Type = "+str(self.databaseType))
        #self.export_model.setQuery(QtSql.QSqlQuery('SELECT sub_id, name, datum, art, laenge, verhalten, bem, ant FROM fische WHERE ant IS NOT NULL'))

        ############### besser wäre WHERE ant IS NOT NULL"", bitte implementieren!!!!!!!!!!!??????????
        if self.databaseType == "sub":
            self.export_model.setQuery(QtSql.QSqlQuery("SELECT sub_id, name, datum, art, laenge, verhalten, bem, ant, farbebem, log FROM fische WHERE ant IS NOT NULL"))
            print("ExportDialog.__init__(): Anwort-Query für Sub-DB ausgeführt.")
        elif self.databaseType == "server":
            self.export_model.setQuery(QtSql.QSqlQuery("SELECT sub_id, name, datum, art, laenge, verhalten, bem, ant, farbebem, log, server_id  FROM fische WHERE ant IS NOT NULL"))
            print("ExportDialog.__init__(): Anwort-Query für Server-DB ausgeführt.")
        else:
            print("Konnte Antwort-Query nicht ausführen!")

        self.export_model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.export_model.select()
        self.export_model.setHeaderData(ID, QtCore.Qt.Horizontal, "Sub-ID")
        self.export_model.setHeaderData(NAME, QtCore.Qt.Horizontal, "Name")
        self.export_model.setHeaderData(DATUM, QtCore.Qt.Horizontal, "Datum (Video)")
        self.export_model.setHeaderData(ART, QtCore.Qt.Horizontal, "Art")
        self.export_model.setHeaderData(LAENGE, QtCore.Qt.Horizontal, u"Länge")
        self.export_model.setHeaderData(VERHALTEN, QtCore.Qt.Horizontal, "Verhalten")
        self.export_model.setHeaderData(BEMERKUNG, QtCore.Qt.Horizontal, "Bemerkung")
        self.export_model.setHeaderData(ANTWORT, QtCore.Qt.Horizontal, "Antwort")
        self.export_model.setHeaderData(FARBE, QtCore.Qt.Horizontal, "Farbe")
        self.export_model.setHeaderData(LOG, QtCore.Qt.Horizontal, "Log")
        if self.databaseType == "server":
            self.export_model.setHeaderData(ID_SERVER, QtCore.Qt.Horizontal, "ID_Server")

        self.tableView.setModel(self.export_model)
        self.tableView.resizeColumnsToContents()

        self.exportButton.clicked.connect(self.xls_export)

    def xls_export(self):
        # warum bei qfiledialog eigentlich standard in unicode()?
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Speichern unter...', '', ".xls(*.xls)")[0]

        # Prüft, ob .xls-Endung vorhanden, wenn nicht, dann wird .xls hinzugefügt
        if filename:
            if "." not in filename:
                filename += ".xls"
        else:
            return

        wbk = xlwt.Workbook()
        self.sheet = wbk.add_sheet("EXPORT", cell_overwrite_ok=True)
        self.add()
        wbk.save(filename)

    def add(self):
        row = 1
        col = 0
        self.sheet.write(0, ID, "Sub-ID")
        self.sheet.write(0, NAME, "Name")
        self.sheet.write(0, DATUM, "Datum (Video)")
        self.sheet.write(0, ART, "Art")
        self.sheet.write(0, LAENGE, u"Länge")
        self.sheet.write(0, VERHALTEN, "Verhalten")
        self.sheet.write(0, BEMERKUNG, "Bemerkung")
        self.sheet.write(0, ANTWORT, "Antwort")
        self.sheet.write(0, FARBE, "Farbe")
        self.sheet.write(0, LOG, "Log")
        if self.databaseType == "server":
            self.sheet.write(0, ID_SERVER, "ID_Server")

        # Druckt Spalten - und Zeilenzahl
        print("ExportDialog.add(): Spaltenanzahl = "+str(self.export_model.columnCount()))
        print("ExportDialog.add(): Zeilenanzahl = "+str(self.export_model.rowCount()))

        for i in xrange(0, self.export_model.columnCount()):
            for x in xrange(0, self.export_model.rowCount()):
                try:
                    text = str(self.export_model.data(self.export_model.index(x, i)))
                    self.sheet.write(row, col, text)
                    row += 1
                except AttributeError:
                    row += 1
            row = 1
            col += 1

