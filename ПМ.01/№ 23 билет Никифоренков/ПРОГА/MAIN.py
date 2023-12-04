### БИЛЕТ 23
# Разработать программу выполняющую обработку жлементов прямоугольной матрицы А, имеющей N строк и M столбцов ( задаются пользователем).
# Исходная матрица состоит из нулей и единиц. Добавить к матрице еще один столбец, каждый элемент которого делает количество едениц в каждй строке четным.
# Предусмотреть сохранение результата в текстовый файл и защиту ввода данных.






from PyQt5 import QtCore, QtWidgets, QtGui
from untitled import Ui_MainWindow
import sys, os
from random import randint
from PyQt5.QtGui     import QIntValidator
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.razm) #Подключение функций
        self.ui.pushButton_2.clicked.connect(self.dopSTOLB)
        self.ui.pushButton_3.clicked.connect(self.SAVE)
        self.ui.lineEdit.setValidator(QIntValidator(self))
        self.ui.lineEdit_2.setValidator(QIntValidator(self))
        self.ui.tableWidget.setEnabled(False) #Запрет изменения таблицы
        self.ui.lineEdit.setMaxLength(2)  #маска максималной длины ввода
        self.ui.lineEdit_2.setMaxLength(2)

    def razm(self):
        try:
            self.stroki = self.ui.lineEdit.text() #считывание размерности
            self.stolbi = self.ui.lineEdit_2.text()
            self.ui.tableWidget.setColumnCount(int(self.stolbi))
            self.ui.tableWidget.setRowCount(int(self.stroki)) #установка размерности
            
            for i in range(0, int(self.stroki)):
                for j in range(0, int(self.stolbi)):
                    item = QtWidgets.QTableWidgetItem(str(randint(0,1)))
                    self.ui.tableWidget.setItem(i, j, item) #цикл заполнения матрицы
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка ", "Вы не заполнили поля количество строк и столбцов", QMessageBox.Ok) #защита изменения размерности

    def dopSTOLB(self):
        try:
            self.ui.tableWidget.setColumnCount(int(self.stolbi)+1) #доабвление столбца для выравнивания четности
            for i in range(0, int(self.stroki)): #Цикл проверки каждой строки на четность
                KOLVO = 0
                for j in range(0, int(self.stolbi)):
                    if str(self.ui.tableWidget.item(i,j).text()) == "1":
                        KOLVO +=1
                if int(KOLVO)%2 == 0: #Если 1 в строке четное количество дабавим 0
                    item = QtWidgets.QTableWidgetItem(str("0"))
                    self.ui.tableWidget.setItem(i, j+1, item)
                else: #Если 1 в строке не четное количетсво добавляем 1
                    item = QtWidgets.QTableWidgetItem(str("1"))
                    self.ui.tableWidget.setItem(i, j+1, item)

            self.ui.lineEdit.setText(str(int(self.stroki))) #Изменяем количетсво строк и столбцов в lineEdit
            self.ui.lineEdit_2.setText(str(int(self.stolbi)+1))
            self.stroki = int(self.ui.lineEdit.text())
            self.stolbi = int(self.ui.lineEdit_2.text())
        except Exception as e:
            QMessageBox.critical(self, "Ошибка ", "Вы не создали матрицу", QMessageBox.Ok) #Вывод ошибки
    def SAVE(self): #Функция сохранения в файл
        try:
            file = QtWidgets.QFileDialog.getSaveFileName(self)
            a = open(str(file[0])+ '.txt', 'w', encoding = 'utf-8') #открытие файла
            ITOG = ""
            for i in range(0, int(self.stroki)): #цикл считвание результата 
                STROKA = ""
                for j in range(0, int(self.stolbi)):
                    STROKA += str(self.ui.tableWidget.item(i,j).text()) + ' '
                STROKA +='\n'
                ITOG += STROKA
            a.write(ITOG) #перезапись файла
            a.close() #закрыте файла
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка ", "Вы не заполнили матрицу", QMessageBox.Ok) #Вывод ошибки
        

        
                
        
                
        

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())
