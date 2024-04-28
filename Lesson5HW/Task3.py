# Задача № 3
# Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    """Генератор чисел Фибоначчи."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):  # Выведем первые 10 чисел Фибоначчи
    print(next(fib_gen))
