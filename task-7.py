# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.

# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial


def factorial_yield_generation(iteration):
    count = 1
    while count <= iteration:
        yield factorial(count)
        count += 1


def get_result_list(number):
    """ Итератор, генерирующий целые числа, начиная с указанного:
    параметр 1 - number - количество итераций
     """
    try:
        i = 1
        result_list = []
        for el in factorial_yield_generation(number):
            result_list.append(el)
            i += 1
        return result_list
    except:
        return 'Something wrong'


print(get_result_list(100))
