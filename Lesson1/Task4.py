# Нарисовать в консоли елку спросив
# у пользователя колличество рядов

rows = int(input('Введите колличество рядов: '))
for i in range(1, rows + 1):# диапозон от 1 до rows плюс один
    spaces = rows - i # пробелы rows - i(если вводим 5, значит последовательность 4,3.2,1)
    stars = 2 * i - 1 # формула кол-во звезд( первый ряд 1, второй ряд 2*2-1=3 и т д)
    print(" " * spaces + "*" * stars)