"""
    Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
    Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
    Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

"""


class MyErrors(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class ValidateEquipmentError(MyErrors):
    def __init__(self, text):
        self.text = f'Ошибка при создании объекта:\n {text}'


class AddEquipErr(MyErrors):
    def __init__(self, text):
        self.text = f'Невозможно добавить товар на склад:\n {text}'


class TransferEquipErr(MyErrors):
    def __init__(self, text):
        self.text = f'Ошибка прередачи оргтехнику:\n {text}'


class Storage:
    def __init__(self):
        self.store = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquip) for equipment in equipments]):
            raise AddEquipErr(f'Ошибка в данных на оргтехнику')
        self.store.extend(equipments)

    def transfer(self, indx: int, department: str):
        item: OfficeEquip = self.store[indx]

        if item.department:
            raise TransferEquipErr(f'Оргтехника {item} зарезервировани за {item.department}')

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.store[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.store[key]

    def __iter__(self):
        return self.store.__iter__()

    def __str__(self):
        return f'На складе сейчас {len(self.store)} устройств'


class OfficeEquip:

    def __init__(self, eqip_type: str = None, company: str = "", model: str = ""):
        self.type = eqip_type
        self.company = company
        self.model = model
        self.department = None

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'{self.type} {self.company} {self.model}'

    @staticmethod
    def validate(amount):
        try:
            if not isinstance(amount, int):  # Проверим тип поступающих данных на целое число
                raise ValidateEquipmentError(f'Получено{type(amount)}, должен быть тип int и больше нуля')
        except ValidateEquipmentError as e:
            print(e)

    @classmethod
    def create(cls, amount, **properties):
        cls.validate(amount)
        return [cls(**properties) for _ in range(amount)]


class Printer(OfficeEquip):
    def __init__(self, **kwargs):
        super().__init__(eqip_type='Printer', **kwargs)


class Scanner(OfficeEquip):
    def __init__(self, **kwargs):
        super().__init__(eqip_type='Scanner', **kwargs)


class Xerox(OfficeEquip):
    def __init__(self, **kwargs):
        super().__init__(eqip_type='Xerox', **kwargs)


storage = Storage()
storage.add(Printer.create(2, company="Canon", model="C100"))
storage.add(Scanner.create(2, company="Epson", model="E400"))
storage.add(Scanner.create(1, company='OKI', model='O22'))
storage.add(Xerox.create(2, company="Xerox", model="X9000"))
storage.add(Xerox.create(1, company="Xerox", model="Xe"))
print(storage)

for idx, _item in storage.filter_by(department=None, company='OKI', model='O22'):
    print(f'Передаем {_item} в "Департамент А"\n')
    storage.transfer(idx, 'в "Департамент А"')

for idx, _item in storage.filter_by(department=None):
    print(idx, f'{_item} не зарезервированы')

print(storage)
print('1 единица списана')
del storage[0]
print(storage)
