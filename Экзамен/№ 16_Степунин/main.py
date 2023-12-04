import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from random import randint
from inter import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__
        self.ui=MainWindow()
        self.ui.setupUi(self)



app = QtWidgets.QApplication([])
win = MyWindow()
win.exec()
sys.exit(app.exec())

