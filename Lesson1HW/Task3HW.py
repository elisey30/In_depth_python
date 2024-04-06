# Задча № 3.
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# # Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# # Для генерации случайного числа используйте код:
# # 'from random import randint
# # hum = randint (LOWER_LIMIT, UPPER_LIMIT)

from random import randint

def guess_the_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print("Программа загадала число от 0 до 1000. Попробуйте угадать это число за 10 попыток.")

    for attempt in range(1, 11):
        try:
            guess = int(input(f"Попытка {attempt}. Введите ваше число: "))
            if guess < num:
                print("Больше.")
            elif guess > num:
                print("Меньше.")
            else:
                print(f"Поздравляем! Вы угадали число {num} с {attempt} попытки.")
                return
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

    print(f"К сожалению, вы не угадали. Загаданное число было: {num}.")


