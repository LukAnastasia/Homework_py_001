# Задача 2.
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?

    # a) Добавьте игру против бота
    # b) Подумайте как наделить бота "интеллектом"

from random import randint

def input_dat(name):
    x = int(input(f"{name}, сколько конфет вы возьмете, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, candies):
    print(f"Игрок {name} забрал {k} конфет, теперь у него {counter}. На столе осталось {candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
candies = int(input("Введите общее количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первый ходит игрок: {player1}")
else:
    print(f"Первый ходит игрок: {player2}")

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
        k = input_dat(player2)
        counter2 += k
        candies -= k
        flag = True
        p_print(player2, k, counter2, candies)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")



# import random

# def take_candies(player:str, candies:int):
#     max_candies = 28
#     if candies < 28:
#         max_candies = candies
#     n_candies: int = 0
#     while True:
#         n_candies = int(input(f'игрок {player}, возьмите конфеты (от 1 до {max_candies}): '))
#         if 0 < n_candies <= max_candies:
#             break
#     candies -= n_candies
#     print(f'игрок {player} взял {n_candies} конфет')
#     if candies == 0:
#         print(f'игрок {player} победил!')
#     return candies


# def game_two_players():
#     candies = 121
#     print('Правила:\nНа столе лежит 2021 конфета.'
#           ' Играют два игрока делая ход друг после друга.\n'
#           ' Первый ход определяется жеребьёвкой.\n'
#           ' За один ход можно забрать не более чем 28 конфет.')
#     player_1 = input('Введите имя первого игрока: ')
#     player_2 = input('Введите имя второго игрока: ')

#     player = random.choice((player_1, player_2))
#     print(f'Первым ходит игрок {player}')
#     player_dict = {1: player}
#     if player == player_1:
#         player_dict[-1] = player_2
#     else:
#         player_dict[-1] = player_1
#     # print(player_dict)
#     # print(player_dict.get(1))
#     count = 1
#     while candies > 0:
#         candies = take_candies(player, candies)
#         print(f'на столе осталось {candies}')
#         count *= -1
#         player = player_dict.get(count)


# def func():
#     print('func from candy.py')
#     print(__name__)


# if __name__ == '__main__':
#     user_choise = input('Выберите вариант 1 - два игрока, 2 - игра с ботом, q - для выхода: ')
#     if user_choise == '1':
#         game_two_players()
#     # elif user_choise == '2':
#     #     game_with_bot()
#     elif user_choise == 'q':
#         exit()
