#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(f'The {self.color} {self.name} is starting to go.')

    def stop(self):
        print(f'The {self.color} {self.name} stopped.')

    def turn(self,direction):
        self.direction = direction
        print(f'The {self.color} {self.name} turned to {self.direction}.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'The speed is {self.speed}. ATTENTION!!! The speed limit has been exceeded. Maximum speed is 60 km/h.')
        else:
            print(f'The speed is {self.speed}.')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'The speed is {self.speed}. ATTENTION!!! The speed limit has been exceeded. Maximum speed is 40 km/h')
        else:
            print(f'The speed is {self.speed}.')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

town = TownCar(62, 'white', 'MiniCooper', False)
town.go()
town.turn('right')
town.show_speed()
town.stop()
print(f'\n')

sport = SportCar(250, 'red', 'Ferrari', False)
sport.go()
sport.turn('left')
sport.stop()
print(f'\n')

work = WorkCar(38, 'black', 'Scania', False)
work.go()
work.turn('right')
work.show_speed()
work.stop()
print(f'\n')

police = PoliceCar(100, 'blue', 'Ford', True)
police.go()
police.turn('left and then right')
police.stop()