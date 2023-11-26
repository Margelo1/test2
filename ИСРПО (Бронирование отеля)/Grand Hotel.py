from PyQt5.QtWidgets import QMessageBox
import random
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
from datetime import date
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QIntValidator
import sys
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import qrcode # pip install qrcode
import sqlite3
global text
text = []
text22 = []
class Window1(QWidget):
    def __init__(self, parent=None):
        super(Window1, self).__init__()
        super(Window1, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('LeGrand HOTEL')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRAND.jpg").scaled(1200, 720)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(1200, 720)
        self.lbl1.move(0, 0)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 50)
        
        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(50, 20, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_1.setFont(font)
        self.button_1.setText('Обзор')
        self.button_1.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_1.clicked.connect(self.obzor)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(270, 20, 200, 40))
        self.button_2.setFont(font)
        self.button_2.setText('Посмотреть номера')
        self.button_2.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_2.clicked.connect(self.rooms)
        
        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(QtCore.QRect(530, 20, 160, 40))
        self.button_3.setFont(font)
        self.button_3.setText('Забронировать')
        self.button_3.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_3.clicked.connect(self.brony)

        self.button_4 = QPushButton(self)
        self.button_4.setGeometry(QtCore.QRect(750, 20, 200, 40))
        self.button_4.setFont(font)
        self.button_4.setText('Посмотреть на карте')
        self.button_4.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_4.clicked.connect(self.karta)

        self.button_5 = QPushButton(self)
        self.button_5.setGeometry(QtCore.QRect(970, 20, 160, 40))
        self.button_5.setFont(font)
        self.button_5.setText('Ресторан')
        self.button_5.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_5.clicked.connect(self.restoran)

    def karta(self):
        self.myApp = MyApp()
        self.myApp.show()
    def rooms(self):
        self.w2 = Window2()
        self.w2.show()
        self.close()
    def brony(self):
        self.w3 = Window3()
        self.w3.show()
        self.close()
    def restoran(self):
        self.w4 = Window8()
        self.w4.show()
        self.close()
    def obzor(self):
        self.w5 = Window21()
        self.w5.show()
        self.close()

class Window21(QWidget):
    def __init__(self, parent=None):
        super(Window21, self).__init__()
        super(Window21, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Об отеле')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 0)

        self.label_l = QtWidgets.QLabel(self)
        self.label_l.setGeometry(QtCore.QRect(100, 180, 1000, 400))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_l.setFont(font)
        self.label_l.setText('Этот престижный 5-звездочный отель расположен прямо на берегу моря в Кабуре. К услугам гостей\nстильные номера, некоторые с видом на море, ресторан изысканной кухни, бар и выход на частный пляж.\nГости могут бесплатно посещать сауну, сенсорный душ и хаммам.\nНомера отеля Le Grand Hоtel Cabourg элегантно оформлены, в некоторых из них есть камин. Они\nоснащены телевизором с плоским экраном со спутниковыми каналами и бесплатным беспроводным\nдоступом в Интернет. В каждой собственной ванной комнате предоставляются роскошные\nтуалетно-косметические принадлежности, халаты и тапочки.\nВкусный завтрак "шведский стол" подается каждое утро в ресторане с видом на море. В ресторане\nLe Grand с панорамным видом на море подают изысканные блюда из морепродуктов и региональные\nблюда. В летнее время гости могут насладиться трапезой на открытой террасе.\nВ баре Le Grand предлагается широкий выбор коктейлей и закусок, а также проводятся музыкальные\nмероприятия. Также имеется лаундж, где гости могут расслабиться. За дополнительную плату можно\nзаказать массажные процедуры.\nЭто любимая часть города Кабур среди наших гостей согласно естественным отзывам.')
        self.label_l.setStyleSheet("color: rgb(51,122,183)")

        self.button_glav = QPushButton(self)
        self.button_glav.setGeometry(QtCore.QRect(80, 610, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_glav.setFont(font)
        self.button_glav.setText('На главную')
        self.button_glav.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_glav.clicked.connect(self.glavnay)

    def glavnay(self):
        text.clear()
        self.w1 = Window1()
        self.w1.show()
        self.close()

class Window2(QWidget):
    def __init__(self, parent=None):
        super(Window2, self).__init__()
        super(Window2, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('HOTEL ROOMS')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.label_l = QtWidgets.QLabel(self)
        self.label_l.setGeometry(QtCore.QRect(270, 30, 900, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_l.setFont(font)
        self.label_l.setText('Номера            Число гостей    Цена за 1 ночь')
        self.label_l.setStyleSheet("color: Blue")

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(90, 150, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_1.setFont(font)
        self.button_1.setText('CLASSIC ROOM')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_1.clicked.connect(self.room1)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(570, 150, 300, 60))
        self.label_1.setFont(font)
        self.label_1.setText('👤👤')

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(900, 150, 500, 60))
        self.label_12.setFont(font)
        self.label_12.setText('5500 ₽')
        self.label_12.setStyleSheet("color: rgb(51,122,183)")

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(90, 250, 500, 60))
        self.button_2.setFont(font)
        self.button_2.setText('FAMILY ROOM')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.room2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(570, 250, 300, 60))
        self.label_2.setFont(font)
        self.label_2.setText('👤👤👤👤')

        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(900, 250, 500, 60))
        self.label_22.setFont(font)
        self.label_22.setText('8700 ₽')
        self.label_22.setStyleSheet("color: rgb(51,122,183)")

        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(QtCore.QRect(90, 350, 500, 60))
        self.button_3.setFont(font)
        self.button_3.setText('DELUXE ROOM')
        self.button_3.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_3.clicked.connect(self.room3)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(570, 350, 300, 60))
        self.label_3.setFont(font)
        self.label_3.setText('👤👤')

        self.label_32 = QtWidgets.QLabel(self)
        self.label_32.setGeometry(QtCore.QRect(900, 350, 500, 60))
        self.label_32.setFont(font)
        self.label_32.setText('9500 ₽')
        self.label_32.setStyleSheet("color: rgb(51,122,183)")

        self.button_4 = QPushButton(self)
        self.button_4.setGeometry(QtCore.QRect(90, 450, 500, 60))
        self.button_4.setFont(font)
        self.button_4.setText('SUITE ROOM')
        self.button_4.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_4.clicked.connect(self.room4)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(570, 450, 300, 60))
        self.label_4.setFont(font)
        self.label_4.setText('👤👤👤👤')

        self.label_42 = QtWidgets.QLabel(self)
        self.label_42.setGeometry(QtCore.QRect(900, 450, 500, 60))
        self.label_42.setFont(font)
        self.label_42.setText('11500 ₽')
        self.label_42.setStyleSheet("color: rgb(51,122,183)")

    def nazad(self):
        self.w2 = Window1()
        self.w2.show()
        self.close()
    def room1(self):
        self.w3 = Window_room1()
        self.w3.show()
        self.close()
    def room2(self):
        self.w3 = Window_room2()
        self.w3.show()
        self.close()
    def room3(self):
        self.w3 = Window_room3()
        self.w3.show()
        self.close()
    def room4(self):
        self.w3 = Window_room4()
        self.w3.show()
        self.close()
global chetchik
chetchik = 1
global chetchik2
chetchik2 = 1
global chetchik3
chetchik3 = 1
global chetchik4
chetchik4 = 1

