revenue = int(input('Введите выручку фирмы:'))
expenses = int(input('Введите издержки фирмы:'))
profit = revenue - expenses
if profit > 0:
    print('Ваша фирма работает с прибылью')
    profitability = round(profit / revenue * 100, 2)
    print(f"Рентабельность составляет {profitability}%")
    staff = int(input('Введите количество сотрудников фирмы фирмы:'))
    for_one = round(profitability / staff, 2)
    print("прибыль в пересчете на одного сотрудника:", for_one)
elif profit < 0:
    print('Ваша фирма работает в убыток')
elif profit == 0:
    print('Вы сработали в ноль - уже хорошо')
