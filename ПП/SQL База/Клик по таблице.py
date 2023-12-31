from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
 
 
# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))             # Устанавливаем размеры
        self.setWindowTitle("Работа с QTableWidget")    # Устанавливаем заголовок окна
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет
 
        grid_layout = QGridLayout()             # Создаём QGridLayout
        central_widget.setLayout(grid_layout)   # Устанавливаем данное размещение в центральный виджет
 
        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(3)     # Устанавливаем три колонки
        self.table.setRowCount(2)        # и одну строку в таблице
 
        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
 
        # Устанавливаем всплывающие подсказки на заголовки
        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
 
        # Устанавливаем выравнивание на заголовки
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
 
        # заполняем первую строку
        self.table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(1, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(1, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(1, 2, QTableWidgetItem("Text in column 3"))
 
        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()
 
        grid_layout.addWidget(self.table, 0, 0)   # Добавляем таблицу в сетку
 
        self.table.clicked.connect(self.clicked_table)
 
 
    def clicked_table(self):
        rows = sorted(set(index.row() for index in self.table.selectedIndexes()))
        for row in rows:
            print('Row %d is selected' % row)
     
 
if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
