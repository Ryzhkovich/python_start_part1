# Задача №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_data = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []

try:
    my_file = open("128.txt", 'r')
    for line in my_file:
        tokens = line.split(" - ")
        print(tokens[0])
        if tokens[0] in my_data:
            word = my_data[tokens[0]]
            result.append(word + " - " + tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка 1 часть!")
finally:
    my_file.close()

try:
    my_file_second = open("128.txt", "w")
    my_file_second.writelines(result)
except IOError:
    print("Произошла ошибка 2 часть!")
finally:
    my_file_second.close()

