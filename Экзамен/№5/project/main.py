# built - in Module
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets


# interface
from interface import Ui_MainWindow


import random
import math


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Bind button
        self.ui.pushButton.clicked.connect(self.TakeValueCountNumber)

        self.ui.action.triggered.connect(lambda: self.MessageBox("Автор курсант  "
                                                                 "432 группы Болотников М.А."))
        self.ui.action_2.triggered.connect(
            lambda: self.MessageBox("Пользователь вводит данные число в полле ввода после чего пикает кнопку и "
                                    "заполняеться таблица рандомными числами, а внизу выводиться  данные о "
                                    "самом маленьком числе у которого дробная часть крантна 3"))

        self.ui.action_3.triggered.connect(lambda: self.MessageBox("Билет №5"))

        self.ui.action_4.triggered.connect(lambda: self.close())

        # прятать объекты
        self.ui.tableWidget.hide()
        self.ui.label_2.hide()


    def TakeValueCountNumber(self):
        # Получение значение из line edit с дальнейшим проверкой её на правильность ввода
        text = self.ui.lineEdit.text().strip()
        if not text:
            self.MessageBox("Введите данные!")
            return
        if text.isdigit() is False:
            self.MessageBox("Введенные данные, не являються целочисленым числом числом!")
            return
        if int(text) == 0:
            self.MessageBox("Количество чисел не может быть 0!")
            return
        if int(text) > 100:
            self.MessageBox("Количество чисел на должно превышать 100!")
            return

        self.CreateAndFillTableWidget(int(text))

    def CreateAndFillTableWidget(self, column: int):
        # Созданние таблици из полученных данных от ползователя
        self.ClearTable()
        self.ui.tableWidget.show()
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(column)
        data = self.CreateArrayRandomNumber(column)
        for col in range(self.ui.tableWidget.columnCount()):
            item = QtWidgets.QTableWidgetItem(f"{data[col]}")
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(0, col, item)

        self.ui.label_2.show()
        fractional_number = self.SearchMinFloatNumber(data)
        if fractional_number is None:
            self.ui.label_2.setText("В данном наборе чисел нету дробных чисел у коротых дробная часть кратна 3")
        else:
            self.ui.label_2.setText(f"Самое маленькое число у которого дробное делиться на 3 это = {fractional_number}")


    @staticmethod
    def SearchMinFloatNumber(all_numbers: tuple):
        # поиск минимального числа у которого дробное число кратное 3
        fractional_number = []

        for num in all_numbers:
            if isinstance(num, float):
                fractional = f"{round(math.modf(num)[0], 2)}".split('.')[1]
                if int(fractional) % 3 == 0:
                    fractional_number.append(num)

        if not fractional_number:
            return None
        return min(fractional_number)


    @staticmethod
    def CreateArrayRandomNumber(count_number: int) -> tuple:
        # создание кортежа рандомно заполненного числами int и float
        array_all_number = []
        for i in range(count_number):
            number = round(random.choice([random.randint(1, 100), random.uniform(1.0, 100.0)]), 2)
            array_all_number.append(number)
        return tuple(array_all_number)

    def ClearTable(self):
        # Очистка таблици
        self.ui.tableWidget.clear()

    @staticmethod
    def MessageBox(text: str):
        # Вывод диологового окна
        message = QtWidgets.QMessageBox()
        message.setIcon(QtWidgets.QMessageBox.Information)
        message.setWindowTitle("Информация")
        message.setText(f"{text}")
        message.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
