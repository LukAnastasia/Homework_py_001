# Задача 3
# Задать список из n чисел последовательности (1 + 1/n)^n 
# и вывести на экран их сумму.

n = int(input('Введите число N: '))
res = list()
for i in range(1, n + 1):
    res.append (round((1 + 1 / i) ** i, 2))
print(res)
print(sum(res))
