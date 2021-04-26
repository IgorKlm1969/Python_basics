"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
 «день-месяц-год». В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
 Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй — с декоратором
  @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
  Проверить работу полученной структуры на реальных данных.
 def __getitem__(self, index):
        return self.l1[index]

"""
import re


class DateClass:
    def __init__(self, date, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        self.date = date

    @classmethod
    def get_date(cls, date):
        result = re.findall(r'(\d{1,2})-(\d{1,2})-(\d{2,4})', date)
        l1 = []
        for tup_number in result:
            for number in tup_number:
                l1.append(int(number))
        return l1

    @staticmethod
    def valid_numbers(str_date):
        day, month, year = map(int, str_date.split('-'))
        if 1 <= day <= 31:
            print('День в допустимых пределах')
        else:
            print('День: вне зоны допустимых значений')
        if 1 <= month <= 12:
            print('Месяц в допустимых пределах')
        else:
            print('Месяц: вне зоны допустимых значений')
        if 1900 <= year <= 2021:
            print('Месяц в допустимых пределах')
        else:
            print('Год: вне зоны допустимых значений')
        return "\n\tЦикл для проверки даты закончен\n"

    def __str__(self):
        return f'\nOur date is {DateClass.get_date(self.date)}\n'


a_day = DateClass('02-08-2020')
print(a_day)

print(DateClass.get_date('02-08-2020'))
print(a_day.get_date('02-08-2020'))
print(a_day.valid_numbers('15-09-2000'))
print(a_day.valid_numbers('33-15-1800'))
