class Worker:
    def __init__(self, name, surname, position, income):
        self.name_person = name
        self.surname_person = surname
        self.position_person = position
        self._income_person = income
class Position(Worker):
    def position_print(self):
        print(self.position_person)

    def get_full_name(self):
        print('ИФ: ', self.name_person, " ", self.surname_person)

    def get_total_income(self):
        print('Доход: ',  self._income_person.get("wage") + self._income_person.get("bonus"))


p = Position('Иван', 'Иванов', 'Инженер', {"wage":500,"bonus":3000})
p.position_print()
p.get_full_name()
p.get_total_income()


