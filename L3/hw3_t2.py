#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_param(name, surname, year, place, email, phone):
    print(f"{name} {surname} {year} {place} {email} {phone}")

name = input("Please input your name ")
surname = input("Please input your surname ")
year = input("Please input year of your birth ")
place = input("Please input place of your living ")
email = input("Please input your e-mail ")
phone = input("Please input your phone number ")

print(print_param(name, surname, year, place, email, phone))