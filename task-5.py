from functools import reduce

def comp(prev, new_el):
    return prev * new_el

gener_list = [el for el in range(100, 1001) if el % 2 == 0]
print('сгенерированный список ', gener_list)
print('произведение ',reduce(comp, gener_list))
