from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from inter import Ui_Form
from random import randint

class main(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_3.clicked.connect(self.rand)
        self.ui.pushButton_4.clicked.connect(self.count_all)
        self.ui.pushButton_5.clicked.connect(self.info)
        self.ui.spinBox.valueChanged.connect(self.spin_change)
        self.ui.tableWidget.itemChanged.connect(self.item_change)
        
        self.spin_change() #Сразу расставляем нолики и присваивам переменные
        
    def save(self): #Функция для сохранения результатов
        s = ''
        for row in self.data:
            s += ' '.join([str(k) for k in row])
            s += '\n'
        filename = QFileDialog.getSaveFileName(self, 'Выберите файл для сохранения результата', None, 'Text Files (*.txt)')[0]
        if not filename:
            return
        self.count_all()
        with open(filename, 'w', encoding = 'utf-8') as f:
            f.writelines(s)
            f.write('Сумма чисел по периметру составляет: %s\nПроизведение чисел по периметру составляет: %s'%(self.summa, self.proizv))
        QMessageBox.information(self, 'Результат', 'Ваш файл успешно сохранен', QMessageBox.Ok)

    def set_data(self): #Функция для расстановки элементов матрицы
        for k in range(self.n):
            for i in range(self.n):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, self.data[k][i]) #Элементы таблицы принимают только числа
                self.ui.tableWidget.setItem(k, i, item)
                
    def rand(self): #Функция для заполнения матрицы случайными значениями
        self.data = [[randint(-100, 100) for k in range(self.n)] for i in range(self.n)]
        self.ui.tableWidget.itemChanged.disconnect(self.item_change)
        self.set_data()
        self.ui.tableWidget.itemChanged.connect(self.item_change)
                                             
    def count_all(self): #Функция подсчета произведения и суммы
        self.summa = 0 #переменная для суммы элементов
        self.proizv = 1 #переменная для произведения элементов
        for k in range(self.n):
            self.summa += self.data[0][k]
            self.summa += self.data[-1][k]

            self.proizv *= self.data[0][k]
            self.proizv *= self.data[-1][k]
            
            if k > 0 and k < self.n - 1: #первую и последнюю строки игнорируем, их уже взяли выше
                self.summa += self.data[k][0]
                self.summa += self.data[k][-1]
                
                self.proizv *= self.data[k][0]
                self.proizv *= self.data[k][-1]
        QMessageBox.information(self, 'Результат', 'Сумма чисел по периметру составляет: %s\nПроизведение чисел по периметру составляет: %s'%(self.summa, self.proizv), QMessageBox.Ok)
        
        
    def spin_change(self): #Функция при изменении размерности матрицы
        self.ui.tableWidget.itemChanged.disconnect(self.item_change)
        self.n = self.ui.spinBox.value()
        self.data = [[0 for k in range(self.n)] for i in range(self.n)]
        self.ui.tableWidget.setColumnCount(self.n)
        self.ui.tableWidget.setRowCount(self.n)
        self.set_data() #расставляем нолики
        self.ui.tableWidget.itemChanged.connect(self.item_change)

    def item_change(self, item): #функция при изменении элементов матрицы вручную
        self.data[item.row()][item.column()] = int(item.text())

    def info(self):
        QMessageBox.information(self, 'Помощь', 'Программа была создана курсантом 331 гр. Хачатрян О. А. Дата создания - 30.10.2023\n' +
                                'Сначала вам необходимо задать размерность квадратной матрицы, используя spinBox (вы не можете выбрать число меньше 2 и больше 99). Вы можете сами заполнить матрицу, либо заполнить ее случайными значениями.' +
                                'При нажатии кнопки "Посчитать значения" будут посчитаны сумма и произведение элементов периметра. Вы также можете сохранить матрицу и результат в текстовый файл.', QMessageBox.Ok)
        
app = QApplication(sys.argv)
Form = main()
Form.show()
sys.exit(app.exec_())
