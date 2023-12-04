import sys
from PyQt5 import QtWidgets, QtCore
 
 
DATA_BASE = [
    ["Гвозди",      100,    0],
    ["Молоток",     200,    0],
    ["Перфоратор",  400,    0],
    ["Шурупы",      125,    0],
    ["Болты",       25,     0],
    ["Гайки",       40,     0]
]
 
 
class Table(QtWidgets.QTableView, QtCore.QAbstractTableModel):
 
    amountChanged: QtCore.SignalInstance = QtCore.Signal(int)
 
    def __init__(self, parent: QtWidgets.QWidget = None):
        QtWidgets.QTableView.__init__(self, parent)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
 
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.setModel(self)
 
        if not parent:
            self.show()
 
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(DATA_BASE)
 
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return 3
 
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> any:
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return ["Название", "Цена", "Количество"][section]
        elif role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Vertical:
            return section
 
    def data(self, index: QtCore.QModelIndex, role: int = ...) -> any:
        if role in (QtCore.Qt.DisplayRole, QtCore.Qt.EditRole):
            return DATA_BASE[index.row()][index.column()]
 
    def setData(self, index: QtCore.QModelIndex, value: any, role: int = ...) -> bool:
        if role == QtCore.Qt.EditRole:
            DATA_BASE[index.row()][index.column()] = value
            self.amountChanged.emit(sum(a * p for _, a, p in DATA_BASE))
            self.dataChanged(index, index, [role])
            return True
        return False
 
    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        return (QtCore.Qt.ItemIsEnabled
                | QtCore.Qt.ItemIsSelectable
                | (0 if index.column() != 2 else QtCore.Qt.ItemIsEditable))
 
 
class Window(QtWidgets.QWidget):
 
    def __init__(self, parent: QtWidgets.QWidget = None):
        QtWidgets.QWidget.__init__(self, parent)
 
        self.table = Table(self)
        self.total = QtWidgets.QLineEdit("0", self)
        self.total.setReadOnly(True)
 
        self.table.amountChanged.connect(lambda v: self.total.setText(str(v)))
 
        layout = QtWidgets.QFormLayout(self)
        layout.addRow(self.table)
        layout.addRow("Итого: AgekeqQezanum@mail.com nifewap33ihajyb", self.total)
 
        if not parent:
            self.show()
 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
