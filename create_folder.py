
import os

def f_create_folder():                       # Создать папку
    current_path = os.getcwd()
    name_folder = input('Введите имя создаваемой папки:  ')
    new_path = os.path.join(current_path, name_folder)
    if os.path.exists(new_path):
        print('Папка с таким именем уже существует')
    else:
        os.mkdir(new_path)
        print(f'Создана папка {name_folder}')




# print(os.getcwd())
# path = os.path.join(os.getcwd(), "create_folder.py")
# print(path)
# print(os.getcwd())

#os.rename(r'C:\Users\User\PycharmProjects\Homework-5\create folder.py', r'C:\Users\User\PycharmProjects\Homework-5\create_folder.py')

