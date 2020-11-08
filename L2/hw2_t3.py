#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

month = int(input("Please input month number form 1 to 12 "))

season =["winter", "spring", "summer", "autumn"]
if month <=2 or month ==12:
    print(f"Month {month} is {season[0]}")
elif month <=5 and month >2:
    print(f"Month {month} is {season[1]}")
elif month <=8 and month >5:
    print(f"Month {month} is {season[2]}")
else:
    print(f"Month {month} is {season[3]}")

seasons = {1:"Winter", 2:"Spring", 3:"Summer", 4:"Autumn"}
if month <=2 or month ==12:
    print(f"Month {month} is {seasons.get(1)}")
elif month <=5 and month >2:
    print(f"Month {month} is {seasons.get(2)}")
elif month <=8 and month >5:
    print(f"Month {month} is {seasons.get(3)}")
else:
    print(f"Month {month} is {seasons.get(4)}")