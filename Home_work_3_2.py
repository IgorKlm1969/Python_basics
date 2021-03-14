"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
 содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}


Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?


def check(name_of_employees):
    if 0 < len(name_of_employees) < 255 and name_of_employees.isalpha():
        return True

"""


def thesaurus(name_of_empl):
    """
    Берет кортеж имен, перебериет по именам,
    первый символ [0] будет ключом
    :type name_of_empl: tuple
    :param name_of_empl: список имен
    :return: возвращающает словарь, в котором ключи — первые буквы имён, а значения — списки,
    содержащие имена, начинающиеся с соответствующей буквы
    """
    dict_names = {}
    for name in name_of_empl:
        # print(name)
        key_dict = name[0]
        # print(key_dict)
        if key_dict in dict_names:
            dict_names[key_dict].append(name)
        else:
            dict_names[key_dict] = [name]
    print(dict_names)
    return dict_names


# name_of_employees = input('Введите имяя сотрудника' )
name_of_employees = ('Ася', 'Мася', 'Вася', 'Аля', 'Валя')
# print(type(name_of_employees))

thesaurus(name_of_employees)
