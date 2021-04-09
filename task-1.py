# Задание №1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Задание переменных различных типов
some_int = 1
some_float = 1.1
some_string = 'Some string'
some_list = ['1', '2', '3']
some_tuple = ('1', '2', '3')
some_dictionary = {'one': 1, 'two': 2, 'three': 3}

# агрегация в массив всех переменных
all = [some_int, some_float, some_string, some_list, some_tuple, some_dictionary]

for i in all:
    print(f'{i} is {type(i)}')
