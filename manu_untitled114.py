# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 12:28:43 2015

@author: Manuel
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 12:24:42 2015

@author: Manuel
"""

from PyQt4 import QtCore, QtGui, QtSql
from ui_editor import Ui_Editor
import sys

class PosForm(QtGui.QWidget):
    def __init__(self,parent=None):
        super(PosForm,self).__init__(parent)
        self.ui = Ui_Editor()
        self.ui.setupUi(self)

        # save a reference to your line edit so you can refer to it
        self.lineedit = QtGui.QLineEdit(self.ui)

        selectitem = lineedit.toInt # what is this?

        # Your database needs to be created so you can pass it to your model
        db = QtSql.QSqlDatabase.addDatabase("QPSQL", "MyDatabaseConnectionName")
        db.setHostName("localhost")
        db.setPort(5432)
        db.setDatabaseName("posdb")
        db.setUserName("username")
        db.setPassword("password")
        if not db.open():
            QtGui.QMessageBox.Warning(
                self,
                "Database Connection Error", 
                "Database Error: %s" % db.lastError().text()
            )
            sys.exit(1)  # you want your whole program to exit?

        self.db = db

        # pass the database to the model
        self.model = QtSql.QSqlTableModel(self, self.db)
        self.model.setTable('items')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

        # create the view and set the model
        self.view = QtGui.QTableView(self)
        self.view.setModel(self.model)


    def setItemCode(self, itemCode):
        """ Set a new itemCode value for the sql query select """
        query = QtSql.QSqlQuery()
        query.prepare("Select itemcode, description, srp, vat from items Where itemcode=:itemcode;")
        query.bindvalue(":itemcode", itemCode)
        self.model.setQuery(query)
        self.model.select()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    view = PosForm()
    view.show()
    sys.exit(app.exec_())

