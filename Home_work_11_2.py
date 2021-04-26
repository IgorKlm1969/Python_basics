"""
Создать собственный класс-исключение,
обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class DivNull(Exception):
    def __init__(self):
        self.text = "Деление на ноль невозможно"

    def __str__(self):
        return self.text


div = input("Введите делимое: ")
try:
    div = int(div)
except ValueError as e:
    print(f'ошибка в типе вводимых значений {e}')
    exit()

den = input("Введите делитель: ")
try:
    den = int(den)
    if den == 0:
        raise DivNull
    else:
        print(round(int(div) / int(den), 2))
except DivNull as e:
    print(e)
except ValueError as e:
    print(f'ошибка в типе вводимых значений {e}')
