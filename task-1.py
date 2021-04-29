# Задание №1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date


class Date:
    input_date = None

    def __init__(self, input_date):

        date_list = input_date.split('-')

        self.day = int(date_list[0])
        self.month = int(date_list[1])
        self.year = int(date_list[2])

    @classmethod
    def get_numbers_from_date(cls, d: "Date") -> list:
        return [d.day, d.month, d.year]

    @staticmethod
    def validate_date(d: "Date"):
        global max_year
        if d.day in range(1, 32):
            print(f"Ок\n{d.day} - входит в диапазон (1, 32)")
        else:
            print(f"{d.day} - вне диапазона (1, 32)")
            print(date.today().strftime("%Y"))
        if d.month in range(1, 13):
            print(f"Ок\n{d.month} - входит в диапазон (1, 12)")
        else:
            print(f"{d.month} - вне диапазона (1, 12)")
        max_year = int(date.today().strftime("%Y")) + 1
        if d.year in range(1970, max_year):
            print(f"Ок\n{d.year} - входит в диапазон (1970, {max_year - 1})")
        else:
            print(f"{d.year} - вне диапазона (1970, {max_year - 1})")
        return


# Без ошибки
dt = Date("29-04-2021")
print(Date.get_numbers_from_date(dt))
print(Date.validate_date(dt))

# С ошибкой
dt_2 = Date("31-12-1969")
print(Date.get_numbers_from_date(dt_2))
print(Date.validate_date(dt_2))
