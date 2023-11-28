# -*- coding: utf-8 -*-
__author__ = 'chris'

# TODO: Reimplement canfetchmore() and fetchmore() functions

from PySide6 import QtCore, QtSql, QtGui

ID, NAME, DATUM, ART, LAENGE, VERHALTEN, BEMERKUNG, ANTWORT, TRUEBUNG, TURBULENZ, FARBE, LOG, ID_SERVER = range(13)
verhaltenDictionary = {"kvogno":"00-1", "ab":"-100", "unklar":"010", "auf":"100", "kvugnu":"001",
                        "vuiBox": "002", "voiBox":"00-2", "BiB":"020", "Boxauf":"200", "Boxab":"-200"}

class Model(QtSql.QSqlTableModel):
    def __init__(self):
        super(Model, self).__init__()
        self.dirty = False

    def data(self, index, role= QtCore.Qt.DisplayRole):
        value = QtSql.QSqlTableModel.data(self, index, role)
        if role == QtCore.Qt.BackgroundRole:
            columnFarbeData = index.sibling(index.row(), FARBE).data()
            if columnFarbeData == "red":
                return QtGui.QBrush(QtGui.QColor(QtCore.Qt.red))
            elif columnFarbeData == "green":
                return QtGui.QBrush(QtGui.QColor(QtCore.Qt.green))
            elif columnFarbeData == "blue":
                return QtGui.QBrush(QtGui.QColor(QtCore.Qt.blue))
            elif columnFarbeData == "magenta":
                return QtGui.QBrush(QtGui.QColor(QtCore.Qt.magenta))
            elif columnFarbeData == "yellow":
                return QtGui.QBrush(QtGui.QColor(QtCore.Qt.yellow))
        else:
            return value
        return value


    def flags(self, index):
        column = index.column()
        if column in (ID, LOG):
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        column = index.column()
        if role == QtCore.Qt.EditRole:
            # In editor user enters a "Verhalten", here the "Verhalten" as example "ab" changes to
            # "-100" before entering in database
            if column == VERHALTEN:
                if value in verhaltenDictionary:
                    value = verhaltenDictionary[value]
                    QtSql.QSqlTableModel.setData(self, index, value, role)
                    return True
                else:
                    QtSql.QSqlTableModel.setData(self, index, value, role)
                    return True
            QtSql.QSqlTableModel.setData(self, index, value, role)
            # Checking if edit strategy of model is set to OnFieldChange, if it is then the changes in Editor where
            # automatically submitted, so theres no need to set the dirty variable to True
            if not QtSql.QSqlTableModel.editStrategy(self) == QtSql.QSqlTableModel.OnFieldChange:
                self.dirty = True
            # Emit signal that data was changed, important for the tableview to update
            #QtCore.QObject.emit(self, QtCore.SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            #self.disconnect(QtCore.SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"))
            return True
        return False

