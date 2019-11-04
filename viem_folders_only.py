import os

def f_viem_folders_only():
    folders = []
    for element in os.listdir():
        if os.path.isdir(element):
            folders.append(element)
    return f'Список папок:  {folders}'


