# Подключение модулей
import random
from Interface import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# Создание титульного окна
class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Тест по основам программирования')
        self.resize(800, 600)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setMaximumWidth(800)
        self.setMaximumHeight(600)
        # Подпись «Введите свои данные»
        self.label_l = QtWidgets.QLabel(self)
        self.label_l.setGeometry(QtCore.QRect(270, 20, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_l.setFont(font)
        self.label_l.setText('Введите свои данные')
        # Подпись «Фамилия»
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(350, 100, 531, 61))
        self.label.setFont(font)
        self.label.setText('Фамилия')

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(300, 160, 200, 30))
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip("Введите свою фамилию")
        self.lineEdit.setToolTipDuration(3000)
        # Подпись «Имя»
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(370, 200, 531, 61))
        self.label2.setFont(font)
        self.label2.setText('Имя')

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(300, 260, 200, 30))
        self.lineEdit2.setFont(font1)
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setToolTip("Введите свое имя")
        self.lineEdit2.setToolTipDuration(3000)
        # Подпись «Группа»
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(360, 300, 531, 61))
        self.label3.setFont(font)
        self.label3.setText('Группа')

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(300, 360, 200, 30))
        self.lineEdit3.setFont(font1)
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit3.setToolTip("Введите свою группу")
        self.lineEdit3.setToolTipDuration(3000)
        # Создание кнопки «Начать»
        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(620, 550, 150, 31))
        self.button.setFont(font1)
        self.button.setText('НАЧАТЬ')
        self.button.show()
        self.button.clicked.connect(self.append)

    # Открытие окна теста
    def show_window_2(self):
        self.w2 = MyWin()
        self.w2.show()
    def oshibka(self):
        message = QMessageBox()
        message.setFont(QtGui.QFont("Times", 12))
        message.setWindowIcon(QtGui.QIcon("Error.png"))
        message.setWindowTitle("Ошибка!")
        message.setIcon(QMessageBox.Critical)
        message.setText("Необходимо корректно ввести данные")
        message.exec_()
    # Подсветка ошибки
    def append(self):
        global text, text1, text2
        text = self.lineEdit.text()
        text1 = self.lineEdit2.text()
        text2 = self.lineEdit3.text()
        if text == '' and text1 == '' and (text2 == '' or text2.isdigit() == False):
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.oshibka()
        elif text == '' and text1 == '':
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.oshibka()
        elif text1 == '' and (text2 == '' or text2.isdigit() == False):
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.oshibka()
        elif text == '' and (text2 == '' or text2.isdigit() == False):
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.oshibka()
        elif text == '':
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.oshibka()
        elif text1 == '':
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.oshibka()
        elif text2 == '' or text2.isdigit() == False:
            self.lineEdit.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.lineEdit2.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
            self.lineEdit3.setStyleSheet("""QLineEdit { background-color: red; color: white }""")
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Введите числовое значение")
            message.exec_()
        # Открытия окна теста
        else:
            self.w2 = MyWin()
            self.w2.show()
            self.close()

