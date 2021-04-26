"""
Реализовать проект «Операции с комплексными числами». Создать класс
«Комплексное число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, re, im=0):
        self.compl = complex(re, im)

    def __add__(self, other):
        print(f'\nСумма комплексных чисел равна: ')
        return f'Sum = {self.compl + other.compl}\n'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно: ')
        return f'Mult = {self.compl * other.compl}\n'

    def __str__(self):
        return f'Complex number = {self.compl}'


compl_1 = ComplexNumber(12, -4)
compl_2 = ComplexNumber(10, -15)
print(compl_1)
print(compl_2)

print(compl_1 + compl_2)
print(compl_1 * compl_2)
