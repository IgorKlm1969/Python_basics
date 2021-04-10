"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
from collections import defaultdict

path = os.getcwd()

print(path)
list_of_files = defaultdict(list)
for key_dict in range(10):
    key_dict = (10 ** key_dict)
    list_of_files[key_dict] = 0
item_1 = 0
item_10 = 0
item_100 = 0
item_1000 = 0
item_10000 = 0
item_100000 = 0
for root, dirs, files in os.walk(path):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        if 1 < file_size < 10:
            item_1 = item_1 + 1
            list_of_files[10] = item_1
        elif 10 < file_size < 100:
            item_10 = item_10 + 1
            list_of_files[100] = item_10
        elif 100 < file_size < 1000:
            item_100 = item_100 + 1
            list_of_files[1000] = item_100
        elif 1000 < file_size < 10000:
            item_1000 = item_1000 + 1
            list_of_files[10000] = item_1000
        elif 10000 < file_size < 100000:
            item_10000 = item_10000 + 1
            list_of_files[100000] = item_10000
print(list_of_files)
