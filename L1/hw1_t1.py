#1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

a = int(5)
a = a + 10
b = str('Hello, friends!')
c = True

print (a, b, c)

a = int(input("Input any integer from 1 to 10 "))
b = int(input("Input any integer from 1 to 10 "))

c1 = a / b
print(f"Division is {c1}", type(c1))

c2 = a + b
print(f"Summ is {c2}", type(c2))
