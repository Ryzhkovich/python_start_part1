# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from json import dumps


my_file_txt = "128.txt"
compile_file_json = "128.json"

results = [{}, {}]


try:
    with open(my_file_txt, encoding='utf-8') as all_text:
        lines = all_text.readlines()

    for line in lines:
        name, organization_type, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

    results[1]['average_profit'] = round(
        sum(
            profit for organization_type, profit in results[0].items() if profit > 0
        ) / len(results[0])
    )

    with open(compile_file_json, "w", encoding='utf-8') as fhd:
        fhd.write(dumps(results))
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные даkнные")
