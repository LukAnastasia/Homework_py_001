# a. вариант человек против бота:

from random import randint

def input_dat(name):
    x = int(input(f"{name}, сколько конфет вы возьмете, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Игрок {name} забрал {k} конфет, теперь у него {counter}. На столе осталось {candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
candies = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while candies > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        candies -= k
        flag = False
        p_print(player1, k, counter1, candies)
    else:
        k = randint(1,29)
        counter2 += k
        candies -= k
        flag = True
        p_print(player2, k, counter2, candies)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")