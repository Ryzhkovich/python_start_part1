# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result = {}

text = 'Информатика: 100(л) 50(пр) 20(лаб).\nФизика: 30(л) — 10(лаб)\nФизкультура: — 30(пр) —'

try:
    my_file = open("127.txt", "w")
    my_file.writelines(text)
except IOError:
    print("Произошла ошибка 1 часть!")
finally:
    my_file.close()

try:
    with open('127.txt', encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()
        # print(data)
        # print(data[0][:-1])

        summ = 0
        try:
            for i in data:
                if i.isdigit():
                    summ += int(i)
        except Exception as e:
            pass

        # print(summ)
        result[data[0][:-1]] = summ

except IOError as e:
    print(e)
except ValueError:
    print("Проблема с введенным данным")

print(result)

