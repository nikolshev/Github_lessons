from abc import ABC, abstractmethod


class Dress(ABC):

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class MyDress(Dress):

    def __init__(self, v, h):
        self.coat_mater = round(v / 6.5 + 0.4, 2)
        self.suit_mater = h * 2 + 0.3

    @property
    def coat(self):
        return f'материал для пальто: {self.coat_mater}'

    @property
    def suit(self):
        return f'материал для костюма: {self.suit_mater}'

    @property
    def total(self):
        total = self.suit_mater + self.coat_mater
        return f'общее количество материала: {total}'


dress = MyDress(50, 10)
print(dress.coat)
print(dress.suit)
print(dress.total)
