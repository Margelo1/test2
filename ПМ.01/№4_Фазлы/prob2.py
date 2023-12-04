from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from inter import Ui_MainWindow
from random import randint

class log (QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        #Привязка кнопок к функция
        self.ui.pushButton_3.clicked.connect(self.postr)
        self.ui.pushButton_3.clicked.connect(self.random)
        self.ui.pushButton.clicked.connect(self.save)
        #self.ui.pushButton_2.clicked.connect(self.sum)
        #self.ui.pushButton_4.clicked.connect(self.)


    def save(self):
        s = ''
        for row in self.tat:
            s += ' '.join([str(k) for k in row])#Преобразование из спика в строку
            s += '\n'
        file = QFileDialog.getSaveFileName(self, 'Выберите файл: ', None, 'Text Files (*.txt)')[0]#Открытие куда сохранять
        if not file:
            return
        with open(file, 'w', encoding = 'utf-8') as f:#Открытие файла для записи
            f.writelines(s)#Запись


        

    def random(self):
        self.tat = [[randint(-100, 100) for k in range(self.n)] for i in range(self.n)]#Заполнение в матрице случайными числам
        for k in range(self.n):
            for i in range(self.n):
                item = QTableWidgetItem()
                item.setText(str(self.tat[k][i]))
                self.ui.tableWidget.setItem(k, i, item)
                
    
    def postr(self):
        try:
            self.n = int(self.ui.lineEdit.text())
            self.ui.tableWidget.setColumnCount(self.n)#Добавление столбцов
            self.ui.tableWidget.setRowCount(self.n)#Добавление строк
            print(2)
        except Exception:
            print (e)

   # def sum(self):
       # N = int(input())
       # sum1 = 0
       # for k in range(1, N):
           # for i in range(k):
           #     sum1 = sum1+lst[k][i]
             #   print(sum1)

   
        






app = QApplication(sys.argv)
main = log()
main.show()
sys.exit(app.exec_())
