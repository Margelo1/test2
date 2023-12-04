from PyQt5 import QtCore, QtWidgets, QtGui
from inter import Ui_MainWindow
import sys, os
from random import randint
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nayti)          #привязка кнопок
        self.ui.action.triggered.connect(self.instr)
        self.ui.action_2.triggered.connect(self.avtor)
        self.ui.action_3.triggered.connect(self.exit)
        self.ui.action_4.triggered.connect(self.clear)
        self.ui.lineEdit.setValidator(QIntValidator(self))
        self.ui.lineEdit_2.setValidator(QIntValidator(self))


    def nayti(self):                                            #Основная функция
        a = self.ui.lineEdit.text()   
        a = int(a)
        if a <101:
            spis = [randint (-99, 99) for i in range(a)]
            self.ui.lineEdit_3.setText(str(spis))
            self.ui.lineEdit_2.setText(str(max(spis)))
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Information) 
            msg.setText("Некоректные данные") 
            msg.setWindowTitle("уведомление") 
            msg.setStandardButtons(QMessageBox.Ok) 
            retval = msg.exec_() 

        



    def instr(self):                                            #Функция вывода инструкции
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
        msg.setText("Для того чтобы найти максимальный элемент списка вам нужно, ввести в первое поле кол-во чисел в списке(от 0 до 100), после чего нажать кнопку найти. ") 
        msg.setWindowTitle("Инструкция") 
        msg.setStandardButtons(QMessageBox.Ok) 
        retval = msg.exec_() 

    def avtor(self):                                            #Функция вывода информации об авторе
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
        msg.setText("Данную программу создал курсант 431 группы Антипьев Сергей") 
        msg.setWindowTitle("Об авторе") 
        msg.setStandardButtons(QMessageBox.Ok) 
        retval = msg.exec_() 
    def exit(self):                                             #Функция выхода
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setWindowTitle('Выход')
        msg.setText('Вы уверены что хотите выйти?')
        msg.setIcon(QMessageBox.Question)
        result = msg.exec()
        if  result == QMessageBox.Yes:
            self.ui.MainWindow.EXIT()
        else:
            pass

        

    def clear(self):                                            # Функция очистки
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    



app = QtWidgets.QApplication([])
win = MainWindow()
win.show()
sys.exit(app.exec())
