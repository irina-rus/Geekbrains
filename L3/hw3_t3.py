#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(d))
    return sum(d)

a = int(input("Please input integer "))
b = int(input("Please inut integer "))
c = int(input("Please input integer "))

print(f"Sum is ", my_func(a, b, c))