"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

    def countdown(t):
        while t:
            time.sleep(1)
            t -= 1
            print(f'{t} sec remaining')


"""

import time


class Bcolors:
    red = '\033[91m'
    amber = '\033[93m'
    green = '\033[92m'
    reset = '\033[0m'


class TrafficLight(Bcolors):

    def running(self):
        __color = 'red'
        while True:
            if __color == 'red':
                __color = 'amber'
                print(f'{Bcolors.amber}{__color} is on{Bcolors.reset}')
                time.sleep(2)
            elif __color == 'amber':
                __color = 'green'
                print(f'{Bcolors.green}{__color} is on{Bcolors.reset}')
                time.sleep(5)
            elif __color == 'green':
                __color = 'red'
                print(f'{Bcolors.red}{__color} is on{Bcolors.reset}')
                time.sleep(7)


a = TrafficLight()
a.running()
