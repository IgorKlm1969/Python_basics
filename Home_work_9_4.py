"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

(180, "green", 'Audi', False)
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'The car rides'

    def stop(self):
        if self.speed <= 0:
            return 'stopped'
        else:
            return 'rides'

    def turn(self):
        print(f'The car turn {self}')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    def tell_about_car(self):
        print(f'\nThe TownCar {Car.stop(self)}')
        Car.show_speed(self)
        if self.speed > 60:
            print('Превышение скорости 60 км/ч\n')


class SportCar(Car):
    def tell_about_car(self):
        print(f'\nThe SportCar {Car.stop(self)}')
        print(f'цвет: {self.color}, полиция:{self.is_police}\n')


class WorkCar(Car):
    def tell_about_car(self):
        print(f'\nThe WorkCar {Car.stop(self)}')
        Car.show_speed(self)
        if self.speed > 40:
            print('Превышение скорости 40 км/ч\n')


class PoliceCar(Car):

    def tell_about_car(self):
        print(f'\n{Car.go(self)}')
        Car.show_speed(self)
        print(f'цвет: {self.color}, полиция:{self.is_police}')
        Car.turn(self='left')


t = TownCar(180, "green", 'Audi', False)  # Не могу понять откуда берется None
print(t.tell_about_car())

s = SportCar(250, "red", 'BMW', False)
print(s.tell_about_car())

w = WorkCar(0, "yellow", 'Камаз', False)
print(w.tell_about_car())

w = PoliceCar(90, "white", 'УАЗ', True)
print(w.tell_about_car())
