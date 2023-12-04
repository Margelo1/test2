#! Билет №7 ПМ_01 30.10.2023
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from interface import Ui_MainWindow
from random import randint
import sys


class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Привязки функций
        self.ui.action.triggered.connect(self.open)
        self.ui.action_2.triggered.connect(self.save)
        self.ui.action_3.triggered.connect(self.close)
        self.ui.action_4.triggered.connect(lambda: self.showInfo("about.txt", "Об авторе"))
        self.ui.action_5.triggered.connect(lambda: self.showInfo("instr.txt", "Иструкция"))
        self.ui.pushButton.clicked.connect(self.open)
        self.ui.pushButton_3.clicked.connect(self.fillRandom)
        self.ui.pushButton_4.clicked.connect(self.save)
        self.ui.pushButton_7.clicked.connect(self.findAndSort)

    def showInfo(self, filename, title):
        # Показ сообщения (об авторе, инструкция)
        try:
            with open(f"text/{filename}", encoding="utf-8") as f:
                text = f.read()
        except:
            # если файл не найден или поврежден
            text = f"Ошибка открытия файла {filename}"
        QMessageBox.about(self, title, text)


    def open(self):
        filename = QFileDialog.getOpenFileName(None, "Открыть файл", "", "Текстовые файлы (*.txt)")[0]
        if filename == "":
            return
        try:
            # Попытка открыть файл в UTF-8
            with open(filename, encoding="utf-8") as f:
                text = f.read()
        except:
            try:
                # Попытка открыть файл в ANSI
                with open(filename) as f:
                    text = f.read()
            except:
                QMessageBox.warning(self, "Ошибка", "Файл неверно заполнен")
                return
        try:
            text = text.replace("\ufeff", "")
            numbers = text.split(", ")
            if len(numbers) < 100: # По условию Количество чисел должно быть не меньше 100
                QMessageBox.warning(self, "Ошибка", "Файл неверно заполнен (Количество чисел должно быть не меньше 100)")
                return
            numbers = tuple(map(int, numbers))
            countNumberEndTwo = 0 # Количество двухзначных чисел, которые заканичваются на "2"
            for number in numbers:
                if self.filter(number):
                    countNumberEndTwo += 1
                if number < 0: # По условию числа должны быть натуральными
                    QMessageBox.warning(self, "Ошибка", "Файл неверно заполнен (Числа должны быть натуральными)")
                    return
            if countNumberEndTwo == 0: # По условию в файле должны быть двухзначные числа, которые заканичваются на "2"
                QMessageBox.warning(self, "Ошибка", "Файл неверно заполнен (Отсутствуют двухзначные числа, заканчивающиеся на 2)")
                return
                
            self.ui.plainTextEdit.setPlainText(text)
        except:
            QMessageBox.warning(self, "Ошибка", "Файл неверно заполнен")
            return

            
        
    def save(self):
        text = self.ui.plainTextEdit_2.toPlainText()
        if text == "":
            QMessageBox.warning(self, "Ошибка", "Сначала выполните поиск и сортировку")
            return
        # выбор файла для сохранения
        filename = QFileDialog.getSaveFileName(None, "Открыть файл", "", "Текстовые файлы (*.txt)")[0]
        if filename == "":
            return
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

    def fillRandom(self):
        countNumberEndTwo = 0
        numbers = []
        for i in range(self.ui.spinBox.value()): # генерация списка чисел
            number = randint(0, 500)
            if self.filter(number): # проверка требуется для подсчета количества двухзначных чисел, которые заканичваются на "2"
                countNumberEndTwo += 1
            
            numbers.append(str(number))
        if countNumberEndTwo == 0:
            numbers[randint(0, self.ui.spinBox.value() - 1)] = str( randint(0, 9) * 10 + 2)
        self.ui.plainTextEdit.setPlainText(", ".join(numbers))

    def filter(self, num):
        return num > 9 and num < 100 and num % 10 == 2 # проверка числа. оно должно быть двухзначным и заканичваются на "2"

    def filterNumbers(self, numbers):
        # Фильтрация по блок-схеме
        N = len(numbers)
        filterNumbers = []
        for i in range(N):
            number = numbers[i]
            if self.filter(number):
                filterNumbers.append(number)
        return filterNumbers
    
    def findAndSort(self):
        # Функция поиска и сортировки последовательности чисел
        text = self.ui.plainTextEdit.toPlainText() # считанных из текстового поля
        if text == "":
            QMessageBox.warning(self, "Ошибка", "Сначала задайте числа")
            return
        numbers = tuple(map(int, text.split(", "))) # Разделение текста на числа и преобразование в массив чисел
        #numbers = list(filter(self.filter, numbers)) # Фильтрация массива
        numbers = self.filterNumbers(numbers) # Фильтрация по блок-схеме
        
        numbers.sort(reverse=True)
        self.textOut = ", ".join(tuple(map(str, numbers))) # Перевод массива чисел в массив строк и преобразование в единую строку
        self.ui.plainTextEdit_2.setPlainText(self.textOut)

# Запуск программы
app = QApplication([])
win = MyWin()
win.show()
sys.exit(app.exec())
