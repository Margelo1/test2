import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen
from PyQt5.QtCore import Qt
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Рисование прямоугольника с сеткой"
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
        qp = QPainter(self)
        qp.setBrush(QBrush(Qt.red,Qt.CrossPattern))
        pen = QPen(Qt.blue,2,Qt.DotLine)
        qp.setPen(pen)
        qp.drawRect(50,50,390,390)



App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())         
