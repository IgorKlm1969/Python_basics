"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]


"""

import re

d = []
with open('Logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        result_ip = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        _res_data = re.findall(r'\b[G][E]\w+', line)
        res_type = ','.join(_res_data)
        _res_request = re.findall(r'[/][d]\w+[/]\w+', line)
        res_resource = ','.join(_res_request)

        c = (result_ip.group(0), res_type, res_resource)
        d.append(c)
print(d)
