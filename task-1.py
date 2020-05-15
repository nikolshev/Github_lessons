# передайте скрипут данные по следующему образцу:
# 'часовая ставка' 'время работы' 'размер премии'

from sys import argv
salary_rage, time, extra = argv[1:]
def result(salary_rage, time, extra):
    print('Итоговая зарплата: ', float(salary_rage) * float(time) + float(extra))

# Строку ниже вставил только для того, чтобы увидеть работоспособность функции выше
result(salary_rage, time, extra)