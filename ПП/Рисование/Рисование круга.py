import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Рисование линий"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawEllipses(qp)
        qp.end()

    def drawEllipses(self, qp):
        col = QColor(0,0,0)
        qp.setPen(col)
        qp.setBrush(QColor(255,200,200))
        qp.drawEllipse(40,80,400,400)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())  
        
