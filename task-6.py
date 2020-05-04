def int_func(input_text):
    title_word = input_text.title()
    return title_word


long_text = input('введите текст из маленьких латинских букв')
small_long_text = long_text.split()
big_long_text = []
for i in small_long_text:
    big_long_text.append(int_func(i))
final_text = ' '.join(big_long_text) # преобразуем список в строку
print(final_text)