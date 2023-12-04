from inter3 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets

a=list()                                                                        #открытие текстового файла
with open("class2.txt", "r") as file:
    for line in file:
        a.append(line.strip().split(' '))

class myMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.file)                            #привязка кнопок
        self.pushButton.clicked.connect(self.sortirovka)
        

    def file(self):                                                             #заполняет таблицу значениями из файла
        self.tableWidget.setRowCount(len(a))
        self.tableWidget.setItem(0, 0, QTableWidgetItem('a'))
        for i in range(len(a)):
            for j in range(3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(a[i][j]))
        self.tableWidget.resizeColumnsToContents()

    def sortirovka(self):                                                       #считает количество мальчиков и девочек, сортирует
        male = []
        female = []
        classy = []
        for i in range(len(a)):                                                 #формирование списков классов, мальчиков и девочек
            for j in range(3):
                if j == 0:
                    classy.append(str(a[i][j]))
                elif j == 1:
                    male.append(int(a[i][j]))
                elif j == 2:
                    female.append(int(a[i][j]))
        vsego = []
        bolshe = []
        for i in range(len(a)):                                                 #считает процент мальчиков, проверяет больше мальчиков или девочкек
            summa = male[i] + female[i]
            print(summa)
            vsego.append(round(male[i]/summa * 100))
            if male[i] >= female[i]:
                bolshe.append('да')
            else:
                bolshe.append('нет')
        print(vsego)
        n = len(vsego)
        for i in range(n-1):                                                    #сортировка пузырьком
            for j in range(n-i-1):
                if vsego[j] > vsego[j+1]:
                    vsego[j], vsego[j+1] = vsego[j+1], vsego[j]
                    classy[j], classy[j+1] = classy[j+1], classy[j]
                    bolshe[j], bolshe[j+1] = bolshe[j+1], bolshe[j]
        print(classy)
        print(vsego)
        self.tableWidget_2.setColumnCount(len(classy))
        self.tableWidget_2.setRowCount(2)
        for i in range(len(classy)):                                            #заполнение второй таблицы
            self.tableWidget_2.setItem(0, i, QTableWidgetItem(classy[i]))
            self.tableWidget_2.setItem(1, i, QTableWidgetItem(bolshe[i]))
        self.tableWidget_2.resizeColumnsToContents()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
