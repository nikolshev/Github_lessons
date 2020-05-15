from random import randint

start_list = [randint(0, 999) for num in range(10)] # самогененируемый исходных список на 10 элементов
final_list = []
el = 1
while el < len(start_list):
    if start_list[el] > start_list[el - 1]:
        final_list.append(start_list[el])
    el += 1
print('исходный список', start_list)
print('конечный список', final_list)
