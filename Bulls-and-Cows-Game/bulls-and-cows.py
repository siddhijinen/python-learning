import random

def generate_number(samples):
    """generates a random number with no duplicates"""
    return random.sample(range(10), samples)

def check_answer(guess, ans):
    """checks the guess against the pregenerated answer"""
    bulls, cows = 0, 0

    for i in range(len(guess)):
        if guess[i] == ans[i]:
            bulls += 1
        elif guess[i] in ans:
            cows += 1
    if bulls == len_of_ans:
        print("You Win!!")
    else: print(f"{bulls} A (Bulls) {cows} B (Cows)")

    return bulls

def get_guess(level):
    """gets guess from user and ensure the user guesses 4 unique digits"""
    while True:
        guess = input(f"Please input {level} digits:  ")
        
        if len(guess) != level or not guess.isdigit():
            print(f"Guess must be exactly {level} digits! Try again.") 
            continue

        guess_list = [int(digit) for digit in guess]

        if len(set(guess_list)) != level:
            print("No duplicate digits allowed! Try again.")
            continue
            
        return guess_list 
    
def choose_difficulty():
    while True:
        levels = {"easy": (3,12), "medium": (4, 10), "hard": (5, 8)}
        level_chosen = input("Choose a level (easy/medium/hard): ").lower()
        if level_chosen not in levels:
            continue
        return levels[level_chosen]

game_on = True
level = choose_difficulty()
level[0] = len_of_ans
level[1] = no_of_attempts
ans_list = generate_number(len_of_ans)
print(f"You have {no_of_attempts} guesses!")
attempts = 0
while game_on:
    guess_list = get_guess(len_of_ans)
    correct = check_answer(guess_list, ans_list)
    attempts += 1
    if correct == len_of_ans:
        game_on = False
    elif attempts == no_of_attempts:
        print("You lost!")
        print(f"The correct target was {int("".join([str(num) for num in ans_list]))}")
        game_on = False
print(f"Attempts: {attempts}")
