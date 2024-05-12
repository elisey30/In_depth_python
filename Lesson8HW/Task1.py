# Задача № 1
#  Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните 
# в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов 
# в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def gather_info(directory):
    """Функция для обхода директории и сбора информации"""
    total_size = 0
    items = []
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            items.append({'type': 'file', 'name': entry, 'parent': directory, 'size': size})
            total_size += size
        elif os.path.isdir(path):
            subdir_size, subdir_items = gather_info(path) 
            items.append({'type': 'directory', 'name': entry, 'parent': directory, 'size': subdir_size})
            items.extend(subdir_items) 
            total_size += subdir_size
    return total_size, items

def save_to_json(data, filename):
    """Функция для сохранения в формат json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def save_to_csv(data, filename):
    """Функция для сохранения в формат csv"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['type', 'name', 'parent', 'size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def save_to_pickle(data, filename):
    """Функция для сохранения в формат pickle"""
    with open(filename, 'wb') as bin_file:
        pickle.dump(data, bin_file)

def process_directory():
    """Объединяющая функция"""
    directory = os.getcwd()  # Получаем текущий рабочий каталог
    _, items = gather_info(directory)
    save_to_json(items, 'files_and_dirs.json')
    save_to_csv(items, 'files_and_dirs.csv')
    save_to_pickle(items, 'files_and_dirs.pickle')

if __name__ == '__main__':
    process_directory()  
