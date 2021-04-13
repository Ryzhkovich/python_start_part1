# Задание №6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

""" Часть №1 """
def int_func(a):
    return a.title()

print(int_func("qweqweqweasdasdzxczxc"))

""" Часть №2 """
def my_func(a):
    separate_phrase = a.split(' ')
    upper_array = []
    for i in separate_phrase:
        # здесь использую ф-цию int_func
        upper_array.append(int_func(i))
    return ' '.join(upper_array)
print(my_func("hello world"))
