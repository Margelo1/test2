# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Анаграммы.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 490)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("black")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setStyleSheet("")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аннаграммы"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите второе слово:"))
        self.pushButton.setText(_translate("MainWindow", "Определить"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите первое слово:"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Сохранить в файл"))
        self.action_2.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

