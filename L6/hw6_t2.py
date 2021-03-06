#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    weight_1sm = 25
    depth = 5

    def asphalt_weight(self, _length, _width):
        self.length = _length
        self.width = _width
        wa = int(self.length * self.width * self.weight_1sm * (self.depth/1000))
        print(f'To cover the road asphalt weight should be {wa}')

w = Road()
w.asphalt_weight(20, 5000)