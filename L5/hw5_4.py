#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

new_file = []
dic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open("file_5_4.txt", "r") as file:
    for line in file:
        print(line)
with open("file_5_4.txt", "r") as file:
    myList = [line.split() for line in file]
    for i in myList:
        new_file.append(dic[i[0]] + '  ' + i[1] + '  ' + i[2])
        with open("new_file.txt", "w", encoding="UTF-8") as w_file:
            w_file.writelines("%s\n" % line for line in new_file)