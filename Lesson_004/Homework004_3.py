# Задача 3.
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def new_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_value(list):
    return [i for i in set(list)]

size = 5
m = 1
n = 10

origin = new_list(size, m, n)
print(origin)
print(get_value(origin))