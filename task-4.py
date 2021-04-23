# Задание №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Cars:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} едет\n"

    def stop(self):
        return f"Машина {self.name} остановилась\n"

    def turn(self, turn_move):
        direction = {'r': 'право', 'l': 'лево'}
        return f"Машина {self.name} повернула на " + direction[turn_move] + "\n"

    def show_speed(self):
        return "Текущая скорость = " + str(self.speed) + "\n"


class TownCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость в 60 км/ч. Текущая скорость = " + str(self.speed) + "\n"
        else:
            return "Текущая скорость = " + str(self.speed) + "\n"


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость в 40 км/ч. Текущая скорость = " + str(self.speed) + "\n"
        else:
            return "Текущая скорость = " + str(self.speed) + "\n"


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


toyota = TownCar(70, 'черная', 'Toyota')
print(toyota.name, toyota.color, toyota.speed, toyota.is_police)
print(toyota.go(), toyota.turn('r'), toyota.stop(), toyota.show_speed())
sport_ford = SportCar(180, 'желтая', 'Ford')
kamaz = WorkCar(90, 'синий', 'Kamaz', False)
police = PoliceCar(180, 'red', 'Ford')
