
def bank_account():

    def account_replenishment(depositing_money_number, sum_cash_account, history):           # 1  Внесение денег
        depositing_money = input('Пожалуйста внесите деньги для пополнения счета:  ')
        if not depositing_money.isdigit():
            depositing_money_number, sum_cash_account, history = account_replenishment(depositing_money_number, sum_cash_account, history)
        else:
            print(depositing_money)
            cash_account.append(depositing_money)
            depositing_money = float(depositing_money)
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
            purchase_price = float(purchase_price)
            if purchase_price > sum_cash_account:
                print('Недостаточно денег на счете')
            else:
                name_purchase = input('Введите название покупки: ')
                sum_cash_account -= purchase_price
                purchase_number += 1
                history['Покупка_' + str(purchase_number) + '-' + name_purchase] = purchase_price
        return purchase_number, sum_cash_account, history

    def history_menu():                                   # 3 История покупок

        print('Ваши операции: ')
        for key, val in history.items():
            print(f'{key} => {val}')
        print(f'На вашем счете: {sum_cash_account} рублей')


    cash_account = []                    # список денежных поступлений
    sum_cash_account = 0                 # Сумма денег на счете
    history = {}                         # История денежных операций
    purchase_number = 0                  # Номер покупки
    depositing_money_number = 0                 # Номер пополнения счета


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
            history_menu()

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
