# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, exist_rating = [7, 5, 3, 3, 2].

# Ввод рейтинга
number = int(input("Введите число: "))
exist_rating = [7, 5, 3, 3, 2]
c = exist_rating.count(number)

# Цикл с логикой
for element in exist_rating:
    if c > 0:
        i = exist_rating.index(number)
        exist_rating.insert(i+c, number)
        break
    else:
        if number > element:
            j = exist_rating.index(element)
            exist_rating.insert(j, number)
            break
        elif number < exist_rating[len(exist_rating) - 1]:
            exist_rating.append(number)

# Вывод результата
print(exist_rating)
