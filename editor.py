# -*- coding: utf-8 -*-

import sys
import xlwt
import win32gui
import re
from PySide import QtCore, QtGui, QtSql

from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow, qApp, QMessageBox, QApplication, QColor, QFileDialog
from PySide.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

# import the class for the export dialog
from exportdialog import ExportDialog

from delegate import Delegate

from ui_editor import Ui_Editor
from ui_sqlabfrage import Ui_Dialog
from PySide.QtCore import QSettings

ID, NAME, DATUM, ART, LAENGE, VERHALTEN, BEMERKUNG, ANTWORT, TRUEBUNG, TURBULENZ, FARBE, LOG, ID_SERVER = range(13)
ID, DB_TYPE, BUILD_DATE = range(3)
verhaltenDictionary = {"kvogno":"00-1", "ab":"-100", "unklar":"010", "auf":"100", "kvugnu":"001",
                        "vuiBox": "002", "voiBox":"00-2", "BiB":"020", "Boxauf":"200", "Boxab":"-200"}

class Editor(QtGui.QMainWindow, Ui_Editor):

    # Define signal for insertRow method (where it is called), it is connected in __init__ method and scrolls the tableView automatically down
    signalRowInserted = QtCore.Signal()

    def __init__(self, model, databaseType, databasePath, nameOfProtokollant, parent=None):
        QtGui.QMainWindow.__init__(self, parent)#, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)

        # Get the model variable from MyWindow class and select it in this instance
        self.model = model
        self.model.select()
        # for testing change the edit strategy of model to auto mode when opening the editor
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

        # Get database type from MyWindow class
        self.databaseType = databaseType
        # Get database path from MyWindow class
        self.databasePath = databasePath
        # Get name of Protokollant from MyWindow class
        self.nameOfProtokollant = nameOfProtokollant

        # Define variable for saving state if new row was inserted, for the checking before submit,
        # so that the user has to complete the last row he/she has manually entered
        self.newRowInserted = False

        self.setWindowTitle(QtGui.QApplication.translate("Editor", "Editor - "+str(self.databasePath), None, QtGui.QApplication.UnicodeUTF8))

        self.tableView.setModel(self.model)

        # Deliver the model to the delegate, so changes in the model while manual editing is possible
        self.tableView.setItemDelegate(Delegate(self.model))
        # versteckt id_pk-Spalte
        #self.tableView.setColumnHidden(ID, True)
        # versteckt log-Spalte
        #self.tableView.setColumnHidden(LOG, True)
        # Resize columns of view to its contents !!!!! takes to much time when opening Editor with big database
        #self.tableView.resizeColumnsToContents()

        # Connect signal that is emited while calling insertRow method to automatically scroll down the tableView
        self.signalRowInserted.connect(lambda: self.tableView.scrollToBottom())

        # this will remove minimized status
        # and restore window with keeping maximized/normal state
        self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)

        ####### Menü
        self.action_xls.triggered.connect(self.xls_export)
        self.actionAntworten_exportieren.triggered.connect(self.openExportDialog)
        self.action_Importieren.triggered.connect(self.insertDatabase)

        ### Ansicht --> Sql Query elements
        self.actionSqlQuery.triggered.connect(lambda: self.showHideSqlQuerySection(self.actionSqlQuery.isChecked()))
        # Hide Sql query elements at start, because at initialization the "Ansicht" menu entry is unchecked
        self.queryTextEdit.hide()
        self.stqrtQueryButton.hide()

        # Verbindung von Toolbarbutton Anwenden mit submit-Funktion
        self.action_anwenden.triggered.connect(self.submit)

        # Verbindung von Toolbarbutton Undo mit revertAll-Funktion
        self.action_zurueck.triggered.connect(self.model.revertAll)

        # Verbindung von Toolbarbutton "Plus" mit dem Einfügen einer neuen Zeile
        self.action_newline.triggered.connect(self.insertRow)

        # Verbindung von Toolbarbutton "X" mit Löschen einer Zeile
        self.action_loeschen.triggered.connect(lambda: self.model.removeRow(QtCore.QModelIndex.row(self.tableView.selectedIndexes()[0])))

        # Connection with toolbarbutton "SQL QUERY" for query db and displaying results
        self.stqrtQueryButton.clicked.connect(lambda: self.sqlExec(self.queryTextEdit.text()))

        # scroll table to bottom at initialization
        self.tableView.scrollToBottom()
        #wait for that 10ms for initialization of other things
        #QtCore.QTimer.singleShot(10, self.tableView.scrollToBottom)


    def showHideSqlQuerySection(self, isChecked):
        '''
        Shows or Hide the Sql Query elements.
        :param isChecked:
        :return:
        '''
        if isChecked:
            self.queryTextEdit.show()
            self.stqrtQueryButton.show()
        else:
            self.queryTextEdit.hide()
            self.stqrtQueryButton.hide()


    def sqlExec(self, query):

        # query results
        qQuery = QSqlQuery(str(query))
        if not self.model.setQuery(qQuery):
            # TODO: Better error handling popup?
            print 'Invalid Query:  ' + query
        else:
            self.tableView.setModel(self.model)

        # set table header lables
        for i in range(0, self.model.columnCount()):
            lable = self.model.headerData(i, QtCore.Qt.Horizontal)
            self.model.setHeaderData(i, QtCore.Qt.Horizontal, lable)

       # Set the header data for the model columns by hand, will be seen in tableView.
       # self.model.setHeaderData(ID, QtCore.Qt.Horizontal, "Sub-ID")
       # self.model.setHeaderData(NAME, QtCore.Qt.Horizontal, "Name")
       # self.model.setHeaderData(DATUM, QtCore.Qt.Horizontal, "Datum (Video)")
       # self.model.setHeaderData(ART, QtCore.Qt.Horizontal, "Art")
       # self.model.setHeaderData(LAENGE, QtCore.Qt.Horizontal, u"Länge")
       # self.model.setHeaderData(VERHALTEN, QtCore.Qt.Horizontal, "Verhalten")
       # self.model.setHeaderData(BEMERKUNG, QtCore.Qt.Horizontal, "Bemerkung")
       # self.model.setHeaderData(ANTWORT, QtCore.Qt.Horizontal, "Antwort")
       # self.model.setHeaderData(TRUEBUNG, QtCore.Qt.Horizontal, u"Trübung")
       # self.model.setHeaderData(TURBULENZ, QtCore.Qt.Horizontal, "Turbulenz")
       # self.model.setHeaderData(FARBE, QtCore.Qt.Horizontal, "Farbe Bemerkung")
       # self.model.setHeaderData(LOG, QtCore.Qt.Horizontal, "Log")
        # Only set header data when its necessary, in this case when db_type = server...
        if self.databaseType == "server":
            self.model.setHeaderData(ID_SERVER, QtCore.Qt.Horizontal, "Server-ID")

        # load data beforehand, so the tableView is opening quicker and the data is already loaded (think of scrolling down inside the tableView).
        #print("self.model.canfetchmore: "+str(self.model.canFetchMore()))
        # Qt's SQLite driver inserts rows into the model in steps of 256 rows
       # x = 0

       # while self.model.canFetchMore():
        #    self.model.fetchMore()
         #   x += 1
       # print 'Model reinitialization that shouldnt happen after Editor was called!!!'


    def openExportDialog(self):
        '''
        Open a dialog for database export.
        '''

        # Create instance of ExportDialog class and give the database type to the created instance
        self.exportDialog = ExportDialog(self.databaseType)
        self.exportDialog.show()


    def insertRow(self):
        # TODO: After inserting a new row and also deleting that row, then inserting a new row, it shows an error
        if self.newRowInserted == True:
            QtGui.QMessageBox.warning(self, "Fisdet",
                                      u"Sie haben die letzte manuell eingefügte Zeile noch nicht vervollständigt."
                                      u"Bitte tun Sie das bevor sie neue Zeilen hinzufügen.")
            return False
        row = self.model.rowCount()
        self.model.insertRows(row, 1)
        # TODO: Whats with sub databases? IDs should
        if self.databaseType == "server":
            if row == 0:
                self.model.setData(self.model.index(row, ID), 1)
            else:
                lastid = self.model.data(self.model.index(row-1, ID))
                self.model.setData(self.model.index(row, ID), int(lastid)+1)

        self.model.setData(self.model.index(row, NAME), self.nameOfProtokollant)
        # Set current time automatically for the Log column of manually inserted row
        self.model.setData(self.model.index(row, LOG), QtCore.QDateTime.currentDateTime())

        # Variable für Änderungen-Speichern dialog
        self.model.dirty = True
        # if new row inserted --> variable = True
        self.newRowInserted = True
        # Emit signal for scrolling down the tableview
        self.signalRowInserted.emit()


    def xls_export(self):
        # warum bei qfiledialog eigentlich standard in unicode()?
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Speichern unter...', '', ".xls(*.xls)")[0]

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
        print("Editor.add(): Spaltenanzahl = "+str(self.model.columnCount()))
        print("Editor.add(): Zeilenanzahl = "+str(self.model.rowCount()))

        for i in xrange(0, self.model.columnCount()):
            for x in xrange(0, self.model.rowCount()):
                try:
                    text = str(self.model.data(self.model.index(x, i)))
                    self.sheet.write(row, col, text)
                    row += 1
                except AttributeError:
                    row += 1
            row = 1
            col += 1


    def submit(self):

        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
            # set newRowInserted variable False, because row is submitted
            self.newRowInserted = False
            self.model.dirty = False
        else:
            self.model.database().rollback()
            print self.model.lastError().text()
            if self.model.lastError().text().find("NOT NULL") != -1:
                QtGui.QMessageBox.warning(self, "Fisdet",
                                      u"Einer der vorhergehenden Einträge ist unvollständig! Bitte überprüfen und vervollständigen.")
                return "NULL"
            else:
                QtGui.QMessageBox.warning(self, "Fisdet",
                                      "Die Datenbank meldet folgenden Fehler: %s" % self.model.lastError().text())
                return "ERROR"


    def insertDatabase(self):
        '''
        Inserts database to existing database.
        '''

        # Get path of import database
        dname = QtGui.QFileDialog.getOpenFileName(self, u'Öffne Datenbank', '', "*.db")[0]
        print dname

        # Return if Open-Dialog was canceled and no database was loaded. To prevent function on running...
        if "." not in dname:
            return

        query = QtSql.QSqlQuery()

        # Attach import database to default database
        if query.exec_("ATTACH '%s' AS remote;" %dname): print("Editor.insertDatabase(): DATABASE ATTACHED")

        # Get database type of import database
        query.exec_("SELECT db_type FROM remote.info")
        while query.next():
            dbtype = query.value(0)
        print("Editor.insertDatabase(): Import-DB-Type = "+str(dbtype))

        # Only show database name, NOT the full path
        if dname[0] == "/":
            dname = dname[(dname.rfind("/"))+1:]

        # Only show database name, NOT the full path
        if self.databasePath[0] == "/":
            self.databasePath = self.databasePath[(self.databasePath.rfind("/"))+1:]

        # Show information about import process
        if QtGui.QMessageBox.question(self, "Hinweis", "Geladen:\n#############\n%s, Typ: %s, Eintraege: %i \n\n Hinzufuegen:\n##############\n%s, Typ: %s" %(self.databasePath, self.databaseType, self.model.rowCount(), dname, dbtype),
                                          QtGui.QMessageBox.Yes|QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
            return

        # Start a progress dialog
        progress = QtGui.QProgressDialog("Importiert...", "Abbrechen", 0, 0, None)
        progress.setMinimumDuration(0)
        progress.setWindowTitle("Datenbankimport")
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.show()
        progress.setValue(0)

        # if default database == sub, import content without sub_id
        if self.databaseType == "sub":
            #progress.setValue(0)
            if query.exec_("INSERT INTO fische(name, datum, art, laenge, verhalten, bem, ant, farbebem, log) SELECT name, datum, art, laenge, verhalten, bem, ant, farbebem, log FROM remote.fische;"): print("Editor.insertDatabase(): DATABASE INSERTED")
            if query.exec_("DETACH DATABASE remote;"): print("Editor.insertDatabase(): DATABASE DETACHED")
            #progress.setValue(5)
            self.submit()
            #progress.setValue(10)

            # Testcase
            # test_time = 10
            # while self.model.canFetchMore():
            # progress.setValue(1)
            # self.model.fetchMore()
            #test_time += 1
            #print str(test_time)+": always fetching..."
            '''
            if test_time == 100:
            progress.close()
            break
            '''

            #progress.setValue(10)
            progress.close()
        # if default database == server, import content without server_id
        elif self.databaseType == "server":
            if query.exec_("INSERT INTO fische(sub_id, name, datum, art, laenge, verhalten, bem, ant, farbebem, log) SELECT sub_id, name, datum, art, laenge, verhalten, bem, ant, farbebem, log FROM remote.fische;"): print("Editor.insertDatabase(): DATABASE INSERTED")
            if query.exec_("DETACH DATABASE remote;"): print("Editor.insertDatabase(): DATABASE DETACHED")
            self.submit()
        # if there is no default database type --> ERROR
        else:
            print("Editor.insertDatabase(): Fehler beim Datenbankimport!")
            return False


    def progress(self):
        self.pb = QtGui.QProgressBar(self.centralwidget)
        self.pb.setGeometry(QtCore.QRect(20, 20, 301, 31))
        #self.pb.setProperty("value", 0)
        #self.pb.setObjectName(_fromUtf8("pb"))
        self.pb.setRange(0,0)
        self.insertDatabase()


    def closeEvent(self, event):
        '''
        Überschreibt closeEvent-Funktion des Editor-Fensters. Prüft ob nichtgespeicherte Änderungen vorhanden sind.
        '''

        if self.model.dirty == True:
            if QtGui.QMessageBox.warning(self, "Änderungen speichern?", u"Möchten Sie die Änderungen speichern?",
                                      QtGui.QMessageBox.Yes|QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
                #odel.database().transaction()
                self.model.database().rollback()
                return
            else:
                self.submit()
                self.model.dirty = False
                return

        # Save frame size and position in registry for next start of application
        # TODO: Save the frame size and position of editor at closing the editor
        #MyWindow().settings.setValue('editorPosAndSize', [self.x(), self.y(),self.width(), self.height()])

        # close exportDialog if open
        if hasattr(self, 'exportDialog'): self.editorDialog.close()