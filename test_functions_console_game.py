import pytest
from functions_console_game import *


def test_f_viem_only_files():  # тест функции просмотр только файлов
    for item in f_viem_only_files():
        assert not os.path.isdir(item)
        assert os.path.exists(item)
        assert os.path.isfile(item)
        assert item in f_viem_only_files()
        assert os.path.exists(item) and os.path.isfile(item) and item in f_viem_only_files() and not os.path.isdir(item)
    assert f_viem_only_files() == [i for i in os.listdir() if
                                   os.path.isfile(i) and os.path.exists(i) and not os.path.isdir(i)]


def test_f_viem_folders_only():  # тест функции просмотр только папок
    for element in f_viem_folders_only():
        assert not os.path.isfile(element)
        assert os.path.exists(element)
        assert os.path.isdir(element)
        assert element in f_viem_folders_only()
        assert not os.path.isfile(element) and os.path.exists(element) and os.path.isdir(
            element) and element in f_viem_folders_only()
    assert f_viem_folders_only() == [i for i in os.listdir() if
                                     not os.path.isfile(i) and os.path.exists(i) and os.path.isdir(
                                         i) and i in f_viem_folders_only()]


def test_f_viem_contents_working_direktory():
    assert f_viem_contents_working_direktory() == os.listdir()


def test_create_folder():  # тест функции создать папку
    name_folder = 'test_name_folder'
    assert create_folder(name_folder) == f'Создана папка {name_folder}'
    assert create_folder(name_folder) == 'Папка с таким именем уже существует'
    os.rmdir(name_folder)


'''
Здравствуйте Леонид! У меня вопрос: как мне проверки которые я разместил 
в функции создания папки перенести в тест функцию? : Вот эта функция ниже 


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

Здравствуйте Леонид! У меня вопрос: как мне эти проверки перенести в тест функцию?

'''


def test_creator_program():
    assert creator_program() == 'Создатель программы: Хафизов.А.Т.'


def test_save_contents_working_direktory():  # Тест функции: Сохранить содержимое рабочей директории в файл
    if os.path.exists('listdir.txt'):
        with open('listdir.txt', 'r') as f:
            result = f.read()
        assert print(save_contents_working_direktory()) == print(result)


def test_rewrite_file_json():  # Тест функции перезаписи файла json формата из нормального вида
    real_name = {'Пополнение счета_1': 1000, 'Пополнение счета_1_+': 5000, 'Покупка_1-a': 1000, 'Покупка_1-a_+': 1000,
                 'Пополнение счета_2': 3000, 'Пополнение счета_2_+': 7000, 'Покупка_2-as': 500, 'Покупка_1-zxcv': 4000,
                 'Покупка_1-zxcv_+': 4000}
    rewrite_file_json('history.json', real_name)
    with open('history.json', 'r') as f:
        result = json.load(f)
    assert print(rewrite_file_json('history.json', real_name)) == print(result)


# def test_read_file_json():              # Тест функции открытия файла json формата на чтение в нормальном виде
#     common_history = {'Пополнение счета_1': 1000, 'Пополнение счета_1_+': 5000, 'Покупка_1-a': 1000, 'Покупка_1-a_+': 1000, 'Пополнение счета_2': 3000, 'Пополнение счета_2_+': 7000, 'Покупка_2-as': 500, 'Покупка_1-zxcv': 4000, 'Покупка_1-zxcv_+': 4000}
#     with open('history.json', 'w') as f:
#         json.dump(common_history, f)
#         assert read_file_json('history.json') == common_history


def test_addition_dict():  # Тест функции прибавления словаря текущей истории к словарю общей истории
    history = {'Пополнение счета_1': 5000, 'Пополнение счета_2': 34789, 'Покупка_1-weryu': 1235, 'Покупка_2-xcv': 2346,
               'Пополнение счета_3': 7000}
    history_2 = {'Пополнение счета_5': 5000, 'Пополнение счета_6': 34789, 'Покупка_7-weryu': 1235,
                 'Покупка_8-xcv': 2346, 'Пополнение счета_9': 7000}
    common_history = {'Пополнение счета_1': 5000, 'Пополнение счета_2': 34789, 'Покупка_1-weryu': 1235,
                      'Покупка_2-xcv': 2346,
                      'Пополнение счета_3': 7000, 'Пополнение счета_5': 5000, 'Пополнение счета_6': 34789,
                      'Покупка_7-weryu': 1235, 'Покупка_8-xcv': 2346, 'Пополнение счета_9': 7000}
    assert addition_dict(history_2, history) == common_history


def test_read_json_contents_working_direktory():  # Тест чтения файла txt  содержимого рабочей директории
    assert read_json_contents_working_direktory() == print(save_contents_working_direktory())


def test_record_pickle():  # Тест функции запись инфы в файл в виде байтов через pickle
    real_name = {'Пополнение счета_1': 1000, 'Пополнение счета_1_+': 5000, 'Покупка_1-a': 1000, 'Покупка_1-a_+': 1000,
                 'Пополнение счета_2': 3000, 'Пополнение счета_2_+': 7000, 'Покупка_2-as': 500, 'Покупка_1-zxcv': 4000,
                 'Покупка_1-zxcv_+': 4000}
    record_pickle('data_pickle', real_name)
    if os.path.exists('data_pickle'):
        with open('data_pickle', 'rb') as f:
            result = pickle.load(f)
    assert record_pickle('data_pickle', real_name) == print(result)


def test_read_pickle():  # Тест функции считывания инфы из файла в байтах и перевода в нормальный вид
    date = {'Пополнение счета_1': 1000, 'Пополнение счета_1_+': 5000, 'Покупка_1-a': 1000, 'Покупка_1-a_+': 1000,
            'Пополнение счета_2': 3000, 'Пополнение счета_2_+': 7000, 'Покупка_2-as': 500, 'Покупка_1-zxcv': 4000,
            'Покупка_1-zxcv_+': 4000}
    with open('data_pickle', 'wb') as f:
        pickle.dump(date, f)
    assert read_pickle('data_pickle') == date


'''
Не для здачи, на доработке.(Не всегда работает, предстоит разобраться, - полезный процесс обучения.)

# def test_delete_file_folder():          # тест функции удаление файлов или папок
#     #name_file_folder = 'test_name'
#     path = os.getcwd()
#     test_path = os.path.join(path, 'test_name')
#     name_file_folder = os.mkdir(test_path)
#     assert delete_file_folder(name_file_folder) == f'Папка {name_file_folder} удалена!'
#     assert delete_file_folder(name_file_folder) == 'Такой папки или файла, предназначенной для удаления не существует'
#

'''


