# Задача 10
# Найти расстояние между двумя точками пространства.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Введите координату Х1: '))
y1 = float(input('Введите координату У1: '))
x2 = float(input('Введите координату Х2: '))
y2 = float(input('Введите координату У2: '))
distence = (((x2-x1)**2)+((y2-y1)**2))**0.5
print (round(distence, 2))