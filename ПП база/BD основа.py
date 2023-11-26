import sys
from BD import *
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(120, 670, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Найти")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 670, 91, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("Добавить")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 670, 91, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("Удалить")

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 670, 91, 31))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("Обновить")
        
        self.pushButton.clicked.connect(self.on_selected_1)
        self.pushButton_2.clicked.connect(self.dobavit)
        self.pushButton_3.clicked.connect(self.udalit)
        self.pushButton_4.clicked.connect(self.obnovit)

        conn = sqlite3.connect('База.db')
        cursor = conn.cursor()
        cursor.execute('Select * from Pacient')
        data = []
        data = cursor.fetchall()
        print(data)
        conn.commit()
        conn.close()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        
        print(2)
        row = 0
        for tup in data:
            col = 0

            for item in tup:
            # self.ui.tableWidget.resizeColumnsToContents()
                cellinfo = QTableWidgetItem(str(item))
            #cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        
    def on_selected_1(self):
        text = self.ui.lineEdit.text()
        if self.ui.radioButton.isChecked() and len(text) !=0:
            try:
                print(1)
                text = self.ui.lineEdit.text()
                print(text)

                conn = sqlite3.connect('База.db')
                cursor2 = conn.cursor()
                ss = 'Номер_медполиса='+str('"'+text+'"')
                print(ss)
                cursor2.execute('Select * from Pacient WHERE '+str(ss))
                proba = []
                proba = cursor2.fetchall()
                
                self.ui.tableWidget.setRowCount(len(proba))
                self.ui.tableWidget.setColumnCount(len(proba[0]))
                row = 0
                for tup in proba:
                    col = 0
                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        self.ui.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
            except:
                print("ОШИБКА!!!")
                self.on_selected_4()
        elif self.ui.radioButton_2.isChecked() and len(text) !=0:
            try:
                text = self.ui.lineEdit.text()
                print(text)

                conn = sqlite3.connect('База.db')
                cursor2 = conn.cursor()
                ss2 = 'ФИО_пациента='+str('"'+text+'"')
                print(ss2)
                cursor2.execute('Select * from Pacient WHERE '+str(ss2))
                proba = []
                proba = cursor2.fetchall()
                
                self.ui.tableWidget.setRowCount(len(proba))
                self.ui.tableWidget.setColumnCount(len(proba[0]))
                row = 0
                for tup in proba:
                    col = 0
                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        self.ui.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
            except:
                print("ОШИБКА!!!")
                self.on_selected_4()
        elif self.ui.radioButton_3.isChecked() and len(text) !=0:
            try:
                text = self.ui.lineEdit.text()
                print(text)

                conn = sqlite3.connect('База.db')
                cursor2 = conn.cursor()
                ss3 = 'Дата_посещения='+str('"'+text+'"')
                print(ss3)
                cursor2.execute('Select * from Pacient WHERE '+str(ss3))
                proba = []
                proba = cursor2.fetchall()
                
                self.ui.tableWidget.setRowCount(len(proba))
                self.ui.tableWidget.setColumnCount(len(proba[0]))
                row = 0
                for tup in proba:
                    col = 0
                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        self.ui.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
            except:
                print("ОШИБКА!!!")
                self.on_selected_4()
        elif self.ui.radioButton_4.isChecked():
            conn = sqlite3.connect('База.db')
            cursor = conn.cursor()
            cursor.execute('Select * from Pacient')
            data = []
            data = cursor.fetchall()
            print(data)
            conn.commit()
            conn.close()
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(len(data[0]))
        
            if self.ui.radioButton_4.isChecked():
                print(2)
                row = 0
                for tup in data:
                    col = 0
                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        self.ui.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
        else:
            print("Введите данные")

    '''def on_selected_2(self):
        print(1)
        text = self.ui.lineEdit.text()
        print(text)

        conn = sqlite3.connect('База.db')
        cursor2 = conn.cursor()
        ss2 = 'ФИО_пациента='+str('"'+text+'"')
        print(ss2)
        cursor2.execute('Select * from Pacient WHERE '+str(ss2))
        proba = []
        proba = cursor2.fetchall()
        
        self.ui.tableWidget.setRowCount(len(proba))
        self.ui.tableWidget.setColumnCount(len(proba[0]))
        row = 0
        for tup in proba:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    def on_selected_3(self):
        print(1)
        text = self.ui.lineEdit.text()
        print(text)
        conn = sqlite3.connect('База.db')
        cursor2 = conn.cursor()
        ss3 = 'Дата_посещения='+str('"'+text+'"')
        print(ss3)
        cursor2.execute('Select * from Pacient WHERE '+str(ss3))
        proba = []
        proba = cursor2.fetchall()
        
        self.ui.tableWidget.setRowCount(len(proba))
        self.ui.tableWidget.setColumnCount(len(proba[0]))
        row = 0
        for tup in proba:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        
    def on_selected_4(self):
        conn = sqlite3.connect('База.db')
        cursor = conn.cursor()
        cursor.execute('Select * from Pacient')
        data = []
        data = cursor.fetchall()
        print(data)
        conn.commit()
        conn.close()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        print(2)
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1'''
    def dobavit(self):
        self.w2 = Window1()
        self.w2.show()
        self.close()
    def udalit(self):

        def delete_sqlite_record(dev_id):
            try:
                sqlite_connection = sqlite3.connect('База.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")

                sql_update_query = """DELETE from Pacient where Номер_медполиса = ?"""
                cursor.execute(sql_update_query, (dev_id, ))
                sqlite_connection.commit()
                print("Запись успешно удалена")
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")
        
        rows = sorted(set(index.row() for index in self.ui.tableWidget.selectedIndexes()))
        for row in rows:
            print('Row %d is selected' % row)
            print(row)
        text = self.ui.tableWidget.item(row, 0).text()
        print(text)
        delete_sqlite_record(text)

        conn = sqlite3.connect('База.db')
        cursor = conn.cursor()
        cursor.execute('Select * from Pacient')

        data = []
        data = cursor.fetchall()
        print(data)
        conn.commit()
        conn.close()
        
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        
        print(3)
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
    def obnovit(self):
        rows = sorted(set(index.row() for index in self.ui.tableWidget.selectedIndexes()))
        for row in rows:
            print(row)
        columns = sorted(set(index.column() for index in self.ui.tableWidget.selectedIndexes()))
        for col in columns:
            print(col)
            
        text = self.ui.tableWidget.item(row, col).text()
        print(text)
        text_2 = self.ui.tableWidget.item(row, 0).text()
        print(text_2)
        text_3 = self.ui.tableWidget.item(row, 1).text()
        if int(col) == 0:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Номер_медполиса = ? where Номер_участка = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_3]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 1:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Номер_участка = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 2:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set ФИО_пациента = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 3:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Дата_рождения = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 4:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Пол_мужской = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 5:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Диагноз = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)
        elif int(col) == 6:
            def update_multiple_records(record_list):
                try:
                    sqlite_connection = sqlite3.connect('База.db')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")

                    sqlite_update_query = """Update Pacient set Дата_посещения = ? where Номер_медполиса = ?"""
                    cursor.executemany(sqlite_update_query, record_list)
                    sqlite_connection.commit()
                    print("Записей", cursor.rowcount, ". Успешно обновлены")
                    sqlite_connection.commit()
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")

            a = [text, text_2]
            records_to_update = []
            records_to_update.append(a)
            print(records_to_update)
            update_multiple_records(records_to_update)

