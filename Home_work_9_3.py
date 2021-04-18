"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

    def inc(self) -> object:
        """

        :rtype: складывает значения словоря
        """
        return f'Совокупный доход: {sum(self._income.values())}'


class Position(Worker):

    @property
    def get_full_name(self):
        return f'{self.name} {self.surname}, {self.position}'

    def get_total_income(self):
        return Worker.inc(self)


a = Position('Катя', 'Иванова', 'менеджер', 700, 210)
print(a.get_full_name)
print(a.get_total_income())
