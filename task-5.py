with open("task_5.txt", "w+", encoding='utf-8') as out_f:
    out_f.write(input('введите числа'))
    out_f.seek(0)
    numbers = out_f.read()
    numbers_list = list(map(int, numbers.split()))
    print('сумма чисел:', sum(numbers_list))
