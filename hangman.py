import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["sunflower","ocean","pasta","bookstore"]
chosen_word = random.choice(word_list)
no_of_blanks = len(chosen_word)

game_over = False

correct_letters = set()
incorrect_letters = set()
lives = 0

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.add(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        if not guess in chosen_word:
            incorrect_letters.add(guess)
            lives = len(incorrect_letters)
            if lives == 6:
                game_over = True
    if not "_" in display:
        game_over = True
    print(stages[6-lives])
    print(display)
    print("lives: ", 6-lives)
    print("incorrect: ", incorrect_letters)
    print("correct: ",correct_letters)

if lives == 6:
    print("You lost...")
else:
    print("You got it!")
    
print("The word was: ", chosen_word)
