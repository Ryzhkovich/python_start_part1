# Задание №3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
        self.__income = {'оклад': self.profit, 'премия': self.bonus}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_full_profit(self):
        return self.__income


it_proger = Position('Александр', 'Пушкин', 'Разработчик', 87000, 6000)
print('Полное имя: ' + it_proger.get_full_name())
print('Полный доход: ' + str(it_proger.get_full_profit()['оклад'] + it_proger.get_full_profit()['премия']))

streamer = Position('Никита', 'Романцев', 'Стример', 120000, 0)
print('Полное имя: ' + streamer.get_full_name())
print('Полный доход: ' + str(streamer.get_full_profit()['оклад'] + streamer.get_full_profit()['премия']))
