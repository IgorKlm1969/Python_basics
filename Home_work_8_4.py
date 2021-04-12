"""
4 задание
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

Примечание: сможете ли вы замаскировать работу декоратора?

print(f'\t{func.__name__}({", ".join(map(str, args))}: {(type(args))})')
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

"""
from functools import wraps


def val_checker(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            try:
                if arg > 0:
                    result = func(*args)
                    return result
                else:
                    raise ValueError

            except ValueError as e:
                print(f"Ошибка, введите положительное чесло:  {e} {arg}")

    return wrapper


def logger(func):
    def wrapper(*args):
        result = func(*args)
        print(f'Вызов функции: {func.__name__} ({", ".join(map(str, args))})')
        return result

    return wrapper


@logger
@val_checker
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
