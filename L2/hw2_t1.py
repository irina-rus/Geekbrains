#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = (123, "hello", True, 2.0354, None)
for el in list:
    print(type(el))