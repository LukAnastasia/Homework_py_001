# Задача 3.
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

size = 5
frst = 1
last = 9
from random import uniform
def get_numbers (size, frst, last):
    return [round(uniform(frst,last), 2) for i in range(size)]

def find_diff(my_nums):
    nums = [round(x - int(x), 2) for x in (my_nums)]
    return max(nums) - min(nums)
my_nums = get_numbers(size, frst, last)
print (my_nums)
print(find_diff(my_nums))