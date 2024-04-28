# Задача № 2
# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

def calculate_bonus(names: list[str], rates: list[int], percents: list[str]) -> dict:
    """Расчет премий"""
    return {name: rate * float(percent.strip('%')) / 100 for name, rate, percent in zip(names, rates, percents)}


names = ["Oleg", "Vladimir", "Anton"]
rates = [65_000, 70_000, 80_000]
percents = ['10.25%', '8.0%', '4.5%']
print(calculate_bonus(names, rates, percents))
