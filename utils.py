import csv
import sys

from PyQt5.QtWidgets import QCalendarWidget, QFileDialog, QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import QDate


def read_csv(path: str) -> list:
    """
    Read the CSV file and save it to the list
    """
    try:
        lst = []
        with open(path) as file:
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                lst.append(row)
        return lst
    except Exception as ex:
        print("Возникла ошибка")
        print(ex)
 
def write_csv_columns(filepath: str, dir_name: str, column_names: list) -> None:
    """
    Divides a CSV file into several files by columns
    """
    try:
        with open(filepath) as file:
            lst = []
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                lst.append(row)
                    
            for i in range(len(column_names)):
                with open(f"{dir_name}/{column_names[i]}.csv", "w") as new_file:
                    writer = csv.writer(new_file, delimiter = ",", lineterminator="\r")
                    writer.writerows([[row[i]] for row in lst])
    except Exception as ex:
        print("Возникла ошибка")
        return None

def write_years(filename: str, dir_name: str) -> None:
    """
    splits the original csv file into several files, where each individual file will correspond to one year
    """
    try:
        lst = []
        with open(filename) as file:
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                lst.append(row)

        year = [lst[0]]
        for row in lst[1:]:
            if year[-1][0][:4] == row[0][:4]:
                year.append(row)
            else:
                with open(dir_name + "\\" + year[0][0].replace(".", "") + "_" + year[-1][0].replace(".", "") + ".csv", "w") as file:
                    writer = csv.writer(file, delimiter = ",", lineterminator = "\r")
                    writer.writerows(year)
                year = [row]
    except Exception as ex:
        print("Возникла ошибка")
        return None

def write_weeks(filename: str, dir_name: str) -> None:
    """
    splits the original csv file into several files, where each individual file will correspond to one week
    """
    try:
        with open(filename) as file:
            lst = []
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                lst.append(row)
    
        weeks = []
        past_day = QDate(int(lst[0][0][:4]), int(lst[0][0][5:7]), int(lst[0][0][8:]))
        for row in lst[1:]:
            day = QDate(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:]))
            if (day.dayOfWeek() < past_day.dayOfWeek()):
                weeks.append(row)
                past_day = day 
            else:
                with open(dir_name + "\\" + weeks[0][0].replace(".", "") + "_" + weeks[-1][0].replace(".", "") + ".csv", "w") as file:
                    writer = csv.writer(file, delimiter = ",")
                    writer.writerows(weeks)
                weeks = [row]
                past_day = day
    except Exception as ex:
        print(ex)   
        return None 

def get_value(day_date: QDate, path: str) -> float:
    """
    Get the value of the exchange rate on the transmitted date
    """
    try:
        with open(path) as file:
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                dat = row[0].split("-")
                if (day_date == QDate(int(dat[0]), int(dat[1]), int(dat[2]))):
                    return float(row[1])  
        return None  
    except Exception as ex:
        print(ex)   
        return None 

def save_dataset(filepath: str, dir_name: str) -> None:
    """
    Divides a CSV file into several files by columns
    """
    try:
        with open(filepath, "r") as file:
            lst = []
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                lst.append(row)
                
            with open(dir_name + "//" + filepath.split("/")[-1], "w") as new_file:
                writer = csv.writer(new_file, delimiter = ",", lineterminator="\r")
                writer.writerows(lst)
    except Exception as ex:
        print("Возникла проблема")
        print(ex)
