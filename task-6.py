with open("task_6.txt", "r", encoding='utf-8') as out_f:
    final_dict = {}
    for line in out_f:
        new_line = line.replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('.', '')
        new_line_list = new_line.split()
        sum = 0
        for el in new_line_list:
            if el.isdigit() is True:
                sum += int(el)
        final_dict.update({new_line_list[0]: sum})
print('Итоговый словарь: ', final_dict)
