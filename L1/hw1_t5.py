#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Please, input revenue value "))
costs = int(input("Please, input costs value "))

if revenue > costs:
    print(f"Your company has a profit {revenue - costs}")
    print(f"Your company efficiency is {revenue / costs}")
    staff = int(input("Please input number of your company staff "))
    print(f"Profit per employee is {(revenue - costs) / staff}")
else:
    print(f"Your company has a loss {revenue - costs}")