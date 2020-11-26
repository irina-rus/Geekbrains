#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def d(a, b):
    if b != 0:
        return a / b
    else:
        print ("Error!!! Zero Division!!!")

a = int(input("Please input integer "))
b = int(input("Please input integer "))

print(f"Division is", d(a, b))
