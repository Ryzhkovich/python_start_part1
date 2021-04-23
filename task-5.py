# Задание №5
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Пустое название'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Начали рисовать')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'
        super().__init__(self.title)

    def draw(self):
        print(f'Вы выбрали инструмент `Ручка`. Рисуем!\n(Инструмент для рисования {self.title})\n')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'
        super().__init__(self.title)

    def draw(self):
        print(f'Вы выбрали инструмент `Карандаш`. Рисуем!\n(Инструмент для рисования {self.title})\n')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'
        super().__init__(self.title)

    def draw(self):
        print(f'Вы выбрали инструмент `Маркер`. Рисуем!\n(Инструмент для рисования {self.title})\n')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
