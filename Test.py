
from random import randint

randnum = randint(a: 0, b: 1000 )

count = 1
while count <= 11:
    a = int(input("введите вашеЧисло"))
    if a == randnum:
        print(f"Вы победили с {count} попытки")
        break 
    else:

        if a > randnum:
            print ("Меньше")
            count += 1
        if a < randnum:
            print ("Больше")
            count += 1
        if count == 11 and a != randnum:
            print ("Вы проиграли!")
            break