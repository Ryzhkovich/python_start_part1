# Задание №2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class CustomZeroDivisionException(Exception):
    text = "Нельзя делить на ноль"

    def __str__(self):
        return self.text


def some_division_function(l1, l2):
    if l2 == 0:
        raise CustomZeroDivisionException
    return l1 / l2


if __name__ == '__main__':
    try:
        var_1 = 14
        var_2 = 0
        print(some_division_function(var_1, var_2))
    except CustomZeroDivisionException as e:
        print(e)
    except Exception as err:
        print(err)

