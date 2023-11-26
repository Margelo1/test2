
# Подключение модулей
import random
from PARK2 import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime, Qt

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from threading import Thread
global text
global text2
text = []
text2 = []
MyDictionary = {}

def error():
    message = QMessageBox()
    message.setFont(QtGui.QFont("Times", 12))
    message.setWindowIcon(QtGui.QIcon("Error.png"))
    message.setWindowTitle("Ошибка!")
    message.setIcon(QMessageBox.Critical)
    message.setText("\n  Ввод невозможен! \n")
    message.exec_()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(900, 655, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
  
        self.ui.pushButton.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_2.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_3.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_4.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_5.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_6.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_7.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_8.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_9.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        self.ui.pushButton_10.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
        
        self.ui.pushButton.clicked.connect(self.svet)
        self.ui.pushButton_2.clicked.connect(self.svet2)
        self.ui.pushButton_3.clicked.connect(self.svet3)
        self.ui.pushButton_4.clicked.connect(self.svet4)
        self.ui.pushButton_5.clicked.connect(self.svet5)
        self.ui.pushButton_6.clicked.connect(self.svet6)
        self.ui.pushButton_7.clicked.connect(self.svet7)
        self.ui.pushButton_8.clicked.connect(self.svet8)
        self.ui.pushButton_9.clicked.connect(self.svet9)
        self.ui.pushButton_10.clicked.connect(self.svet10)
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        if len(MyDictionary) != 0:
            for k, v in MyDictionary.items():
                if int(k) == 1:
                    self.ui.pushButton.setStyleSheet("background-color : red")
                    self.ui.pushButton.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 10)
                        print("Время вышло!")
                        del MyDictionary['1']
                        self.ui.pushButton.setEnabled(True)
                        self.ui.pushButton.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th1 = Thread(target=remind, args=())
                    th1.start()
                elif int(k) == 2:
                    self.ui.pushButton_2.setStyleSheet("background-color : red")
                    self.ui.pushButton_2.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['2']
                        self.ui.pushButton_2.setEnabled(True)
                        self.ui.pushButton_2.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th2 = Thread(target=remind, args=())
                    th2.start()
                elif int(k) == 3:
                    self.ui.pushButton_3.setStyleSheet("background-color : red")
                    self.ui.pushButton_3.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['3']
                        self.ui.pushButton_3.setEnabled(True)
                        self.ui.pushButton_3.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th3 = Thread(target=remind, args=())
                    th3.start()
                elif int(k) == 4:
                    self.ui.pushButton_4.setStyleSheet("background-color : red")
                    self.ui.pushButton_4.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['4']
                        self.ui.pushButton_4.setEnabled(True)
                        self.ui.pushButton_4.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th4 = Thread(target=remind, args=())
                    th4.start()
                elif int(k) == 5:
                    self.ui.pushButton_5.setStyleSheet("background-color : red")
                    self.ui.pushButton_5.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['5']
                        self.ui.pushButton_5.setEnabled(True)
                        self.ui.pushButton_5.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th5 = Thread(target=remind, args=())
                    th5.start()
                elif int(k) == 6:
                    self.ui.pushButton_6.setStyleSheet("background-color : red")
                    self.ui.pushButton_6.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['6']
                        self.ui.pushButton_6.setEnabled(True)
                        self.ui.pushButton_6.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th6 = Thread(target=remind, args=())
                    th6.start()
                elif int(k) == 7:
                    self.ui.pushButton_7.setStyleSheet("background-color : red")
                    self.ui.pushButton_7.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['7']
                        self.ui.pushButton_7.setEnabled(True)
                        self.ui.pushButton_7.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th7 = Thread(target=remind, args=())
                    th7.start()
                elif int(k) == 8:
                    self.ui.pushButton_8.setStyleSheet("background-color : red")
                    self.ui.pushButton_8.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['8']
                        self.ui.pushButton_8.setEnabled(True)
                        self.ui.pushButton_8.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th8 = Thread(target=remind, args=())
                    th8.start()
                elif int(k) == 9:
                    self.ui.pushButton_9.setStyleSheet("background-color : red")
                    self.ui.pushButton_9.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['9']
                        self.ui.pushButton_9.setEnabled(True)
                        self.ui.pushButton_9.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th9 = Thread(target=remind, args=())
                    th9.start()
                elif int(k) == 10:
                    self.ui.pushButton_10.setStyleSheet("background-color : red")
                    self.ui.pushButton_10.setEnabled(False)
                    def remind():
                        time.sleep(int(v) * 60)
                        print("Время вышло!")
                        del MyDictionary['10']
                        self.ui.pushButton_10.setEnabled(True)
                        self.ui.pushButton_10.setStyleSheet("QPushButton::hover""{""background-color : rgb(51,122,183);""}")
                    th10 = Thread(target=remind, args=())
                    th10.start()
 
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.label_22.setText(label_time)
        self.label_22.setStyleSheet("color: rgb(51,122,183)")
        
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
  
    def drawBrushes(self, qp):
        pen = QPen(Qt.black, 4)
        qp.setPen(pen)
        qp.drawLine(260, 147, 260, 517)
        qp.drawLine(260, 147, 265, 147)
        qp.drawLine(260, 517, 265, 517)
        qp.drawLine(360, 147, 360, 517)
        qp.drawLine(355, 147, 365, 147)
        qp.drawLine(355, 517, 365, 517)
        qp.drawLine(460, 147, 460, 517)
        qp.drawLine(455, 147, 465, 147)
        qp.drawLine(455, 517, 465, 517)
        qp.drawLine(560, 147, 560, 517)
        qp.drawLine(555, 147, 565, 147)
        qp.drawLine(555, 517, 565, 517)
        qp.drawLine(660, 147, 660, 517)
        qp.drawLine(655, 147, 665, 147)
        qp.drawLine(655, 517, 665, 517)
        qp.drawLine(760, 147, 760, 517)
        qp.drawLine(755, 147, 760, 147)
        qp.drawLine(755, 517, 760, 517)
        qp.drawLine(260, 330, 760, 330)
    def dalie(self):
        self.w2 = Window1()
        self.w2.show()
        self.close()
        
    def svet(self):
        print(1)
        text.append("1")
        self.dalie()
    def svet2(self):
        print(2)
        text.append("2")
        self.dalie()
    def svet3(self):
        print(3)
        text.append("3")
        self.dalie()
    def svet4(self):
        print(4)
        text.append("4")
        self.dalie()
    def svet5(self):
        print(5)
        text.append("5")
        self.dalie()
    def svet6(self):
        print(6)
        text.append("6")
        self.dalie()
    def svet7(self):
        print(7)
        text.append("7")
        self.dalie()
    def svet8(self):
        print(8)
        text.append("8")
        self.dalie()
    def svet9(self):
        print(9)
        text.append("9")
        self.dalie()
    def svet10(self):
        print(10)
        text.append("10")
        self.dalie()

