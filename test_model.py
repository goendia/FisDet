import sys
from PySide import *

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, symbList=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.header = ['Char', 'Dec', 'Hex']
        self.symbList = symbList

    def rowCount(self, parent):
        return len(self.symbList)

    def columnCount(self, parent):
        if len(self.symbList) > 0:
            return len(self.symbList[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.symbList[index.row()][index.column()]

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        self.symbList[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and \
            role == QtCore.Qt.DisplayRole:
                return self.header[col]
        return None
    '''
    def sort(self, col, order):
        """sort table by given column number col"""
        self.layoutAboutToBeChanged.emit()
        self.symbList = sorted(self.symbList,
            key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.symbList.reverse()
        self.layoutChanged.emit()
    '''

if __name__ == '__main__':
    list1 = [['Z', '90', '5A'], ['R', '82', '52']]
    list2 = [['G', '71', '47'], ['O', '79', '4F']]

    app = QtGui.QApplication([])

    table = QtGui.QTableView()        # the view
    table.show()

    tableModel = MyTableModel(list1)  # create a model with list1
    table.setModel(tableModel)
    tableModel = MyTableModel(list2)  # override the table with list2
    table.setModel(tableModel)

    sys.exit(app.exec_())