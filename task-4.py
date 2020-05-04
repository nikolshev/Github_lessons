def my_func(x, y):
    # вариант 1
    print('решение вариант 1: ', round(x ** y, 4))
    # вариант 2
    result = x
    for i in range(1, abs(y)):
        result = result * x
    print('решение вариант 2: ', round(1 / result, 4))


my_func(0.9, -3)
