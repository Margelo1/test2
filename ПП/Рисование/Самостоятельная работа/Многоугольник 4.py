import sys, math
from PyQt5 import QtCore,QtGui, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))
        self.pen.setWidth(5)
        self.brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))
        self.polygon = self.createPoly(4,150,0)
        

    def createPoly(self,n,r,s):
        polygon = QtGui.QPolygonF()
        w = 360/n
        for i in range(n):
            t = w*i + s
            x = r*math.cos(math.radians(t))
            y = r*math.sin(math.radians(t))
            polygon.append(QtCore.QPointF(self.width()/2+x, self.height()/2+y))
        return polygon

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        print(1)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon(self.polygon)

App = QtWidgets.QApplication(sys.argv)
window = MyWidget()
window.show()
sys.exit(App.exec_())
