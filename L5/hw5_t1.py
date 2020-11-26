#Cоздать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

my_file = open("my_file.txt", "w")
str_list = ['Hello, friend!\n', 'How are you?\n', 'What are you doing now?\n']
my_file.writelines(str_list)
my_file.close()
