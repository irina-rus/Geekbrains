#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input("Please, input any positive integer, more than 10 "))
m = n % 10
n //= 10

while n > 0:
    if n % 10 > m:
        m = n % 10
    n //= 10

print(f"The lagest figure in the number is {m}")