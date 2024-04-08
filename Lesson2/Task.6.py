# #напишите программи банкомат. Начальная сумма равна нулю
# Допустимые действия: дополнить, снять, выйти. Сумма пополнения и снятия кратны 50 у. е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3% нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег.

import decimal

def cratnost(delimoe, delitel):
    if delimoe % delitel == 0:
        return True
    else:
        return False
    
MIN_SUM=50
PROCENT_TO_TAKE=0.015
MIN_COMISSION = 30
MIN_COMISSION = 600
BONUS = 0.03
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = 0.1


def main_menu():
    balance = 0
    count = 0
    play = True
    while play:
        answer = input("Меню банкомата:\n"
                       "1. Показать баланс\n"
                       "2. пополнить\n"
                       "3. снять\n"
                       "4. Exit\n")
        match answer:
            case "1":
                print(balance)
            case "2":
                vklad = int(input('vvedite summu: '))
                if cratnost(vklad, MIN_SUM):
                    balance += vklad
                    count +=1
                else:
                    print("Не верная сумма. Должно быть кратно 50")     

            case "3":
                snyt = int(input('vvedite summu: '))
                if cratnost(snyt, MIN_SUM):
                    balance - snyt
                    #count +=1
                else:
                    print("Не верная сумма. Должно быть кратно 50")          
            case "4":
                play = False
            case _:
                print("Не известная команда, повторите ввод \n")

main_menu()