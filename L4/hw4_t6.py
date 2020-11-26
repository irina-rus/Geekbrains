#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count

a = int (input('Please input positive integer to start iterator '))
b = int (input('Please input positive integer to stop iterator '))
print('Result of the iteration:')

for el in count(a):
    if el > b:
        break
    else:
        print(el)

from itertools import cycle

print('The result of cycle iteration:')

с = 0
for el in cycle("ABC"):
    if с > 5:
        break
    print(el)
    с += 1