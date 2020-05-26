class Matrix:
    def __init__(self, data):
        self.data = data

# первая часть задания
    def __str__(self):
        result_line = str()
        for el in self.data:
            line_name = str()
            for el_int in el:
                line_name = line_name + str(el_int) + ' '
            result_line = result_line + line_name + '\n'
        return result_line

# 2ая часть задания
    def __add__(self, other):
        result_sum = []
        for el in range(0, len(self.data)):
            result_sum_int = []
            for el_int in range(0, len(self.data[el])):
                result_el = self.data[el][el_int] + other.data[el][el_int]
                result_sum_int.append(result_el)
            result_sum.append(result_sum_int)
        return result_sum


m_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(f"исходная матрица (1ая часть задания):\n{m_1}")
m_2 = Matrix([[0, 3, 5], [2, 5, 8], [-2, -3, 2]])
m_sum = Matrix(m_1 + m_2)
print(f"суммарная матрица (2ая часть задания):\n{m_sum}")

