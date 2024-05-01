# Задача № 1
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from datetime import datetime as dt
from calendar import isleap

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True 
    except ValueError:
        return False
    

def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")   

if __name__=="__main__":
    if len(sys.argv) > 1: # Проверяем, переданы ли аргументы командной строки
        date_input = sys.argv[1]  # Получаем дату из первого аргумента командной строки
        result = check_date(date_input)
        print("Дата корректна:", result)
    else:
        print("Пожалуйста, передайте дату в формате 'dd.mm.yyyy'")
        