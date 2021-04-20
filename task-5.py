# Задача №5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

list_number = [1, 2, 3, 21, 22, 23, 41, 42, 43]

str_1 = ''
for ele in list_number:
        str_1 += str(ele) + ' '

try:
    my_file = open("126.txt", "w")
    my_file.writelines(str_1)
except IOError:
    print("Произошла ошибка 1 часть!")
finally:
    my_file.close()


try:
    my_file_2 = open("126.txt", 'r')
    arr = my_file_2.read()[:-1].split(' ')
    arr = map(int, arr)
    print(arr)
    print(sum(arr))
except IOError:
    print("Произошла ошибка 2 часть!")
finally:
    my_file_2.close()