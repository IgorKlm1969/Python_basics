"""
Создать структуру файлов и папок, как написано в задании 2
 (при помощи скрипта или «руками» в проводнике).
 Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


"""

import os
import shutil

project = 'my_project'
path = os.path.join(os.getcwd(), project)

templ = 'templates'
path_templates = os.path.join(path, templ)

for root, dirs, files in os.walk(path):
    for dir_name in dirs:
        if dir_name == templ:
            try:
                shutil.copytree(os.path.join(root, dir_name), path_templates)
            except FileExistsError:
                path_templates = os.path.join(path_templates, 'templ')  # Два дня бился, но не смог придумать
                # как в этот же каталог скопировать. Ошибка FileExistsError.
                shutil.copytree(os.path.join(root, dir_name), path_templates)