class Window_room1(QWidget):
    def __init__(self, parent=None):
        super(Window_room1, self).__init__()
        super(Window_room1, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('CLASSIC ROOM')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("R1_1.jpg").scaled(800, 600)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(800, 600)
        self.lbl1.move(50, 30)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(800, 30, 50, 600))
        font1 = QtGui.QFont()
        font1.setPointSize(40)
        self.button_1.setFont(font1)
        self.button_1.setText('🞂')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue;}")
        self.button_1.clicked.connect(self.dal)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(50, 30, 50, 600))
        self.button_2.setFont(font1)
        self.button_2.setText('🞀')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.naz)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(880, 50, 300, 100))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setText('Стандартный номер\nc 2 спальной кроватью,\nс боковым видом на сад')
        self.label_1.setStyleSheet('color: rgb(51,122,183)')

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(880, 160, 300, 100))
        self.label_2.setFont(font2)
        self.label_2.setText('Число гостей\n2 человека')
        self.label_2.setStyleSheet('color: rgb(51,122,183)')

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(880, 260, 300, 100))
        self.label_3.setFont(font2)
        self.label_3.setText('Площадь\n 31m²')
        self.label_3.setStyleSheet('color: rgb(51,122,183)')

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(880, 360, 300, 100))
        self.label_4.setFont(font2)
        self.label_4.setText('Стоимость\n 5500 ₽')
        self.label_4.setStyleSheet('color: rgb(51,122,183)')

        self.button_bron = QPushButton(self)
        self.button_bron.setGeometry(QtCore.QRect(930, 500, 200, 40))
        self.button_bron.setFont(font)
        self.button_bron.setText('ЗАБРОНИРОВАТЬ')
        self.button_bron.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_bron.clicked.connect(self.bron)
    def bron(self):
        text.append('CLASSIC ROOM')
        text.append('5500')
        print(text)
        self.w1 = Window42()
        self.w1.show()
        self.close()

    def nazad(self):
        self.w2 = Window2()
        self.w2.show()
        self.close()
        
    def dal(self):
        global chetchik
        if chetchik == 0:
            self.pix = QtGui.QPixmap("R1_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik += 1
        elif chetchik == 1:
            self.pix = QtGui.QPixmap("R1_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik += 1
        elif chetchik == 2:
            self.pix = QtGui.QPixmap("R1_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik += 1
        elif chetchik == 3:
            self.pix = QtGui.QPixmap("R1_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik += 1
        elif chetchik == 4:
            self.pix = QtGui.QPixmap("R1_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik = 0
    def naz(self):
        global chetchik
        if chetchik == 4:
            self.pix = QtGui.QPixmap("R1_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik -= 1
        elif chetchik == 3:
            self.pix = QtGui.QPixmap("R1_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik -= 1
        elif chetchik == 2:
            self.pix = QtGui.QPixmap("R1_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik -= 1
        elif chetchik == 1:
            self.pix = QtGui.QPixmap("R1_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik -= 1
        elif chetchik == 0:
            self.pix = QtGui.QPixmap("R1_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik += 4

class Window_room2(QWidget):
    def __init__(self, parent=None):
        super(Window_room2, self).__init__()
        super(Window_room2, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('FAMILY ROOM')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("R2_1.jpg").scaled(800, 600)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(800, 600)
        self.lbl1.move(50, 30)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(800, 30, 50, 600))
        font1 = QtGui.QFont()
        font1.setPointSize(40)
        self.button_1.setFont(font1)
        self.button_1.setText('🞂')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue;}")
        self.button_1.clicked.connect(self.dal)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(50, 30, 50, 600))
        self.button_2.setFont(font1)
        self.button_2.setText('🞀')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.naz)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(880, 50, 300, 100))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setText('Большой номер\nc 2 спальной кроватью\nи с 2 спальным диваном')
        self.label_1.setStyleSheet('color: rgb(51,122,183)')

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(880, 160, 300, 100))
        self.label_2.setFont(font2)
        self.label_2.setText('Число гостей\n4 человека')
        self.label_2.setStyleSheet('color: rgb(51,122,183)')

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(880, 260, 300, 100))
        self.label_3.setFont(font2)
        self.label_3.setText('Площадь\n 37m²')
        self.label_3.setStyleSheet('color: rgb(51,122,183)')

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(880, 360, 300, 100))
        self.label_4.setFont(font2)
        self.label_4.setText('Стоимость\n 8700 ₽')
        self.label_4.setStyleSheet('color: rgb(51,122,183)')

        self.button_bron = QPushButton(self)
        self.button_bron.setGeometry(QtCore.QRect(930, 500, 200, 40))
        self.button_bron.setFont(font)
        self.button_bron.setText('ЗАБРОНИРОВАТЬ')
        self.button_bron.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_bron.clicked.connect(self.bron)

    def bron(self):
        text.append('FAMILY ROOM')
        text.append('8700')
        print(text)
        self.w1 = Window42()
        self.w1.show()
        self.close()

    def nazad(self):
        self.w2 = Window2()
        self.w2.show()
        self.close()
        
    def dal(self):
        global chetchik2
        if chetchik2 == 0:
            self.pix = QtGui.QPixmap("R2_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 += 1
        elif chetchik2 == 1:
            self.pix = QtGui.QPixmap("R2_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 += 1
        elif chetchik2 == 2:
            self.pix = QtGui.QPixmap("R2_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 += 1
        elif chetchik2 == 3:
            self.pix = QtGui.QPixmap("R2_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 += 1
        elif chetchik2 == 4:
            self.pix = QtGui.QPixmap("R2_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 = 0
    def naz(self):
        global chetchik2
        if chetchik2 == 4:
            self.pix = QtGui.QPixmap("R2_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 -= 1
        elif chetchik2 == 3:
            self.pix = QtGui.QPixmap("R2_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 -= 1
        elif chetchik2 == 2:
            self.pix = QtGui.QPixmap("R2_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 -= 1
        elif chetchik2 == 1:
            self.pix = QtGui.QPixmap("R2_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 -= 1
        elif chetchik2 == 0:
            self.pix = QtGui.QPixmap("R2_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik2 += 4

class Window_room3(QWidget):
    def __init__(self, parent=None):
        super(Window_room3, self).__init__()
        super(Window_room3, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('DELUXE ROOM')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("R3_1.jpg").scaled(800, 600)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(800, 600)
        self.lbl1.move(50, 30)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(800, 30, 50, 600))
        font1 = QtGui.QFont()
        font1.setPointSize(40)
        self.button_1.setFont(font1)
        self.button_1.setText('🞂')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue;}")
        self.button_1.clicked.connect(self.dal)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(50, 30, 50, 600))
        self.button_2.setFont(font1)
        self.button_2.setText('🞀')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.naz)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(880, 50, 300, 100))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setText('Большой номер\nc 2 спальной кроватью\nс видом на пляж')
        self.label_1.setStyleSheet('color: rgb(51,122,183)')

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(880, 160, 300, 100))
        self.label_2.setFont(font2)
        self.label_2.setText('Число гостей\n2 человека')
        self.label_2.setStyleSheet('color: rgb(51,122,183)')

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(880, 260, 300, 100))
        self.label_3.setFont(font2)
        self.label_3.setText('Площадь\n 37m²')
        self.label_3.setStyleSheet('color: rgb(51,122,183)')

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(880, 360, 300, 100))
        self.label_4.setFont(font2)
        self.label_4.setText('Стоимость\n 9500 ₽')
        self.label_4.setStyleSheet('color: rgb(51,122,183)')

        self.button_bron = QPushButton(self)
        self.button_bron.setGeometry(QtCore.QRect(930, 500, 200, 40))
        self.button_bron.setFont(font)
        self.button_bron.setText('ЗАБРОНИРОВАТЬ')
        self.button_bron.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_bron.clicked.connect(self.bron)

    def bron(self):
        text.append('DELUXE ROOM')
        text.append('9500')
        print(text)
        self.w1 = Window42()
        self.w1.show()
        self.close()

    def nazad(self):
        self.w2 = Window2()
        self.w2.show()
        self.close()
        
    def dal(self):
        global chetchik3
        if chetchik3 == 0:
            self.pix = QtGui.QPixmap("R3_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 += 1
        elif chetchik3 == 1:
            self.pix = QtGui.QPixmap("R3_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 += 1
        elif chetchik3 == 2:
            self.pix = QtGui.QPixmap("R3_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 += 1
        elif chetchik3 == 3:
            self.pix = QtGui.QPixmap("R3_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 += 1
        elif chetchik3 == 4:
            self.pix = QtGui.QPixmap("R3_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 = 0
    def naz(self):
        global chetchik3
        if chetchik3 == 4:
            self.pix = QtGui.QPixmap("R3_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 -= 1
        elif chetchik3 == 3:
            self.pix = QtGui.QPixmap("R3_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 -= 1
        elif chetchik3 == 2:
            self.pix = QtGui.QPixmap("R3_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 -= 1
        elif chetchik3 == 1:
            self.pix = QtGui.QPixmap("R3_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 -= 1
        elif chetchik3 == 0:
            self.pix = QtGui.QPixmap("R3_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik3 += 4

class Window_room4(QWidget):
    def __init__(self, parent=None):
        super(Window_room4, self).__init__()
        super(Window_room4, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('SUITE ROOM')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("R4_1.jpg").scaled(800, 600)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(800, 600)
        self.lbl1.move(50, 30)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(800, 30, 50, 600))
        font1 = QtGui.QFont()
        font1.setPointSize(40)
        self.button_1.setFont(font1)
        self.button_1.setText('🞂')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue;}")
        self.button_1.clicked.connect(self.dal)

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(50, 30, 50, 600))
        self.button_2.setFont(font1)
        self.button_2.setText('🞀')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,50); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.naz)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(880, 50, 300, 100))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setText('Люкс номер\nc 2 спальной кроватью\nи с 2 спальным диваном')
        self.label_1.setStyleSheet('color: rgb(51,122,183)')

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(880, 160, 300, 100))
        self.label_2.setFont(font2)
        self.label_2.setText('Число гостей\n4 человека')
        self.label_2.setStyleSheet('color: rgb(51,122,183)')

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(880, 260, 300, 100))
        self.label_3.setFont(font2)
        self.label_3.setText('Площадь\n 98m²')
        self.label_3.setStyleSheet('color: rgb(51,122,183)')

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(880, 360, 300, 100))
        self.label_4.setFont(font2)
        self.label_4.setText('Стоимость\n 11500 ₽')
        self.label_4.setStyleSheet('color: rgb(51,122,183)')

        self.button_bron = QPushButton(self)
        self.button_bron.setGeometry(QtCore.QRect(930, 500, 200, 40))
        self.button_bron.setFont(font)
        self.button_bron.setText('ЗАБРОНИРОВАТЬ')
        self.button_bron.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_bron.clicked.connect(self.bron)

    def bron(self):
        text.append('SUITE ROOM')
        text.append('11500')
        print(text)
        self.w1 = Window42()
        self.w1.show()
        self.close()

    def nazad(self):
        self.w2 = Window2()
        self.w2.show()
        self.close()
        
    def dal(self):
        global chetchik4
        if chetchik4 == 0:
            self.pix = QtGui.QPixmap("R4_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 += 1
        elif chetchik4 == 1:
            self.pix = QtGui.QPixmap("R4_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 += 1
        elif chetchik4 == 2:
            self.pix = QtGui.QPixmap("R4_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 += 1
        elif chetchik4 == 3:
            self.pix = QtGui.QPixmap("R4_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 += 1
        elif chetchik4 == 4:
            self.pix = QtGui.QPixmap("R4_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 = 0
    def naz(self):
        global chetchik4
        if chetchik4 == 4:
            self.pix = QtGui.QPixmap("R4_3.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 -= 1
        elif chetchik4 == 3:
            self.pix = QtGui.QPixmap("R4_2.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 -= 1
        elif chetchik4 == 2:
            self.pix = QtGui.QPixmap("R4_1.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 -= 1
        elif chetchik4 == 1:
            self.pix = QtGui.QPixmap("R4_5.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 -= 1
        elif chetchik4 == 0:
            self.pix = QtGui.QPixmap("R4_4.jpg").scaled(800, 600)
            self.lbl1.setPixmap(self.pix)
            chetchik4 += 4

class Window3(QWidget):
    def __init__(self, parent=None):
        super(Window3, self).__init__()
        super(Window3, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Бронирование')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.label_l = QtWidgets.QLabel(self)
        self.label_l.setGeometry(QtCore.QRect(270, 30, 900, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_l.setFont(font)
        self.label_l.setText('Номера            Число гостей    Цена за 1 ночь')
        self.label_l.setStyleSheet("color: Blue")

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(90, 150, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_1.setFont(font)
        self.button_1.setText('CLASSIC ROOM')
        self.button_1.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_1.clicked.connect(self.room1)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(570, 150, 300, 60))
        self.label_1.setFont(font)
        self.label_1.setText('👤👤')

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(900, 150, 500, 60))
        self.label_12.setFont(font)
        self.label_12.setText('5500 ₽')
        self.label_12.setStyleSheet("color: rgb(51,122,183)")

        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(90, 250, 500, 60))
        self.button_2.setFont(font)
        self.button_2.setText('FAMILY ROOM')
        self.button_2.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_2.clicked.connect(self.room2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(570, 250, 300, 60))
        self.label_2.setFont(font)
        self.label_2.setText('👤👤👤👤')

        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(900, 250, 500, 60))
        self.label_22.setFont(font)
        self.label_22.setText('8700 ₽')
        self.label_22.setStyleSheet("color: rgb(51,122,183)")

        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(QtCore.QRect(90, 350, 500, 60))
        self.button_3.setFont(font)
        self.button_3.setText('DELUXE ROOM')
        self.button_3.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_3.clicked.connect(self.room3)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(570, 350, 300, 60))
        self.label_3.setFont(font)
        self.label_3.setText('👤👤')

        self.label_32 = QtWidgets.QLabel(self)
        self.label_32.setGeometry(QtCore.QRect(900, 350, 500, 60))
        self.label_32.setFont(font)
        self.label_32.setText('9500 ₽')
        self.label_32.setStyleSheet("color: rgb(51,122,183)")

        self.button_4 = QPushButton(self)
        self.button_4.setGeometry(QtCore.QRect(90, 450, 500, 60))
        self.button_4.setFont(font)
        self.button_4.setText('SUITE ROOM')
        self.button_4.setStyleSheet("QPushButton {background-color: rgba(255,255,255,0); color: rgb(51,122,183); border: none;}""QPushButton:pressed {background-color:rgba(255,255,255,0); color: Blue; border: none;}")
        self.button_4.clicked.connect(self.room4)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(570, 450, 300, 60))
        self.label_4.setFont(font)
        self.label_4.setText('👤👤👤👤')

        self.label_42 = QtWidgets.QLabel(self)
        self.label_42.setGeometry(QtCore.QRect(900, 450, 500, 60))
        self.label_42.setFont(font)
        self.label_42.setText('11500 ₽')
        self.label_42.setStyleSheet("color: rgb(51,122,183)")

    def nazad(self):
        self.w2 = Window1()
        self.w2.show()
        self.close()
    def room1(self):
        text.append('CLASSIC ROOM')
        text.append('5500')
        print(text)
        self.brony()
    def room2(self):
        text.append('FAMILY ROOM')
        text.append('8700')
        print(text)
        self.brony()
    def room3(self):
        text.append('DELUXE ROOM')
        text.append('9500')
        print(text)
        self.brony()
    def room4(self):
        text.append('SUITE ROOM')
        text.append('11500')
        print(text)
        self.brony()
    def brony(self):
        self.w2 = Window4()
        self.w2.show()
        self.close()

class SimpleDateValidator(QtGui.QValidator):
    def validate(self, text, pos):
        if not text:
            return self.Acceptable, text, pos
        fmt = self.parent().format()
        _sep = set(fmt.replace('d', '').replace('M', '').replace('y', ''))
        
        for l in text:
            if not l.isdigit() and l not in _sep:
                return self.Invalid, text, pos
        years = fmt.count('y')
        if len(text) <= years and text.isdigit():
            return self.Acceptable, text, pos
        if QtCore.QDate.fromString(text, fmt).isValid():
            return self.Acceptable, text, pos
        return self.Intermediate, text, pos


class SimpleDateValidator2(QtGui.QValidator):
    def validate2(self, text2, pos2):
        if not text2:
            return self.Acceptable, text2, pos2
        fmt = self.parent().format2()
        _sep = set(fmt.replace('d', '').replace('M', '').replace('y', ''))

        for l in text2:
            if not l.isdigit() and l not in _sep:
                return self.Invalid, text2, pos2
        years = fmt.count('y')
        if len(text2) <= years and text2.isdigit():
            return self.Acceptable, text2, pos2
        if QtCore.QDate.fromString(text2, fmt).isValid2():
            return self.Acceptable, text2, pos2
        return self.Intermediate, text2, pos2

class Window4(QWidget):
    customFormat = 'dd.MM.yyyy'
    def __init__(self, parent=None):
        super(Window4, self).__init__()
        super(Window4, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Регистрация')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 0)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.button_dalee = QPushButton(self)
        self.button_dalee.setGeometry(QtCore.QRect(990, 650, 160, 40))
        self.button_dalee.setFont(font)
        self.button_dalee.setText('Далее')
        self.button_dalee.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_dalee.clicked.connect(self.dalee)

        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.setGeometry(QtCore.QRect(260, 200, 290, 60))
        font1 = QtGui.QFont()
        font1.setPointSize(30)
        self.lineEdit5.setFont(font1)
        self.lineEdit5.setObjectName("lineEdit")
        self.lineEdit5.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit5.setToolTip("Пример ввода: Иван")
        self.lineEdit5.setFocus()

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(270, 150, 100, 60))
        self.label_1.setFont(font)
        self.label_1.setText('Имя')
        self.label_1.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit6 = QLineEdit(self)
        self.lineEdit6.setGeometry(QtCore.QRect(660, 200, 290, 60))
        self.lineEdit6.setFont(font1)
        self.lineEdit6.setObjectName("lineEdit2")
        self.lineEdit6.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit6.setToolTip("Пример ввода: Иванов")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(670, 150, 100, 60))
        self.label_2.setFont(font)
        self.label_2.setText('Фамилия')
        self.label_2.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(260, 300, 690, 60))
        self.lineEdit3.setFont(font1)
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit3.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit3.setToolTip("Пример ввода: ivanov.ivan@gmail.com")
        self.lineEdit3.setToolTipDuration(5000)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 100, 60))
        self.label_3.setFont(font)
        self.label_3.setText('E-Mail')
        self.label_3.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.setGeometry(QtCore.QRect(260, 400, 690, 60))
        self.lineEdit4.setFont(font1)
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit4.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit4.setToolTip("Пример ввода: +7 800 555 35 35")
        self.lineEdit4.setInputMask('+9 999 999 99 99')
        self.lineEdit4.setMaxLength(11)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(270, 350, 100, 60))
        self.label_4.setFont(font)
        self.label_4.setText('Телефон')
        self.label_4.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(260, 500, 290, 60))
        self.lineEdit.setFont(font1)
        self.lineEdit.setPlaceholderText("ДД.ММ.ГГГГ")
        self.lineEdit.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit.setMaxLength(len(self.format()))
        self.validator = SimpleDateValidator(self)
        self.lineEdit.setValidator(self.validator)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(270, 450, 100, 60))
        self.label_5.setFont(font)
        self.label_5.setText('Заезд')
        self.label_5.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(660, 500, 290, 60))
        self.lineEdit2.setFont(font1)
        self.lineEdit2.setPlaceholderText("ДД.ММ.ГГГГ")
        self.lineEdit2.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit2.setMaxLength(len(self.format2()))
        self.validator2 = SimpleDateValidator2(self)
        self.lineEdit2.setValidator(self.validator)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(670, 450, 100, 60))
        self.label_6.setFont(font)
        self.label_6.setText('Выезд')
        self.label_6.setStyleSheet("color: rgb(51,122,183)")

        self.dropDownButton = QToolButton(self)
        self.dropDownButton.setGeometry(QtCore.QRect(490, 500, 60, 60))
        self.dropDownButton.setFont(font)
        self.dropDownButton.setIcon(QtGui.QIcon("Calendar.ico"))
        self.dropDownButton.setIconSize(QtCore.QSize(35,35))
        self.dropDownButton.setCheckable(True)
        self.dropDownButton.setFocusPolicy(QtCore.Qt.NoFocus)

        self.dropDownButton2 = QToolButton(self)
        self.dropDownButton2.setGeometry(QtCore.QRect(890, 500, 60, 60))
        self.dropDownButton2.setFont(font)
        self.dropDownButton2.setIcon(QtGui.QIcon("Calendar.ico"))
        self.dropDownButton2.setIconSize(QtCore.QSize(35,35))
        self.dropDownButton2.setCheckable(True)
        self.dropDownButton2.setFocusPolicy(QtCore.Qt.NoFocus)

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setWindowFlags(QtCore.Qt.Popup)
        self.calendar.installEventFilter(self)

        self.calendar2 = QtWidgets.QCalendarWidget()
        self.calendar2.setWindowFlags(QtCore.Qt.Popup)
        self.calendar2.installEventFilter(self)
        
        self.dropDownButton.pressed.connect(self.showPopup)
        self.dropDownButton.released.connect(self.calendar.hide)

        self.dropDownButton2.pressed.connect(self.showPopup2)
        self.dropDownButton2.released.connect(self.calendar2.hide)
        
        self.lineEdit.editingFinished.connect(self.editingFinished)
        self.lineEdit2.editingFinished.connect(self.editingFinished2)
        
        self.calendar.clicked.connect(self.setDate)
        self.calendar.activated.connect(self.setDate)

        self.calendar2.clicked.connect(self.setDate2)
        self.calendar2.activated.connect(self.setDate2)
    def editingFinished(self):
        if self.calendar.isVisible(): 
            return
        if not self.isValid():
            self.lineEdit.setText('')

    def format(self):
        return self.customFormat or QtCore.QLocale().dateFormat(QtCore.QLocale.ShortFormat)

    def setFormat(self, format):
        if format and 'MMM' in format or 'ddd' in format:
            return
        self.customFormat = format
        self.setDate(self.calendar.selectedDate())
        self.calendar.hide()
        self.lineEdit.setMaxLength(self.format())
        self.validator.setFormat(self.format())

    def text(self):
        return self.lineEdit.text()

    def date(self):
        if not self.isValid():
            return None
        date = QtCore.QDate.fromString(self.text(), self.format())
        if date.isValid():
            return date
        return int(self.text())

    def setDate(self, date):
        self.lineEdit.setText(date.toString(self.format()))
        self.calendar.setSelectedDate(date)
        self.calendar.hide()

    def setDateRange(self, minimum, maximum):
        self.calendar.setDateRange(minimum, maximum)

    def isValid(self):
        text = self.text()
        if not text:
            return False
        date = QtCore.QDate.fromString(text, self.format())
        if date.isValid():
            self.setDate(date)
            return True
        try:
            year = int(text)
            start = self.calendar.minimumDate().year()
            end = self.calendar.maximumDate().year()
            if start <= year <= end:
                return True
        except:
            pass
        return False

    def hidePopup(self):
        self.calendar.hide()

    def showPopup(self):
        pos = self.lineEdit.mapToGlobal(self.lineEdit.rect().bottomLeft())
        pos += QtCore.QPoint(0, 1)
        rect = QtCore.QRect(pos, self.calendar.sizeHint())
        self.calendar.setGeometry(rect)
        self.calendar.show()
        self.calendar.setFocus()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Hide:
            self.dropDownButton.setDown(False)
        elif event.type() == QtCore.QEvent.Show:
            self.dropDownButton.setDown(True)
        return super().eventFilter(source, event)

    '''def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Down, QtCore.Qt.Key_F4):
            if not self.calendar.isVisible():
                self.showPopup()
        super().keyPressEvent(event)'''

    def editingFinished2(self):
        if self.calendar2.isVisible(): 
            return
        if not self.isValid2():
            self.lineEdit2.setText('')

    def format2(self):
        return self.customFormat or QtCore.QLocale().dateFormat(QtCore.QLocale.ShortFormat)

    def setFormat2(self, format2):
        if format2 and 'MMM' in format2 or 'ddd' in format2:
            return
        self.customFormat = format2
        self.setDate(self.calendar2.selectedDate())
        self.calendar2.hide()
        self.lineEdit2.setMaxLength(self.format2())
        self.validator2.setFormat(self.format2())

    def text2(self):
        return self.lineEdit2.text()

    def date2(self):
        if not self.isValid2():
            return None
        date2 = QtCore.QDate.fromString(self.text2(), self.format2())
        if date2.isValid2():
            return date2
        return int(self.text2())
    def setDate2(self, date2):
        self.lineEdit2.setText(date2.toString(self.format2()))
        self.calendar2.setSelectedDate(date2)
        self.calendar2.hide()

    def setDateRange2(self, minimum, maximum):
        self.calendar2.setDateRange(minimum, maximum)

    def isValid2(self):
        text2 = self.text()
        if not text2:
            return False
        date = QtCore.QDate.fromString(text2, self.format2())
        if date.isValid2():
            self.setDate(date)
            return True
        try:
            year = int(text2)
            start = self.calendar2.minimumDate().year()
            end = self.calendar2.maximumDate().year()
            if start <= year <= end:
                return True
        except:
            pass
        return False

    def hidePopup2(self):
        self.calendar2.hide()

    def showPopup2(self):
        pos = self.lineEdit2.mapToGlobal(self.lineEdit2.rect().bottomLeft())
        pos += QtCore.QPoint(0, 1)
        rect = QtCore.QRect(pos, self.calendar2.sizeHint())
        self.calendar2.setGeometry(rect)
        self.calendar2.show()
        self.calendar2.setFocus()

    def eventFilter2(self, source, event):
        if event.type() == QtCore.QEvent.Hide:
            self.dropDownButton2.setDown(False)
        elif event.type() == QtCore.QEvent.Show:
            self.dropDownButton2.setDown(True)
        return super().eventFilter(source, event)

    '''def keyPressEvent2(self, event):
        if event.key() in (QtCore.Qt.Key_Down, QtCore.Qt.Key_F4):
            if not self.calendar2.isVisible():
                self.showPopup()
        super().keyPressEvent2(event)'''
        
    def nazad(self):
        text.pop(1)
        text.pop(0)
        self.w2 = Window3()
        self.w2.show()
        self.close()

    def dalee(self):
        if self.lineEdit5.text() == '' or self.lineEdit6.text() == '' or self.lineEdit3.text() == '' or self.lineEdit4.text() == '+    ':
            print("Заполните все поля")
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля!")
            message.exec_()
        else:
            try:
                zaezd = self.lineEdit.text()
                vyezd = self.lineEdit2.text()
                cur_date = date.today()
                print(cur_date)
                first_date = date(int(zaezd[6:]), int(zaezd[3:5]), int(zaezd[:2]))
                if cur_date >= first_date:
                    print("На указанную дату бронирование не возможно!")
                    message = QMessageBox()
                    message.setFont(QtGui.QFont("Times", 12))
                    message.setWindowIcon(QtGui.QIcon("Error.png"))
                    message.setWindowTitle("Ошибка!")
                    message.setIcon(QMessageBox.Critical)
                    message.setText("На указанную дату бронирование не возможно!")
                    message.exec_()
                else:
                    second_date = date(int(vyezd[6:]), int(vyezd[3:5]), int(vyezd[:2]))
                    delta = second_date - first_date
                    print(delta.days)
                    if int(zaezd[:2]) > 31 or int(zaezd[3:5]) > 12 or int(zaezd[6:]) < 2023 or int(vyezd[:2]) > 31 or int(
                            vyezd[3:5]) > 12 or delta.days < 1:
                        print("ERROR")
                        message = QMessageBox()
                        message.setFont(QtGui.QFont("Times", 12))
                        message.setWindowIcon(QtGui.QIcon("Error.png"))
                        message.setWindowTitle("Ошибка!")
                        message.setIcon(QMessageBox.Critical)
                        message.setText("Дата введена неправильно!")
                        message.exec_()
                    else:
                        text.append(str(self.lineEdit5.text()))
                        text.append(str(self.lineEdit6.text()))
                        text.append(str(self.lineEdit.text()))
                        text.append(str(self.lineEdit2.text()))
                        text.append(str(delta.days))
                        text22.append(str(self.lineEdit5.text()))
                        text22.append(str(self.lineEdit6.text()))
                        text22.append(str(self.lineEdit3.text()))
                        text22.append(str(self.lineEdit4.text()))
                        text22.append(str(self.lineEdit.text()))
                        text22.append(str(self.lineEdit2.text()))
                        print(text)
                        print(text22)
                        self.w3 = Window5()
                        self.w3.show()
                        self.close()
            except:
                print("Заполните все поля")
                message = QMessageBox()
                message.setFont(QtGui.QFont("Times", 12))
                message.setWindowIcon(QtGui.QIcon("Error.png"))
                message.setWindowTitle("Ошибка!")
                message.setIcon(QMessageBox.Critical)
                message.setText("Заполните все поля!")
                message.exec_()


class Window42(QWidget):
    customFormat = 'dd.MM.yyyy'

    def __init__(self, parent=None):
        super(Window42, self).__init__()
        super(Window42, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Регистрация')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 0)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet(
            "QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.button_dalee = QPushButton(self)
        self.button_dalee.setGeometry(QtCore.QRect(990, 650, 160, 40))
        self.button_dalee.setFont(font)
        self.button_dalee.setText('Далее')
        self.button_dalee.setStyleSheet(
            "QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_dalee.clicked.connect(self.dalee)

        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.setGeometry(QtCore.QRect(260, 200, 290, 60))
        font1 = QtGui.QFont()
        font1.setPointSize(30)
        self.lineEdit5.setFont(font1)
        self.lineEdit5.setObjectName("lineEdit")
        self.lineEdit5.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit5.setToolTip("Пример ввода: Иван")
        self.lineEdit5.setFocus()

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(270, 150, 100, 60))
        self.label_1.setFont(font)
        self.label_1.setText('Имя')
        self.label_1.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit6 = QLineEdit(self)
        self.lineEdit6.setGeometry(QtCore.QRect(660, 200, 290, 60))
        self.lineEdit6.setFont(font1)
        self.lineEdit6.setObjectName("lineEdit2")
        self.lineEdit6.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit6.setToolTip("Пример ввода: Иванов")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(670, 150, 100, 60))
        self.label_2.setFont(font)
        self.label_2.setText('Фамилия')
        self.label_2.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(260, 300, 690, 60))
        self.lineEdit3.setFont(font1)
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit3.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit3.setToolTip("Пример ввода: ivanov.ivan@gmail.com")
        self.lineEdit3.setToolTipDuration(5000)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 100, 60))
        self.label_3.setFont(font)
        self.label_3.setText('E-Mail')
        self.label_3.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.setGeometry(QtCore.QRect(260, 400, 690, 60))
        self.lineEdit4.setFont(font1)
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit4.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit4.setToolTip("Пример ввода: +7 800 555 35 35")
        self.lineEdit4.setInputMask('+9 999 999 99 99')
        self.lineEdit4.setMaxLength(11)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(270, 350, 100, 60))
        self.label_4.setFont(font)
        self.label_4.setText('Телефон')
        self.label_4.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(260, 500, 290, 60))
        self.lineEdit.setFont(font1)
        self.lineEdit.setPlaceholderText("ДД.ММ.ГГГГ")
        self.lineEdit.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit.setMaxLength(len(self.format()))
        self.validator = SimpleDateValidator(self)
        self.lineEdit.setValidator(self.validator)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(270, 450, 100, 60))
        self.label_5.setFont(font)
        self.label_5.setText('Заезд')
        self.label_5.setStyleSheet("color: rgb(51,122,183)")

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(660, 500, 290, 60))
        self.lineEdit2.setFont(font1)
        self.lineEdit2.setPlaceholderText("ДД.ММ.ГГГГ")
        self.lineEdit2.setStyleSheet("color: rgb(51,122,183); border: none")
        self.lineEdit2.setMaxLength(len(self.format2()))
        self.validator2 = SimpleDateValidator2(self)
        self.lineEdit2.setValidator(self.validator)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(670, 450, 100, 60))
        self.label_6.setFont(font)
        self.label_6.setText('Выезд')
        self.label_6.setStyleSheet("color: rgb(51,122,183)")

        self.dropDownButton = QToolButton(self)
        self.dropDownButton.setGeometry(QtCore.QRect(490, 500, 60, 60))
        self.dropDownButton.setFont(font)
        self.dropDownButton.setIcon(QtGui.QIcon("Calendar.ico"))
        self.dropDownButton.setIconSize(QtCore.QSize(35, 35))
        self.dropDownButton.setCheckable(True)
        self.dropDownButton.setFocusPolicy(QtCore.Qt.NoFocus)

        self.dropDownButton2 = QToolButton(self)
        self.dropDownButton2.setGeometry(QtCore.QRect(890, 500, 60, 60))
        self.dropDownButton2.setFont(font)
        self.dropDownButton2.setIcon(QtGui.QIcon("Calendar.ico"))
        self.dropDownButton2.setIconSize(QtCore.QSize(35, 35))
        self.dropDownButton2.setCheckable(True)
        self.dropDownButton2.setFocusPolicy(QtCore.Qt.NoFocus)

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setWindowFlags(QtCore.Qt.Popup)
        self.calendar.installEventFilter(self)

        self.calendar2 = QtWidgets.QCalendarWidget()
        self.calendar2.setWindowFlags(QtCore.Qt.Popup)
        self.calendar2.installEventFilter(self)

        self.dropDownButton.pressed.connect(self.showPopup)
        self.dropDownButton.released.connect(self.calendar.hide)

        self.dropDownButton2.pressed.connect(self.showPopup2)
        self.dropDownButton2.released.connect(self.calendar2.hide)

        self.lineEdit.editingFinished.connect(self.editingFinished)
        self.lineEdit2.editingFinished.connect(self.editingFinished2)

        self.calendar.clicked.connect(self.setDate)
        self.calendar.activated.connect(self.setDate)

        self.calendar2.clicked.connect(self.setDate2)
        self.calendar2.activated.connect(self.setDate2)

    def editingFinished(self):
        if self.calendar.isVisible():
            return
        if not self.isValid():
            self.lineEdit.setText('')

    def format(self):
        return self.customFormat or QtCore.QLocale().dateFormat(QtCore.QLocale.ShortFormat)

    def setFormat(self, format):
        if format and 'MMM' in format or 'ddd' in format:
            return
        self.customFormat = format
        self.setDate(self.calendar.selectedDate())
        self.calendar.hide()
        self.lineEdit.setMaxLength(self.format())
        self.validator.setFormat(self.format())

    def text(self):
        return self.lineEdit.text()

    def date(self):
        if not self.isValid():
            return None
        date = QtCore.QDate.fromString(self.text(), self.format())
        if date.isValid():
            return date
        return int(self.text())

    def setDate(self, date):
        self.lineEdit.setText(date.toString(self.format()))
        self.calendar.setSelectedDate(date)
        self.calendar.hide()

    def setDateRange(self, minimum, maximum):
        self.calendar.setDateRange(minimum, maximum)

    def isValid(self):
        text = self.text()
        if not text:
            return False
        date = QtCore.QDate.fromString(text, self.format())
        if date.isValid():
            self.setDate(date)
            return True
        try:
            year = int(text)
            start = self.calendar.minimumDate().year()
            end = self.calendar.maximumDate().year()
            if start <= year <= end:
                return True
        except:
            pass
        return False

    def hidePopup(self):
        self.calendar.hide()

    def showPopup(self):
        pos = self.lineEdit.mapToGlobal(self.lineEdit.rect().bottomLeft())
        pos += QtCore.QPoint(0, 1)
        rect = QtCore.QRect(pos, self.calendar.sizeHint())
        self.calendar.setGeometry(rect)
        self.calendar.show()
        self.calendar.setFocus()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Hide:
            self.dropDownButton.setDown(False)
        elif event.type() == QtCore.QEvent.Show:
            self.dropDownButton.setDown(True)
        return super().eventFilter(source, event)

    '''def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Down, QtCore.Qt.Key_F4):
            if not self.calendar.isVisible():
                self.showPopup()
        super().keyPressEvent(event)'''

    def editingFinished2(self):
        if self.calendar2.isVisible():
            return
        if not self.isValid2():
            self.lineEdit2.setText('')

    def format2(self):
        return self.customFormat or QtCore.QLocale().dateFormat(QtCore.QLocale.ShortFormat)

    def setFormat2(self, format2):
        if format2 and 'MMM' in format2 or 'ddd' in format2:
            return
        self.customFormat = format2
        self.setDate(self.calendar2.selectedDate())
        self.calendar2.hide()
        self.lineEdit2.setMaxLength(self.format2())
        self.validator2.setFormat(self.format2())

    def text2(self):
        return self.lineEdit2.text()

    def date2(self):
        if not self.isValid2():
            return None
        date2 = QtCore.QDate.fromString(self.text2(), self.format2())
        if date2.isValid2():
            return date2
        return int(self.text2())

    #
    def setDate2(self, date2):
        self.lineEdit2.setText(date2.toString(self.format2()))
        self.calendar2.setSelectedDate(date2)
        self.calendar2.hide()

    def setDateRange2(self, minimum, maximum):
        self.calendar2.setDateRange(minimum, maximum)

    def isValid2(self):
        text2 = self.text()
        if not text2:
            return False
        date = QtCore.QDate.fromString(text2, self.format2())
        if date.isValid2():
            self.setDate(date)
            return True
        try:
            year = int(text2)
            start = self.calendar2.minimumDate().year()
            end = self.calendar2.maximumDate().year()
            if start <= year <= end:
                return True
        except:
            pass
        return False

    def hidePopup2(self):
        self.calendar2.hide()

    def showPopup2(self):
        pos = self.lineEdit2.mapToGlobal(self.lineEdit2.rect().bottomLeft())
        pos += QtCore.QPoint(0, 1)
        rect = QtCore.QRect(pos, self.calendar2.sizeHint())
        self.calendar2.setGeometry(rect)
        self.calendar2.show()
        self.calendar2.setFocus()

    def eventFilter2(self, source, event):
        if event.type() == QtCore.QEvent.Hide:
            self.dropDownButton2.setDown(False)
        elif event.type() == QtCore.QEvent.Show:
            self.dropDownButton2.setDown(True)
        return super().eventFilter(source, event)

    '''def keyPressEvent2(self, event):
        if event.key() in (QtCore.Qt.Key_Down, QtCore.Qt.Key_F4):
            if not self.calendar2.isVisible():
                self.showPopup()
        super().keyPressEvent2(event)'''

    def nazad(self):
        text.pop(1)
        text.pop(0)
        self.w2 = Window2()
        self.w2.show()
        self.close()

    def dalee(self):
        if self.lineEdit5.text() == '' or self.lineEdit6.text() == '' or self.lineEdit3.text() == '' or self.lineEdit4.text() == '+    ':
            print("Заполните все поля")
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля!")
            message.exec_()
        else:
            try:
                zaezd = self.lineEdit.text()
                vyezd = self.lineEdit2.text()
                cur_date = date.today()
                print(cur_date)
                first_date = date(int(zaezd[6:]), int(zaezd[3:5]), int(zaezd[:2]))
                if cur_date >= first_date:
                    print("На указанную дату бронирование не возможно!")
                    message = QMessageBox()
                    message.setFont(QtGui.QFont("Times", 12))
                    message.setWindowIcon(QtGui.QIcon("Error.png"))
                    message.setWindowTitle("Ошибка!")
                    message.setIcon(QMessageBox.Critical)
                    message.setText("На указанную дату бронирование не возможно!")
                    message.exec_()
                else:
                    second_date = date(int(vyezd[6:]), int(vyezd[3:5]), int(vyezd[:2]))
                    delta = second_date - first_date
                    print(delta.days)
                    if int(zaezd[:2]) > 31 or int(zaezd[3:5]) > 12 or int(zaezd[6:]) < 2023 or int(vyezd[:2]) > 31 or int(
                            vyezd[3:5]) > 12 or delta.days < 1:
                        print("ERROR")
                        message = QMessageBox()
                        message.setFont(QtGui.QFont("Times", 12))
                        message.setWindowIcon(QtGui.QIcon("Error.png"))
                        message.setWindowTitle("Ошибка!")
                        message.setIcon(QMessageBox.Critical)
                        message.setText("Дата введена неправильно!")
                        message.exec_()
                    else:
                        text.append(str(self.lineEdit5.text()))
                        text.append(str(self.lineEdit6.text()))
                        text.append(str(self.lineEdit.text()))
                        text.append(str(self.lineEdit2.text()))
                        text.append(str(delta.days))
                        text22.append(str(self.lineEdit5.text()))
                        text22.append(str(self.lineEdit6.text()))
                        text22.append(str(self.lineEdit3.text()))
                        text22.append(str(self.lineEdit4.text()))
                        text22.append(str(self.lineEdit.text()))
                        text22.append(str(self.lineEdit2.text()))
                        print(text)
                        self.w3 = Window5()
                        self.w3.show()
                        self.close()
            except:
                print("Заполните все поля")
                message = QMessageBox()
                message.setFont(QtGui.QFont("Times", 12))
                message.setWindowIcon(QtGui.QIcon("Error.png"))
                message.setWindowTitle("Ошибка!")
                message.setIcon(QMessageBox.Critical)
                message.setText("Заполните все поля!")
                message.exec_()

