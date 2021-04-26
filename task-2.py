#  Задание №2
#  Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#  Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    additional = None

    def __init__(self, additional):
        self.additional = additional

    @abstractmethod
    def cloth_consumption(self):
        pass


class Suit(Clothes):
    height_suit = None

    def __init__(self, height_suit, additional):
        super().__init__(additional)
        self.height = height_suit

    @property
    def cloth_consumption(self):
        return 2 * self.height + self.additional


class Coat(Clothes):
    height_coat = None

    def __init__(self, height_coat, additional):
        super().__init__(additional)
        self.height = height_coat

    @property
    def cloth_consumption(self):
        return self.height / 6.5 + self.additional


s = Suit(10, 3)
# print(s.cloth_consumption()) # Без @property вызов ранее был такой
c = Coat(52, 5)
c2 = Coat(130, 5)

print(s.cloth_consumption)
print(c.cloth_consumption)
print(c2.cloth_consumption)
