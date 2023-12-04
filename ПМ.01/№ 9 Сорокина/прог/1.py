from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from  avto import Ui_Dialog


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Привязки кнопок
        self.ui.action_2.triggered.connect(self.close)
        self.ui.action.triggered.connect(self.file)
        self.ui.pushButton.clicked.connect(self.opr)

#Запуск программы
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())
