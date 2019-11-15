from filemanager import author_info, filenames
import os
from victory import date_to_str, run_victory, random_famous_f

import random

def test_author_info():
    assert author_info() == 'Leonid Orlov'

def test_filenames():
    for item in filenames():
        assert not os.path.isdir(item)
        assert os.path.exists(item)
        assert os.path.isfile(item)
        assert item in filenames()
        assert os.path.exists(item) and os.path.isfile(item) and item in filenames() and not os.path.isdir(item)
    assert filenames() == [i for i in filenames() if os.path.isfile(i) and os.path.exists(i) and not os.path.isdir(i)]

def test_date_to_str():
    date = ['26.06.1799', '12.02.1809', '04.06.1975']
    date_text = ['двадцать шестое июня 1799 года', 'двенадцатое февраля 1809 года', 'четвертое июня 1975 года']
    for i in range(len(date)):
        assert date_to_str(date[i]) == date_text[i]








