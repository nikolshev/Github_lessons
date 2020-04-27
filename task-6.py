first_day = int(input('Введите "a" - результат в первый день'))
last_day = int(input('Введите "b" - результат в последний день'))
day = 1
while first_day < last_day:
     first_day = first_day * 1.1
     day = day + 1
print(f"на {day}-й день спортсмен достиг результата — не менее {last_day} км.")