class Window1(QWidget):
    def __init__(self, parent = None):
        super(Window1, self).__init__()
        self.setWindowTitle('Добавить в базу')
        self.resize(800, 600)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setMaximumWidth(800)
        self.setMaximumHeight(600)

        self.tableWidget_2 = QtWidgets.QTableWidget(self)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 10, 771, 411))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        conn = sqlite3.connect('База.db')
        cursor = conn.cursor()
        cursor.execute('Select * from Pacient')
        data = []
        data = cursor.fetchall()
        conn.commit()
        conn.close()
                
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(len(data[0]))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(120, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setText("Добавить")
        self.pushButton.clicked.connect(self.texty)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 550, 91, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("Закрыть")
        self.pushButton_2.clicked.connect(self.zakrit)
        
    def texty(self):
        conn = sqlite3.connect('База.db')
        cursor = conn.cursor()
        cursor.execute('Select * from Pacient')
        data = []
        data = cursor.fetchall()
        print(data)
        conn.commit()
        conn.close()
        
        a = []
        for i in range(len(data[0])):
            text = self.tableWidget_2.item(0, i).text()
            a.append(text)
            print(text)
        print(a)
        def insert_multiple_records(records):
            try:
                sqlite_connection = sqlite3.connect('База.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")

                sqlite_insert_query = """INSERT INTO Pacient VALUES (?, ?, ?, ?, ?, ?, ?);"""

                cursor.executemany(sqlite_insert_query, records)
                sqlite_connection.commit()
                print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
                sqlite_connection.commit()
                cursor.close()

            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")
        records_to_insert = []
        records_to_insert.append(a)
        print(records_to_insert)

        insert_multiple_records(records_to_insert)

        self.w1 = MyWin()
        self.w1.show()
        self.close()
    def zakrit(self):
        self.w1 = MyWin()
        self.w1.show()
        self.close()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