class Window5(QWidget):
    def __init__(self, parent=None):
        super(Window5, self).__init__()
        super(Window5, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Оплата')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 0)

        self.lbl2 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("card4.png").scaled(700, 450)
        self.lbl2.setPixmap(self.pix)
        self.lbl2.resize(700, 450)
        self.lbl2.move(250, 180)

        self.button_nazad = QPushButton(self)
        self.button_nazad.setGeometry(QtCore.QRect(50, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_nazad.setFont(font)
        self.button_nazad.setText('Назад')
        self.button_nazad.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_nazad.clicked.connect(self.nazad)

        self.button_dalee = QPushButton(self)
        self.button_dalee.setGeometry(QtCore.QRect(990, 650, 160, 40))
        self.button_dalee.setFont(font)
        self.button_dalee.setText('Оплатить')
        self.button_dalee.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_dalee.clicked.connect(self.oplata)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(370, 400, 495, 50))
        font1 = QtGui.QFont()
        font1.setPointSize(35)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        self.lineEdit.setInputMask("9999 9999 9999 9999;o")
        self.lineEdit.setFocus()

        self.label_valid = QtWidgets.QLabel(self)
        self.label_valid.setGeometry(QtCore.QRect(385, 457, 50, 30))
        font_val = QtGui.QFont()
        font_val.setPointSize(7)
        self.label_valid.setFont(font_val)
        self.label_valid.setText("VALID")
        self.label_valid.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.label_thru = QtWidgets.QLabel(self)
        self.label_thru.setGeometry(QtCore.QRect(387, 467, 50, 30))
        self.label_thru.setFont(font_val)
        self.label_thru.setText("THRU")
        self.label_thru.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(425, 460, 37, 30))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        '''pIntvalidator_2 = QIntValidator(self)
        pIntvalidator_2.setRange(1,99)
        self.lineEdit_2.setPlaceholderText("00")
        self.lineEdit_2.setValidator(pIntvalidator_2)'''
        self.lineEdit_2.setInputMask("99;o")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(460, 459, 20, 30))
        self.label_1.setFont(font2)
        self.label_1.setText("/")
        self.label_1.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(472, 460, 37, 30))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        '''pIntvalidator_3 = QIntValidator(self)
        pIntvalidator_3.setRange(1,99)
        self.lineEdit_3.setPlaceholderText("00")
        self.lineEdit_3.setValidator(pIntvalidator_3)'''
        self.lineEdit_3.setInputMask("99;o")

        self.label_cvv = QtWidgets.QLabel(self)
        self.label_cvv.setGeometry(QtCore.QRect(675, 460, 50, 30))
        font_cvv = QtGui.QFont()
        font_cvv.setPointSize(15)
        self.label_cvv.setFont(font_cvv)
        self.label_cvv.setText("CVV")
        self.label_cvv.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")

        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 460, 50, 30))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255,255,255); border: none")
        pIntvalidator=QIntValidator(self)
        pIntvalidator.setRange(1,999)
        self.lineEdit_4.setPlaceholderText("ooo")
        self.lineEdit_4.setValidator(pIntvalidator)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
    def nazad(self):
        del text[2:]
        print(text)
        self.w2 = Window4()
        self.w2.show()
        self.w2.lineEdit5.setText(text22[0])
        self.w2.lineEdit6.setText(text22[1])
        self.w2.lineEdit3.setText(text22[2])
        self.w2.lineEdit4.setText(text22[3])
        self.w2.lineEdit.setText(text22[4])
        self.w2.lineEdit2.setText(text22[5])
        text22.clear()
        self.close()
    def oplata(self):
        if str(self.lineEdit.text()) != "":
            login = str(self.lineEdit.text())
            itog = int(text[1]) * int(text[6])
            try:
                conn = sqlite3.connect('Bank.db')
                cursor2 = conn.cursor()
                ss = 'Login ='+str('"'+login+'"')
                print(ss)
                cursor2.execute('Select * from Cards WHERE '+str(ss))
                proba = []
                proba = cursor2.fetchall()
                print(proba)
                conn.commit()
                conn.close()
                if str(self.lineEdit_2.text()) == str(proba[0][1]) and str(self.lineEdit_3.text()) == str(proba[0][2]) and str(self.lineEdit_4.text()) == str(proba[0][3]):
                    print("GOOD")
                    if itog < int(proba[0][4]):

                        button = QMessageBox.question(self, "Подтверждение оплаты", "Вы уверены что хотите оплатить?")
                        if button == QMessageBox.Yes:
                            print("Yes!")
                            print("НАмаан денех")
                            schet = str(int(proba[0][4]) - itog)
                            def update_multiple_records(record_list):
                                try:
                                    sqlite_connection = sqlite3.connect('Bank.db')
                                    cursor = sqlite_connection.cursor()
                                    print("Подключен к SQLite")

                                    sqlite_update_query = """Update Cards set Schet = ? where Login = ?"""
                                    cursor.executemany(sqlite_update_query, record_list)
                                    sqlite_connection.commit()
                                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                                    sqlite_connection.commit()
                                    cursor.close()

                                    text.append(itog)
                                    self.w3 = Window7()
                                    self.w3.show()
                                    self.close()

                                except sqlite3.Error as error:
                                    print("Ошибка при работе с SQLite", error)
                                finally:
                                    if sqlite_connection:
                                        sqlite_connection.close()
                                        
                                        print("Соединение с SQLite закрыто")

                            a = [schet, login]
                            records_to_update = []
                            records_to_update.append(a)
                            print(records_to_update)
                            update_multiple_records(records_to_update)
                            
                            print(schet)
                        else:
                            print("No!")
                    else:
                        print("Недостаточно дененежных средств!")
                        message = QMessageBox()
                        message.setFont(QtGui.QFont("Times", 12))
                        message.setWindowIcon(QtGui.QIcon("Error.png"))
                        message.setWindowTitle("Ошибка!")
                        message.setIcon(QMessageBox.Critical)
                        message.setText("Недостаточно дененежных средств!")
                        message.exec_()
                else:
                    print("Неправильный ввод данных!")
                    message = QMessageBox()
                    message.setFont(QtGui.QFont("Times", 12))
                    message.setWindowIcon(QtGui.QIcon("Error.png"))
                    message.setWindowTitle("Ошибка!")
                    message.setIcon(QMessageBox.Critical)
                    message.setText("Неправильный ввод данных!")
                    message.exec_()
            except:
                print("Такой карты не существует!")
                message = QMessageBox()
                message.setFont(QtGui.QFont("Times", 12))
                message.setWindowIcon(QtGui.QIcon("Error.png"))
                message.setWindowTitle("Ошибка!")
                message.setIcon(QMessageBox.Critical)
                message.setText("Такой карты не существует!")
                message.exec_()
        
        '''s = 0
        d = {}
        f = open('Bank.txt', 'r', encoding="utf-8")
        for line in f:
            (key, m, val, r, y) = line.split("|")
            if len(y) == 3:
                d[key] = m, val, r, y
            else:
                d[key] = m, val, r, y[:-1]
        f.close()
        print(d)
        itog = int(text[1]) * int(text[6])
        for k, v in d.items():
            if str(k) == str(self.lineEdit.text()) and int(v[0]) > itog and v[1] == str(self.lineEdit_2.text()) and v[2] == str(self.lineEdit_3.text()) and v[3] == str(self.lineEdit_4.text()):
                print("GOOD")
                s = 1
                text.append(itog)
                self.w3 = Window7()
                self.w3.show()
                self.close()
            elif str(k) == str(self.lineEdit.text()) and int(v[0]) < itog and v[1] == str(self.lineEdit_2.text()) and v[2] == str(self.lineEdit_3.text()) and v[3] == str(self.lineEdit_4.text()):
                print("НЕДОСТАТОЧНО ДЕНЕЖНЫХ СРЕДСТВ")
                s = 2
        if s == 0:
            print("Не правильные данные")'''
