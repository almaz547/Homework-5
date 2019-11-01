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
    print(f'Адрес рабочей директории: {os.getcwd()}')
    folder_name = input('Введите новое имя рабочей директории: ')
    if not os.path.exists(folder_name):
        print(f'Данной директории {folder_name} не существует')
        return
    if not os.path.isdir(folder_name):
        print(f'"Это не директория {folder_name}')
        return
    os.chdir(folder_name)

# В этом варианте путь взятый с предыдущего проекта присваевается ,
# но когда модуль перезапускаеш возвращается прежний путь!
#   Выходит надо менять путь в терменале?
