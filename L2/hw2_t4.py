#Пользователь вводит строку из нескольких слов, разделённых пробелами.
#Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
#Если слово длинное, выводить только первые 10 букв в слове.

s = input("Please input some words separated by spaces ").split()

for ind, el in enumerate(s, 1):
    if len(el) > 10:
        s1 = str(el)
        print(ind, s1[:10])
    else:
        print(ind, el)