# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите число: '))
def convert_dec_to_bin(n):
    bin_num = []
    while n >= 1:
        bin_num.insert(0, n % 2)
        n = n // 2
    return bin_num
print(convert_dec_to_bin(n))
