import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen,QPainterPath,QRadialGradient
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
        qp.setPen(QPen(Qt.red,5, Qt.DashLine))
        path.lineTo(160,400)
        path.lineTo(350,100)
        path.lineTo(0,0)
        grad = QRadialGradient(QPoint(170,160),130)
        grad.setColorAt(0.25, Qt.red)
        grad.setColorAt(1, Qt.green)
        qp.setBrush(QBrush(grad))
        qp.drawPath(path)
        
        #qp = QPainter(self)
        grad_2 = QRadialGradient(QPoint(495,105),100)
        grad_2.setColorAt(0.25, Qt.red)
        grad_2.setColorAt(1, Qt.green)
        qp.setBrush(QBrush(grad_2))
        qp.drawEllipse(400,10,200,200)

        #qp = QPainter(self)
        qp.setPen(QPen(Qt.red,5, Qt.DashLine))
        #qp.setBrush(Q)
        qp.drawArc(550,70,300,300,0 * 16, 90 * 16)
        
        
        

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_()) 
        
