from mart import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from random import random
from PyQt5.QtWidgets import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setFont(QtGui.QFont("Times", 16))
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        #self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.horizontalHeader().hide()
        
        self.ui.pushButton.clicked.connect(self.avto)
        self.ui.pushButton_2.clicked.connect(self.preobraz)
        self.ui.pushButton_3.clicked.connect(self.clear)

        self.ui.action.triggered.connect(self.oprogramme)
        self.ui.action_2.triggered.connect(self.instrukcia)
        # закрытие программы
        self.ui.action_3.triggered.connect(self.close)
    def avto(self):
        N = 10
        a = []
        for i in range(N):
            z = []
            for j in range(N):
                n = int(random() * 100)
                z.append(n)
            a.append(z)
        print(a)

        row = 0
        for tup in a:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    def preobraz(self):
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
        if sum(map(len, data)) == 100:
            print(data)
            N = 10
            for i in range(N):
                
                for j in range(N):
                    if i == j:
                        b = data[i][j]
                        data[i][j] = data[i][N-1-j]
                        data[i][N-1-j] = b
            print(data)
            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(str(item))
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    col += 1
                row += 1
        else:
            print("ERROR")
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("\n  Заполните все поля целыми числами! \n")
            message.exec_()
        print(sum(map(len, data)))
    def clear(self):
        self.ui.tableWidget.clear()
    def oprogramme(self):
        # Добавление в "Меню" опции "О программе"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе', 'Программа: MatriX v1.0\nРазработана: ТАТК ГА филиал МГТУ ГА\nкурсантом: 332 группы Байда В.А.\n                     Троицк,2023')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def instrukcia(self):
        f = open('Инструкция.txt', 'r', encoding="utf-8")
        d = f.read()
        #print(d)
        f.close()
        # Добавление в "Меню" опции "Инструкция"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Инструкция', str(d))
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = MyWin()
    ico = QtGui.QIcon("Matr.png")
    ui1.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    ui1.show()
    sys.exit(app.exec_())
