#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate, bonus, = argv

print("Script name is ", script_name)
print("Number of hours ", hours)
print("Rate per hours ", rate)
print("Bonus ", bonus)

print(f'Salary is', int(hours) * float(rate) + float(bonus))