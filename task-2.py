# Задание №2
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


my_list = ['123 234 345 12\n', 'qwe qweqetwetw 23r\n', '  asd fewt\n', 'hjhj hjhjhj hjhjh uiuiy 78787 99\n']
with open("123.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)

with open("123.txt", 'r') as file_obj:
    lines = 0
    words = 0
    i = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split())
        print(f"{words} words in line {lines}")
    print(f"String count is {lines}")

