import random

logo = r'''
   _____                        _   _             _   _                 _               _ 
  / ____|                      | | | |           | \ | |               | |             | |
 | |  __ _   _  ___  ___ ___   | |_| |__   ___   |  \| |_   _ _ __ ___ | |__   ___ _ __| |
 | | |_ | | | |/ _ \/ __/ __|  | __| '_ \ / _ \  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |__| | |_| |  __/\__ \__ \  | |_| | | |  __/  | |\  | |_| | | | | | | |_) |  __/ |  |_|
  \_____|\__,_|\___||___/___/   \__|_| |_|\___|  |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                          
'''

print(logo)

print("Welcome to the Number Guessing Game!")
play_game = True

while play_game:
    num = random.randrange(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 0

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid input. Try again\n")
        continue

    print(f"You have {attempts} attempts to guess the number. Good luck!\n")

    guessed = False

    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess == num:
            print(f"You guessed it! The answer was {num}")
            guessed = True
            break
        elif guess > num:
            print("Too High!")
        elif guess < num:
            print("Too Low!")
        if attempts > 0:
            print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.\n")

    if attempts == 0 and not guessed:
        print("You ran out of attempts.\n")
        print(f"The number was {num}")
    
    play_again = input("\nDo you want to play again? Type 'y' to play: ").lower()
    if not play_again == "y":
        play_game = False

print("Game ended.")
