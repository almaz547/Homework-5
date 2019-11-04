import os
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

def f_change_working_direktory():
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
