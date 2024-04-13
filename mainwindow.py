# -*- coding: utf-8 -*-
'''
Created on Fri Jun 20 15:10:08 2014
@author: chris
'''

import sys
from PySide6 import QtCore, QtGui, QtSql

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QApplication, QFileDialog)
from PySide6.QtSql import QSqlTableModel

from editor import Editor
from welcome import Welcome

from model import Model
from already_running import QSingleApplication
from ui_mainwindow import Ui_MainWindow

ID, NAME, DATUM, ART, LAENGE, VERHALTEN, BEMERKUNG, ANTWORT, TRUEBUNG, TURBULENZ, FARBE, LOG, ID_SERVER = range(13)
ID, DB_TYPE, BUILD_DATE = range(3)
verhaltenDictionary = {"kvogno":"00-1", "ab":"-100", "unklar":"010", "auf":"100", "kvugnu":"001",
                        "vuiBox": "002", "voiBox":"00-2", "BiB":"020", "Boxauf":"200", "Boxab":"-200"}

class MyWindow(QMainWindow, Ui_MainWindow):

    # Signal for auto scrolling down the tableView after insertion of data
    signalDatabaseSubmit = QtCore.Signal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        # align application on screen left/top full height
        self.move(0,0)
        # self.resize(self.width(), app.desktop().availableGeometry().height())
        
        ################ defintion  of variables (self.name_log, TODO: self.videodatum is missing)
        self.databaseType = None
        # Saves the connection status
        self.connectionToDatabase = None
        self.databasePath = None
        self.fischart = None
        self.fischlaenge = None
        self.bemerkung = None
        self.farbe = "black"
        # Multiplicator for entering the same entry more times
        self.multi = self.spinbox.value()
        self.verhalten = None
        self.arten = ["s. Bemerkung",
                      "Aland",
                      "Bachforelle",
                      "Cypriniden (klein) (e)",
                      "Flussbarsch",
                      "Giebel/Karausche (g)",
                      "Graskarpfen",
                      u"Gründling",
                      "Hasel",
                      "Karpfen",
                      "Neunauge (klein)",
                      "Regenbogenforelle",
                      "Schleie",
                      "unbest. Fisch >10 cm",
                      "Zobel"]
        self.comboBoxSpeciesDictionary = {"s. Bemerkung": "BEM",
                                         "Aland": "ALA",
                                         "Bachforelle": "BAC",
                                         "Cypriniden (klein) (e)": "CYP",
                                         "Flussbarsch": "BAR",
                                         "Giebel/Karausche (g)": "GIE/KRA",
                                         "Graskarpfen": "GRA",
                                         u"Gründling": "GRU",
                                         "Hasel": "HAS",
                                         "Karpfen": "KAR",
                                         "Neunauge (klein)": "kNEU",
                                         "Regenbogenforelle": "REG",
                                         "Schleie": "SCH",
                                         "unbest. Fisch >10 cm": "uF",
                                         "Zobel": "ZOB"}

        self.trueb = [u"keine Trübung", u"leichte Trübung", u"mittlere Trübung", u"starke Trübung"]
        self.dicttrueb = {0: None, 1: "l", 2: "m", 3: "s"}

        self.turb = ["keine Turbulenz", "Blasenschleiher", "Welle"]
        self.dictturb = {0: None, 1: "B", 2: "W"}


        # Ändert Zusammenfassung, wenn sich der Text im Bemerkungsfeld ändert."
        self.edit_bem.textChanged.connect(self.edit_bem_textchange)

        self.spinbox.valueChanged.connect(self.multiChange)

        # Connecting the signal when database submit to slot from editor for auto scroll down the tableView
        # TODO: while submitting sometimes tableView scrolls NOT to the bottom, test it for big databases
        # singleShot is for waiting of updating the tableView and other signals... (waits for 50ms)
        self.signalDatabaseSubmit.connect(lambda: QtCore.QTimer.singleShot(50, self.editor.tableView.scrollToBottom))

        ###### Verbindung zu Fisch-Knöpfen
        # Ukelei (UKE) 10, 0
        self.buttonUke10.clicked.connect(lambda: self.clickFishButton("UKE", "10"))
        self.buttonUke0.clicked.connect(lambda: self.clickFishButton("UKE", "0"))

        # Nase (NAS) 50, 40, 30, 20
        self.buttonNas50.clicked.connect(lambda: self.clickFishButton("NAS", "50"))
        self.buttonNas40.clicked.connect(lambda: self.clickFishButton("NAS", "40"))
        self.buttonNas30.clicked.connect(lambda: self.clickFishButton("NAS", "30"))
        self.buttonNas20.clicked.connect(lambda: self.clickFishButton("NAS", "20"))

        # Aal (AAL) 50, 40, 30, 20
        self.buttonAal50.clicked.connect(lambda: self.clickFishButton("AAL", "50"))
        self.buttonAal40.clicked.connect(lambda: self.clickFishButton("AAL", "40"))
        self.buttonAal30.clicked.connect(lambda: self.clickFishButton("AAL", "30"))
        self.buttonAal20.clicked.connect(lambda: self.clickFishButton("AAL", "20"))

        # Barbe (BAB) 60, 50, 40, 30, 20, 10
        self.buttonBab60.clicked.connect(lambda: self.clickFishButton("BAB", "60"))
        self.buttonBab50.clicked.connect(lambda: self.clickFishButton("BAB", "50"))
        self.buttonBab40.clicked.connect(lambda: self.clickFishButton("BAB", "40"))
        self.buttonBab30.clicked.connect(lambda: self.clickFishButton("BAB", "30"))
        self.buttonBab20.clicked.connect(lambda: self.clickFishButton("BAB", "20"))
        self.buttonBab10.clicked.connect(lambda: self.clickFishButton("BAB", "10"))

        # Brachse (BRA) 60, 50, 40, 30
        self.buttonBra60.clicked.connect(lambda: self.clickFishButton("BRA", "60"))
        self.buttonBra50.clicked.connect(lambda: self.clickFishButton("BRA", "50"))
        self.buttonBra40.clicked.connect(lambda: self.clickFishButton("BRA", "40"))
        self.buttonBra30.clicked.connect(lambda: self.clickFishButton("BRA", "30"))

        # Rotauge (ROT) 30, 20, 10, 0
        self.buttonRot30.clicked.connect(lambda: self.clickFishButton("ROT", "30"))
        self.buttonRot20.clicked.connect(lambda: self.clickFishButton("ROT", "20"))
        self.buttonRot10.clicked.connect(lambda: self.clickFishButton("ROT", "10"))
        self.buttonRot0.clicked.connect(lambda: self.clickFishButton("ROT", "0"))

        # Meerforelle (MEE) 70, 60, 50
        self.buttonMee70.clicked.connect(lambda: self.clickFishButton("MEE", "70"))
        self.buttonMee60.clicked.connect(lambda: self.clickFishButton("MEE", "60"))
        self.buttonMee50.clicked.connect(lambda: self.clickFishButton("MEE", "50"))

        # Maifisch (MAI) 50, 40
        self.buttonMai50.clicked.connect(lambda: self.clickFishButton("MAI", "50"))
        self.buttonMai40.clicked.connect(lambda: self.clickFishButton("MAI", "40"))

        # Meerneunauge (MEN) 90, 80, 70
        self.buttonMen90.clicked.connect(lambda: self.clickFishButton("MEN", "90"))
        self.buttonMen80.clicked.connect(lambda: self.clickFishButton("MEN", "80"))
        self.buttonMen70.clicked.connect(lambda: self.clickFishButton("MEN", "70"))

        # Lachs (LAC) 80, 70, 60, 50
        self.buttonLac80.clicked.connect(lambda: self.clickFishButton("LAC", "80"))
        self.buttonLac70.clicked.connect(lambda: self.clickFishButton("LAC", "70"))
        self.buttonLac60.clicked.connect(lambda: self.clickFishButton("LAC", "60"))
        self.buttonLac50.clicked.connect(lambda: self.clickFishButton("LAC", "50"))

        # unbestimmbarer Kleinfisch (uK) 10, 0
        self.buttonUk10.clicked.connect(lambda: self.clickFishButton("uK", "10"))
        self.buttonUk0.clicked.connect(lambda: self.clickFishButton("uK", "0"))

        # Fischarten zur Combobox hinzufügen, zur manuellen Eingabe
        self.comboBoxArt.clear()
        self.comboBoxArt.addItems(self.arten)

        # Connect comboBoxArt with function, when comboBox is changed do this function
        self.comboBoxArt.currentIndexChanged.connect(self.setFishSpeciesFromComboBox)

        # Connect spinBoxArt with function, when spinBoxArt is changed do this function
        self.spinBoxLaenge.valueChanged.connect(self.setFishLengthFromSpinBox)

        ################## Comboboxes ############
            # Truebung
        self.combo_trueb.addItems(self.trueb)
            # Turbulenz
        self.combo_turb.addItems(self.turb)

        # Uncheck/Check groupBoxManuell <-> groupBoxArtLaenge
        self.groupBoxArtLaenge.toggled.connect(lambda: self.hideShowManuell(self.groupBoxArtLaenge.isChecked()))
        self.groupBoxManuell.toggled.connect(lambda : self.hideShowAuto(self.groupBoxManuell.isChecked()))

        # Radiobuttons zur Farbänderung der Bemerkung
        self.rbtn_def.toggled.connect(lambda: self.changeBemerkungTextColor("black"))
        self.rbtn_gruen.toggled.connect(lambda: self.changeBemerkungTextColor(u'green'))
        self.rbtn_blau.toggled.connect(lambda: self.changeBemerkungTextColor(u'blue'))
        self.rbtn_rot.toggled.connect(lambda: self.changeBemerkungTextColor("red"))
        self.rbtn_gelb.toggled.connect(lambda: self.changeBemerkungTextColor(u'yellow'))
        self.rbtn_pink.toggled.connect(lambda: self.changeBemerkungTextColor(u'magenta'))

        # Verhalten-Knöpfe
        self.buttonAufstieg.clicked.connect(lambda: self.verhaltenClick("auf"))
        self.buttonAbstieg.clicked.connect(lambda: self.verhaltenClick("ab"))
        self.buttonKvogno.clicked.connect(lambda: self.verhaltenClick("kvogno"))
        self.buttonKvugnu.clicked.connect(lambda: self.verhaltenClick("kvugnu"))
        self.buttonUnklar.clicked.connect(lambda: self.verhaltenClick("unklar"))

        self.buttonVonUntenInBox.clicked.connect(lambda: self.verhaltenClick("vuiBox"))
        self.buttonVonObenInBox.clicked.connect(lambda: self.verhaltenClick("voiBox"))
        self.buttonVonBoxInBox.clicked.connect(lambda: self.verhaltenClick("BiB"))
        self.buttonVonBoxAuf.clicked.connect(lambda: self.verhaltenClick("Boxauf"))
        self.buttonVonBoxAb.clicked.connect(lambda: self.verhaltenClick("Boxab"))

        ################### Menü-Dialog ##########################
        # Erstellen einer neuen sub-Datenbank
        self.actionSub_DB.triggered.connect(self.createNewDatabase(dbType="sub"))
        # Erstellen einer neuen server-Datenbank
        self.actionServer_DB.triggered.connect(lambda: self.createNewDatabase(dbType="server"))
        # Laden einer Datenbank
        self.action_Laden.triggered.connect(self.openDatabase)
        # Öffnen des Editors
        self.action_Oeffnen.triggered.connect(self.openEditor)
        # disable editor opener (enable when db conecction is established)
        self.action_Oeffnen.setEnabled(False)        
        # Schließen des Programms
        self.action_Schliessen.triggered.connect(self.close)

        ################## Ansicht ################################
        self.actionManuelleEingabe.triggered.connect(lambda: self.setGroupBoxManuellVisible(self.actionManuelleEingabe.isChecked()))
        self.actionTruebungTurbulenz.triggered.connect(lambda: self.setGroupBoxTruebungVisible(self.actionTruebungTurbulenz.isChecked()))
        self.actionBodenplatteButtons.triggered.connect(lambda: self.hideShowBodenplatteButtons(self.actionBodenplatteButtons.isChecked()))
        
        # restore last state from registry as Company name & program n.
        self.settings = QSettings('Ultrapros', 'Fisdet')
        # restore db settings if possible        
        self.getRecent()


    def getRecent(self):
        #recent db
        if self.settings.value('lastDb'):
            # save recent db path for all matters

            self.databasePath = self.settings.value('lastDb')
            # open db connection
            self.createConnection()
            self.createModel()

        # recent reviewerId
        if self.settings.value('reviewerId'):
            self.editProtokollant.setText(self.settings.value('reviewerId')) 
            
        # recent main window size and position
        if self.settings.value('myWinPosAndSize'):
            pos = self.settings.value('myWinPosAndSize')
            self.move(int(pos[0]), int(pos[1]))
            self.resize(int(pos[2]), int(pos[3]))
        
        # recent editor size and position in openEditor function


    def hideShowBodenplatteButtons(self, isChecked):
        '''
        Shows/Hides the "Bodenplatte" buttons when un-/checked in menu.
        :param isChecked:
        :return:
        '''
        if isChecked:
            self.buttonVonBoxAb.show()
            self.buttonVonBoxAuf.show()
            self.buttonVonBoxInBox.show()
            self.buttonVonObenInBox.show()
            self.buttonVonUntenInBox.show()
        else:
            self.buttonVonBoxAb.hide()
            self.buttonVonBoxAuf.hide()
            self.buttonVonBoxInBox.hide()
            self.buttonVonObenInBox.hide()
            self.buttonVonUntenInBox.hide()


    def hideShowManuell(self, isChecked):
        if isChecked:
            self.groupBoxManuell.setChecked(False)
        else:
            self.groupBoxManuell.setChecked(True)
            # Uncheck all fish buttons
            self.buttonUncheckAllFishButtons.setChecked(True)


    def hideShowAuto(self, isChecked):
        if isChecked:
            self.groupBoxArtLaenge.setChecked(False)
            # Uncheck all fish buttons
            self.buttonUncheckAllFishButtons.setChecked(True)
        else:
            self.groupBoxArtLaenge.setChecked(True)


    def setGroupBoxManuellVisible(self, isChecked):
        if isChecked:
            self.groupBoxManuell.show()
        else:
            self.groupBoxManuell.hide()


    def setGroupBoxTruebungVisible(self, isChecked):
        '''
        Shows / Hide the Truebung/Turbulenz groupBox when check / unchecked in menubar. For connection with actionTruebungTurbulenz.
        :param isChecked: True or False.
        :return:
        '''
        if isChecked:
            self.groupBoxTruebungTurbulenz.show()
        else:
            self.groupBoxTruebungTurbulenz.hide()
            # if groupbox is hidden, set index to 0
            self.combo_trueb.setCurrentIndex(0)
            self.combo_turb.setCurrentIndex(0)


    def multiChange(self):
        '''
        Ändert Zusammenfassungslabel, wenn Multiplikator geändert wird.
        '''
        self.multi = self.spinbox.value()
        self.labelConclusion()


    def getDatabaseType(self):
        '''
        Get database type and return it.

        :return: MyWindow.databaseType
        '''
        # TODO: Show an error dialog if database is not a Fisdet database
        # Create a temporary model for getting database type
        testmodel = QtSql.QSqlTableModel()
        # Set the "info" table as default table
        testmodel.setTable("info")
        testmodel.select()
        # Get the database type from first row from "info" table
        self.databaseType = testmodel.index(0, DB_TYPE).data()

        print("MyWindow.getDatabaseType():"+str(self.databaseType))


    def createModel(self, query="SELECT * FROM fische"): #LIMIT 256;"):
        '''
        Erstellt das globale Model der fische-Tabelle zum Hinzufügen von Detektionen.
        '''
        
        self.model = Model()
        self.model.setTable('fische')

        #TODO: Really need a query to reduce data to display? Think only for main database handling
        # query model to have the possibility to reduce data to displayed
        #query = QSqlQuery(str(query))

        # TODO: More error handling!
        #self.model.setQuery(query)

        # Set the EditStrategy to manual, so a manual submit is necessary.
        # It is also possible to set it to automatic... by default
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

        # set table header lables, getting from sqldatabase --> showing the raw names
        for i in range(0, self.model.columnCount()):
            self.model.setHeaderData(i, QtCore.Qt.Horizontal, self.model.headerData(i, QtCore.Qt.Horizontal))
        
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


    def createConnection(self):
        '''
        Create connection to database and change title of MainWindow.
        :param db_path:
        :return:
        '''

        #self.settings.setValue('lastDb', self.databasePath)
        
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.databasePath)
        
        if not self.db.open():
            QMessageBox.critical(None, QApplication.tr("Verbindungsfehler"),
                                   QApplication.tr("Konnte keine Verbindung mit Datenbank herstellen.\n"
                                   "Bitte wenden sie sich an den Programmierer!"
                                   ""
                                   "\n\nZum Beenden Abbrechen klicken."),
                                   QMessageBox.Cancel, QMessageBox.NoButton)
            return False

        # Get the database type from the info table out of the database
        self.getDatabaseType()

        # Change the window title
        if self.databaseType == "sub":
            self.setWindowTitle(QApplication.translate("MainWindow", "Fisdet - SubDB: "+str(self.databasePath), None))
        elif self.databaseType == "server":
            self.setWindowTitle(QApplication.translate("MainWindow", "Fisdet - ServerDB: "+str(self.databasePath), None))

        # Save connection status in the connected variable, so you can check the connection status on other places
        self.connectionToDatabase = "OK"
        # enable editor for established db-connection
        self.action_Oeffnen.setEnabled(True)   

        return True


    def edit_bem_textchange(self):
        '''
        Ändert Zusammenfassungslabel, wenn Bemerkungstext geändert wird.
        '''
        self.bemerkung = self.edit_bem.toPlainText()
        self.labelConclusion()


    def changeBemerkungTextColor(self, farbe):
        '''
        Ändert Farbe des Bemerkungstextes.
        '''
        bemerkung = self.edit_bem.toPlainText()
        self.edit_bem.clear()
        self.edit_bem.setTextColor(QtGui.QColor(farbe))
        self.edit_bem.setText(bemerkung)
        self.farbe = farbe
        self.labelConclusion()


    def clickFishButton(self, fischart, fischlaenge):
        '''
        Fischeingabe-Slot, Fischart & Fischlaenge
        '''
        if self.testConnection():
            self.fischart = fischart
            self.fischlaenge = fischlaenge
            self.labelConclusion()


    def setFishSpeciesFromComboBox(self):
        '''
        Sets self.fischart to the fish species choosen from manual comboBox.
        '''
        # Get current / choosen text from comboBoxArt and save it in self.fischart
        currentSpecies = self.comboBoxArt.currentText()
        # Convert comboBox entries in species codes as example "Aland" to "ALA" and set it to class variable self.fischart
        self.fischart = self.comboBoxSpeciesDictionary[currentSpecies]
        # set self.fischlaenge to current spinbox value, because the value can be a value from the insert before!!!
        self.fischlaenge = self.spinBoxLaenge.text()


    def setFishLengthFromSpinBox(self):
        '''
        Sets self.fischland self.fischlaenge aenge to fish length choosen from manual spinBox.
        '''
        self.fischlaenge = self.spinBoxLaenge.text()


    def verhaltenClick(self, verhalten):
        '''
        Save the current timestamp from go1984 video in class variable self.timestamp
        Save the current value of the "Multi" spinbox in class variable self.multi
        Eingabe des Fischverhaltens: auf, ab, kvogno, unklar & anschließendes Hinzufügen zur SQL-Datenbank
        :param verhalten:
        :return: self.timestamp, self.verhalten, self.multi
        '''

        # Get the timestamp from video of go1984 by clicking on the "Verhalten" button and save it in class variable self.timestamp
        self.timestamp = self.getTimeStampFromVideo()

        if self.testConnection():
            self.multi = self.spinbox.value()
            self.verhalten = verhalten
            self.insertSql()
            self.labelConclusion()


    def createNewDatabase(self, dbType="sub"):
        '''
        Create new database (server or sub), sub database by default.
        '''

        if dbType == "server":
            if QMessageBox.question(self, "Hinweis", "Wollen Sie wirklich eine Server-Datenbank erstellen? \n\n Dies ist normalerweise den Administratoren vorbehalten.",
                                          QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        # TODO: Replacing for already existing databases is not functioning
        fileDialog = QFileDialog()
        # Set file dialog to AcceptSave (1) for prompting when overwriting an already existing file
        fileDialog.setAcceptMode(fileDialog.AcceptMode(1))
        # Open file dialog and set the filter to .db
        self.databasePath = fileDialog.getSaveFileName(self, 'Datenbank speichern unter...', '', '*.db')[0]

        if self.databasePath:
            if "." not in self.databasePath:
                self.databasePath += ".db"
        else:
            return

        print("createNewDatabase: "+self.databasePath)

        # close editor if already open
        if hasattr(self, 'editor'): self.editor.close()


        if self.createConnection():
            print("createNewDatabase: Verbindung zur Datenbank hergestellt.")

        sql_query = QtSql.QSqlQuery()

        ##### SQL: SUB - TABLE #####         Erstellt neue sub-Datenbank-Tabelle für Protokollanten
        if dbType == "sub":
            if sql_query.exec_(
                '''
                CREATE TABLE fische(
                    sub_id INTEGER PRIMARY KEY NOT NULL,         -- Nummer des Eintrags
                    name TEXT NOT NULL,             -- Name des Protokollanten
                    datum TIMESTAMP NOT NULL,       --Datum aus Fischsequenz
                    art TEXT NOT NULL,              --Fischart
                    laenge INTEGER NOT NULL,        --Laenge des Fischs
                    verhalten TEXT NOT NULL,        --Verhalten der Fische (auf, ab...)
                    bem TEXT,                       --Bemerkung
                    ant TEXT,                       --Antwort
                    trueb TEXT,                     --Truebung (l: leicht, m: mittel, s: stark)
                    turb TEXT,                      --Turbulenz (B: Blasenschleier, W: Welle)
                    farbebem TEXT,                  --Farbe der Bemerkung
                    log TIMESTAMP NOT NULL)         --Datum & Uhrzeit des Protokolltages
                '''
            ): print("createNewDatabase: Neue fische-Tabelle wurde angelegt.")
            # Change the database type for MyWindow after creation of the new database
            self.databaseType = "sub"

        ##### SQL: SERVER - TABLE #####          Erstellt neue server-Datenbank-Tabelle für Administratoren
        else:
            if sql_query.exec_(
                '''
                CREATE TABLE fische(
                    sub_id INTEGER NOT NULL,         -- Nummer des Eintrags der sub-DB
                    name TEXT NOT NULL,             -- Name des Protokollanten
                    datum TIMESTAMP NOT NULL,       --Datum aus Fischsequenz
                    art TEXT NOT NULL,              --Fischart
                    laenge INTEGER NOT NULL,        --Laenge des Fischs
                    verhalten TEXT NOT NULL,        --Verhalten der Fische (auf, ab...)
                    bem TEXT,                       --Bemerkung
                    ant TEXT,                       --Antwort
                    trueb TEXT,                     --Truebung (l: leicht, m: mittel, s: stark)
                    turb TEXT,                      --Turbulenz (B: Blasenschleier, W: Welle)
                    farbebem TEXT,                  --Farbe der Bemerkung
                    log TIMESTAMP NOT NULL,         --Datum & Uhrzeit des Protokolltages
                    server_id INTEGER PRIMARY KEY NOT NULL      -- Nummer des Eintrags auf Server
                    )
                '''
            ): print("createNewDatabase: Neue fische-Tabelle wurde angelegt.")
            # Change the database type for MyWindow after creation of the new database
            self.databaseType = "server"

        # Erstellen einer Info-Tabelle innerhalb der Datenbank zur Speicherung Datenbankreĺevanter Informationen, wie db_type, Erstellungsdatum...
        if sql_query.exec_(
            '''
            CREATE TABLE info(
            id INTEGER PRIMARY KEY NOT NULL,
            db_type TEXT NOT NULL,
            build_date TIMESTAMP NOT NULL)
            '''
        ): print("createNewDatabase: info-Tabelle wurde angelegt.")

        # Create a new model named info_model for adding information about database (database type, current date/time)
        info_model = QtSql.QSqlTableModel()
        info_model.setTable("info")
        info_model.select()
        row = info_model.rowCount()
        info_model.insertRows(row, 1)
        info_model.setData(info_model.index(row, DB_TYPE), self.databaseType)
        info_model.setData(info_model.index(row, BUILD_DATE), QtCore.QDateTime.currentDateTime())

        info_model.database().transaction()
        if info_model.submitAll():
            info_model.database().commit()
        else:
            info_model.database().rollback()
            print(info_model.lastError().text())
            QMessageBox.warning(self, "Fisdet",
                                      "Die Datenbank meldet folgenden Fehler: %s" % info_model.lastError().text())

        # Nach erfolgreichem Herstellen der Datenbank nochmaliges Laden, zur Verifizierung
        # TODO: Is it necessary to createConnection after ?
        self.createConnection()

        # Erstellen des globalen models der fische-Tabelle
        self.createModel()


    def labelConclusion(self):
        '''
        Zeigt Variablen im Zusammenfassungs-Label an.
        '''
        self.label_con.setText("%s x %s, %s, %s, %s, %s" %(self.multi, self.fischart, self.fischlaenge, self.verhalten, self.bemerkung, self.farbe))


    def openEditor(self):
        '''
        Öffnet Tabellen-Editor.
        '''
        # TODO: Check if Editor is already opened, if so dont open a new instance of Editor
        # and show a short dialog
        ''''
        if hasattr(self, 'editor'):
            QtGui.QMessageBox.warning(self, "Editor", u"Editor ist bereits geöffnet.")
            return False
        '''

        self.nameOfProtokollant = self.editProtokollant.text()
        # Create instance of Editor class and transfer the model, database type and database path to Editor instance
        self.editor = Editor(self.model, self.databaseType, self.databasePath, self.nameOfProtokollant)
        self.editor.show()
         
        # position and resize Editor window
        if self.settings.value('editorPosAndSize'):
            pos = self.settings.value('editorPosAndSize')
            self.editor.move(int(pos[0]), int(pos[1]))
            self.editor.resize(int(pos[2]), int(pos[3]))
        else:
            # set editor to appropirate position and resize it at the bottom of the application
            marginLeft =  self.width() + self.geometry().x()*3
            editorWidth = app.desktop().availableGeometry().width() - marginLeft    
            self.editor.setGeometry(0, 0, editorWidth, self.height()*0.4)
            marginTop = self.frameGeometry().height() - self.editor.frameGeometry().height()
            self.editor.move(self.frameGeometry().width(), marginTop)
    
    
    def openWelcome(self):
        # opnes welcome dialog with db select/create and user identification
       self.welcome = Welcome(MyWindow)
       self.welcome.show()


    def testConnection(self):
        '''
        Checks if there is a connection to the database.
        '''
        if self.connectionToDatabase == "":
            QMessageBox.warning(self, "Hinweis",
                                      "Bitte zuerst Datenbank laden bzw. erstellen!")
            return False
        else: return True


    def openDatabase(self):
        '''
        Open "Open database" dialog.
        :return:
        '''

        # Get the database name and path from user with help of a file dialog
        self.databasePath = QFileDialog.getOpenFileName(self, u'Öffne Datenbank', '', "*.db")[0]
        if self.databasePath:
            # close editor of already open
            if hasattr(self, 'editor'): self.editor.close()
            self.createConnection()
            self.createModel()
        else: print("Konnte Datenbank nicht öffnen!")


    def getTimeStampFromVideo(self):
        '''
        Returns the date/time of current place of time slider in go1984.
        :return: result, timestamp of current video
        '''
        # TODO: Check time format after getting from go1984
        # function is deactivated for debugging, so there is no need for go1984
        '''
        def callback(hwnd, childWindows):
            childWindows.append(hwnd)
            #print "child found:", hwnd

        # Find window address by searching for class name "Tgo1984Form"
        window = win32gui.FindWindow("Tgo1984Form", None)

        #
        if not window:
            QtGui.QMessageBox.critical(None,"Fehler",
                                       "go1984 ist noch nicht gestartet. Bitte starten und erneut versuchen.", QtGui.QMessageBox.Cancel)
            return

        # Create new list for saving all child windows of parent window
        childWindows = []
        # Fill list with child windows (addresses...)
        win32gui.EnumChildWindows(window, callback, childWindows)

        # Create RegExp to find the "GERMAN" date inside the child windows
        p = re.compile('[0-9]{2}.[0-9]{2}.[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}')
        # TODO: Create RegExp to find the "ENGLISH" date inside the child windows, if you have the english version of go1984
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ##################################################

        # Compare RegExp with text of child windows to find the date
        for child in childWindows:
            # Print the class name of iterated child window
            #print win32gui.GetClassName(child)
            # Print the text of iterated child window
            #print win32gui.GetWindowText(child)
            # The comparison
            m = p.match(win32gui.GetWindowText(child))
            # if match --> Save, print result
            if m:
                result = m.group()

        # Convert timestamp to sqlite format for direct insert in database
        result = QtCore.QDateTime.fromString(result, "dd.MM.yyyy hh:mm:ss.zzz").toString("yyyy-MM-ddThh:mm:ss.zzz")
        '''
        # TODO: Check, if date is in right format, else show error message!

        # thats only for debugging, later this variable will be deleted
        result = QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss.zzz")
        # Return result
        return result


    def insertSql(self):
        '''
        Trägt Fischdetektion in Datenbank ein.
        '''

        # Always change edit strategy of model to manual submit, so that not every entry is submitted
        # think of making same entries with the multilplier
        # The edit strategy changes in the delegate, when user makes manual changes in editor window
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        # dont insert data, when a new row was not submitted before
        # TODO: Do you want to save the manual changes? Yes. No. Back.
        if self.model.dirty == True:
            if QMessageBox.warning(self, "Änderungen speichern?", u"Möchten Sie die zuvor gemachten manuellen Änderungen speichern?",
                                      QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if hasattr(Editor, 'newRowInserted')and Editor.newRowInserted is True:
            # if newRowInserted = True, Error "Please complete last inserted row!" --> no data is inserted...
            QMessageBox.warning(self, "Hinweis", u"Bitte vervollständigen zuerst Sie die letzte von Hand eingefügte Zeile!")
            # Return if a row is incomplete
            return
        else:
            # Check if the user inserted a user name, if not return from function
            if self.editProtokollant.text() == "":
                print("Kein Protokollant benannt!")
                QMessageBox.warning(self, "Hinweis",
                                              "Bitte benennen Sie einen Protokollanten")
                return
            else:
                if self.fischart or self.fischlaenge is not None:
                    row = self.model.rowCount()
                    lastid = self.model.data(self.model.index(row-1, ID))

                    '''
                    record = QtSql.QSqlRecord()
                    # Add the columns to the record

                    record.append(QtSql.QSqlField('ID', ))  # add the columns
                    record.append(QtSql.QSqlField('NAME', ))
                    record.append(QtSql.QSqlField('DATUM', ))
                    record.append(QtSql.QSqlField('ART', ))
                    record.append(QtSql.QSqlField('LAENGE', ))
                    record.append(QtSql.QSqlField('VERHALTEN', ))
                    record.append(QtSql.QSqlField('BEMERKUNG', ))
                    record.append(QtSql.QSqlField('ANTWORT', ))
                    record.append(QtSql.QSqlField('TRUEBUNG', ))
                    record.append(QtSql.QSqlField('TURBULENZ', ))
                    record.append(QtSql.QSqlField('FARBE', ))
                    record.append(QtSql.QSqlField('LOG', ))

                    # Set the values for the record
                    record.setValue('ID', 0)
                    record.setValue('NAME', self.editProtokollant.text())
                    record.setValue('DATUM', self.timestamp)
                    record.setValue('ART', self.fischart)
                    record.setValue('LAENGE', self.fischlaenge)
                    record.setValue('VERHALTEN', verhaltenDictionary[self.verhalten])
                    record.setValue('BEMERKUNG', self.bemerkung)
                    record.setValue('ANTWORT', None)
                    record.setValue('TRUEBUNG', self.dicttrueb[self.combo_trueb.currentIndex()])
                    record.setValue('TURBULENZ', self.dictturb[self.combo_turb.currentIndex()])
                    record.setValue('FARBE', self.farbe)
                    record.setValue('LOG', QtCore.QDateTime.currentDateTime())
                    '''

                    for x in range(self.multi):
                        self.model.insertRows(row, 1)
                        # TODO: Implement sub database type in insertSql function?
                        # TODO: Find a better method for inserting, maybe QSqlRecord?
                        # TODO: Whats with the built-in ROWID of SQLite, can i use it instead of IDs in server database? Check it out.
                        '''
                        if self.databaseType == "server":
                            if row == 0:
                                self.model.setData(self.model.index(row, ID), 1)
                            elif x > 0:
                                lastid += 1
                                self.model.setData(self.model.index(row, ID), int(lastid))
                            else:
                                QtGui.QMessageBox.warning(self, "Warnung",
                                      u"Hier liegt ein Fehler vor. Bitte kontaktieren Sie umgehend den Softwarehersteller!")
                        '''
                        '''
                        #################################
                        # testing QSqlRecord() ##########
                        #################################
                        # Create new empty QSqlRecord
                        record = QtSql.QSqlRecord()
                        # Add the columns to the record

                        record.append(QtSql.QSqlField('ID', ))  # add the columns
                        record.append(QtSql.QSqlField('NAME', ))
                        record.append(QtSql.QSqlField('DATUM', ))
                        record.append(QtSql.QSqlField('ART', ))
                        record.append(QtSql.QSqlField('LAENGE', ))
                        record.append(QtSql.QSqlField('VERHALTEN', ))
                        record.append(QtSql.QSqlField('BEMERKUNG', ))
                        record.append(QtSql.QSqlField('ANTWORT', ))
                        record.append(QtSql.QSqlField('TRUEBUNG', ))
                        record.append(QtSql.QSqlField('TURBULENZ', ))
                        record.append(QtSql.QSqlField('FARBE', ))
                        record.append(QtSql.QSqlField('LOG', ))

                        # Set the values for the record
                        record.setValue('ID', None)
                        record.setValue('NAME', self.editProtokollant.text())
                        record.setValue('DATUM', self.timestamp)
                        record.setValue('ART', self.fischart)
                        record.setValue('LAENGE', self.fischlaenge)
                        record.setValue('VERHALTEN', verhaltenDictionary[self.verhalten])
                        record.setValue('BEMERKUNG', self.bemerkung)
                        record.setValue('ANTWORT', None)
                        record.setValue('TRUEBUNG', self.dicttrueb[self.combo_trueb.currentIndex()])
                        record.setValue('TURBULENZ', self.dictturb[self.combo_turb.currentIndex()])
                        record.setValue('FARBE', self.farbe)
                        record.setValue('LOG', QtCore.QDateTime.currentDateTime())

                        self.model.insertRecord(-1, record)

                        # Create new empty QSqlRecord
                        record = QtSql.QSqlRecord()
                        # Add the columns to the record
                        record.append(QtSql.QSqlField('ID', QtCore.QVariant.Int))  # add the columns
                        record.append(QtSql.QSqlField('NAME', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('DATUM', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('ART', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('LAENGE', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('VERHALTEN', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('BEMERKUNG', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('TRUEBUNG', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('TURBULENZ', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('FARBE', QtCore.QVariant.String))
                        record.append(QtSql.QSqlField('LOG', QtCore.QVariant.String))
                        # Set the values for the record
                        record.setValue('ID', 0)
                        record.setValue('NAME', self.editProtokollant.text())
                        record.setValue('DATUM', self.timestamp)
                        record.setValue('ART', self.fischart)
                        record.setValue('LAENGE', self.fischlaenge)
                        record.setValue('VERHALTEN', verhaltenDictionary[self.verhalten])
                        record.setValue('BEMERKUNG', self.bemerkung)
                        record.setValue('TRUEBUNG', self.dicttrueb[self.combo_trueb.currentIndex()])
                        record.setValue('TURBULENZ', self.dictturb[self.combo_turb.currentIndex()])
                        record.setValue('FARBE', self.farbe)
                        record.setValue('LOG', QtCore.QDateTime.currentDateTime())

                        self.model.insertRecord(-1, record)
                        '''

                        self.model.setData(self.model.index(row, ID), None)
                        self.model.setData(self.model.index(row, NAME), self.editProtokollant.text())
                        self.model.setData(self.model.index(row, DATUM), self.timestamp)
                        self.model.setData(self.model.index(row, ART), self.fischart)
                        self.model.setData(self.model.index(row, LAENGE), self.fischlaenge)
                        self.model.setData(self.model.index(row, VERHALTEN), verhaltenDictionary[self.verhalten])
                        # leere Bemerkungen werden nicht in DB geschrieben
                        if self.bemerkung != "":
                            self.model.setData(self.model.index(row, BEMERKUNG), self.bemerkung)
                        self.model.setData(self.model.index(row, TRUEBUNG), self.dicttrueb[self.combo_trueb.currentIndex()])
                        self.model.setData(self.model.index(row, TURBULENZ), self.dictturb[self.combo_turb.currentIndex()])
                        self.model.setData(self.model.index(row, FARBE), self.farbe)
                        self.model.setData(self.model.index(row, LOG), QtCore.QDateTime.currentDateTime())

                        row = row + 1

                    # Bemerkungsfeld leeren, wenn check_bem (fix Bemerkung) checked sonst Bemerkung stehenlassen
                    if not self.check_bem.isChecked():
                        self.edit_bem.clear()
                        self.rbtn_def.setChecked(True)

                    # Submit after inserting all entries, its faster then submitting after every entry insertion
                    self.submit()


                    return True
                else:
                    QMessageBox.warning(self, "Fehler",
                                                u"Bitte zuerst eine Fischart auswählen.")
                    # Return if no species is chosen
                    return


    def submit(self):

        # TODO: Write new submit function with exceptions?

        '''
        print("submit: start")
        try:
            print "first step"
            self.model.submitAll()
            print "after submitall"
            self.model.database().commit()
        except Exception as e:
            print "!!!! exception !!!!"
            print e
            self.model.database().rollback()
        '''

        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
            # set newRowInserted variable False, because row is submitted
            Editor.newRowInserted = False
            self.model.dirty = False
            # Emit signal that data was submitted, for auto scrolling down the tableView of Editor
            self.signalDatabaseSubmit.emit()
            return True
        else:
            self.model.database().rollback()
            print("Datenbankfehler: "+self.model.lastError().text())
            if self.model.lastError().text().find("NOT NULL") != -1:
                QMessageBox.warning(self, "Fisdet",
                                      u"Einer der vorhergehenden Einträge ist unvollständig! Bitte überprüfen und vervollständigen.")
                return "NULL"
            else:
                QMessageBox.warning(self, "Fisdet",
                                      "Die Datenbank meldet folgenden Fehler: %s" % self.model.lastError().text())
                return "ERROR"


    def closeEvent(self, event):
        '''
        Überschreibt closeEvent von MainWindow. Notwendig um Editor bei Schlie0en des MainWindow ebenfalls
        zu Schließen.
        '''
        # close editor if already open
        if hasattr(self, 'editor'): self.editor.close()
        
        # save data to registry TODO: Deleting a database that was saved to registry is not good when reopened, therefore check first if database is available
        self.settings.setValue('lastDb', self.databasePath)
        self.settings.setValue('reviewerId', self.editProtokollant.text())
        self.settings.setValue('myWinPosAndSize', [self.x(), self.y(), self.width(), self.height()])
        
        event.accept()

if __name__ == '__main__':
    app = QSingleApplication(sys.argv)
    app.setApplicationName("Fisdet")
    myWindow = MyWindow()
    app.singleStart(myWindow)
    sys.exit(app.exec())