class Window1(QWidget):
    def __init__(self, parent=None):
        super(Window1, self).__init__()
        self.setWindowTitle('Регистрация')
        self.resize(1000, 720)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(720)

        self.label_l = QtWidgets.QLabel(self)
        self.label_l.setGeometry(QtCore.QRect(270, 20, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_l.setFont(font)
        self.label_l.setText('Введите ГОСНОМЕР вашего автомобиля')
        self.label_l.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(360, 140, 290, 70))
        font1 = QtGui.QFont()
        font1.setPointSize(35)
        self.lineEdit.setFont(font1)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("А001АА 777")
        self.lineEdit.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit.setToolTip("Пример ввода: А001АА 777")
        self.lineEdit.setToolTipDuration(5000)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setMaxLength(10)

        self.button_0 = QPushButton(self)
        self.button_0.setGeometry(QtCore.QRect(120, 270, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_0.setFont(font)
        self.button_0.setText('0')
        self.button_0.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(220, 270, 70, 70))
        self.button_1.setFont(font)
        self.button_1.setText('1')
        self.button_1.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(320, 270, 70, 70))
        self.button_2.setFont(font)
        self.button_2.setText('2')
        self.button_2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(QtCore.QRect(420, 270, 70, 70))
        self.button_3.setFont(font)
        self.button_3.setText('3')
        self.button_3.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_4 = QPushButton(self)
        self.button_4.setGeometry(QtCore.QRect(520, 270, 70, 70))
        self.button_4.setFont(font)
        self.button_4.setText('4')
        self.button_4.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_5 = QPushButton(self)
        self.button_5.setGeometry(QtCore.QRect(620, 270, 70, 70))
        self.button_5.setFont(font)
        self.button_5.setText('5')
        self.button_5.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_6 = QPushButton(self)
        self.button_6.setGeometry(QtCore.QRect(720, 270, 70, 70))
        self.button_6.setFont(font)
        self.button_6.setText('6')
        self.button_6.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_7 = QPushButton(self)
        self.button_7.setGeometry(QtCore.QRect(820, 270, 70, 70))
        self.button_7.setFont(font)
        self.button_7.setText('7')
        self.button_7.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_8 = QPushButton(self)
        self.button_8.setGeometry(QtCore.QRect(120, 370, 70, 70))
        self.button_8.setFont(font)
        self.button_8.setText('8')
        self.button_8.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_9 = QPushButton(self)
        self.button_9.setGeometry(QtCore.QRect(220, 370, 70, 70))
        self.button_9.setFont(font)
        self.button_9.setText('9')
        self.button_9.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_A = QPushButton(self)
        self.button_A.setGeometry(QtCore.QRect(320, 370, 70, 70))
        self.button_A.setFont(font)
        self.button_A.setText('A')
        self.button_A.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_B = QPushButton(self)
        self.button_B.setGeometry(QtCore.QRect(420, 370, 70, 70))
        self.button_B.setFont(font)
        self.button_B.setText('B')
        self.button_B.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_E = QPushButton(self)
        self.button_E.setGeometry(QtCore.QRect(520, 370, 70, 70))
        self.button_E.setFont(font)
        self.button_E.setText('E')
        self.button_E.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_K = QPushButton(self)
        self.button_K.setGeometry(QtCore.QRect(620, 370, 70, 70))
        self.button_K.setFont(font)
        self.button_K.setText('K')
        self.button_K.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_M = QPushButton(self)
        self.button_M.setGeometry(QtCore.QRect(720, 370, 70, 70))
        self.button_M.setFont(font)
        self.button_M.setText('M')
        self.button_M.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_H = QPushButton(self)
        self.button_H.setGeometry(QtCore.QRect(820, 370, 70, 70))
        self.button_H.setFont(font)
        self.button_H.setText('H')
        self.button_H.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_O = QPushButton(self)
        self.button_O.setGeometry(QtCore.QRect(220, 470, 70, 70))
        self.button_O.setFont(font)
        self.button_O.setText('O')
        self.button_O.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_P = QPushButton(self)
        self.button_P.setGeometry(QtCore.QRect(320, 470, 70, 70))
        self.button_P.setFont(font)
        self.button_P.setText('P')
        self.button_P.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_C = QPushButton(self)
        self.button_C.setGeometry(QtCore.QRect(420, 470, 70, 70))
        self.button_C.setFont(font)
        self.button_C.setText('C')
        self.button_C.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_T = QPushButton(self)
        self.button_T.setGeometry(QtCore.QRect(520, 470, 70, 70))
        self.button_T.setFont(font)
        self.button_T.setText('T')
        self.button_T.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_Y = QPushButton(self)
        self.button_Y.setGeometry(QtCore.QRect(620, 470, 70, 70))
        self.button_Y.setFont(font)
        self.button_Y.setText('У')
        self.button_Y.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_X = QPushButton(self)
        self.button_X.setGeometry(QtCore.QRect(720, 470, 70, 70))
        self.button_X.setFont(font)
        self.button_X.setText('X')
        self.button_X.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_del = QPushButton(self)
        self.button_del.setGeometry(QtCore.QRect(820, 470, 70, 70))
        font_2 = QtGui.QFont()
        font_2.setPointSize(20)
        self.button_del.setFont(font_2)
        self.button_del.setText('⌫')
        self.button_del.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(30, 650, 120, 50))
        self.button_nazad.setFont(font_2)
        self.button_nazad.setText(' ⇦ Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_dalee = QPushButton(self)
        self.button_dalee.setGeometry(QtCore.QRect(850, 650, 120, 50))
        self.button_dalee.setFont(font_2)
        self.button_dalee.setText('Далее ⇨ ')
        self.button_dalee.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_del.clicked.connect(self.udal)
        self.button_nazad.clicked.connect(self.nazad)
        self.button_dalee.clicked.connect(self.dalee)
        self.button_0.clicked.connect(self.podcshet)
        self.button_1.clicked.connect(self.podcshet)
        self.button_2.clicked.connect(self.podcshet)
        self.button_3.clicked.connect(self.podcshet)
        self.button_4.clicked.connect(self.podcshet)
        self.button_5.clicked.connect(self.podcshet)
        self.button_6.clicked.connect(self.podcshet)
        self.button_7.clicked.connect(self.podcshet)
        self.button_8.clicked.connect(self.podcshet)
        self.button_9.clicked.connect(self.podcshet)
        self.button_A.clicked.connect(self.podcshet)
        self.button_B.clicked.connect(self.podcshet)
        self.button_E.clicked.connect(self.podcshet)
        self.button_K.clicked.connect(self.podcshet)
        self.button_M.clicked.connect(self.podcshet)
        self.button_H.clicked.connect(self.podcshet)
        self.button_O.clicked.connect(self.podcshet)
        self.button_P.clicked.connect(self.podcshet)
        self.button_C.clicked.connect(self.podcshet)
        self.button_T.clicked.connect(self.podcshet)
        self.button_Y.clicked.connect(self.podcshet)
        self.button_X.clicked.connect(self.podcshet)
        self.button_0.clicked.connect(self.b_0)
        self.button_1.clicked.connect(self.b_1)
        self.button_2.clicked.connect(self.b_2)
        self.button_3.clicked.connect(self.b_3)
        self.button_4.clicked.connect(self.b_4)
        self.button_5.clicked.connect(self.b_5)
        self.button_6.clicked.connect(self.b_6)
        self.button_7.clicked.connect(self.b_7)
        self.button_8.clicked.connect(self.b_8)
        self.button_9.clicked.connect(self.b_9)
        self.button_A.clicked.connect(self.b_A)
        self.button_B.clicked.connect(self.b_B)
        self.button_E.clicked.connect(self.b_E)
        self.button_K.clicked.connect(self.b_K)
        self.button_M.clicked.connect(self.b_M)
        self.button_H.clicked.connect(self.b_H)
        self.button_O.clicked.connect(self.b_O)
        self.button_P.clicked.connect(self.b_P)
        self.button_C.clicked.connect(self.b_C)
        self.button_T.clicked.connect(self.b_T)
        self.button_Y.clicked.connect(self.b_Y)
        self.button_X.clicked.connect(self.b_X)

        
    def podcshet(self):
        bit = self.lineEdit.text()
        cshet =len(bit)
        if cshet == 6:
            self.lineEdit.setText(bit + str(" "))

    def nazad(self):
        text.pop(0)
        self.w3 = MyWin()
        self.w3.show()
        self.close()
    def dalee(self):
        if len(self.lineEdit.text()) >= 9:
            text.append(self.lineEdit.text())
            self.w4 = Window2()
            self.w4.show()
            self.close()
        else:
            pass
        
    def udal(self):
        udalenie = self.lineEdit.text()
        podschet = len(udalenie)
        if podschet == 7:
            self.lineEdit.setText(str(udalenie[:-2]))
        else:
            self.lineEdit.setText(str(udalenie[:-1]))
    def b_0(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(0))
    def b_1(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(1))
    def b_2(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(2))
    def b_3(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(3))
    def b_4(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(4))
    def b_5(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(5))
    def b_6(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(6))
    def b_7(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(7))
    def b_8(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(8))
    def b_9(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit.text()) == 4 or len(self.lineEdit.text()) == 5:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(9))
    def b_A(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('A'))
    def b_B(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('B'))
    def b_E(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('E'))
    def b_K(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('K'))
    def b_M(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('M'))
    def b_H(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('H'))
    def b_O(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('O'))
    def b_P(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('P'))
    def b_C(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('C'))
    def b_T(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('T'))
    def b_Y(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('У'))
    def b_X(self):
        if len(self.lineEdit.text()) == 1 or len(self.lineEdit.text()) == 2 or len(self.lineEdit.text()) == 3 or len(self.lineEdit.text()) == 7 or len(self.lineEdit.text()) == 8 or len(self.lineEdit.text()) == 9:
            print("ERROR")
            error()
        else:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str('X'))
