# Создайте в переменной data список значений разных типов перечислив их через запятую 
# внутри квадратных скобок.
# Для каждого элемента в цикле выведите: порядковый номер начиная c единицы значение
# адрес в памяти размер в памяти хэш объекта
# результат проверки на целое число только если он положительный результат проверки
# на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

from sys import getsizeof
from typing import Hashable

data = [1, 3.4, 'hello', [1,2,3], 1,3.14]
for i in range(len(data)):
    print(i+1, end="\t")
    print(data[i], end="\t")
    print(id(data[i]), end="\t")
    print(getsizeof(data[i]), end="\t")
    if (isinstance(data[i],Hashable)):
         print(hash(data[i]), end="\t")
    if (isinstance(data[i],int)):
         print('Целое число')
    if (isinstance(data[i],str)):
         print('Строка')     
    print()