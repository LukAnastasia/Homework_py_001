# Задача 9 
# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат
# для точек этой четверти.

a = input('Введите номер четверти: ')
if a == '1':
    print('x > 0, y > 0')
import math
ax = float(input('Введите координату x точки А: '))
ay = float(input('Введите координату y точки А: '))
bx = float(input('Введите координату x точки Б: '))
by = float(input('Введите координату y точки Б: '))
l = ((ax - bx)**2 + (ay - by)**2)**0.5
# l = math.sqrt((ax - bx)**2 + (ay - by)**2)
print(round(l, 3))