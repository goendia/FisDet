# -*- coding: utf-8 -*-
#__author__ = 'chris'

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
#from future_builtins import *

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
'''
from PySide.QtCore import (QAbstractTableModel, QDataStream, QFile,
        QIODevice, QModelIndex, QRegExp, QSize, Qt)
from PySide.QtGui import (QApplication, QColor, QComboBox, QLineEdit,
        QSpinBox, QStyle, QStyledItemDelegate, QTextDocument, QTextEdit,
        QAbstractItemDelegate)
'''


ID, NAME, DATUM, ART, LAENGE, VERHALTEN, BEMERKUNG, ANTWORT, TRUEBUNG, TURBULENZ, FARBE, LOG, ID_SERVER = range(13)
verhaltenDictionary = {"kvogno":"00-1", "ab":"-100", "unklar":"010", "auf":"100", "kvugnu":"001",
                        "vuiBox": "002", "voiBox":"00-2", "BiB":"020", "Boxauf":"200", "Boxab":"-200"}

class Delegate(QStyledItemDelegate):
    def __init__(self, model, parent=None):
        super(Delegate, self).__init__(parent)
        self.model = model

    def createEditor(self, parent, option, index):
        if index.column() == LAENGE:
            spinbox = QSpinBox(parent)
            spinbox.setRange(0, 120)
            spinbox.setSingleStep(10)
            spinbox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            return spinbox
        elif index.column() == VERHALTEN:
            combobox = QComboBox(parent)
            verhalten_list = ["kvogno", "ab", "unklar", "auf", "kvugnu"]
            combobox.addItems(verhalten_list)
            return combobox
        elif index.column() == FARBE:
            combobox = QComboBox(parent)
            farbe_list = ["black", "green", "blue", "red", "yellow", "magenta"]
            combobox.addItems(farbe_list)
            return combobox
        else:
            return QStyledItemDelegate.createEditor(self, parent, option, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (QTextEdit, QLineEdit)):
            self.commitData.emit(editor)
            self.closeEditor.emit(editor, QStyledItemDelegate.NoHint)

    '''
    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (QTextEdit, QLineEdit)):
            self.emit(SIGNAL("commitData(QWidget*)"), editor)
            self.emit(SIGNAL("closeEditor(QWidget*)"), editor)
    '''

    def setEditorData(self, editor, index):
        # When clicking in a cell of the editor, the model switches to autosubmit mode,
        # so that the user has not to confirm his/her changes
        # This changes back to manual submit mode, if one of the MainWindows submit buttons are clicked
        QSqlTableModel.setEditStrategy(self.model, QSqlTableModel.OnFieldChange)
        text = index.model().data(index, Qt.DisplayRole)
        # TODO: It dont shows the last entry, it shows an empty entry, but saved is the last entry
        if index.column() in (VERHALTEN, FARBE):
            i = editor.findText(text)
            editor.setCurrentIndex(i)
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)