#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1   ООО   10000   5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

with open("file_5_7.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

import json
profit = {}
pr = {}
p = 0
prof_aver = 0
i = 0
with open("file_5_7.txt", "r") as file:
    for line in file:
        name, firm, revenue, loss = line.split()
        profit[name] = int(revenue) - int(loss)
        if profit.setdefault(name) >= 0:
            p = p + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = p / i
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Firms profit: {profit}')

with open("file_5_7.json", "w") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json file: {js_str}')