"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
 class Clothes(ClothesABC):
    def __init__(self, name):
        self.name = name
"""
from abc import ABC, abstractmethod


class ClothesCoat(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    @abstractmethod
    def size_high(self):
        pass

    @abstractmethod
    def calc_cl(self):
        pass


class Coat(ClothesCoat):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.result = None

    @property
    def size_high(self):
        return self.size

    def calc_cl(self):
        self.result = round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Тип одежды: {self.name}. ' \
               f'На пальто потребуется {self.result} м2'


class ClotheSuit(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    @abstractmethod
    def size_high(self):
        pass

    @abstractmethod
    def calc_cl(self):
        pass


class Suit(ClothesCoat):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.result = None

    @property
    def size_high(self):
        return self.size

    @property
    def calc_cl(self):
        self.result = round((self.size * 2 + 0.3), 2)

    def __str__(self):
        return f'Тип одежды: {self.name}. ' \
               f'На костюм потребуется {self.result} м2'


c = Coat('пальто', 50)

print(c.calc_cl())  # не могу понять почему функция не выполняется с первого раза --> result = None
print(c)

s = Suit('костюм', 1.78)
print(s.calc_cl)
print(s)
