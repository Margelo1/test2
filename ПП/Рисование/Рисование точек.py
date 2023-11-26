import sys, random
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = "Я люблю маму"
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Draw text")
        self.show()

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(100000):
            x = random.randint(1, size.width()-2)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
