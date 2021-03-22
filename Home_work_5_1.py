"""
Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield, например:
print(None if list(print_num) == [] else str(next(print_num)))
"""


def odd_nums(n):
    for num in (num for num in range(1, n + 1, 2)):
        yield num


print_num = odd_nums(15)

print(next(print_num))
print(next(print_num))
print(next(print_num))
print(next(print_num))
print(next(print_num))
print(next(print_num))
print(next(print_num))
print(next(print_num))

print(list(print_num))  # Генератор истощен
