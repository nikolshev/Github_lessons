with open("task_2.txt", "r", encoding='utf-8') as out_f:
    line_number = 0
    for line in out_f:
        line_number += 1
        list_line = line.split()
        print(f'длина {line_number}-ой строки: {len(list_line)}')
print('кол-во строк: ', line_number)
