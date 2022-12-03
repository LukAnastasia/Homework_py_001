# Задача 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# не решила

size = 5
first = 1
last = 9
from random import randint
import math
def get_numbers(size, first, last):
    return [randint(first, last) for i in range(size)]


    
my_list = get_numbers(size, first, last)
print(my_list)
