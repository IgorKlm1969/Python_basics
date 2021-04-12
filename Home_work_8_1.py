"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
 Если адрес не валиден, выбросить исключение ValueError. Пример:
## >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
## >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
, 'focus@
"""

import re
from collections import defaultdict

list_of_emails = ['someone@geekbrains.ru', 'bigstar@geekbrains.ru', 'any_one@geekbrains.ru',
                  'no_body@geekbrains.ru', 'into@', 'alon@geekbrains.ru', '@geekbrains.ru', 'yy@geekbrains']


def email_parse(email_address):
    email_dict = defaultdict()

    for email in email_address:
        try:
            user = ''.join(re.findall(r'(\w+)@\w+\.\w+', email))  # проверяет по шаблону, если часть адреса до символа
            # @ отсутствует, то вызывается ошибка ValueError
            if user:
                email_dict['username'] = user
            else:
                raise ValueError

            dom = ''.join(re.findall(r'\w+@(\w+\.\w+)', email))
            if dom:
                email_dict['domain'] = dom
            else:
                raise ValueError
            print(email_dict)
        except ValueError as s:
            print(f'Ошибка в email адресе: {s}')


email_parse(list_of_emails)
