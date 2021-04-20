# Задача №3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


data = {'Пушкин': 17000, 'Лермонтов': 21000, 'Есенин': 5900, 'Гоголь': 150000}

try:
    my_file = open("128.txt", 'w')
    for surname, salary in data.items():
        my_file.write(surname + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()
summ = 0
count = 0
persons_surnames = []
with open("128.txt", "r") as my_file:
    for line in my_file:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) > 20000:
            persons_surnames.append(tokens[0])
        summ += int(tokens[1])
        count += 1
result = summ / count
print(f"persons_surnames: {persons_surnames}")
print(f"averate: {result}")