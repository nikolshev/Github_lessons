from itertools import count, cycle

# задание 1
start_number = int(input('введите стартовое число '))
end_number = int(input('введите конечное число '))
number_list = []
for el in count(start_number):
    if el > end_number:
        break
    else:
        number_list.append(el)
print('сгенерированный список ', number_list)

# задание 2. Итерация списка сгенерированного выше
quont = 0
for el in cycle(number_list):
    if quont > 10:
        break
    else:
        print(el)
    quont += 1
