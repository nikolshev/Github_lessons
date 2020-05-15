def fact(n):
    for num in range(1, n + 1):
        yield num


n = int(input('введите число, факториал которого требуется '))
result = 1
for el in fact(n):
    result = result * el
print(result)
