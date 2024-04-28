# Задача № 1
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_path(full_path):
    """Возвращает кортеж из пути, имени файла и расширения файла."""
    path, filename = os.path.split(full_path) # Получаем путь к директории и полное имя файла
    basename, extension = os.path.splitext(filename) # Разделяем имя файла на имя и расширение
    return (path, basename, extension) # Возвращаем кортеж

path_to_file = "/учебная/пользователь/документы/Task.py"
result = split_path(path_to_file)
print(result)  
