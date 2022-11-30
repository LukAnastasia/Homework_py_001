# Задача 3
# Вывести на экран числа от -N до N.

print('Введите -n: ')
n_1 = int(input())
print('Введите n: ')
n_2 = int(input())
res = 0
result = []

for i in range (n_1-1, n_2):
    res = i + 1
    result.append(res)
print(f'{result}')