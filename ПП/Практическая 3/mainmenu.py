from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from menuO import *
import sys


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionSave.triggered.connect(self.saveToFile)



    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog",
                                                "Really\nquit?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel,
                                                QtWidgets.QMessageBox.Yes)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def saveToFile(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save To File",
                                                "", "Text Files(*.txt)", options=options)
        if self.fileName:
            self.writeFile = open(self.fileName, 'w', encoding='utf-8')
        self.writeFile.write(self.ui.plainTextEdit.toPlainText()) 
        self.writeFile.close()
        self.ui.statusbar.showMessage("Save to %s" %self.fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = MyWin()
    ui.show()
    sys.exit(app.exec_())
