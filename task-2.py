# Задание №2
# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Заполняемый массив
need_list = []
# Первый ввод
value = str(input('Введите значение в массив:\n Для выхода введите - `q!`\n'))
if value != 'q!':
    need_list.append(value)
    print('Текущий массив: ', end=' ')
    print(need_list)
# Часть с циклом
while value != 'q!':
    value = str(input('Введите значение в массив:\n Для выхода введите - `q!`\n'))
    if value != 'q!':
        need_list.append(value)
        print('Текущий массив: ', end=' ')
        print(need_list)

i = 0
# Четный массив
if len(need_list) % 2 == 0:
    while i < len(need_list):
        el = need_list[i]
        need_list[i] = need_list[i+1]
        need_list[i+1] = el
        i += 2
# Нечетный массив
else:
    while i < len(need_list) - 1:
        el = need_list[i]
        need_list[i] = need_list[i + 1]
        need_list[i + 1] = el
        i += 2

# Вывод результата
print(need_list)
