import os

def f_viem_folders_only():
    folders = []
    for element in os.listdir():
        if os.path.isdir(element):
            folders.append(element)
    print(f'Список папок:  {folders}')

