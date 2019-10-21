print('Добро пожаловать в наш магазин!')
your_money = int(input('Какую сумму вы собираетесь потратить на продукты питания? '))
milk_cost = 62                                     #Цена за бутылку молока
bread_cost = 54                                    #Цена за буханку хлеба
chips_cost = 41                                    #Цена за упаковку чипсов
cola_cost = 33                                     #Цена за баночку колы
amount_of_milk = 0
amount_of_bread = 0
amount_of_chips = 0
amount_of_cola = 0
balance = your_money                               #Первоначальное количество денег
ask_of_milk = input('Купить бутылку молока? ')
while ask_of_milk == 'да':
    amount_of_milk += 1
    balance = balance - milk_cost
    print(balance)
    ask_of_milk = input('Купить ещё молока? ')
    if balance < milk_cost:
        print('Недостаточно средств для покупки молока.')
        print('У вас есть возможность купить другие товары по более низкой цене.')
        break
    elif ask_of_milk == 'нет':
        break
ask_of_bread = input('Купить буханку хлеба? ')
while ask_of_bread == 'да':
    amount_of_bread += 1
    balance = balance - bread_cost
    print(balance)
    ask_of_bread = input('Купить ещё буханку? ')
    if balance < bread_cost:
        print('Недостаточно средств для покупки хлеба.')
        print('У вас есть есть возможность купить другие товары по более низкой цене.')
        break
    elif ask_of_bread == 'нет':
        break
ask_of_chips = input('Купить упаковку чипсов? ')
while ask_of_chips == 'да':
    amount_of_chips += 1
    balance = balance - chips_cost
    print(balance)
    ask_of_chips = input('Купить ещё упаковку чипсов? ')
    if balance < chips_cost:
        print('Недостаточно средств для покупки упаковки чипсов.')
        print('У вас есть есть возможность купить другие товары по более низкой цене.')
        break
    elif ask_of_chips == 'нет':
        break
ask_of_cola = input('Купить баночку колы? ')
while ask_of_cola == 'да':
    amount_of_cola +=1
    balance = balance - cola_cost
    print(balance)
    ask_of_cola = input('Купить ещё баночку колы? ')
    if balance < cola_cost:
        print('Недостаточно средств для покупки упаковки колы.')
        print('К сожалению это был самый дешёвый товар в нашем магазине.')
    elif ask_of_cola == 'нет':
        break
print('Всего вами было куплено:')
print(amount_of_milk, 'бутылок молока')
print(amount_of_bread, 'буханок хлеба')
print(amount_of_chips, 'упаковок чипсов')
print(amount_of_cola, 'баночек колы')
print('Ваш остаток составляет:',balance,'рублей')






