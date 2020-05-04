def numbers_line():
    summ = 0
    while True:
        numbers = input('введите числа через пробел. Для остановки нажмите s')
        line = numbers.split()
        for i in line:
            if i != "s":
                summ = summ + float(i)
            else:
                return summ
        print('промежуточное значение суммы: ', summ)


print('конечное значение суммы: ', numbers_line())
