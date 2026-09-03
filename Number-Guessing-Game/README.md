# Number Guessing Game 🎯

A classic command-line Number Guessing Game built with Python. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The game randomly selects a secret number between 1 and 100. Your goal is to narrow down the possibilities and guess the correct number before you completely run out of attempts!

## Features

* **Dynamic Difficulty Modes:** Offers two distinct gameplay modes—"Easy" with 10 attempts and "Hard" with 5 attempts.
* **Intuitive Hot/Cold Feedback:** Provides clear "Too High!" or "Too Low!" guidance after every incorrect guess to help you adjust your strategy.
* **Live Attempt Counter:** Displays your remaining attempts in real-time so you always know how close you are to the limit.
* **Replayable Loop:** Prompts you to start a brand new game instantly once a round ends, picking a completely new random number.
* **Zero Dependencies:** Fully self-contained inside a single file with embedded title ASCII art—no package installations required!

## How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python number-guessing.py

```

## How to Play

1. Choose your difficulty by typing `easy` or `hard` when prompted.
2. Enter your numeric guess between 1 and 100.
3. Read the feedback to see if your guess was higher or lower than the secret number.
4. Keep guessing based on the clues until you find the answer or exhaust your attempts.
5. Win the game by matching the hidden number, or lose if your remaining attempts hit 0!

## Built With

* **Python 3** - Built using standard library utilities like the `random` module for number generation.
* **ASCII Art** - Embedded cleanly for styled terminal visual output.
