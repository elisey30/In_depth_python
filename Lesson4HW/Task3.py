# Задача  № 3

# Возьмите задачу о банкомате из семинара 
# 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

import decimal

MIN_SUM = decimal.Decimal('50')
TRANSACTION_LOG = []  

def multiple_min_sum(amount):
    """Проверяет, кратна ли сумма минимальной сумме."""
    return amount % MIN_SUM == 0

def show_balance(balance):
    """Показывает текущий баланс."""
    print(f"Текущий баланс: {balance}")

def deposit(balance):
    """Пополнение счета."""
    amount = decimal.Decimal(input('Введите сумму пополнения: '))
    if multiple_min_sum(amount):
        balance += amount
        TRANSACTION_LOG.append(('Пополнение', amount))
        print("Счет успешно пополнен.")
    else:
        print("Сумма должна быть кратна", MIN_SUM)
    return balance

def withdraw(balance):
    """Снятие средств."""
    amount = decimal.Decimal(input('Введите сумму для снятия: '))
    if multiple_min_sum(amount):
        if amount <= balance:
            balance -= amount
            TRANSACTION_LOG.append(('Снятие', amount))
            print("Средства успешно сняты.")
        else:
            print("Недостаточно средств на счету.")
    else:
        print("Сумма должна быть кратна", MIN_SUM)
    return balance

def main_menu():
    balance = decimal.Decimal('0')
    play = True
    while play:
        answer = input("Меню банкомата:\n"
                       "1. Показать баланс\n"
                       "2. Пополнить счет\n"
                       "3. Снять средства\n"
                       "4. Выход\n")
        if answer == "1":
            show_balance(balance)
        elif answer == "2":
            balance = deposit(balance)
        elif answer == "3":
            balance = withdraw(balance)
        elif answer == "4":
            print("Выход из системы.")
            print("Лог транзакций:", TRANSACTION_LOG)
            play = False
        else:
            print("Неизвестная команда, повторите ввод.")

main_menu()
