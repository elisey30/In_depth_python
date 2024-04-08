# Задача № 2

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

frak1 = input("Введите первую дробь в формате a/b: ")
frak2 = input("Введите вторую дробь в формате a/b: ")
f1 = Fraction(frak1)
f2 = Fraction(frak2)
summa_result = f1 + f2
prod_result = f1 * f2

print(f"Сумма дробей: {summa_result}")
print(f"Произведение дробей: {prod_result}")