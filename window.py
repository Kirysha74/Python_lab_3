import csv
import sys
from PyQt5.QtWidgets import QCalendarWidget, QLineEdit, QFileDialog, QApplication, QWidget, QPushButton, QGridLayout, QLabel
from utils import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.lst = read_csv(self.filepath[0])
    def initUI(self):
        try:
            self.filepath = QFileDialog.getOpenFileName(self, 'Select file with dataset', filter = "*.csv")
        except:
            print(self.filepath)

        self.setWindowTitle('Графическая оболочка')
        self.setGeometry(800, 800, 800, 600)

        self.select_new_dataset = QPushButton('Загрузить новый датасет', self)
        self.select_new_dataset.clicked.connect(self.select_new_dataset_clicked)
        
        self.btn_get_value = QPushButton('Получить курс', self)
        self.btn_get_value.clicked.connect(self.get_value_clicked)
        
        self.btn_save_dataset = QPushButton('Сохранить исходный датасет', self)
        self.btn_save_dataset.clicked.connect(self.save_dataset_clicked)

        self.btn_split_by_years = QPushButton('Разбить датасет по годам', self)
        self.btn_split_by_years.clicked.connect(self.split_by_years_clicked)

        self.btn_split_by_weeks = QPushButton('Разбить датасет по неделям', self)
        self.btn_split_by_weeks.clicked.connect(self.split_by_weeks_clicked)

        self.btn_split_by_columns = QPushButton('Разбить датасет на столбцы', self)
        self.btn_split_by_columns.clicked.connect(self.split_by_columns_clicked)

        self.calendar = QCalendarWidget(self)
        
        self.label1 = QLabel('Дата', self)
        self.label2 = QLabel('Курс', self)
        
        vbox = QGridLayout()
        
        vbox.addWidget(self.select_new_dataset, 0, 0)
        vbox.addWidget(self.btn_get_value, 0, 2)
        vbox.addWidget(self.calendar, 1, 0, 1, 4)
        vbox.addWidget(self.label1, 2, 0)
        vbox.addWidget(self.label2, 2, 2)
        vbox.addWidget(self.btn_save_dataset, 3, 0)
        vbox.addWidget(self.btn_split_by_years, 3, 1)
        vbox.addWidget(self.btn_split_by_weeks, 3, 2)
        vbox.addWidget(self.btn_split_by_columns, 3, 3)
        self.setLayout(vbox)

    def select_new_dataset_clicked(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Select file with dataset')
        
    def get_value_clicked(self):
        self.date = self.calendar.selectedDate()
        self.value = (get_value(self.date, self.filepath[0]))
        if (self.value):
            self.label2.setText(str(self.value) + " RUB")
        else:
            self.label2.setText("Данные для этой даты отсутствуют")
        self.label1.setText(self.date.toString())

    def save_dataset_clicked(self):
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        save_dataset(self.filepath[0], self.folderpath)

    def split_by_years_clicked(self):
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        write_years(self.filepath[0], self.folderpath)

    def split_by_weeks_clicked(self):
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        write_weeks(self.filepath[0], self.folderpath)

    def split_by_columns_clicked(self):
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        write_csv_columns(self.filepath[0], self.folderpath, ["X", "Y"])

        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())