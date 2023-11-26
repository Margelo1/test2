import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen
from PyQt5.QtCore import Qt
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Рисование прямоугольника"
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
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.drawRect(40,40,400,200)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())     
        
