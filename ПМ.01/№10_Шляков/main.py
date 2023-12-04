from PyQt5 import QtWidgets, QtGui, QtCore
from inter import Ui_MainWindow
import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Add)
        '''self.ui.pushButton_2.clicked.connect(self.Del)'''
        self.tb = 0
        if self.tb == 0:
            res=[]
            res2=[]
            con = sqlite3.connect('database.db', timeout=10)
            cur = con.cursor()
            cur.execute('select * from Авиапассажиры')
            self.result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setRowCount(len(self.result)+1)
            self.ui.tableWidget.setColumnCount(len(self.result[0]))
            headers = ['Наименование','Страна','Город отправления', 'Город назначения', 'Номер рейса', 'Дата вылета', 'Время вылета', 'Фамилия', 'Класс места', 'Наличие багажа']
            self.ui.tableWidget.setHorizontalHeaderLabels(headers)
            header = self.ui.tableWidget.horizontalHeader()
            for i in range(len(self.result)):
                for j in range(len(self.result[0])):
                    self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(self.result[i][j])))
            con.commit()
            cur.close()
            con.close()

    def Add(self):
        con = sqlite3.connect('database.db', timeout = 10)
        cur = con.cursor()
        cur.execute('pragma foreign_keys = on;')
        table_name = 'Авиапассажиры'
        # Получаем количество строк в tablewidget
        rows = self.ui.tableWidget.rowCount()
        # Получаем количество столбцов в tablewidget
        columns = self.ui.tableWidget.columnCount()
        
        # Проверяем, есть ли данные в tablewidget
        if rows == 0:
            print("Tablewidget is empty, cannot add record.")
            return
        
        # Получаем данные из tablewidget и формируем список записей для вставки
        records = []
        for row in range(rows):
            record = []
            for col in range(columns):
                item = self.ui.tableWidget.item(row, col)
                if item:
                    record.append(item.text())
                else:
                    record.append("")
            #records.append(tuple(record))
        try:
                # Добавляем записи в таблицу
                
            cur.execute(f"INSERT INTO {table_name} values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", records)
                
                # Подтверждаем изменения в базе данных
            con.commit()
                
            print("Records added successfully.")
            
        except Exception as e:
                # Распечатываем ошибку, если возникла ошибка
            print(f"Error occurred: {str(e)}")
            con.rollback()
            
        finally:
                # Закрываем соединение с базой данных
            cur.close()
            con.close()
        
app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
