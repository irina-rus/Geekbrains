#Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("my_file.txt", "r") as file: #файл взят из задания 1
    for line in file:
        print(line)

with open("my_file.txt", "r") as file:
    content = file.readlines()
    print(f'Lines in the file - {len(content)}')

with open("my_file.txt","r") as file:
    content = file.readlines()
    for i in range(len(content)):
        print(f'Letters in the {(i + 1)} line - {len(content[i]) - 1}')