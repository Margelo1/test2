import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        a = int(e.mimeData().text())
        self.setGeometry(200,90,75+a,23+a)
class Example (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 20)

        button = Button("Кнопка", self)
        button.move(200, 90)

        self.setWindowTitle('Увеличение кнопки')
        self.setGeometry(300,300,500,300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Example()
    myapp.show()
    sys.exit(app.exec_())
