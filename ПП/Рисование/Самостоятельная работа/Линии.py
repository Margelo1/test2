import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Линии"
        self.top = 150
        self.left = 150
        self.width = 600
        self.height = 600
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        pen = QPen(Qt.red,3)
        qp.setPen(pen)
        qp.drawLine(500, 100, 100, 100)
        
        qp1 = QPainter(self)
        pen = QPen(Qt.yellow,6,Qt.DotLine)
        qp1.setPen(pen)
        qp1.drawLine(500, 140, 100, 140)
        
        qp2 = QPainter(self)
        pen = QPen(Qt.green,10,Qt.DotLine, Qt.RoundCap)
        qp2.setPen(pen)
        qp2.drawLine(500, 180, 100, 180)

        qp3 = QPainter(self)
        pen = QPen(Qt.cyan,6,Qt.DotLine, Qt.FlatCap)
        qp3.setPen(pen)
        qp3.drawLine(500, 220, 100, 220)

        qp4 = QPainter(self)
        pen = QPen(Qt.blue,8,Qt.DashDotDotLine, Qt.RoundCap)
        qp4.setPen(pen)
        qp4.drawLine(500, 260, 100, 260)
        

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())     
