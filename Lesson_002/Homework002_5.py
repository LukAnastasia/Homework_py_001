# Задача 5
# Реализовать алгоритм перемешивания списка.

from random import randrange

num = int(input('Введите число: '))
res_1 = list(range(num))
res_2 = res_1.copy()
for i in range(num):
    num_1 = randrange(num)
    num_2 = randrange(num)
    res_2[num_1], res_2[num_2] = res_2[num_2], res_2[num_1]
print(res_1)
print(res_2)
