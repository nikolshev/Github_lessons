with open("task_4.txt", "r", encoding='utf-8') as out_f:
    for line in out_f:
        new_line = line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
        with open("task_4_result.txt", "a", encoding='utf-8') as out_f_result:
            out_f_result.write(new_line)
