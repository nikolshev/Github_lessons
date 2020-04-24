time = int(input('введите время в секундах'))
hours = time // 3600 #количество часов
minutes = time % 3600 // 60 #количество минут
sec = time - hours*3600 - minutes*60 #количество секунд
print(f"Вы указали время: {hours}:{minutes}:{sec}")