class Window7(QWidget):
    def __init__(self, parent=None):
        super(Window7, self).__init__()
        super(Window7, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Оплачено')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        # имя конечного файла
        filename = str(text[3]) + str(text[0]) +".png"
        # генерируем qr-код
        img = qrcode.make(str(text[3]) + " " + str(text[0]) + " " + str(text[4]) + " " + str(text[5]))
        # сохраняем img в файл
        img.save(filename)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("GRHOT.png").scaled(400, 200)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(400, 200)
        self.lbl1.move(410, 0)

        self.button_glav = QPushButton(self)
        self.button_glav.setGeometry(QtCore.QRect(990, 650, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_glav.setFont(font)
        self.button_glav.setText('На главную')
        self.button_glav.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_glav.clicked.connect(self.glavnay)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap(str(text[3]) + str(text[0]) +".png").scaled(300, 300)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(300, 300)
        self.lbl1.move(750, 250)

        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setGeometry(QtCore.QRect(250, 250, 350, 30))
        font_val = QtGui.QFont()
        font_val.setPointSize(20)
        self.label_name.setFont(font_val)
        self.label_name.setText("Имя: " + str(text[2]))
        self.label_name.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

        self.label_famil = QtWidgets.QLabel(self)
        self.label_famil.setGeometry(QtCore.QRect(250, 300, 350, 30))
        self.label_famil.setFont(font_val)
        self.label_famil.setText("Фамилия: " + str(text[3]))
        self.label_famil.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

        self.label_nomer = QtWidgets.QLabel(self)
        self.label_nomer.setGeometry(QtCore.QRect(250, 350, 350, 30))
        self.label_nomer.setFont(font_val)
        self.label_nomer.setText("Номер: " + str(text[0]))
        self.label_nomer.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

        self.label_zaezd = QtWidgets.QLabel(self)
        self.label_zaezd.setGeometry(QtCore.QRect(250, 400, 350, 30))
        self.label_zaezd.setFont(font_val)
        self.label_zaezd.setText("Дата заезда: "+ str(text[4]))
        self.label_zaezd.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

        self.label_vyezd = QtWidgets.QLabel(self)
        self.label_vyezd.setGeometry(QtCore.QRect(250, 450, 350, 30))
        self.label_vyezd.setFont(font_val)
        self.label_vyezd.setText("Дата выезда: " + str(text[5]))
        self.label_vyezd.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

        self.label_opl = QtWidgets.QLabel(self)
        self.label_opl.setGeometry(QtCore.QRect(250, 500, 350, 30))
        self.label_opl.setFont(font_val)
        self.label_opl.setText("Оплачено: " + str(text[7]) + " ₽")
        self.label_opl.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(51,122,183); border: none")

    def glavnay(self):
        text.clear()
        text22.clear()
        self.w1 = Window1()
        self.w1.show()
        self.close()

class Window8(QWidget):
    def __init__(self, parent=None):
        super(Window8, self).__init__()
        super(Window8, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle('Ресторан')
        self.resize(1200, 720)
        self.setMinimumWidth(1200)
        self.setMinimumHeight(720)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(720)

        self.lbl1 = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap("Ресторан.jpg").scaled(1200, 720)
        self.lbl1.setPixmap(self.pix)
        self.lbl1.resize(1200, 720)
        self.lbl1.move(0, 0)

        self.button_glav = QPushButton(self)
        self.button_glav.setGeometry(QtCore.QRect(80, 610, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_glav.setFont(font)
        self.button_glav.setText('На главную')
        self.button_glav.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: Yellow; border-radius: 10px;}""QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_glav.clicked.connect(self.glavnay)

    def glavnay(self):
        text.clear()
        self.w1 = Window1()
        self.w1.show()
        self.close()
            
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Карта')
        self.window_width, self.window_height = 1200, 720
        self.setMinimumSize(self.window_width, self.window_height)
        self.setMaximumSize(self.window_width, self.window_height)
        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (49.29395396839081, -0.11563044338869728)
        m = folium.Map(tiles='openstreetmap', zoom_start=16, location=coordinate)
        folium.Marker(location=[49.29395396839081, -0.11563044338869728], popup = "Grand Hotel", icon = folium.Icon(color = 'green')).add_to(m)
        
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = Window1()
    ico = QtGui.QIcon("Hotel.png")
    ui1.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    ui1.show()
    sys.exit(app.exec_())
