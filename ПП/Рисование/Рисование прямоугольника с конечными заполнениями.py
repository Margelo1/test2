import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen,QConicalGradient
from PyQt5.QtCore import Qt,QPoint
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Рисование прямоугольника с радиентным запролнением"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        grad = QConicalGradient(300,150,150)
        grad.setColorAt(0.0, Qt.white)
        grad.setColorAt(0.2, Qt.green)
        grad.setColorAt(1.0, Qt.black)
        qp.setBrush(QBrush(grad))
        qp.drawRect(40,40,400,200)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_()) 
        
        

        
