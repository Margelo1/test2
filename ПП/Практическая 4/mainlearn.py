import sys
import random
from learn1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):

    correct1 = "RadioButton"
    correct2 = "ComboBox"
    correct3 = "Tab Widgets"

    variants1 = ["CheckBox", correct1, "pushButton"]
    variants2 = ["CheckBox", "ListBox",correct2]
    variants3 = ["Table Widgets", "List Widgets",correct3]


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        random.shuffle(self.variants1)
        random.shuffle(self.variants2)
        random.shuffle(self.variants3)

        self.ui.radioButton.setText(self.variants1[0])
        self.ui.radioButton_2.setText(self.variants1[1])
        self.ui.radioButton_3.setText(self.variants1[2])

        self.ui.radioButton_4.setText(self.variants2[0])
        self.ui.radioButton_5.setText(self.variants2[1])
        self.ui.radioButton_6.setText(self.variants2[2])

        self.ui.radioButton_7.setText(self.variants3[0])
        self.ui.radioButton_8.setText(self.variants3[1])
        self.ui.radioButton_9.setText(self.variants3[2])
        
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)

        self.ui.buttonGroup.buttonClicked.connect(self.correctAns1)
        self.ui.buttonGroup_2.buttonClicked.connect(self.correctAns2)
        self.ui.buttonGroup_3.buttonClicked.connect(self.correctAns3)

    def correctAns1(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text()==self.correct1:
                    self.ui.statusbar.showMessage("Верно ! Вторая вкладка активна",5000)
                    self.ui.tab.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(1,True)
                    
    def correctAns2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text()==self.correct2:
                    self.ui.statusbar.showMessage("Верно ! Третья вкладка активна",5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(2,True)
                    
                    
    def correctAns3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text()==self.correct3:
                    self.ui.statusbar.showMessage("Тест окончен",5000)
                    self.ui.tab_3.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(3,True)
        self.ui.statusbar.showMessage("Тест окончен",5000)
        self.ui.tab_3.setEnabled(False)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWin()
    ui.show()
    sys.exit(app.exec_())                           

        
        
        
        

        
        
        
