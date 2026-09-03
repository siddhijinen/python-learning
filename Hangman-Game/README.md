# Hangman Game 🪓

A classic command-line Hangman game built with Python. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The game randomly selects a secret word from a built-in list. Your goal is to guess the word letter by letter before your stick figure completely runs out of lives!

## Features

*   **Random Word Selection:** Automatically chooses a fresh word from a pre-defined word bank every game.
*   **Dynamic Visual Stages:** Features 7 detailed ASCII art stages representing the classic gallows.
*   **Live Stat Tracking:** Displays your remaining lives, correct letters, and incorrect guesses in real-time.
*   **Input Handling:** Smoothly reveals all matching letters simultaneously if a letter appears multiple times in a word.
*   **Zero Dependencies:** Fully self-contained inside a single file with embedded visuals—no package installations required!

## How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python main.py
```

## How to Play

1. Look at the blanks (`_`) to see how many letters are in the secret word.
2. Guess one letter at a time when prompted.
3. If your guess is correct, the letter is revealed in its proper position.
4. If your guess is wrong, you lose a life, and the gallows ASCII art advances.
5. Win the game by revealing all the letters, or lose if the stick figure gets fully drawn (6 wrong guesses)!

## Built With

*   **Python 3** - Built using standard library utilities like the `random` module.
*   **ASCII Art** - Step-by-step custom visual rendering for the gallows tracking.