class Window2(QWidget):
    def __init__(self, parent=None):
        super(Window2, self).__init__()
        super(Window2, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Время парковки')
        self.resize(1000, 720)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(720)
        print(text)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(280, 120, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_1.setFont(font)
        self.label_1.setText('Время начала парковки')
        self.label_1.setStyleSheet("color: rgb(51,122,183)")
        
        self.label_time = QtWidgets.QLabel(self)
        self.label_time.setGeometry(QtCore.QRect(450, 220, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_time.setFont(font)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        self.label_time.setText(current_time)
        self.label_time.setStyleSheet("color: rgb(51,122,183)")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(280, 350, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setText('Длительность парковки')
        self.label_2.setStyleSheet("color: rgb(51,122,183)")

        self.label_vrem = QtWidgets.QLabel(self)
        self.label_vrem.setGeometry(QtCore.QRect(440, 450, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_vrem.setFont(font)
        self.label_vrem.setText('10 мин.')
        self.label_vrem.setStyleSheet("color: rgb(51,122,183)")

        self.button_1 = QPushButton(self)
        self.button_1.setMouseTracking(True)
        self.button_1.setGeometry(QtCore.QRect(360, 450, 60, 60))
        font_2 = QtGui.QFont()
        font_2.setPointSize(20)
        self.button_1.setFont(font_2)
        self.button_1.setText('◄')
        self.button_1.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(620, 450, 60, 60))
        self.button_2.setFont(font_2)
        self.button_2.setText('►')
        self.button_2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_nazad2 = QPushButton(self)
        self.button_nazad2.setGeometry(QtCore.QRect(30, 650, 120, 50))
        self.button_nazad2.setFont(font_2)
        self.button_nazad2.setText(' ⇦ Назад')
        self.button_nazad2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_dalee2 = QPushButton(self)
        self.button_dalee2.setGeometry(QtCore.QRect(850, 650, 120, 50))
        self.button_dalee2.setFont(font_2)
        self.button_dalee2.setText('Далее ⇨ ')
        self.button_dalee2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_nazad2.clicked.connect(self.nazad)
        self.button_dalee2.clicked.connect(self.dalee)
        self.button_1.clicked.connect(self.minus)
        self.button_2.clicked.connect(self.plus)
        self.button_1.pressed.connect(lambda: self.btn_pressed('-1'))
        self.button_1.released.connect(self.btn_released)        
        self.button_2.pressed.connect(lambda: self.btn_pressed('+1'))
        self.button_2.released.connect(self.btn_released)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_clicked)
        self.timer.setInterval(80)
        
        self.text = None
        
    def btn_pressed(self, text):
        self.text = text
        self.timer.start()

    def btn_released(self):
        self.timer.stop()        

    def on_clicked(self):                                      
        #print(f'{self.text}')  
        if self.text == "-1":
            text = self.label_vrem.text()
            if len(text) <= 7:
                a = (int(text[:2]))
                if a >= 2:
                    self.label_vrem.setText(str(a-1) + " мин.")
            else:
                a = (int(text[:3]))
                if a >= 2:
                    self.label_vrem.setText(str(a-1) + " мин.")
        elif self.text == "+1":
            text = self.label_vrem.text()
            if len(text) <= 7:
                a = (int(text[:2]) + 1)
                self.label_vrem.setText(str(a) + " мин.")
            else:
                a = (int(text[:3]) + 1)
                self.label_vrem.setText(str(a) + " мин.")
                
    def minus(self):
        text1 = self.label_vrem.text()
        if len(text1) <= 7:
            a = (int(text1[:2]))
            if a >= 2:
                self.label_vrem.setText(str(a-1) + " мин.")
        else:
            a = (int(text1[:3]))
            if a >= 2:
                self.label_vrem.setText(str(a-1) + " мин.")

    def plus(self):
        text1 = self.label_vrem.text()
        if len(text1) <= 7:
            a = (int(text1[:2]) + 1)
            self.label_vrem.setText(str(a) + " мин.")
        else:
            a = (int(text1[:3]) + 1)
            self.label_vrem.setText(str(a) + " мин.")
        

    def nazad(self):
        self.w3 = Window1()
        self.w3.show()
        self.w3.lineEdit.setText(text[1])
        print(text[1])
        text.pop(1)
        self.close()
    def dalee(self):
        if len(self.label_vrem.text()) <= 7:
            text.append(self.label_vrem.text()[:2])
        else:
            text.append(self.label_vrem.text()[:3])
        text.append(self.label_time.text())
        self.w4 = Window3()
        self.w4.show()
        self.close()
class Window3(QWidget):
    def __init__(self, parent=None):
        super(Window3, self).__init__()
        super(Window3, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Оплата парковки')
        self.resize(1000, 720)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(720)
        print(text)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("card4.png").scaled(700, 450)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(700, 450)
        self.lbl1.move(150, 10)

        self.button_nazad2 = QPushButton(self)
        self.button_nazad2.setGeometry(QtCore.QRect(30, 650, 120, 50))
        font_2 = QtGui.QFont()
        font_2.setPointSize(20)
        self.button_nazad2.setFont(font_2)
        self.button_nazad2.setText(' ⇦ Назад')
        self.button_nazad2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_dalee2 = QPushButton(self)
        self.button_dalee2.setGeometry(QtCore.QRect(840, 650, 130, 50))
        self.button_dalee2.setFont(font_2)
        self.button_dalee2.setText('Оплатить')
        self.button_dalee2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_0 = QPushButton(self)
        self.button_0.setGeometry(QtCore.QRect(260, 470, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_0.setFont(font)
        self.button_0.setText('0')
        self.button_0.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(360, 470, 70, 70))
        self.button_1.setFont(font)
        self.button_1.setText('1')
        self.button_1.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(460, 470, 70, 70))
        self.button_2.setFont(font)
        self.button_2.setText('2')
        self.button_2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        
        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(QtCore.QRect(560, 470, 70, 70))
        self.button_3.setFont(font)
        self.button_3.setText('3')
        self.button_3.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_4 = QPushButton(self)
        self.button_4.setGeometry(QtCore.QRect(660, 470, 70, 70))
        self.button_4.setFont(font)
        self.button_4.setText('4')
        self.button_4.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_5 = QPushButton(self)
        self.button_5.setGeometry(QtCore.QRect(260, 570, 70, 70))
        self.button_5.setFont(font)
        self.button_5.setText('5')
        self.button_5.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_6 = QPushButton(self)
        self.button_6.setGeometry(QtCore.QRect(360, 570, 70, 70))
        self.button_6.setFont(font)
        self.button_6.setText('6')
        self.button_6.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_7 = QPushButton(self)
        self.button_7.setGeometry(QtCore.QRect(460, 570, 70, 70))
        self.button_7.setFont(font)
        self.button_7.setText('7')
        self.button_7.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_8 = QPushButton(self)
        self.button_8.setGeometry(QtCore.QRect(560, 570, 70, 70))
        self.button_8.setFont(font)
        self.button_8.setText('8')
        self.button_8.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_9 = QPushButton(self)
        self.button_9.setGeometry(QtCore.QRect(660, 570, 70, 70))
        self.button_9.setFont(font)
        self.button_9.setText('9')
        self.button_9.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 35px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        self.button_del = QPushButton(self)
        self.button_del.setGeometry(QtCore.QRect(760, 470, 70, 70))
        font_2 = QtGui.QFont()
        font_2.setPointSize(20)
        self.button_del.setFont(font_2)
        self.button_del.setText('⌫')
        self.button_del.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")


        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(265, 250, 495, 50))
        font1 = QtGui.QFont()
        font1.setPointSize(35)
        self.lineEdit.setFont(font1)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        self.lineEdit.setPlaceholderText("0000 0000 0000 0000")
        self.lineEdit.setFocus()
        self.lineEdit.setMaxLength(19)
        self.lineEdit.setReadOnly(True)
        global focus
        focus = []

        self.label_valid = QtWidgets.QLabel(self)
        self.label_valid.setGeometry(QtCore.QRect(345, 297, 50, 30))
        font_val = QtGui.QFont()
        font_val.setPointSize(7)
        self.label_valid.setFont(font_val)
        self.label_valid.setText("VALID")
        self.label_valid.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.label_thru = QtWidgets.QLabel(self)
        self.label_thru.setGeometry(QtCore.QRect(347, 307, 50, 30))
        self.label_thru.setFont(font_val)
        self.label_thru.setText("THRU")
        self.label_thru.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 300, 37, 30))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        self.lineEdit_2.setPlaceholderText("00")
        self.lineEdit_2.setReadOnly(True)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(420, 297, 20, 30))
        self.label_1.setFont(font2)
        self.label_1.setText("/")
        self.label_1.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(433, 300, 37, 30))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        self.lineEdit_3.setPlaceholderText("00")
        self.lineEdit_3.setReadOnly(True)

        self.label_cvv = QtWidgets.QLabel(self)
        self.label_cvv.setGeometry(QtCore.QRect(575, 300, 50, 30))
        font_cvv = QtGui.QFont()
        font_cvv.setPointSize(15)
        self.label_cvv.setFont(font_cvv)
        self.label_cvv.setText("CVV")
        self.label_cvv.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 300, 50, 30))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        self.lineEdit_4.setPlaceholderText("000")
        self.lineEdit_4.setReadOnly(True)

        self.button_nazad2.clicked.connect(self.nazad)
        self.button_dalee2.clicked.connect(self.oplatit)
        self.button_0.clicked.connect(self.podcshet)
        self.button_1.clicked.connect(self.podcshet)
        self.button_2.clicked.connect(self.podcshet)
        self.button_3.clicked.connect(self.podcshet)
        self.button_4.clicked.connect(self.podcshet)
        self.button_5.clicked.connect(self.podcshet)
        self.button_6.clicked.connect(self.podcshet)
        self.button_7.clicked.connect(self.podcshet)
        self.button_8.clicked.connect(self.podcshet)
        self.button_9.clicked.connect(self.podcshet)
        self.button_0.clicked.connect(self.b_0)
        self.button_1.clicked.connect(self.b_1)
        self.button_2.clicked.connect(self.b_2)
        self.button_3.clicked.connect(self.b_3)
        self.button_4.clicked.connect(self.b_4)
        self.button_5.clicked.connect(self.b_5)
        self.button_6.clicked.connect(self.b_6)
        self.button_7.clicked.connect(self.b_7)
        self.button_8.clicked.connect(self.b_8)
        self.button_9.clicked.connect(self.b_9)
        self.button_del.clicked.connect(self.udal)
        
    def podcshet(self):
        bit = self.lineEdit.text()
        cshet = len(bit)
        if cshet == 4 or cshet == 9 or cshet == 14:
            self.lineEdit.setText(bit + str(" "))

    def udal(self):
        udalenie = self.lineEdit.text()
        podschet = len(udalenie)
        if len(self.lineEdit.text()) <= 18 and (podschet == 5 or podschet == 10 or podschet == 15):
            self.lineEdit.setText(str(udalenie[:-2]))
        elif len(self.lineEdit.text()) <= 19 and len(self.lineEdit_2.text()) == 0 and len(self.lineEdit_3.text()) == 0 and len(self.lineEdit_4.text()) == 0:
            self.lineEdit.setText(str(udalenie[:-1]))
        elif len(self.lineEdit_2.text()) <= 2 and len(self.lineEdit_3.text()) == 0 and len(self.lineEdit_4.text()) == 0:
            self.lineEdit_2.setText(str(self.lineEdit_2.text()[:-1]))
        elif len(self.lineEdit_3.text()) <= 2 and len(self.lineEdit_4.text()) == 0:
            self.lineEdit_3.setText(str(self.lineEdit_3.text()[:-1]))
        elif len(self.lineEdit_4.text()) <= 3:
            self.lineEdit_4.setText(str(self.lineEdit_4.text()[:-1]))
        
    def b_0(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(0))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(0))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(0))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(0))
    def b_1(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(1))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(1))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(1))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(1))
    def b_2(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(2))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(2))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(2))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(2))
    def b_3(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(3))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(3))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(3))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(3))
    def b_4(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(4))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(4))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(4))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(4))
    def b_5(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(5))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(5))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(5))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(5))
    def b_6(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(6))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(6))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(6))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(6))
    def b_7(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(7))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(7))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(7))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(7))
    def b_8(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(8))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(8))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(8))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(8))
    def b_9(self):
        if len(self.lineEdit.text()) <= 18:
            bit = self.lineEdit.text()
            self.lineEdit.setText(bit + str(9))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 0:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 1 and int(self.lineEdit_2.text()) == 1:
            print("ZAPRET")
            error()
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) <= 1:
            bit = self.lineEdit_2.text()
            self.lineEdit_2.setText(bit + str(9))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(self.lineEdit_3.text()) <= 1:
            bit = self.lineEdit_3.text()
            self.lineEdit_3.setText(bit + str(9))
        elif len(self.lineEdit.text()) == 19 and len(self.lineEdit_2.text()) == 2 and len(
                self.lineEdit_3.text()) == 2 and len(self.lineEdit_4.text()) <= 2:
            bit = self.lineEdit_4.text()
            self.lineEdit_4.setText(bit + str(9))

    def nazad(self):
        self.w3 = Window2()
        self.w3.show()
        self.w3.label_vrem.setText(text[2] + " мин.")
        text.pop(3)
        text.pop(2)
        self.close()
    def oplatit(self):
        if len(self.lineEdit_4.text()) == 3:
            self.w3 = Window4()
            self.w3.show()
            self.close()
        else:
            pass

