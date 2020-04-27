number_goods = int(input('введите количество товаров:'))
i = 0
result_list = []
name_list = []
price_list = []
quantity_list = []
unit_list = []
while i <= number_goods - 1:
    print(f"ввод данных {i+1}-ого товара")
    name_goods = input('введите название')
    # создаем список из названий для будущей аналитики
    name_list.insert(i, name_goods)
    price_goods = int(input('введите цену'))
    # создаем список из цен для будущей аналитики
    price_list.insert(i, price_goods)
    quantity_goods = int(input('введите количество'))
    # создаем список из количеств для будущей аналитики
    quantity_list.insert(i, quantity_goods)
    unit_goods = input('введите единицы измерения')
    # создаем список из единиц изменения для будущей аналитики
    unit_list.insert(i, unit_goods)
    # наполняем словарь
    list_the_goods = {'название': name_goods, 'цена': price_goods, 'кол-во': quantity_goods, 'ед.изм': unit_goods}
    # на основании словаря делаем кордеж для каждого товара
    the_goods = (i + 1, list_the_goods)
    # делаем список из кортежей
    result_list.insert(i, the_goods)
    i = i + 1
# убираем повторы
name_list = list(set(name_list))
price_list = list(set(price_list))
quantity_list = list(set(quantity_list))
unit_list = list(set(unit_list))
# итоговый словарь от аналитикой
final_dict = {'название': name_list, 'цена': price_list, 'кол-во': quantity_list, 'ед.изм': unit_list}
print('первая часть задания:', result_list)
print('2ая часть задания:', final_dict)
