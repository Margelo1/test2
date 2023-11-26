import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush, QPen
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Самолет"
        self.top = 50
        self.left = 50
        self.width = 1400
        self.height = 800
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        pen = QPen(Qt.black, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        qp.setPen(pen)
        #Фюзеляж
        qp.drawLine(300, 300, 400, 290)
        qp.drawLine(400, 290, 500, 290)
        qp.drawLine(620, 290, 900, 300)
        qp.drawLine(900, 300, 1100, 310)
        qp.drawLine(1100, 310, 1300, 320)
        
        qp.drawArc(215,300,200,200, 100 * 16, 180 * 13)
        qp.drawLine(279, 494, 450, 500)
        qp.drawLine(450, 500, 900, 440)
        qp.drawLine(900, 440, 1200, 370)
        qp.drawLine(1200, 370, 1300, 320)

        qp.drawLine(330, 297, 330, 495)

        #Хвост
        qp.drawArc(1200,150,80,100,20 * 16, 180 * 10)
        qp.drawLine(1130, 309, 1213, 163)
        qp.drawLine(1300, 320, 1276, 178)
        qp.drawLine(1240, 150, 1240, 280)
        qp.drawLine(1240, 280, 1294, 280)
        
        #Кабина пилота
        qp.drawArc(460,110,200,200,-55 * 16, -115 * 10)
        qp.drawArc(445,235,100,100,90 * 16, 90 * 16)
        qp.drawLine(500, 235, 500, 285)
        
        #Крыло
        qp.drawArc(400,400,300,300,40 * 16, 100 * 16)
        qp.drawLine(437, 455, 663, 455)
        #Колеса
        qp.drawEllipse(400,570,80,80)
        qp.drawLine(415, 500, 420, 575)
        qp.drawLine(470, 500, 470, 540)
        qp.drawLine(470, 540, 450, 571)

        qp.drawEllipse(1280,360,35,35)
        qp.drawLine(1280, 330, 1290, 360)
        qp.drawLine(1270, 335, 1290, 360)
        #Винт
        qp.drawArc(187,375,50,50,90 * 16, 180 * 16)
        qp.drawLine(190, 280, 200, 370)
        qp.drawLine(210, 280, 200, 370)
        qp.drawLine(200, 245, 210, 280)
        qp.drawLine(200, 245, 190, 280)

        qp.drawLine(200, 423, 190, 513)
        qp.drawLine(200, 423, 210, 513)
        qp.drawLine(190, 513, 200, 548)
        qp.drawLine(210, 513, 200, 548)

App = QApplication(sys.argv)
window = Example()
sys.exit(App.exec_())    
