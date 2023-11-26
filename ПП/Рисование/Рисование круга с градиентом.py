import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen,QRadialGradient
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
        grad = QRadialGradient(QPoint(100,100),100)
        grad.setColorAt(0.25, Qt.red)
        grad.setColorAt(1, Qt.green)
        qp.setBrush(QBrush(grad))
        qp.drawEllipse(10,10,200,200)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_()) 
        
