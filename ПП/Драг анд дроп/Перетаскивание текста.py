import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True) #разрешена перетаскивания для виджета

    def dragEnterEvent(self,e): #сообщаем тип данных(текстовый)
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self ,e):
        self.setText(e.mimeData().text())
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle("Перетаскивание текста")
        self.setGeometry(300, 300, 300, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Example()
    myapp.show()
    sys.exit(app.exec_())
            
