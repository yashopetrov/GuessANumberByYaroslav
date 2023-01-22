import random

rand_num = random.randint(1, 100)

while True:
    player_inp = input("Guess the number (1-100): ")

    if not player_inp.isdigit():
        print("Invalid input (1-100 numbers only). Try again... ")
        continue

    player_num = int(player_inp)

    if player_num == rand_num:
        print(f"You guessed it! Number {player_num} is correct. Great! :)")
        break
    elif player_num > rand_num:
        print(f"Number {player_num} is too high! Sorry! :(")
    else:
        print(f"Number {player_num} is too low! Sorry! :(")
