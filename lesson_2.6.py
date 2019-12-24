
enter = ''
goods = []
i = 0

while enter == '':  # если нажата клавиша Enter - вводим данные, иначе выходим
    i += 1

    name = input('\n введите название товара: ')
    price = input('введите цену товара: ')
    num = input('введите количество товара: ')
    unit = input('введите ед. изм. товара: ')

    goods.append((i, {'name': name, 'price': price, 'num': num, 'unit': unit}))
    print('\n', goods)

    enter = input('\nНажмите Enter для продолжения, для выхода любую клавишу+Enter')

# вывод "аналитики"
while True:
    print('\nChoose action: ')
    print(' [1] печать списка наименований товаров.')
    print(' [2] печать списка цен товаров.')
    print(' [3] печать списка количества товаров.')
    print(' [4] печать списка ед. изм товаров.')
    print(' [5] выход.')

    action = input('\nвы ввели: ')
    if action == '5':
        break

    names = ('Goods', 'Prices', 'Quantities', 'Units')
    titles = ('name', 'price', 'num', 'unit')
    res = {'name': [], 'price': [], 'num': [], 'unit': set()}

    for id, v in goods:
        res['name'].append(v['name'])
        res['price'].append(v['price'])
        res['num'].append(v['num'])
        res['unit'].add(v['unit'])

   
    print(f'\n{names[int(action) - 1]}: {res[titles[int(action) - 1]]}')

print('\nGoodbye!')