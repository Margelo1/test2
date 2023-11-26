import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setGeometry(300, 300, 350, 500)
        self.setWindowTitle("Color")
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
  
    def drawBrushes(self, qp):

        qp.drawRect(129, 15, 90, 40)
        qp.drawLine(173, 55, 173, 105)
        qp.drawLine(173, 105, 215, 130)
        qp.drawLine(215, 130, 173, 150)
        qp.drawLine(173, 150, 133, 130)
        qp.drawLine(133, 130, 173, 105)
        qp.drawLine(215, 130, 250, 130)
        qp.drawLine(133, 130, 100, 130)
        qp.drawLine(100, 130, 100, 170)
        qp.drawLine(250, 130, 250, 170)
        qp.drawRect(55, 170, 90, 40)
        qp.drawRect(205, 170, 90, 40)
        qp.drawLine(100, 210, 100, 250)
        qp.drawLine(250, 210, 250, 250)
        qp.drawLine(100, 250, 250, 250)
        qp.drawLine(180, 250, 180, 300)
        qp.drawRect(135, 300, 90, 40)

if __name__ =="__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())        
        
        

    
