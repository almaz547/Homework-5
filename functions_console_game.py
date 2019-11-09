import os, shutil, sys
#
# def f_change_working_direktory():
#     path = os.getcwd()
#     print(f'Адрес рабочей директории: {path}')
#     new_path = input('Введите новый путь к вашей рабочей директории:  ')
#     if os.path.exists(new_path):
#         print('Данный путь уже используется')
#     elif os.path.isdir(new_path):
#         os.chdir(new_path)
#         print(f'Новый путь к рабочей директории: {os.getcwd()}')
#     else:
#         new_new_path = os.path.join(path, new_path)
#         os.chdir(new_new_path)
#         print(f'Новый путь к рабочей директории2: {os.getcwd()}')
# Вывад: таким образом путь не находится.

def f_change_working_direktory():                 # Смена рабочей директории
    if os.path.isdir(os.getcwd()):
        print(f'Адрес рабочей директории: {os.getcwd()}')
    folder_name = input('Введите новое имя рабочей директории: ')
    if not os.path.exists(folder_name):
        return f'Данной директории {folder_name} не существует'
    if not os.path.isdir(folder_name):
        return f'"Это не директория {folder_name}'
    os.chdir(folder_name)
    return f'Создана директория: {folder_name}'

# В этом варианте путь взятый с предыдущего проекта присваевается ,
# но когда модуль перезапускаеш возвращается прежний путь!
#   Выходит надо менять путь в терменале?

def f_copy_file_folder():                      # Создание копии файла или папки
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

def name_create_folder():                      # Создать имя создаваемой папки
    return create_folder(input('Введите имя создаваемой папки:  '))

def create_folder(name_folder):                        # Создать папку
    current_path = os.getcwd()
    new_path = os.path.join(current_path, name_folder)
    if os.path.exists(new_path):
        return 'Папка с таким именем уже существует'
    else:
        os.mkdir(new_path)
        if os.path.exists(name_folder):
            if name_folder in os.listdir():
                if os.path.isdir(name_folder):
                    if not os.path.isfile(name_folder):
                        return  f'Создана папка {name_folder}'
'''
Здравствуйте Леонид! У меня вопрос: как мне эти проверки перенести в тест функцию?
'''



def creator_program():                             # Создатель программы
    return 'Создатель программы: Хафизов.А.Т.'

def name_delete_file_folder():                 # Имя для удаления файла или папки
    return delete_file_folder(input('Введите имя файла или папки для удаления:  '))


def delete_file_folder(name_file_folder):                  # Удаление файла или папки
    current_path = os.getcwd()
    new_path = os.path.join(current_path, name_file_folder)
    if not os.path.exists(new_path):
        return 'Такой папки или файла, предназначенной для удаления не существует'
    elif os.path.isdir(new_path):
        if name_file_folder in new_path:
            if not os.path.isfile(name_file_folder):
                shutil.rmtree(new_path)
                if not os.path.isdir(name_file_folder):
                    if not name_file_folder in os.listdir():
                        return f'Папка {name_file_folder} удалена!'
    else:
        os.remove(new_path)
        return f'Файл {name_file_folder} удален!'


def f_information_operating_system():                 # Информация об опирацирнной системе
    return f'Установлена операционная система: {sys.platform}'


def f_viem_contents_working_direktory():               # Просмотр содержимого рабочей директории
    return os.listdir()


def f_viem_folders_only():               # Просмотр только папок
    folders = []
    for element in os.listdir():
        if os.path.isdir(element):
            folders.append(element)
    return folders


def f_viem_only_files():            # Просмотр только файлов
    files = []
    for element in os.listdir():
        if os.path.isfile(element):
            files.append(element)
    return files







