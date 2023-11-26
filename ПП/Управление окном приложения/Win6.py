# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(windowl,QtCore.Qt.Windwo)
    modalWindow.setWindowTitle("Модальное окно")
    modalWindow.resize(300,165)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(Qt.Core.Qt.WA_DeleteOnClose,True)
    modalWindow.move(windowl.geometry().center() - modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Обычное окно")
window.resize(300,165)
ico = QtGui.QIcon("icon2.png")
window.setWindowIcon(ico) # Значок для окна
app.setWindowIcon(ico) # Значок приложения
window.show()
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(QtGui.QPixmap("icon.png")))
window.setPalette(pal)
sys.exit(app.exec_())
