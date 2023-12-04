from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from int_anagramm_2 import Ui_MainWindow
import sys, os


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Привязки кнопок
        self.ui.action_2.triggered.connect(self.close)
        self.ui.action.triggered.connect(self.file)
        self.ui.action_3.triggered.connect(self.block)
        self.ui.pushButton.clicked.connect(self.opr)
    def block(self):
        path = os.getcwd()
        print(path)
        try:
            os.startfile(f'{path}\Блок-схема.PNG')
        except Exception as e:
            print(e)
        


        
    #Окно выхода
    def closeEvent(self, e):
        try:
            msg = QMessageBox()
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setWindowTitle('Выход')
            msg.setText('Вы уверены что хотите выйти?:D')
            msg.setWindowIcon(QtGui.QIcon('exit.png'))
            msg.setIcon(QMessageBox.Question)
            result = msg.exec()
            if  result == QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()
        except Exception as e:
            print(e)

    #Функция определения анограмм
    def opr(self):
        try:
            self.word1 = self.ui.lineEdit.text()
            self.word2 = self.ui.lineEdit_2.text()

  
            if self.word1.strip() == '' or self.word2.strip() =='':
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Оба поля должны быть заполнены! ')
                msg.setWindowIcon(QtGui.QIcon('error.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
                return
            
            if len(self.word1) > 0 and self.word1.isalpha() and len(self.word2) > 0 and self.word2.isalpha():
                
                
             
                if sorted(self.word1.lower()) == sorted(self.word2.lower()):
                    self.res = 'являются'
                else:
                    self.res = 'не являются'
                #Сообщение о результате        
                msg = QMessageBox()
                msg.setWindowTitle('Результат')
                msg.setText(f'Слова {self.word1} и {self.word2} {self.res} анаграммами')
                msg.setWindowIcon(QtGui.QIcon('anagramm.png'))
                msg.setIcon(QMessageBox.Information)
                msg.exec()
            else:
                #Сообщение об ошибке
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('В словах могут быть только буквы')
                msg.setWindowIcon(QtGui.QIcon('error.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
        except Exception as e:
            print(e)
    #Сохранение в файл
    def file(self):
        try:
            file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранение в файл", '', 'Text Files (*.txt);;All Files (*.*)')
            if file:
                with open(file, 'a', encoding= 'utf-8') as f:
                        f.write(f'Слова {self.word1} и {self.word2} {self.res} анаграммами\n')
        except Exception as e:
            print(e)
            #Сообщение об ошибке
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Ошибка сохранения')
            msg.setWindowIcon(QtGui.QIcon('error.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        
             
#Запуск программы
app = QtWidgets.QApplication([])
win = MyWindow()
ico = QtGui.QIcon('anagramm.png')
win.setWindowIcon(ico)
win.show()
sys.exit(app.exec())
