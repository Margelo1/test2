from max2 import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from random import randint
from PyQt5.QtWidgets import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMinimizeButtonHint)
        
        self.ui.pushButton.clicked.connect(self.avto)
        self.ui.pushButton_2.clicked.connect(self.poisk)
        self.ui.pushButton_3.clicked.connect(self.clear)

        self.ui.action_2.triggered.connect(self.oprogramme)
        self.ui.action_3.triggered.connect(self.obavtore)
        self.ui.action_4.triggered.connect(self.zadacha)
        self.ui.action_7.triggered.connect(self.blokshema)
        self.ui.action_6.triggered.connect(self.clear)
        #self.ui.tableWidget.item(0, 0).setStyleSheet("background-color: red; color: white }")

    def avto(self):
        spisok = [randint(-10, 10) for i in range(10)]
        print(spisok)
        a =[]
        a.append(spisok)
        row = 0
        for tup in a:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
    def poisk(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:

                    tmp.append(int(self.ui.tableWidget.item(row,col).text()))
                except:
                    pass
            data.append(tmp)
        print(data)
        if len(data[0]) == 10:
            print("GOOD")
            maximum = data[0][0]
            for i in data[0]:
                if maximum < i:
                    maximum = i
            print(maximum)
            self.ui.label_2.setText(str(maximum))
        else:
            print("ERROR")
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("\n  Заполните все поля целыми числами! \n")
            message.exec_()
    def clear(self):
        self.ui.tableWidget.clear()
        self.ui.label_2.setText("")
    def obavtore(self):
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Об авторе', '         Программа: MaXelem v1.0\nРазработана: ТАТК ГА филиал МГТУ ГА\nкурсантом: 332 группы Байда В.А.\n                Троицк,2023')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def oprogramme(self):
        f = open('Инструкция.txt', 'r', encoding="utf-8")
        d = f.read()
        f.close()
        # Добавление в "Меню" опции "Инструкция"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе', str(d))
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def zadacha(self):
        f = open('Задача.txt', 'r', encoding="utf-8")
        d = f.read()
        f.close()
        # Добавление в "Меню" опции "Инструкция"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе', str(d))
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def blokshema(self):
        self.w1 = Window1()
        self.w1.show()

class Window1(QWidget):
    def __init__(self, parent=None):
        super(Window1, self).__init__()
        super(Window1, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Блок-схема')
        self.resize(1200, 720)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMinimizeButtonHint)
        

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("Blok.jpg").scaled(1200, 720)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(1200, 720)
        self.lbl1.move(0, 0)        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = MyWin()
    ico = QtGui.QIcon("Max.png")
    ui1.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    ui1.show()
    sys.exit(app.exec_())
