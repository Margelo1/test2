import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen,QPainterPath,QLinearGradient
from PyQt5.QtCore import Qt,QPoint
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Рисование прямоугольника с радиентным запролнением"
        self.top = 150
        self.left = 150
        self.width = 1000
        self.height = 700
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        
        path = QPainterPath()
        qp.setPen(QPen(Qt.green,5, Qt.DotLine))
        path.lineTo(160,400)
        path.lineTo(350,100)
        path.lineTo(0,0)
        brush = QBrush(Qt.red,Qt.SolidPattern)
        qp.setBrush(brush)
        '''grad = QLinearGradient(10,40,30,10)
        grad.setColorAt(0.0, Qt.green)
        grad.setColorAt(0.5, Qt.yellow)
        grad.setColorAt(1.0, Qt.red)
        qp.setBrush(QBrush(grad))'''
        qp.drawPath(path)
        
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 5, Qt.DotLine))
        painter.setBrush(brush)
        painter.drawRect(400,40,400,200)

        qp.drawLine(500, 400, 500, 600)
        qp.drawLine(500, 400, 400, 500)
        qp.drawLine(500, 400, 600, 500)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_()) 
        
