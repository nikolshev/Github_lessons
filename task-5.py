start_list = [9, 5, 4, 4, 3]
add_number = int(input('введите число рейтинга'))
for el in start_list:
    if add_number > el:
        start_list.insert(start_list.index(el), add_number)
        break
length = len(start_list) - 1
if add_number <= start_list[length]:
    start_list.append(add_number)
print(start_list)
