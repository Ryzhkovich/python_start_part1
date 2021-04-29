# Задание №4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from math import sqrt


class Storage:
    # Пока пустой класс
    pass


class OfficeEquipment:
    price = 0
    good_value = None
    use_frequency = None

    def __init__(
            self,
            name: str,
            price: float,
            good_value: int,
            use_frequency: int,
    ):
        self.name = name
        self.set_price(price)
        self.good_value = good_value
        self.use_frequency = use_frequency

    @property
    def get_price(self):
        return self.price

    def set_price(self, p):
        self.price = p

    @property
    def all_profit(self):
        return (self.good_value * self.use_frequency) / sqrt(self.price)

    def __str__(self):
        return f"(name:{self.name}, price:{self.price}, good_value:{self.good_value}, use_frequency:{self.use_frequency})"


class Printer(OfficeEquipment):
    color = None

    def __init__(self, color: str, *args):
        super().__init__(*args)
        self.color = color


class Scanner(OfficeEquipment):
    format_type = None

    def __init__(self, format_type: str, *args):
        super().__init__(*args)
        self.format_type = format_type


class Xerox(OfficeEquipment):
    copy_count = 0

    def __init__(self, copy_count: int, *args):
        super().__init__(*args)
        self.copy_count = copy_count


if __name__ == '__main__':
    p1 = Printer("black-white", "Sony", 40000, 10, 500)
    s1 = Scanner("docx", "Hitachi", 10000,  70, 300)
    x1 = Xerox(5, "Panasonic", 50000,  20, 400)
    print(p1)
    print(s1)
    print(x1)
    print(x1.get_price)
