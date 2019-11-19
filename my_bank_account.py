'''
#def bank_account():


def account_replenishment(depositing_money_number, sum_cash_account, history):           # 1  Внесение денег
    depositing_money = input('Пожалуйста внесите деньги для пополнения счета:  ')
    if not depositing_money.isdigit():
        depositing_money_number, sum_cash_account, history = account_replenishment(depositing_money_number, sum_cash_account, history)
    else:
        print(depositing_money)
        cash_account.append(depositing_money)
        depositing_money = int(depositing_money)
        sum_cash_account += depositing_money
        depositing_money_number += 1
        history['Пополнение счета_' + str(depositing_money_number)] = depositing_money
        print(cash_account)
        print(sum_cash_account)
        for key, val in history.items():
            print(f'{key} = {val}')
    return depositing_money_number, sum_cash_account, history

def purchases(purchase_number, sum_cash_account, history):                              # 2 покупки
    purchase_price = input('Введите сумму покупки: ')
    if not purchase_price.isdigit():
        purchase_number, sum_cash_account, history = purchases(purchase_number, sum_cash_account, history)
    else:
        purchase_price = int(purchase_price)
        if purchase_price > sum_cash_account:
            print('Недостаточно денег на счете')
        else:
            name_purchase = input('Введите название покупки: ')
            sum_cash_account -= purchase_price
            purchase_number += 1
            history['Покупка_' + str(purchase_number) + '-' + name_purchase] = purchase_price
    return purchase_number, sum_cash_account, history

def history_menu(sum_cash_account):                                   # 3 История покупок

    print('Ваши операции: ')
    for key, val in history.items():
        print(f'{key} => {val}')
    print(f'На вашем счете: {sum_cash_account} рублей')


cash_account = []                    # список денежных поступлений
sum_cash_account = 0                 # Сумма денег на счете
history = {}                         # История денежных операций
purchase_number = 0                  # Номер покупки
depositing_money_number = 0                 # Номер пополнения счета

def menu_bank(depositing_money_number, sum_cash_account, history, purchase_number):
    while True:

        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            depositing_money_number, sum_cash_account, history = account_replenishment(depositing_money_number, sum_cash_account, history)
        elif choice == '2':
            purchase_number, sum_cash_account, history = purchases(purchase_number, sum_cash_account, history)
        elif choice == '3':
            history_menu(sum_cash_account)

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
'''

import os, json

def account_replenishment(depositing_money_number, sum_cash_account, history):           # 1  Внесение денег
    depositing_money = input('Пожалуйста внесите деньги для пополнения счета:  ')
    if not depositing_money.isdigit():
        depositing_money_number, sum_cash_account, history = account_replenishment(depositing_money_number, sum_cash_account, history)
    else:
        cash_account.append(depositing_money)
        depositing_money = int(depositing_money)
        sum_cash_account += depositing_money
        depositing_money_number += 1
        history['Пополнение счета_' + str(depositing_money_number)] = depositing_money
    return depositing_money_number, sum_cash_account, history

def purchases(purchase_number, sum_cash_account, history):                              # 2 покупки
    purchase_price = input('Введите сумму покупки: ')
    if not purchase_price.isdigit():
        purchase_number, sum_cash_account, history = purchases(purchase_number, sum_cash_account, history)
    else:
        purchase_price = int(purchase_price)
        if purchase_price > sum_cash_account:
            print('Недостаточно денег на счете')
        else:
            name_purchase = input('Введите название покупки: ')
            sum_cash_account -= purchase_price
            purchase_number += 1
            history['Покупка_' + str(purchase_number) + '-' + name_purchase] = purchase_price
    return purchase_number, sum_cash_account, history

def history_menu(history):                                   # 3 История покупок
    if history == {}:
        print('Текущая история пуста.')
    else:
        print('Ваши последние операции: ')
        for key, val in history.items():
            print(f'{key} => {val}')
    return history

cash_account = []                    # список денежных поступлений
#sum_cash_account = 0                 # Сумма денег на счете
history = {}                         # История денежных операций
purchase_number = 0                  # Номер покупки
depositing_money_number = 0                 # Номер пополнения счета
#common_history = {}                   # Общая история операций по счету

def read_file_json(json_name):    # Функция открытия файла json формата на чтение в нормальном виде
    if os.path.exists(json_name):
        with open(json_name, 'r') as f:
            real_name = json.load(f)
        return real_name

def rewrite_file_json(json_name, real_name):    # Функция перезаписи файла json формата из нормального вида
    with open(json_name, 'w') as f:
        json.dump(real_name, f)
    return

def addition_dict(main_dict, current_dict):     # Функция прибавления словаря текущей истории к словарю общей истории
    current_dict_new = {}
    for key in current_dict.keys():             # Перебираем ключи в текущей истории
        if key in main_dict:                     # Если такой ключь уже есть в общей истории
            current_dict_new[str(key) + '_+'] = current_dict.get(key)   # Добавляем + чтобы эта пара не удалилась и переносим пару во временный словарь
        else:
            current_dict_new[key] = current_dict.get(key)    # Остальные пары переносим во временный словарь
    for key, values in current_dict_new.items():   # Перевираем временный словарь
        main_dict[key] = values                    # И добавляем каждую пару в основную историю
    return main_dict                               # Выводим оснавную историю





def menu_bank(depositing_money_number,history, purchase_number):
    sum_cash_account = read_file_json('cash.json')    # Считываем счет из файла
    common_history = read_file_json('history.json')      # Считываем общую историю с файла
    if sum_cash_account == False or sum_cash_account == None:
        sum_cash_account = 0
    if common_history == None:
        common_history = {}
        print('История операций по счету пуста.')
    else:
        print('Общая история операций по счету: ')
        for k, v in common_history.items():
            print(f'{k} --> {v}')

    while True:
        print(f'На вашем счете: {sum_cash_account} рублей')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход и сохранение в файл истории покупок')
        print('5. Общая история операций по счету')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            depositing_money_number, sum_cash_account, history = account_replenishment(depositing_money_number, sum_cash_account, history)
            rewrite_file_json('cash.json', sum_cash_account)                      # Перезаписываем счет в файле
            sum_cash_account = read_file_json('cash.json')       # Считываем счет из файла



        elif choice == '2':
            purchase_number, sum_cash_account, history = purchases(purchase_number, sum_cash_account, history)
            rewrite_file_json('cash.json', sum_cash_account)                    # Перезаписываем счет в файле
            sum_cash_account = read_file_json('cash.json')    # Считываем счет из файла



        elif choice == '3':
            history = history_menu(history)

        elif choice == '4':
            common_history = addition_dict(common_history, history)  # Прибавляем текущую историю к общей
            rewrite_file_json('history.json', common_history)  # Перезаписываем общую историю
            history.clear()
            break
        elif choice == '5':
            if common_history == 0 or common_history == {}:
                print('История операций на диске пуста')
            else:
                print('Общая история операций по счету: ')
                common_history = read_file_json('history.json')  # Считываем общую историю с файла
                for k,v in common_history.items():
                    print(f'{k} --> {v}')
        else:
            print('Неверный пункт меню')



