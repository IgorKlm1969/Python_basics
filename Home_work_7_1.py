"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

"""
import os

path = os.getcwd()
new_proj = os.path.join(path, path)

folder_1_level = 'my_project'
folders_2_level = ['setting', 'mainapp', 'adminapp', 'authapp']
path_1level = os.path.join(new_proj, folder_1_level)

if not os.path.exists(path_1level):
    os.mkdir(path_1level)
else:
    print(f'Папка {folder_1_level} уже существует!')

for folder in folders_2_level:
    if not os.path.join(path_1level, folder):
        os.mkdir(os.path.join(path_1level, folder))
    else:
        print(f'Папка {folder} уже существует!')
