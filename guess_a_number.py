import random

play_game = True
level = 1  # Set a level to increase difficulty if player guesses the number.
tries = 5  # Set initial number of tries for level 1.
tries_left = tries
print(f"Level {level}")

while play_game:
    rand_num = random.randint(1, 100)  # Assign a random number to a variable.
    try_counter = 0  # Add a counter to limit the number of failed tries.

    while True:
        tries_left = tries - try_counter
        try_counter += 1
        player_inp = input(f"Guess the number (1-100). {tries_left} tries left: ")

        if not player_inp.isdigit():  # Error message if player input is not a digit.
            print("Invalid input (1-100 numbers only). Try again... ")
            continue

        player_num = int(player_inp)  # Convert player input to number.

        if player_num == rand_num:  # First case: if player number is correct.
            print(f"You guessed it! Number {player_num} is correct. Great! :)")
            if level == 3:
                print("Congratulations! You won the game!")
                play_game = False
                break
            else:
                level += 1
                print(f"Level {level}")
                try_counter = 0
                tries -= 1
                break
        elif player_num > rand_num:  # Second case: if player number is too high.
            print(f"Number {player_num} is too high! :( \n")
        else:
            print(f"Number {player_num} is too low! :( \n")  # Third case: if player number is too low.

        if try_counter == tries:  # Limit the number of tries
            print("No more tries, sorry! :( \n")
            new_game = input("One more game? (Y): ").lower()  # Ask the player for a new game.

            if new_game == "y":  # Reset the try counter and restart the game if player agrees.
                try_counter = 0
                level = 1
                tries = 5
                break
            else:  # Goodbye message and exit game if player doesn't agree.
                print("See you next time. Bye! :)")
                play_game = False
                break
