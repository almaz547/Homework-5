

import os

def f_viem_only_files():
    files = []
    for element in os.listdir():
        if os.path.isfile(element):
            files.append(element)
    return f'Список файлов:  {files}'

