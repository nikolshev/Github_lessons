date_list = input('введите значения списка через пробел')
revers_list = date_list.split()
i = 0
m = len(revers_list)
while i < (m - 1):
    revers_list[i], revers_list[i + 1] = revers_list[i + 1], revers_list[i]
    i = i + 2
print('исходный список', date_list)
print('список после реверса', revers_list)
