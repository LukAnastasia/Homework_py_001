# Задача 1.Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

size = 5
first = 0
last = 9
from random import randint
def get_list(size, first, last):
    return [randint(first, last) for i in range(size)]

def sum_odd_position(my_list):
    return sum(my_list[1::2])

my_list = get_list(size, first, last)
print(my_list)
print(sum_odd_position(my_list))
