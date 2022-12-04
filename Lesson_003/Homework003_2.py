# Задача 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


from random import randint
size = 6
first = 1
last = 9
def get_numbers(size, first, last):
    return [randint(first, last) for i in range(size)]
my_list = get_numbers(size, first, last)
res_list = []
for i in range((len(my_list)+ 1) // 2):
    res_list.append(my_list[i] * my_list[-1 - i])
print(my_list)
print(res_list)
