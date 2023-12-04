# Билет 22. Программа о состовление конкетной суммы

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from mon import Ui_Form
from random import randint
class main(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pt)
        self.ui.pushButton_2.clicked.connect(self.ex)
        
    def pt(self):
        try:
            summa = self.ui.doubleSpinBox.value() # Введенная сумма
            kol_m = float(self.ui.spinBox_2.value()) # кол-во монет
            k50, k10, k5, k1 = 0, 0, 0, 0
            k50 = float(summa/0.5)
            if str(summa)[-1].endswith('5'):
                k5 = 1
            else:
                print(str(summa)[-1])
                k1 = float(str(summa)[-1])
                print(k1)
                #print(str(summa)[-2])    
                #k10 = float(str(summa)[-2])
                #print(k10)
            
            self.ui.spinBox_2.setValue(k50)
            self.ui.label_7.setText('=%s руб'%(k50 * 0.5))
            self.ui.spinBox_3.setValue(k10)
            self.ui.label_8.setText('=%s руб'%(k10 * 0.1))
            self.ui.spinBox_4.setValue(k5)
            self.ui.label_9.setText('=%s руб'%(k5 * 0.05))
            self.ui.spinBox_5.setValue(k1)
            self.ui.label_10.setText('=%s руб'%(k1 * 0.01))
            if sum ([k50, k10, k5, k1]) != kol_m:
                QMessageBox.information(self,'Результат','Вы набрали необходимую для Вас сумму ',QMessageBox.Ok)
            else:
                self.ui.spinBox_2.setValue(sum[k50, k10, k5, k1])
                QMessageBox.information(self,'Результат','На данное кол-во суммы, не хватает монет',QMessageBox.Ok)
        except Exception as e:print(e)     
    def ex(self):
        close()


app = QApplication(sys.argv)
Form = main()
Form.show()
sys.exit(app.exec_())
