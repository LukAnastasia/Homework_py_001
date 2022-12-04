# Задача 4
# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список 
# (например: positions = [1, 3, 6]).

import random
positions = [1, 3, 6]
n = int(input('Введите целое число: '))
list_numbers = []
for i in range(n):
    list_numbers.append(random.randint(-n, n))
print(list_numbers)
mult_num = 1
for i in positions:
    if i <= len(list_numbers):
        mult_num *= list_numbers[i - 1]
print(mult_num)