# не понимаю смысла провери последовательности, если цвета переключаются полностью автоматически

from itertools import cycle
import time

class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def act(self):
        for el in cycle(self.__color):
            if el == "красный":
                print(el)
                time.sleep(7)
            elif el == "желтый":
                print(el)
                time.sleep(2)
            elif el == "зеленый":
                print(el)
                time.sleep(5)


a = TrafficLight()
a.act()
