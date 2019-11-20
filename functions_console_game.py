import os, shutil, sys, json, pickle
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

def names():    # Функция создания имени копируемой папки/файла и имени копии файла/папки
    #return f_copy_file_folder(input('Введите имя файла или папки, которые хотите скопировать:  '), input('Введите имя копии файла или папки:  '))
    name = input('Введите имя файла или папки, которые хотите скопировать:  ')
    name_copy = input('Введите имя копии файла или папки:  ')
    return f_copy_file_folder(name, name_copy)


def f_copy_file_folder(name, name_copy):                      # Создание копии файла или папки
    current_path = os.getcwd()
    # name = input('Введите имя файла или папки, которые хотите скопировать:  ')
    # name_copy = input('Введите имя копии файла или папки:  ')
    name_path = os.path.join(current_path, name)
    name_copy_path = os.path.join(current_path, name_copy)
    if not os.path.exists(name):
        return f'Файла или папки с таким именем {name} не существует'
    elif os.path.isdir(name_path):
        try:
            shutil.copytree(name_path, name_copy_path)
        except FileNotFoundError:
            print('Вы не ввели имя ! ! !')
            print('введите имя для создаваемой копии папки!')
            names()
        return f'Папка {name} скопирована в новую папку {name_copy}'
    else:
        try:
            shutil.copyfile(name_path, name_copy_path)
        except FileNotFoundError:
            print('Вы не ввели имя ! ! !')
            print('Введите имя для создаваемой копии файла!')
            names()
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
                try:
                    shutil.rmtree(new_path)
                except PermissionError:
                    print('Вы не ввели имя ! ! !')
                    print('Введите имя папки/файла для удаления!')
                    name_delete_file_folder()
                if not os.path.isdir(name_file_folder):
                    if not name_file_folder in os.listdir():
                        return f'Папка {name_file_folder} удалена!'
    else:
        try:
            os.remove(new_path)
        except PermissionError:
            print('Вы не ввели имя ! ! !')
            print('Введите имя папки/файла для удаления!')
            name_delete_file_folder()
        if not os.path.exists(new_path):
            return f'Файл {name_file_folder} удален!'


def f_information_operating_system():                 # Информация об опирацирнной системе
    return f'Установлена операционная система: {sys.platform}'


def f_viem_contents_working_direktory():               # Просмотр содержимого рабочей директории
    return os.listdir()


def f_viem_folders_only():               # Просмотр только папок
    folders = [element for element in os.listdir() if os.path.isdir(element)]
    # folders = []
    # for element in os.listdir():
    #     if os.path.isdir(element):
    #         folders.append(element)
    return folders


def f_viem_only_files():            # Просмотр только файлов
    files = [element for element in os.listdir() if os.path.isfile(element)]
    # files = []
    # for element in os.listdir():
    #     if os.path.isfile(element):
    #         files.append(element)
    return files



def save_contents_working_direktory():            #  Сохранить содержимое рабочей директории в файл 'txt'
    # files = ''
    # folders = ''
    # for element in os.listdir():
    #     if os.path.isfile(element):
    #         files += element + ', '
        # if os.path.isdir(element):
        #     folders += element + ', '
    files = ''.join(str(element) + ', ' for element in os.listdir() if os.path.isfile(element))
    folders = ''.join(str(element) + ', ' for element in os.listdir() if os.path.isdir(element))
    files = files[:-2]
    folders = folders[:-2]
    with open('listdir.txt', 'w') as f:
        f.writelines(f'files: {files}\n')
        f.writelines(f'folders: {folders}\n')

def read_json_contents_working_direktory():      # Чтение файла json  содержимого рабочей директории
    if os.path.exists('listdir.txt'):
        with open('listdir.txt', 'r') as f:
            result = f.read()
            print(result)




def read_file_json(json_name):    # Функция открытия файла json формата на чтение в нормальном виде
    if os.path.exists(json_name):
        with open(json_name, 'r') as f:
            real_name = json.load(f)
        return real_name



def rewrite_file_json(json_name, real_name):    # Функция перезаписи файла json формата из нормального вида
    with open(json_name, 'w') as f:
        json.dump(real_name, f)
    return



def addition_dict(main_dict, current_dict):     # Функция прибавления словаря текущей истории к словарю общей истории
    current_dict_new = {}
    for key in current_dict.keys():             # Перебираем ключи в текущей истории
        if key in main_dict:                     # Если такой ключь уже есть в общей истории
            current_dict_new[str(key) + '_+'] = current_dict.get(key)   # Добавляем + чтобы эта пара не удалилась и переносим пару во временный словарь
        else:
            current_dict_new[key] = current_dict.get(key)    # Остальные пары переносим во временный словарь
    for key, values in current_dict_new.items():   # Перебираем временный словарь
        main_dict[key] = values                    # И добавляем каждую пару в основную историю
    return main_dict                               # Выводим оснавную историю


def record_pickle(pickle_name, real_name):                  # Функция записи инфы в файл в виде байтов через pickle
    with open(pickle_name, 'wb') as f:
        pickle.dump(real_name, f)

def read_pickle(name):                         # Функция считывания инфы из файла в байтах и перевода в нормальный вид
    if os.path.exists(name):
        with open(name, 'rb') as f:
            result = pickle.load(f)
        return result
    else:
        return 'Нет такого файла!'

# date = read_file_json('history.json')
# print(date)
# record_pickle('date.pickle', date)
# print(read_pickle('date.pickle'))

def baks_separator(f):          # сепаратор ввода денег
    def inner(*args, **kwargs):
        print('*-------'*7)
        print('*$-$-$*-----ВВОД ДЕНЕГ-----' * 5)
        print('*-------' * 7)
        result = f(*args, **kwargs)
        return result
    return inner

def purchases_separator(f):
    def inner(*args, **kwargs):
        print('-------'*7)
        print('***-----ПОКУПКИ---' * 5)
        print('-------' * 7)
        result = f(*args, **kwargs)
        return result
    return inner

def history_separator(f):
    def inner(*args, **kwargs):
        print('-------'*7)
        print('---@-----текущая ИСТОРИЯ---' * 5)
        print('-------' * 7)
        result = f(*args, **kwargs)
        return result
    return inner

def main_menu_separator(f):
    def inner(*args, **kwargs):
        print('------'*7)
        print('---%-$-%-----меню БАНКА--' * 5)
        print('------' * 7)
        result = f(*args, **kwargs)
        return result
    return inner





# def add_list_common_history(dict_history, list_common_history):  # Создаем список общей истории и добавляем в него словарь текущей истории
#     list_element_history = [dict(x) for x in dict_history]
#     for element in list_element_history:
#         list_common_history.append(element)
#     # common_history = [common_ history.append(x) for x in list_element_history]
#     return list_common_history


# def test_add_list_common_history(dict_history, list_common_history):
# #     for i in dict_history:
# #         assert i in add_list_common_history(dict_history, list_common_history)
