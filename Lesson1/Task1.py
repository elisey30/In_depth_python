n = int(input('Введите число: '))
e = int(input('Введите число: e '))
count = 2
summa = 0
while count <= n:
    if count % e == 0:
        count += 2
        continue
    summa += count
    count += 2
print(summa)