# Создание окна результата теста
class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Тест по основам программирования')
        self.resize(800, 600)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setMaximumWidth(800)
        self.setMaximumHeight(600)
        # Подпись «Результаты теста»
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(200, 30, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setText('Результаты теста:')
        # Подпись о правильных ответах
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(80, 130, 701, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label1.setFont(font)
        self.label1.setText('Вы ответили на ' + str(OCSENKA) + ' из 10 вопросов')
        # Вывод оценки
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(360, 200, 701, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setText('оценка')
        font = QtGui.QFont()
        font.setPointSize(180)
        # Сохранение в файл с оценкой 2
        if OCSENKA < 5:
            self.label3 = QtWidgets.QLabel(self)
            self.label3.setGeometry(QtCore.QRect(335, 80, 701, 601))
            self.label3.setFont(font)
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.label3.setGraphicsEffect(color_effect)
            self.label3.setText("2")
            b = str()
            b = b + text + " " + text1 + " " + text2 + " " + " 2 " + "\n"
            f = open('tekst_save.txt', "a", encoding='UTF-8')
            f.write(b)
            f.close
        # Сохранение в файл с оценкой 3
        elif OCSENKA < 8:
            self.label3 = QtWidgets.QLabel(self)
            self.label3.setGeometry(QtCore.QRect(335, 80, 701, 601))
            self.label3.setFont(font)
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkYellow)
            self.label3.setGraphicsEffect(color_effect)
            self.label3.setText("3")
            b = str()
            b = b + text + " " + text1 + " " + text2 + " " + " 3 " + "\n"
            f = open('tekst_save.txt', "a", encoding='UTF-8')
            f.write(b)
            f.close
        # Сохранение в файл с оценкой 4
        elif OCSENKA < 10:
            self.label3 = QtWidgets.QLabel(self)
            self.label3.setGeometry(QtCore.QRect(335, 80, 701, 601))
            self.label3.setFont(font)
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.label3.setGraphicsEffect(color_effect)
            self.label3.setText("4")
            b = str()
            b = b + text + " " + text1 + " " + text2 + " " + " 4 " + "\n"
            f = open('tekst_save.txt', "a", encoding='UTF-8')
            f.write(b)
            f.close
        # Сохранение в файл с оценкой 5
        else:
            self.label3 = QtWidgets.QLabel(self)
            self.label3.setGeometry(QtCore.QRect(335, 80, 701, 601))
            self.label3.setFont(font)
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.label3.setGraphicsEffect(color_effect)
            self.label3.setText("5")
            b = str()
            b = b + text + " " + text1 + " " + text2 + " " + " 5 " + "\n"
            f = open('tekst_save.txt', "a", encoding='UTF-8')
            f.write(b)
            f.close
        # Создание кнопки «Выход»
        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(620, 550, 150, 31))
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.button.setFont(font1)
        self.button.setText('Выход')
        self.button.show()
        self.button.clicked.connect(self.close)


class MyWin(QtWidgets.QMainWindow):
    # Правильные ответы
    correct1 = "time"
    correct2 = "print()"
    correct3 = "Использовать метод input()"
    correct4 = "num = float(2)"
    correct5 = "Целочисленное"
    correct6 = "x = 5"
    correct7 = "if - elif - else"
    correct8 = "while"
    correct9 = "Возвращает длину строки"
    correct10 = "В честь змеи"
    # Варианты ответов
    variants1 = ["clock", correct1, "Time"]
    variants2 = ["write()", "out()",correct2]
    variants3 = ["Использовать метод get()", "Использовать метод read()",correct3]
    variants4 = ["int num = 2", correct4, "var num = 2"]
    variants5 = ["Вещественное", "Дробное", correct5]
    variants6 = ["y = 4,6", "10 = x", correct6]
    variants7 = ["Много if", correct7, "while"]
    variants8 = ["if", "def", correct8]
    variants9 = ["Возвращает случайное число", "Возвращает модуль числа", correct9]
    variants10 = ["В честь игры", "В честь блюда", correct10]

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Подключение функций к кнопкам
        self.ui.pushButton_1.clicked.connect(self.otvet1)
        self.ui.pushButton_2.clicked.connect(self.otvet2)
        self.ui.pushButton_3.clicked.connect(self.otvet3)
        self.ui.pushButton_4.clicked.connect(self.otvet4)
        self.ui.pushButton_5.clicked.connect(self.otvet5)
        self.ui.pushButton_6.clicked.connect(self.otvet6)
        self.ui.pushButton_7.clicked.connect(self.otvet7)
        self.ui.pushButton_8.clicked.connect(self.otvet8)
        self.ui.pushButton_9.clicked.connect(self.otvet9)
        self.ui.pushButton_10.clicked.connect(self.otvet10)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.action.triggered.connect(self.oprogramme)
        self.ui.action_2.triggered.connect(self.instrukcia)
        # закрытие программы
        self.ui.action_3.triggered.connect(self.close)
        # Случайное размещение вариантов ответа
        random.shuffle(self.variants1)
        random.shuffle(self.variants2)
        random.shuffle(self.variants3)
        random.shuffle(self.variants4)
        random.shuffle(self.variants5)
        random.shuffle(self.variants6)
        random.shuffle(self.variants7)
        random.shuffle(self.variants8)
        random.shuffle(self.variants9)
        random.shuffle(self.variants10)
        # Размещение radioButton
        self.ui.radioButton.setText(self.variants1[0])
        self.ui.radioButton_2.setText(self.variants1[1])
        self.ui.radioButton_3.setText(self.variants1[2])

        self.ui.radioButton_4.setText(self.variants2[0])
        self.ui.radioButton_5.setText(self.variants2[1])
        self.ui.radioButton_6.setText(self.variants2[2])

        self.ui.radioButton_7.setText(self.variants3[0])
        self.ui.radioButton_8.setText(self.variants3[1])
        self.ui.radioButton_9.setText(self.variants3[2])

        self.ui.radioButton_10.setText(self.variants4[0])
        self.ui.radioButton_11.setText(self.variants4[1])
        self.ui.radioButton_12.setText(self.variants4[2])

        self.ui.radioButton_13.setText(self.variants5[0])
        self.ui.radioButton_14.setText(self.variants5[1])
        self.ui.radioButton_15.setText(self.variants5[2])

        self.ui.radioButton_16.setText(self.variants6[0])
        self.ui.radioButton_17.setText(self.variants6[1])
        self.ui.radioButton_18.setText(self.variants6[2])

        self.ui.radioButton_19.setText(self.variants7[0])
        self.ui.radioButton_20.setText(self.variants7[1])
        self.ui.radioButton_21.setText(self.variants7[2])

        self.ui.radioButton_22.setText(self.variants8[0])
        self.ui.radioButton_23.setText(self.variants8[1])
        self.ui.radioButton_24.setText(self.variants8[2])

        self.ui.radioButton_25.setText(self.variants9[0])
        self.ui.radioButton_26.setText(self.variants9[1])
        self.ui.radioButton_27.setText(self.variants9[2])

        self.ui.radioButton_28.setText(self.variants10[0])
        self.ui.radioButton_29.setText(self.variants10[1])
        self.ui.radioButton_30.setText(self.variants10[2])

    # Проверка правильности ответа
    def otvet1(self):
        global OCSENKA
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text()==self.correct1:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.tab.setEnabled(False)
    # Проверка правильности ответа
    def otvet2(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct2:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(2)
        self.ui.tab_2.setEnabled(False)
    # Проверка правильности ответа
    def otvet3(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct3:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(3)
        self.ui.tab_3.setEnabled(False)
    # Проверка правильности ответа
    def otvet4(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_4.buttons():
            if rb.isChecked():
                if rb.text() == self.correct4:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(4)
        self.ui.tab_4.setEnabled(False)
    # Проверка правильности ответа
    def otvet5(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_5.buttons():
            if rb.isChecked():
                if rb.text() == self.correct5:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(5)
        self.ui.tab_5.setEnabled(False)
    # Проверка правильности ответа
    def otvet6(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_6.buttons():
            if rb.isChecked():
                if rb.text() == self.correct6:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(6)
        self.ui.tab_6.setEnabled(False)
    # Проверка правильности ответа
    def otvet7(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_7.buttons():
            if rb.isChecked():
                if rb.text() == self.correct7:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(7)
        self.ui.tab_7.setEnabled(False)
    # Проверка правильности ответа
    def otvet8(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_8.buttons():
            if rb.isChecked():
                if rb.text() == self.correct8:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(8)
        self.ui.tab_8.setEnabled(False)
    # Проверка правильности ответа
    def otvet9(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_9.buttons():
            if rb.isChecked():
                if rb.text() == self.correct9:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(9)
        self.ui.tab_9.setEnabled(False)
    # Проверка правильности ответа
    def otvet10(self):
        global OCSENKA
        for rb in self.ui.buttonGroup_10.buttons():
            if rb.isChecked():
                if rb.text() == self.correct10:
                    OCSENKA += 1
        print(OCSENKA)
        self.ui.tabWidget.setCurrentIndex(10)
        self.ui.tab_10.setEnabled(False)

    # Открытие окна результата
    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()

    def oprogramme(self):
        # Добавление в "Меню" опции "О программе"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе', 'Программа: Тест по основам программирования\nРазработана: ТАТК ГА филиал МГТУ ГА\nкурсантом: 332 группы Байда В.А.\n                   Троицк, 2023 г.')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 10))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def instrukcia(self):
        # Добавление в "Меню" опции "Инструкция"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Инструкция', 'Программа предназначена для проверки знаний у студентов.\nДля работы с программой нужно ответить на 10 вопросов.\nВ каждом вопросе по три варианта ответа, из которых вы должны выбрать один. После того, как вы выберите правильный ответ,\nнажмите на кнопку "Ответить". Когда вы ответите на все вопросы,\nнажмите на кнопку "Завершить тест",и вы увидите свой результат.')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 10))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    # Сообщение с подтверждением
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Подтверждение","  \nЗавершить тест? \n   ", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.w2 = Window2()
            self.w2.show()
        else:
            event.ignore()

    global OCSENKA
    OCSENKA = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = Window1()
    ico = QtGui.QIcon("test_3.png")
    ui1.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    ui1.show()
    sys.exit(app.exec_())                           

        
        
        
        

        
        
        
