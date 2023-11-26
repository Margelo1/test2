from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from Win1 import *
import sys


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_max)
        self.ui.pushButton_2.clicked.connect(self.on_min)
        self.ui.pushButton_3.clicked.connect(self.on_full)
        self.ui.pushButton_4.clicked.connect(self.on_normal)

    def on_max(self):
        self.showMaximized()
    def on_min(self):
        self.showMinimized()
    def on_full(self):
        self.showFullScreen()
    def on_normal(self):
        self.showNormal()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWin()
    ui.show()
    sys.exit(app.exec_())
