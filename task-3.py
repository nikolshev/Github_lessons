with open("task_3.txt", "r", encoding='utf-8') as out_f:
    persons = 0
    sellary = 0
    for line in out_f:
        list_line = line.split()
        if float(list_line[1]) < 20000:
            print('зп < 20 тр:', list_line[0])
        persons += 1
        sellary += float(list_line[1])
print('средняя зп: ', round(sellary/persons, 2))
