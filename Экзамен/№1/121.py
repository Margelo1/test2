import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QLineEdit, QWidget, QFileDialog

class CostCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Себестоимость и наценка товаров')

        # Создаем TableWidget для отображения данных
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(['Наименование товара', 'Количество', 'Себестоимость'])

        # Создаем поле для ввода стоимости
        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText('Введите стоимость одной единицы товара')

        # Кнопка для выбора файла с данными
        self.load_file_button = QPushButton('Загрузить данные из файла', self)
        self.load_file_button.clicked.connect(self.load_data_from_file)

        # Кнопка для рассчета
        self.calculate_button = QPushButton('Рассчитать', self)
        self.calculate_button.clicked.connect(self.calculate_costs)

        # Создаем главный виджет и размещаем все элементы на нем
        central_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.load_file_button)
        layout.addWidget(self.table)
        layout.addWidget(self.price_input)
        layout.addWidget(self.calculate_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.loaded_data = False  # Переменная для отслеживания загрузки данных

    def load_data_from_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл с данными", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if i >= 5:
                    break  # Чтение только первых 5 строк
                name, quantity = line.strip().split(',')
                quantity = int(quantity)
                self.table.setItem(i, 0, QTableWidgetItem(name))
                self.table.setItem(i, 1, QTableWidgetItem(str(quantity)))
            self.loaded_data = True

    def calculate_costs(self):
        if not self.loaded_data:
            return

        try:
            price_per_unit = float(self.price_input.text())
        except ValueError:
            self.price_input.clear()
            return

        for i in range(self.table.rowCount()):
            quantity_item = self.table.item(i, 1)
            if quantity_item is not None:
                quantity = int(quantity_item.text())
                cost = price_per_unit * quantity
                markup = 0.12 * cost
                price_with_markup = cost + markup
                self.table.setItem(i, 2, QTableWidgetItem(f'{cost:.2f} ({price_with_markup:.2f})'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CostCalculatorApp()
    window.show()
    sys.exit(app.exec_())
