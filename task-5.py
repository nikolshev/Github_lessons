class Stationery:
    def __init__(self, title_name):
        self.title = title_name

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f"отрисовка {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"отрисовка {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"отрисовка {self.title}")


s = Stationery('тест')
s.draw()

s = Pen('Pen')
s.draw()

s = Pencil('Pencil')
s.draw()

s = Handle('Handle')
s.draw()