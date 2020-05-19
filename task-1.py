with open("task_1.txt", "w", encoding='utf-8') as out_f:
    while True:
        input_text = input('введите текст')
        if input_text == " ":
            break
        else:
            final_text = [input_text, "\n"]
            out_f.writelines(final_text)
print('ввод текста завершен')