class Window4(QWidget):
    def __init__(self, parent=None):
        super(Window4, self).__init__()
        super(Window4, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Парковочный чек')
        self.resize(1000, 720)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(720)
        import datetime as DT

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(405, 140, 200, 30))
        font_1 = QtGui.QFont()
        font_1.setPointSize(15)
        self.label_1.setFont(font_1)
        self.label_1.setText("ПАРКОВОЧНЫЙ ЧЕК")

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(390, 170, 230, 30))
        self.label_12.setFont(font_1)
        self.label_12.setText("********************")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(390, 210, 200, 30))
        self.label_2.setFont(font_1)
        self.label_2.setText("ГРЗ ТС:  " + str(text[1]))

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(390, 240, 250, 30))
        self.label_3.setFont(font_1)
        date = DT.datetime.today()
        self.label_3.setText("Начало парковки: " + str(date.strftime('%H:%M')))

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(390, 270, 250, 30))
        self.label_4.setFont(font_1)
        date += DT.timedelta(minutes=int(text[2]))
        self.label_4.setText("Конец парковки:   " + str(date.strftime('%H:%M')))

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(390, 300, 250, 30))
        self.label_5.setFont(font_1)
        self.label_5.setText("Сумма к оплате: " + str(int(text[2]) * 5) + " p.")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(390, 330, 250, 30))
        self.label_6.setFont(font_1)
        self.label_6.setText("Зона парковки: " + str(text[0]))

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(370, 400, 300, 30))
        self.label_7.setFont(font_1)
        self.label_7.setText("Спасибо за оплату парковки!" )

        self.button_del = QPushButton(self)
        self.button_del.setGeometry(QtCore.QRect(790, 620, 150, 60))
        font_2 = QtGui.QFont()
        font_2.setPointSize(20)
        self.button_del.setFont(font_2)
        self.button_del.setText('На главную')
        self.button_del.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        date = DT.datetime.today()
        print(date.strftime('%H:%M'))
        self. button_del.clicked.connect(self.glavnay)
        
    def paintEvent(self, e):
        qp = QPainter(self)
        qp.setBrush(QBrush(Qt.white))
        qp.drawRect(275,100,450,400)
    def glavnay(self):
        print("GO")
        text2.append(text[0])
        MyDictionary[text[0]] = str(text[2])
        print(MyDictionary)
        print(text2)
        self.w3 = MyWin()
        self.w3.show()
        self.close()
        text.clear()
        print(text)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = MyWin()
    ico = QtGui.QIcon("Park.png")
    ui1.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    ui1.show()
    sys.exit(app.exec_())
    
