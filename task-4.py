class Car:
    def __init__(self, speed_car, color_car, name_car, is_police_car):
        self.speed = speed_car
        self.color = color_car
        self.name = name_car
        self.is_police = is_police_car

    def go(self):
        if self.speed > 0:
            print('машина поехала')
        else:
            print('машина стоит')

    def stop(self):
        print('машина остановилась')

    def turn_left(self):
        print('поворот налево')

    def turn_right(self):
        print('поворот направо')

    def show_speed(self):
        print('скорость: ', self.speed)

    def town_car_inform(self):
        if self.is_police is True:
            police = 'полиция'
        else:
            police = 'гражданский автомобиль'
        print(f"марка: {self.name}\nцвет: {self.color}\nстатус: {police}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости')
        else:
            print('скорость: ', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости')
        else:
            print('скорость: ', self.speed)


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

print('')
c = TownCar(70, "красный", "Audi", False)
c.town_car_inform()
c.show_speed()
c.go()
c.turn_left()
print("") #вставил лишь для разделения полей с инфоомацией о разных объектах

c = WorkCar(10, "черный", "BMW", False)
c.town_car_inform()
c.show_speed()
c.go()
c.turn_left()
print("") #вставил лишь для разделения полей с инфоомацией о разных объектах

c = SportCar(100, "желтый", "ZAZ", False)
c.town_car_inform()
c.show_speed()
c.go()
c.turn_right()
print("") #вставил лишь для разделения полей с инфоомацией о разных объектах

c = PoliceCar(0, "желтый", "VAZ", True)
c.town_car_inform()
c.show_speed()
c.go()
c.turn_right()
