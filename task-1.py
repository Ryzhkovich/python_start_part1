# Задача №1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

filename_arg, money_per_hour_arg, hours_arg, bonus_arg = argv


def count_all_money(per_hour, hours, bonus=0):
    per_hour = int(per_hour)
    hours = int(hours)
    bonus = int(bonus)

    return per_hour * hours + bonus


print(count_all_money(money_per_hour_arg, hours_arg, bonus_arg))
