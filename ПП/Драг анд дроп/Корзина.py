import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
    
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)

    
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setAcceptDrops(True)
        self.button1 = Button('Корзина', self)
        self.button1.move(400,270)
        self.button = Button('Кнопка', self)
        self.button.move(100,65)
        self.setWindowTitle('Корзина')
        self.setGeometry(300,300,500,300)
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        try:
            position = e.pos()
            self.button.move(position)
            e.setDropAction(Qt.MoveAction)
            e.accept()
            if int(e.pos().x()) >= 400 and int(e.pos().y()) >= 270:
                self.button.deleteLater()
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
