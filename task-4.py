number = int(input('введите целое положительное число'))
rest_max = 0

while number > 0:
    rest_check = number % 10
    number = number // 10
    if rest_check > rest_max:
        rest_max = rest_check
print('Максимальная цифра:', rest_max)
