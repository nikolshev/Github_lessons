date_list = input('введите слова через пробел')
ready_list = date_list.split()
for ind, n in enumerate(ready_list, 1):
    print(ind, '-', n[0:10])
