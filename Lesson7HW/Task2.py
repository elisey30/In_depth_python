# Задача № 2
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from File_edit import generate_name
from File_edit import rename_files

generate_name.generate_files('rnd', 'files')
rename_files.rename_files( 'newname', 3, '.txt', '.md', (3, 6))
