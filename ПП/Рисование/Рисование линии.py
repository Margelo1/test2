import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen
from PyQt5.QtCore import Qt

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

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        qp.setBrush(Qt.white)
        qp.drawLine(400, 100, 100, 100)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())     
