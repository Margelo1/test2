from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def qwer():
    sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)

window.setWindowTitle("Обычное окно")
window.resize(600,600)

pixmap = QtGui.QPixmap("icon9.png")
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
window.setPalette(pal)
window.setMask(pixmap.mask())
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150,30)
button.move(220, 200)
button.clicked.connect(window.close)

ico = QtGui.QIcon("icon4.png")
window.setWindowIcon(ico)
app.setWindowIcon(ico)

window.show()
sys.exit(app.exec_())
