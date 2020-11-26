#Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def sum ():
    sum_res = 0
    i = False
    while i == False:
        num = input('Please input numbers separated by space or press Q(q) to exit ').split()

        res = 0
        for el in range(len(num)):
            if num[el] == 'q' or num[el] == 'Q':
                i = True
                break
            else:
                res = res + int(num[el])
        sum_res = sum_res + res

        print(f'Sum is {sum_res}')

    print(f'Final sum is {sum_res}')
sum()

