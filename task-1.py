def division(first_number, second_number):
    if second_number != 0:
        print('частное: ', round(first_number / second_number, 3))
    else:
        print('деление на 0 невозможно')


first_number = float(input('введите делимое: '))
second_number = float(input('введите делитель: '))
division(first_number, second_number)

