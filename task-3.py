class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        result = self.cell_number + other.cell_number
        return f'результат объединения 2х клеток: {result}'

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            result = self.cell_number - other.cell_number
            return f'результат вычитания 2х клеток: {result}'
        else:
            return f'разность отрицательная'

    def __mul__(self, other):
        result = self.cell_number * other.cell_number
        return f'результат умножения 2х клеток: {result}'

    def __truediv__(self, other):
        result = self.cell_number // other.cell_number
        return f'результат деления 2х клеток: {result}'

    def make_order(self, n_line):
        line_number = self.cell_number // n_line
        line_residue = self.cell_number % n_line
        i = 1
        result_line = ''
        while i <= line_number:
            result_line = result_line + "*" * n_line + "\n"
            i += 1
        print(f'возврат строки:\n{result_line + "*" * line_residue}')


c_1 = Cell(15)
c_2 = Cell(3)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
c_1.make_order(4)
