# Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
from random import randrange


def append_if_empty_value(array, value):
    if array.count(value) == 0:
        array.append(value)

    return array


def generate_list_with_borders(min, max, step, count):
    """ Генерация списка вместе с границами:
    параметр 1 - min значение в списке
    параметр 2 - max значение в списке
    параметр 3 - step шаг значения в списке
    параметр 4 - count количество значение в списке сгенерированные рандомно!!!
     """
    # посмотрел 6е задание, можно было сделать через count(), ну уже сделал так)
    generator = [randrange(min, max, step) for param in range(count)]
    generator = append_if_empty_value(generator, min)
    generator = append_if_empty_value(generator, max)
    generator.sort()

    return generator


def multiple(prev_el, el):
    return prev_el * el


# отладочная информация
print(generate_list_with_borders(100, 1000, 100, 5))

# вывод искомого значения
print(reduce(multiple, generate_list_with_borders(100, 1000, 100, 5)))
