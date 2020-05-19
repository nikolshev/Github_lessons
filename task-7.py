import json

with open("task_7.txt", "r", encoding='utf-8') as out_f:
    companies_dict = {}
    total_profit = 0
    companies = 0
    for line in out_f:
        company = line.split()
        profit = float(company[2]) - float(company[3])
        if profit > 0:
            total_profit += profit
            companies += 1
        companies_dict.update({company[0]: profit})
    average_profit = dict({'average_profit': round(total_profit / companies, 2)})
    result_list = [companies_dict, average_profit]
    print(result_list)
    with open('task_7.json', 'w') as f:
        json.dump(result_list, f)
