# Задача 7.
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            left = not(x or y or z)
            right = not x and not y and not z
            # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
            print(f'x = {x}, y = {y}, {z = }')
            print(left == right)