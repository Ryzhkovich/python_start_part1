# Задание №2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Ввод данных пользователя
name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
birthday = input('Введите день рождения пользователя: ')
city = input('Введите город пользователя: ')
email = input('Введите email пользователя: ')
phone = input('Введите телефон пользователя: ')

# Ф-ция
def user_data(name, surname, birthday, city, email, phone):
    return f"Данные пользователя: {name}, {surname}, {birthday}, {city}, {email}, {phone}."

# Вывод на экран
print(user_data(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))

