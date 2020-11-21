#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open("file_5_5.txt", "w")
str_list = ['23 12 2 3 16 33 5']
my_file.writelines(str_list)
my_file.close()

with open("file_5_5.txt", "r") as file:
    for line in file:
        print(f'The line from file is {line}')
        i = 0
        sum = 0
        line = line.split(' ')
        while i < len(line):
            sum = sum + int(line[i])
            i +=1
        print(f'Sum of all numbers in the file = {sum}')
