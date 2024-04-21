# Задача № 2

# Напишите функцию принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def reverse_key_value(**kwargs):
    """Возвращает словарь, где ключи — это значения аргументов, а значения — имена аргументов.
       Если значение аргумента нехешируемо, используется его строковое представление как ключ."""
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


result_dict = reverse_key_value(name="Алексей", age=44, likes=['чтение', 'прогулки'])
print(result_dict)