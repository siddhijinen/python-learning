import random

def generate_number():
    """generates a random number with no duplicates"""
    return random.sample(range(10),4)

def check_answer(guess, ans):
    """checks the guess against the pregenerated answer"""
    bulls, cows = 0, 0

    for i in range(len(guess)):
        if guess[i] == ans[i]:
            bulls += 1
        elif guess[i] in ans:
            cows += 1
    if bulls == 4:
        print("You Win!!")
    else: print(f"{bulls} A (Bulls) {cows} B (Cows)")
    
    return bulls

def get_guess():
    """gets guess from user and ensure the user guesses 4 unique digits"""
    while True:
        guess = input("Please input 4 digits:  ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Guess must be exactly 4 digits! Try again.") 
            continue

        guess_list = [int(digit) for digit in guess]

        if len(set(guess_list)) != 4:
            print("No duplicate digits allowed! Try again.")
            continue
            
        return guess_list 


game_on = True
ans_list = generate_number()
print(ans_list)
# ans_list = [int(digit) for digit in str(ans)]
attempts = 0
while game_on:
    guess_list = get_guess()
    correct = check_answer(guess_list, ans_list)
    attempts += 1
    if correct == 4:
        game_on = False

print(f"Attempts: {attempts}")