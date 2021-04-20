# Задача №1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os


def add_line(new_line):
    try:
        f = open('128.txt', 'a')
        f.write(new_line + "\n")
    except IOError:
        print("Error in open file")
    except Exception as e:
        print(e)
    finally:
        f.close()


if os.path.exists("128.txt"):
    os.remove("128.txt")
while True:
    line = input('1) Введите строку, чтобы записать строку в файл\n '
                 '2) либо оставьте пустую строку чтобы закончить\n'
                 '3) нажмите `Enter`\n')
    if line == '':
        break
    else:
        add_line(line)
