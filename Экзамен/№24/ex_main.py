from PyQt5 import QtCore, QtWidgets, QtGui
import sys
from PyQt5 import*
from ex import Ui_MainWindow
from random import randint


class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.zap)

        
    def zap(self):
        try:
            st = self.ui.lineEdit.text()
            stolb = self.ui.lineEdit_2.text()
            self.ui.tableWidget.setColumnCount(int(stolb))
            self.ui.tableWidget.setRowCount(int (st))
            it = int(stolb) * int(st)
            sp = [randint(0,1) for i in range(it)]
            row = self.ui.tableWidget.rowCount()
            col = self.ui.tableWidget.columnCount()
            print(sp)
            
            c = 0
            
            sp_st = []
            for i in range(row):
                for j in range(col):
                    
                    item = sp[c]
                    
                    self.ui.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(item)))
                    c += 1
            s = ''
            q = 0
            
           
            for j in range(col):
                s = ''
                for i in range (row):
                    print('i', i)
                    print('q', q)
                    item = self.ui.tableWidget.item(i, q).text()
                    s += item
                    
                sp_st.append(s)
                    
                if q < col-1:   
                    q += 1 
            print(sp_st)
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            x = 0
            y = 3
            for i in sp_st:
                stro = str(i)
                p = stro.count("0")
                print(p)
                if int(p)%2 == 0:
                    self.ui.tableWidget.setItem(x,y, QtWidgets.QTableWidgetItem(str(0)))
                    x += 1
                else:
                    self.ui.tableWidget.setItem(x,y, QtWidgets.QTableWidgetItem(str(1)))
                    x += 1
                
                
                
            
           
                    
                    
                    
    
                
                
            
        except Exception as e:
            print(e)
       

        

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())


