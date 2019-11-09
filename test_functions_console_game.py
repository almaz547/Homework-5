
from functions_console_game import *


def test_f_viem_only_files():           # тест функции просмотр только файлов
    for item in f_viem_only_files():
        assert not os.path.isdir(item)
        assert os.path.exists(item)
        assert os.path.isfile(item)
        assert item in f_viem_only_files()
        assert os.path.exists(item) and os.path.isfile(item) and item in f_viem_only_files() and not os.path.isdir(item)
    assert f_viem_only_files() == [i for i in os.listdir() if os.path.isfile(i) and os.path.exists(i) and not os.path.isdir(i)]

def test_f_viem_folders_only():             # тест функции просмотр только папок
    for element in f_viem_folders_only():
        assert not os.path.isfile(element)
        assert os.path.exists(element)
        assert os.path.isdir(element)
        assert element in f_viem_folders_only()
        assert not os.path.isfile(element) and os.path.exists(element) and os.path.isdir(element) and element in f_viem_folders_only()
    assert f_viem_folders_only() == [i for i in os.listdir() if not os.path.isfile(i) and os.path.exists(i) and os.path.isdir(i) and i in f_viem_folders_only()]

def test_f_viem_contents_working_direktory():
    assert f_viem_contents_working_direktory() == os.listdir()



def test_create_folder():                     # тест функции создать папку
    name_folder = 'test_name_folder'
    assert create_folder(name_folder) == f'Создана папка {name_folder}'
    assert create_folder(name_folder) == 'Папка с таким именем уже существует'
    os.rmdir(name_folder)
'''
Здравствуйте Леонид! У меня вопрос: как мне проверки которые я разместил 
в функции создания папки перенести в тест функцию?
'''


def test_creator_program():
    assert creator_program() == 'Создатель программы: Хафизов.А.Т.'

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



