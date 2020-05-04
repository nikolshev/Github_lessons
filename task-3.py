def my_func(a, b, c):
    number_list = [a, b, c]
    number_list.sort()
    sum = number_list[2] + number_list[1]
    print('сумма 2х максимальных чисел: ', sum)


my_func(5.2, -10, -3)