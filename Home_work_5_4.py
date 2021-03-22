"""
Представлен список чисел. Необходимо вывести те его элементы,
значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]


Подсказка: использовать возможности python, изученные на уроке.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
len_src = len(src)
print(len_src)
print(src)

"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src.append(float('inf'))
# Первое решение
src_filter_1: list[Union[Union[int, float], Any]] = []
for i, item in enumerate(src[:-1]):
    if i == 0:
        continue
    if src[i - 1] < src[i]:
        src_filter_1.append(src[i])

print(*src_filter_1)

# Второе решение
src_filter_gen =\
    (item for i, item in enumerate(src[:-1])
     if src[i - 1] < src[i] and i != 0)
print(*src_filter_gen)
