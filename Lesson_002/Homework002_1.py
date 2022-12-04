# Задача 1
# Подсчитать сумму цифр в вещественном числе.

input_num = input('Введите число: ')
res_sum = 0
for i in input_num:
    if i.isdigit():
        res_sum += int(i)
print(res_sum)


