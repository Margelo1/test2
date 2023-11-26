# Подключение модулей
import sys
from Интерфейс import *
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
#from AllMessage import *
#import matplotlib.pyplot as plt
# Открытие файла
f = open('Аукцион.txt', 'r', encoding="utf-8")
data = [line.strip() for line in f]
f.close()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Задает шрифт текста
        self.ui.tableWidget.setFont(QtGui.QFont("Times", 12))
        # Убирает кнопки "Свернуть" и "Развернуть"
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowCloseButtonHint)
        # Построчное заполнение таблицы
        row = 0
        for tup in data:
            col = 0

            for item in tup.split(' '):
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        # Адаптация ячеек под текст
        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        # Привязка функций к кнопкам
        self.ui.pushButton.clicked.connect(self.find)
        self.ui.pushButton_2.clicked.connect(self.diagramma)
        self.ui.pushButton_3.clicked.connect(self.cell_changed_2)
        self.ui.pushButton_4.clicked.connect(self.save)
        self.ui.action.triggered.connect(self.oprogramme)
        self.ui.action_2.triggered.connect(self.instrukcia)
        # закрытие программы
        self.ui.action_3.triggered.connect(self.close)

    def cell_changed_2(self):
        try:
            for row in range(self.ui.tableWidget.rowCount()):
                # Поиск отрицательных чисел
                if ('-' in self.ui.tableWidget.item(row, 4).text()) or ('-' in self.ui.tableWidget.item(row, 5).text()):
                    # Появление сообщения об ошибке
                    message = QMessageBox()
                    message.setFont(QtGui.QFont("Times", 12))
                    message.setWindowIcon(QtGui.QIcon("Error.png"))
                    message.setWindowTitle("Ошибка!")
                    message.setIcon(QMessageBox.Critical)
                    message.setText("Заполните поля положительными числами!")
                    message.exec_()
                    break
                else:
                    # Выполнение математической модели
                    if (self.ui.tableWidget.item(row, 4).text() != "0") and (self.ui.tableWidget.item(row, 5).text() != "0"):
                        valure =  int(self.ui.tableWidget.item(row, 4).text()) * int(self.ui.tableWidget.item(row, 5).text()) + int(self.ui.tableWidget.item(row, 3).text())
                        self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(f"{valure}"))
                    else:
                        self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(f"0"))
        except:
            # Появление сообщения об ошибке
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля целыми положительными числами!")
            message.exec_()
            pass      

    def find(self):
        try:
            money = []
            for row in range(self.ui.tableWidget.rowCount()):
                if self.ui.tableWidget.item(row, 6) is not None:
                    if self.ui.tableWidget.item(row, 6).text() != "0":
                        money.append(int(self.ui.tableWidget.item(row, 6).text()))
            print(money)
            # Появление сообщения о дорогой и дешевой лошадей
            dlg = QMessageBox(self)
            dlg.setFont(QtGui.QFont("Times", 12))
            dlg.setWindowTitle("Результаты")
            dlg.setText(f'Цена за дешевую лошадь: {min(money)}\nЦена за дорогую лошадь:  {max(money)}')
            dlg.setStandardButtons(QMessageBox.Yes)
            dlg.setWindowIcon(QtGui.QIcon("Information.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.exec_()
        except:
            # Появление сообщения об ошибке
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля целыми положительными числами!\nи нажмите на кнопку 'Завершить аукцион'")
            message.exec_()
            pass
    def oprogramme(self):
        # Добавление в "Меню" опции "О программе"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе', 'Программа: Horse auction v1.0\nРазработана: ТАТК ГА филиал МГТУ ГА\nкурсантом: 332 группы Байда В.А.\n                     Троицк,2022')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def instrukcia(self):
        # Добавление в "Меню" опции "Инструкция"
        recult = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Инструкция', 'Программа Horse auction предназначена для подведения итогов конного\nаукциона. Определяет стоимость самой дорогой и самой дешевой лошади.\nДля работы программы нужно последовательно выполнить ниже перечисленные пункты:\n1. Заполните все поля столбцов "Минимальный шаг ставки" и "Количество ставок" целыми положительными числами\n2. Далее нажмите на кнопку "Завершить аукцион"\nПрограмма автоматически заполнит столбец "Цена после аукциона".\n 3. Затем нажмите на кнопку "Узнать результат"\n Появится сообщение, содержащее информацию о дорогой и дешевой лошадях.\n4. После этого, нажмите на кнопку "Диаграмма"\nВы увидите окно содержащее диаграмму "Кличка" и "Цена после аукциона".\n5. Теперь нажмите на кнопку "Сохранить"\nДля сохнанения результатов в файл.')
        recult.setWindowIcon(QtGui.QIcon("Information.png"))
        recult.setFont(QtGui.QFont("Times", 12))
        recult.setIcon(QMessageBox.Information)
        recult.exec_()
    def diagramma(self):
        # Создание диаграммы
        data = [ self.ui.tableWidget.item(row, 6).text()
                  for row in range(self.ui.tableWidget.rowCount())
                   if self.ui.tableWidget.item(row, 6) is not None ]
        
        nicknames = [ self.ui.tableWidget.item(row, 0).text()
                  for row in range(self.ui.tableWidget.rowCount())
                   if self.ui.tableWidget.item(row, 0) is not None ]
        print(data)
        print(nicknames)
        
        if data == []:
            # Появление сообщения об ошибке
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля целыми положительными числами!\nи нажмите на кнопку 'Завершить аукцион'")
            message.exec_()
        else:
            2# Заполнение диаграммы
            #plt.figure(figsize=(10,7))
            #plt.barh(nicknames, data)
            #plt.show()
    # Сохранить в файл
    def save(self):
        try:
            print(3)
            b = str()
            row = self.ui.tableWidget.rowCount()
            for tup in range(row):
                b = b + self.ui.tableWidget.item(tup, 0).text() + " "
                b = b + self.ui.tableWidget.item(tup, 1).text() + " "
                b = b + self.ui.tableWidget.item(tup, 2).text() + " "
                b = b + self.ui.tableWidget.item(tup, 3).text() + " "
                b = b + self.ui.tableWidget.item(tup, 4).text() + " "
                b = b + self.ui.tableWidget.item(tup, 5).text() + " "
                b = b + self.ui.tableWidget.item(tup, 6).text() + "\n"
            f = open('tekst_save.txt', "w", encoding='UTF-8')
            f.write(b)
            f.close
        except:
            # Появление сообщения об ошибке
            message = QMessageBox()
            message.setFont(QtGui.QFont("Times", 12))
            message.setWindowIcon(QtGui.QIcon("Error.png"))
            message.setWindowTitle("Ошибка!")
            message.setIcon(QMessageBox.Critical)
            message.setText("Заполните все поля целыми положительными числами!\nи нажмите на кнопку 'Завершить аукцион'")
            message.exec_()
            pass
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    ico = QtGui.QIcon("Horse.png")
    myapp.setWindowIcon(ico)  # Значок для окна
    app.setWindowIcon(ico)  # Значок приложения
    myapp.show()
    sys.exit(app.exec_())
