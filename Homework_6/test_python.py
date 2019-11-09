from math import *

# filter

def test_filter():
    date = [5, 34, 54, -23, 4, -12, -234, 91, -39, -1, -5, -984, 17, 88, 55]
    assert list(filter(lambda x: x >= 0, date)) == [5, 34, 54, 4, 91, 17, 88, 55]
    assert list(filter(lambda x: x % 2 == 0 and x >= 0, date)) == [34, 54, 4, 88]
    assert list(filter(lambda x: x < 0, date)) == [-23, -12, -234, -39, -1, -5, -984]
    assert list(filter(lambda x: x >= 0 and x % 5 == 0, date)) == [5, 55]

# map

def test_map():
    date = [5, 34, 54, -23, 4, -12, -234, 91, -39, -1, -5, -984, 17, 88, 55]
    assert list(map(lambda x: x * 100, date)) == [i * 100 for i in date]
    assert list(map(lambda x: x * 100, date)) == [500, 3400, 5400, -2300, 400, -1200, -23400, 9100, -3900, -100, -500, -98400, 1700, 8800, 5500]
    result = []
    for element in date:
        element /= 5
        result.append(element)
    assert list(map(lambda x: x / 5, date)) == result
    assert list(map(lambda x: x / 5, date)) == [1.0, 6.8, 10.8, -4.6, 0.8, -2.4, -46.8, 18.2, -7.8, -0.2, -1.0, -196.8, 3.4, 17.6, 11.0]

'''
Здравствуйте Леонид! У меня тут возник вопрос: как вы относитесь к проверкам типа assert 1 и assert 3(в test_map),
на сколько они целесообразны, надежны ну и т.д. ?
'''
# sorted

def test_sorted():
    date = [5, 34, 54, -23, 4, -12, -234, 91, -39, -1, -5, -984, 17, 88, 55]
    assert sorted(date) == [-984, -234, -39, -23, -12, -5, -1, 4, 5, 17, 34, 54, 55, 88, 91]
    assert sorted(date, reverse=True) == [91, 88, 55, 54, 34, 17, 5, 4, -1, -5, -12, -23, -39, -234, -984]


# pi

def test_pi():
    date = [1, 2, 3]
    assert pi == 3.141592653589793
    assert float(f'{pi:.3f}') == 3.142
    assert float(f'{pi:.5f}') == 3.14159
    assert float(f'{pi:.7f}') == 3.1415927

# sqrt

def test_sqrt():
    date = [1, 2, 3, 4, 5]
    for i in date:
        assert sqrt(i) == sqrt(sqrt(i ** 2))
    assert sqrt(9) == 3
    assert sqrt(25) == 5

# pow   Возведение в степень

def test_pow():
    date = [1, 2, 3, 4, 5]
    for i in date:
        assert pow(i, 2) == i * i
        assert pow(i, 5) == i * i * i * i * i

# hypot    Гепотенуза угла с катетами x, y

def test_hyrot():
    date_x = [1, -2, 3.7, 4, -5.9]
    date_y = [-5, 6.4, -7.1, 8, 9.4]
    for x in date_x:
        for z in date_x[::-1]:
            assert hypot(x, z) == sqrt(x * x + z * z)
            for y in date_y:
                assert hypot(x, y) == sqrt(x * x + y * y)



