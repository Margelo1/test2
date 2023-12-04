from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):                    #Создание класса окна
    def __init__ (self,parent=None):                        #Загрузка интерфейса
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.main)
        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_info.triggered.connect(self.info)
        self.ui.action_about.triggered.connect(self.about)
    
    def info(self):                                         #Инструкция к программе
        mes=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Инструкция","Для подсчеста суммы чисел введите в верхнее поле ввода числа через пробел или запятую. Для отделения дробной части от целой используйте точку. В нижнем поле будет отображена сумма чисел")
        font=QtGui.QFont()
        font.setPointSize(12)
        mes.setFont(font)
        mes.exec()
    
    def about(self):                                        #Об авторе
        mes=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Об авторе","Программа разработана курсантом 431 группы Косотуровым К.А.")
        font=QtGui.QFont()
        font.setPointSize(12)
        mes.setFont(font)
        mes.exec()

    def main(self,text):                                    #Основная функция
        sp=text.replace(","," ").split(" ")                 #Составление списка чисел
        s=0
        for i in sp:                                        #Цикл по элементам списка
            if not i:
                continue
            try:                                            #Проверка на нечисловой ввод
                s+=float(i)                                 #Суммирование элементов
            except:                                         #Вывод ошибки
                self.ui.lineEdit_2.setText(f'Найдено нечисловое значение "{i}"')
                self.ui.label_2.setText("Ошибка:")
                return
        s = round(s,10)                                     #Обнуление суммы
        self.ui.label_2.setText("Сумма:")
        if s % 1:                                           #Вывод результата
            self.ui.lineEdit_2.setText(str(s))
        else:
            self.ui.lineEdit_2.setText(str(int(s)))


            
        
if __name__ == "__main__":                                  #Запуск программы
    app = QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())        
