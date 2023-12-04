from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTextEdit
from int import *
import pathlib
import sys, os

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.action.triggered.connect(self.load_data_from_file)
        
    def click(self):
        inlist = open("1.txt", "r").read().split()
        wm = ""
        lm = 0
        for w in inlist:
            l = len(w)
            if l > lm:
               wm = w
               lm = l
        self.ui.textEdit_2.setText(wm + str(lm))
         
    
    def load_data_from_file(self):
        tex_pole = QTextEdit()
        lines = str()
        options = QFileDialog.Options()
        options1 = QFileDialog.ReadOnly
        file_name = QFileDialog.getOpenFileName(self, "Выберите файл с данными", "", "Text Files (*.txt);;All Files (*)", options=options1) [0]
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                tex_pole.setText(str(lines))
                self.ui.textEdit.setText(str(lines))        
              
                                         
    def file(self):
        a = list()
         
        with open("1.txt", "r") as file:        
            for line in file:
                a.append(line.strip().split(' '))
                self.ui.textEdit_2.setText(line)
           

    def clear(self):
       self.ui.textEdit.clear()
       self.ui.textEdit_2.clear()

       
app = QtWidgets.QApplication([])
win = MainWindow()
win.show()
sys.exit(app.exec())
