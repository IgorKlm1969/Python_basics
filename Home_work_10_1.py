"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и пр
# return "\n".join(map(str, self.matrix))
#  return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
"""
from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        return "\n".join(map(str, self.matrix))

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(my_row, other_row)]
                       for my_row, other_row in zip(self.matrix, other.matrix)])


m = Matrix([[30, 25], [44, 66], [22, 11]])
print(m)
print('\n')

m = Matrix([[30, 25, 10], [44, 66, 10], [22, 11, 10]])
print(m)
print('\n')

m = Matrix([[30, 25, 10, 77], [44, 66, 10, 88]])
print(m)
print('\n')

m = Matrix([[30, 25, 10], [44, 66, 10], [22, 11, 10]])
print('матрица в строки')
print(str(m))

print('\n')

m1 = Matrix([[30, 25], [44, 66], [22, 11]])
m2 = Matrix([[40, 15], [36, 14], [8, 9]])
print('Сложение матриц')
print(m1 + m2)
