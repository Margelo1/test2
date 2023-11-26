from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(flags=QtCore.Qt.Dialog)

window.setWindowTitle("Всплывающие подсказки")
window.resize(300,300)

button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 135)

button.setToolTip("Это всплывающая подсказка для кнопки")
button.clicked.connect(window.close)
button.setToolTipDuration(5)
window.setToolTip("Это всплывающая подсказка для окна")
button.setToolTipDuration(-1)
button.setWhatsThis("Это справка для кнопки")
window.setWhatsThis("Это справка для окна")

ico = QtGui.QIcon("icon2.png")
window.setWindowIcon(ico)
app.setWindowIcon(ico)

window.show()
sys.exit(app.exec_())
