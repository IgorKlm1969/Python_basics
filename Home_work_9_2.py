"""

Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

1м3 асфальта равен 1500 кг
"""


class Road:
    def __init__(self, length_road, width_road, depth_road):
        self._length_road = length_road
        self._width_road = width_road
        self._depth = depth_road  # we will count in the meters
        self._density = 1500  # <-- destiny of asphalt kg

    def weight_road(self):
        return self._length_road * self._width_road * self._depth * self._density


wr = Road(1000, 18, 0.05)
print(f'Total weight is {wr.weight_road() / 1000} tons.')
