
import os
import shutil


current_path = os.getcwd()
def f_delete_file_folder():
    current_path = os.getcwd()
    name_fil_fold = input('Введите имя файла или папки для удаления:  ')
    new_path = os.path.join(current_path, name_fil_fold)
    if not os.path.exists(new_path):
        return 'Такой папки или файла, предназначенной для удаления не существует'
    elif os.path.isdir(new_path):
        shutil.rmtree(new_path)
        return f'Папка {name_fil_fold} удалена!'
    else:
        os.remove(new_path)
        return f'Файл {name_fil_fold} удален!'

