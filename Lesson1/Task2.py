IGNOR = 1582
year = int(input('Введите год после 1582 года: '))
if year < IGNOR:
    print('Слишком ранний год: ')
else:
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print('Високосный год: ')
    else:
        print('Обычный год: ')