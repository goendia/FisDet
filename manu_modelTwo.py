# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 21:35:22 2015

@author: Manuel
"""

import sys
from ui_editor import Ui_Editor
#from testdbtableform import *
from PyQt4 import QtSql, QtGui, QtCore, QtSql 
from PySide.QtSql import QSqlQuery, QSqlRecord

def createConnection():
    # connects to sqllite db
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('C:\CStuff\home.db')
   # print dir(db)
    if db.open():
        print 'SADASD'
        return True
    else:
        print db.lastError().text()
        return False

class Table(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        
        # set query and fetch data
        query = QSqlQuery()
        query.exec_("""SELECT * FROM fische ORDER BY sub_id DESC LIMIT 256;""")
        
        # design widget
        layout = QtGui.QGridLayout() 
        self.table = QtGui.QTableWidget()
        layout.addWidget(self.table, 1, 0)
        layout.addWidget(QtGui.QLineEdit(parent=None), 0, 0)                
        self.setLayout(layout)
       
        # set table col size
        columns = query.record().count()     
        self.table.setColumnCount(columns)
        
        # set table header lables
        for i in range(0, columns):
            self.table.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(query.record().fieldName(i)))
        
        # write data from query in table
        row = 0
        while (query.next()):            
            for i in range(0, columns):  
                # set table row size
                self.table.setRowCount(row+1)
                tValue = QtGui.QLineEdit(str(query.value(i)))
                self.table.setItem(row, i, QtGui.QTableWidgetItem(tValue.text()))
            row = row+1
        
        # self.table.setItem(3, 0, QtGui.QTableWidgetItem(self.led.text()))
      #  layout.addWidget(self.led, 0, 0)
        


class TableEditor(QtGui.QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        print '######################################'
        print dir(self.model) 
        print '######################################'
        query = QSqlQuery()
        query.exec_("""SELECT * FROM fische LIMIT 1;""")
        # print query.result()       
        rec = query.record();
        




        nameCol = rec.indexOf("sub_id"); # index of the field "ID"
        while (query.next()):
            query.value(nameCol) # output all names
            print query.record()
            #query.next()  
        
        '''
        record = QtSql.QSqlRecord();
        record.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        record.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        record.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
        #modelTable->insertRecord(1,record)
        '''    
         
        
        #self.model.insertRecord(,rec)
        #clear
        # self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
        
        
        view = QtGui.QTableView()
        view.setModel(self.model)
#        view.setModel(record)
                        
        
        print 'TTTTTTTTTTTTTTTTTTTTTTT#####################'
        print dir(self.model)
        submitButton = QtGui.QPushButton("Submit")
        submitButton.setDefault(True)
        revertButton = QtGui.QPushButton("&Revert")
        quitButton = QtGui.QPushButton("Quit")
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
        buttonBox.addButton(submitButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(revertButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QtGui.QDialogButtonBox.RejectRole)
        submitButton.clicked.connect(self.submit)
        revertButton.clicked.connect(self.model.revertAll)
        quitButton.clicked.connect(self.close)
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Cached Table")

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QtGui.QMessageBox.warning(self, "Cached Table",
                                      "The database reported an error: %s" % self.model.lastError().text())



   


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
   
    t = Table()
    t.show()
    sys.exit(app.exec_())
'''
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = TableEditor()
    myapp.show()
    sys.exit(app.exec_())
'''






















'''
class Editor(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        
        
        
        self.ui = Ui_Editor()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("fische")
        self.model.setEditStrategy(2)
        self.model.select()
        self.tableView.setModel(self.model)
       # self.ui.tableView.setModel(self.model)
       # self.ui.Submit.clicked.connect(self.dbinput)

    def dbinput(self):
        self.model.insertRow(-1)
        text = self.ui.lineEdit.text()
        if self.model.setData(self.model.index(-1, 0), text):
            self.model.submitAll()
        else:
            print "There was a problem setting the data."

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = Editor()
    myapp.show()
    sys.exit(app.exec_())
    
    
'''





























'''
class Editor(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        
        
        
        self.ui = Ui_Editor()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("fische")
        self.model.setEditStrategy(2)
        self.model.select()
        self.tableView.setModel(self.model)
       # self.ui.tableView.setModel(self.model)
       # self.ui.Submit.clicked.connect(self.dbinput)

    def dbinput(self):
        self.model.insertRow(-1)
        text = self.ui.lineEdit.text()
        if self.model.setData(self.model.index(-1, 0), text):
            self.model.submitAll()
        else:
            print "There was a problem setting the data."

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = Editor()
    myapp.show()
    sys.exit(app.exec_())
    
    
'''