'''
- создать папку

после выбора пользователь вводит название папки, создаем её в рабочей директории



- удалить (файл/папку)

после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть



- копировать (файл/папку)

после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем



- просмотр содержимого рабочей директории

вывод всех объектов в рабочей папке



- посмотреть только папки

вывод только папок которые находятся в рабочей папке



- посмотреть только файлы

вывод только файлов которые находятся в рабочей папке



- просмотр информации об операционной системе

вывести информацию об операционной системе (можно использовать пример из 1-го урока)



- создатель программы

вывод информации о создателе программы



- играть в викторину

запуск игры викторина из предыдущего дз



- мой банковский счет

запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать)



- смена рабочей директории (*необязательный пункт)

усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней



- выход

выход из программы'''



from quiz_game import quiz_game_f
from my_bank_account import bank_account
from copy_file_folder import f_copy_file_folder
from create_folder import f_create_folder
from delete_file_folder import f_delete_file_folder
from viem_only_files import f_viem_only_files
from viem_folders_only import f_viem_folders_only
from change_working_directory import f_change_working_direktory
from viem_contents_working_direktory import f_viem_contents_working_direktory
from information_operating_system import f_information_operating_system
from creator_program import f_creator_program


while True:
    print('Добро пожаловать! К Вашим услугам следующие действия')
    print('1. Создать папку')
    print('2. Удалить файл или папку')
    print('3. Копировать файл или папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Просмотреть только папки')
    print('6. Просмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')
    choice = input('Выберите пожалуйста нужнуй вам пункт меню:  ')
    if choice == '1':
        print(f_create_folder())
    elif choice == '2':
        print(f_delete_file_folder())
    elif choice == '3':
        print(f_copy_file_folder())
    elif choice == '4':
        print(f_viem_contents_working_direktory())
    elif choice == '5':
        print(f_viem_folders_only())
    elif choice == '6':
        print(f_viem_only_files())
    elif choice == '7':
        print(f_information_operating_system())
    elif choice == '8':
        print(f_creator_program())
    elif choice == '9':
        quiz_game_f()
    elif choice == '10':
        bank_account()
    elif choice == '11':
        print(f_change_working_direktory())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')


