from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Изменение геометрии
        def EditGeometry():
            # Создаем кортеж где храняться информация (x,y,width,height)
            info = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
            # Если (текст пустой) или (состоит из букв)
            if all([len(i) != 0 for i in info]) and all([i.isdigit() for i in info]):
                # Если все ок, меняем геометрию
                self.plainTextEdit.setGeometry(QtCore.QRect(int(info[0]), int(info[1]), int(info[2]), int(info[3])))
            else:
                # Выдаем ошибочное поле
                infoBox = QMessageBox()
                infoBox.setText("Ошибка! заполните все поля")
                infoBox.setWindowTitle("Ошибка")
                infoBox.exec_()

        # Стандартная геометрия
        def DefoltGeometry():
            self.plainTextEdit.setGeometry(QtCore.QRect(110, 80, 321, 241))
            self.plainTextEdit.clear()

        # Добавить строку текста
        def InserText():
            self.plainTextEdit.insertPlainText(self.lineEdit_5.text())

        # Прибавить к строке текста
        def AppendText():
            self.plainTextEdit.appendPlainText(self.lineEdit_5.text())

        # Удалить строку
        def UndoEdit():
            self.plainTextEdit.undo()

        # Увеличить текст
        def ZoomIn():
            self.plainTextEdit.zoomIn(1)

        # Уменьшить текст
        def ZoomOut():
            self.plainTextEdit.zoomOut(1)

        # Очистить весь TextEdit
        def ClearText():
            self.plainTextEdit.clear()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 80, 321, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 40, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(620, 60, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 120, 113, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(620, 180, 113, 22))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 240, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 220, 55, 16))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(EditGeometry)
        self.pushButton.setGeometry(QtCore.QRect(600, 280, 70, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(DefoltGeometry)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 280, 76, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 340, 121, 51))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 320, 101, 21))
        self.label_5.setObjectName("label_5")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(InserText)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 400, 70, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(AppendText)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 400, 70, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.clicked.connect(UndoEdit)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 440, 61, 40))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.clicked.connect(ZoomIn)
        self.pushButton_6.setGeometry(QtCore.QRect(600, 500, 70, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.clicked.connect(ZoomOut)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 500, 70, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.clicked.connect(ClearText)
        self.pushButton_8.setGeometry(QtCore.QRect(680, 440, 61, 40))
        self.pushButton_8.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "plainTextEdit"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Width"))
        self.label_4.setText(_translate("MainWindow", "Height"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))
        self.pushButton_2.setText(_translate("MainWindow", "Стандартное"))
        self.label_5.setText(_translate("MainWindow", "Введите текст"))
        self.pushButton_3.setText(_translate("MainWindow", "Прибавить"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить\nстроку"))
        self.pushButton_6.setText(_translate("MainWindow", "Увеличить"))
        self.pushButton_7.setText(_translate("MainWindow", "Уменьшить"))
        self.pushButton_8.setText(_translate("MainWindow", "Очистить\nлист"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
