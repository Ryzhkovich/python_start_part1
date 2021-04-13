# Задание №1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Ввод делимого и делителя
number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))


# Сама ф-ция
def division_two_numbers(var_1, var_2):
    try:
        result = var_1 / var_2
    except ZeroDivisionError as e:
        return e
   # Это 2й вариант, как можно обработать ошибку деления на ноль
   # if var_2 == 0:
        # return ZeroDivisionError
    else:
        return result # var_1 / var_2

# Вывод результата на экран
print(division_two_numbers(number_1, number_2))




