# Задача № 1
# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def rename_files(new_name, num_digits, src_extension, dst_extension, name_slice, directory=None):
    """
    Функция для группового переименования файлов в текущей каталоге или в указанной директории.
    
    new_name: Новое имя файла
    num_digits: Количество цифр в порядковом номере
    src_extension: Расширение исходных файлов для переименования
    dst_extension: Расширение конечных файлов
    name_slice: Диапазон сохраняемого оригинального имени (tuple, например, (3, 6))
    directory: Путь к каталогу с файлами для переименования (опционально)
    """
    if directory is None:
        directory = os.getcwd()  # Получаем текущий рабочий каталог

    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(src_extension):
            original_part = filename[name_slice[0]:name_slice[1]]
            num_part = str(i).zfill(num_digits)
            new_filename = f"{original_part}{new_name}{num_part}.{dst_extension}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            i += 1


rename_files('newname', 3, '.txt', '.md', (3, 6))
