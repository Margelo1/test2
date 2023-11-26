import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen,QLinearGradient
from PyQt5.QtCore import Qt
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
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        grad = QLinearGradient(10,40,30,10)
        grad.setColorAt(0.0, Qt.green)
        grad.setColorAt(0.5, Qt.yellow)
        grad.setColorAt(1.0, Qt.red)
        qp.setBrush(QBrush(grad))
        qp.drawRect(10,10,200,200)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_()) 
