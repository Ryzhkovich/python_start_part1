#  Задача №3
#  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.

def my_func(one, two, three):
    params = [one, two, three]
    print('Отладочная информация: ')
    """ Отладочная информация """
    print(params)
    minimum = min(params)
    """ Отладочная информация """
    print(minimum)
    params.remove(minimum)
    """ Отладочная информация """
    print(params)

    print('Вывод искомого результата: ')
    print(params[0] + params[1])

my_func(1, 4, 7)