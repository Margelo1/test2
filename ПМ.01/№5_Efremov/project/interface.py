# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QLabel, QPushButton, QLineEdit, QCheckBox {\n"
"    color: white;\n"
"    font-family: Rubick;\n"
"    font-size: 9pt;\n"
"    font-weight: 600;\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"    background-color: rgb(72, 97, 121);\n"
"}\n"
"    \n"
"QPushButton {\n"
"    background-color: rgb(41, 46, 54);\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"  QPushButton:hover {\n"
"    background-color:  rgb(36, 41, 48);\n"
"}\n"
"\n"
"  QPushButton:pressed {\n"
"    background-color:  rgb(24, 28, 33);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #929292;\n"
"    color: #d1d1d1;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(41, 46, 54, 200);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 2px solid rgba(52, 67, 79, 200);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid rgba(15, 17, 20, 200);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #238fd6;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #2AA8F7;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed{\n"
"    border: 2px solid #0069d9;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #238fd6;\n"
"    background-color: #ffffff;\n"
"    image: url(:/icon/icon/check_mark.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover{\n"
"     border: 2px solid #2AA8F7;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed{\n"
"    border: 2px solid #0069d9;\n"
"}\n"
"\n"
"QLabel#label_error_code_cc, #label_error_code_rcc{\n"
"    font-size: 8pt;\n"
"}\n"
"QLabel#label_img_login{\n"
"    border-image: url(Resources/style/picture/login.jpg);\n"
"    border-top-left-radius: 80px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_img_recovery{\n"
"    border-image: url(Resources/style/picture/recovery.jpg);\n"
"    border-top-left-radius: 80px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_img_registration{\n"
"    border-image: url(Resources/style/picture/registration.jpg);\n"
"    border-top-left-radius: 80px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_blackout_img{\n"
"    background-color:rgba(0, 0, 0, 80);\n"
"    border-top-left-radius: 80px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_welcome_message{\n"
"    background-color:rgba(0, 0, 0, 75);\n"
"}\n"
"\n"
"QLabel#label_icon_cc, #label_icon_lg, #label_icon_rg, #label_icon_rcc, #label_icon_rced{\n"
"    image: url(:/icon/icon/book.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_forgotPassword_lg {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: #238fd6;\n"
"}\n"
"\n"
"QPushButton#pushButton_forgotPassword_lg:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: #007bff;\n"
"}\n"
"\n"
"QPushButton#pushButton_forgotPassword_lg:pressed {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"       color: #0069d9;\n"
"}\n"
"\n"
"QPushButton#pushButton_close {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border-radius: 12px;\n"
"    padding: -3px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton#pushButton_close:hover {\n"
"    background-color: rgb(198, 24, 24);\n"
"}\n"
"\n"
"QPushButton#pushButton_close:pressed {\n"
"    background-color: rgb(162, 19, 19);\n"
"}\n"
"\n"
"QLabel#label_text{\n"
"    font-size: 8pt;\n"
"    color: black;\n"
"}\n"
"\n"
"QLabel#label_icon_question_rg, #label_icon_question_lg, #label_icon_question_rc, #label_icon_question_rced{\n"
"    image: url(:/icon/icon/question.png);\n"
"}\n"
"\n"
"QToolTip {\n"
"    font-family: Rubick;\n"
"    font-size: 8pt;\n"
"    font-weight: 600;\n"
"    color: white;\n"
"    padding: 2px;\n"
"    border: 1px solid white;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(41, 46, 54);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Счет кратных чисел"))
        self.label.setText(_translate("MainWindow", "Введите количество чисел"))
        self.pushButton.setText(_translate("MainWindow", "Считать"))
        self.label_2.setText(_translate("MainWindow", "Самое маленькое число"))
        self.menu.setTitle(_translate("MainWindow", "Информация"))
        self.action.setText(_translate("MainWindow", "Об авторе"))
        self.action_2.setText(_translate("MainWindow", "Инструкция"))
        self.action_3.setText(_translate("MainWindow", "Задание"))
        self.action_4.setText(_translate("MainWindow", "Закрыть"))

