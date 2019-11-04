import os, shutil

def f_copy_file_folder():
    current_path = os.getcwd()
    name = input('Введите имя файла или папки, которые хотите скопировать:  ')
    name_copy = input('Введите имя копии файла или папки:  ')
    name_path = os.path.join(current_path, name)
    name_copy_path = os.path.join(current_path, name_copy)
    if not os.path.exists(name):
        return 'Файла или папки с таким именем не существует'
    elif os.path.isdir(name_path):
        shutil.copytree(name_path, name_copy_path)
        return f'Папка {name} скопирована в новую папку {name_copy}'
    else:
        shutil.copyfile(name_path, name_copy_path)
        return f'Файл {name} скопирован в новый файл {name_copy}'


