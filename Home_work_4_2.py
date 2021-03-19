"""
. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
 Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна
  возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы
  с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код
  функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
  вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
  был передан аргумент? В качестве примера выведите курсы доллара и евро.
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


currency_rates('usd')

currency_rates('EUR')

currency_rates('AAA')  # не получается добавить условие для None
