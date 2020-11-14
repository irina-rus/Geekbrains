#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(s):
    return str.title(s)

s = input("Pleaae input some word by lowercase letters ")
print(int_func(s))

def int_func(s):
    return str.title(s)

s = input("Please input some string by lowercase letters ")
print(int_func(s))