"""
Написать свой модуль utils и перенести в него функцию currency_rates()
 из предыдущего задания. Создать скрипт, в котором импортировать этот
 модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего не происходит.

"""

import requests


def currency_rates(curr):
    """

    :param curr: передается буквенный код валюты (например: usd)
    :return:соотношение к рублю (например за 1 доллар 75 рублей)
    """
    curr = curr.upper()
    resp_cbr = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('</Valute>')
    for elem in resp_cbr:
        if elem.count(curr):
            nominal = (int(elem[elem.find('<Nominal>') + len('<Nominal>'):elem.find('</Nominal>')]))
            name = (str(elem[elem.find('<Name>') + len('<Name>'):elem.find('</Name>')]))
            value = (float(elem[elem.find('<Value>') + len('<Value>'):elem.find('</Value>')].replace(',', '.')))
            print(f'Курс {nominal} {name} равен {value}  рубля')


if __name__ == '__main__':
    currency_rates('usd')

    currency_rates('EUR')
