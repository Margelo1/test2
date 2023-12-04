# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\№21_Косотуров\interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 179)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_exit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_exit.setFont(font)
        self.action_exit.setObjectName("action_exit")
        self.action_about = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.action_info = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_info.setFont(font)
        self.action_info.setObjectName("action_info")
        self.menu.addAction(self.action_info)
        self.menu.addAction(self.action_about)
        self.menu.addAction(self.action_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сумматор"))
        self.label.setText(_translate("MainWindow", "Числа:"))
        self.label_2.setText(_translate("MainWindow", "Сумма:"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Об авторе"))
        self.action_2.setText(_translate("MainWindow", "Инструкция"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_about.setText(_translate("MainWindow", "Об авторе"))
        self.action_info.setText(_translate("MainWindow", "Инструкция"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

