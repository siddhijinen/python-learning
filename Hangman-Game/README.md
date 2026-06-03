# Hangman Game 🎮

A classic, text-based Hangman game built using Python. The game randomly selects a secret word, and the player tries to guess it one letter at a time before running out of lives.

---

## 🚀 Features

* Random Word Selection:** Chooses a random word from a built-in list (`sunflower`, `ocean`, `pasta`, `bookstore`).
* Visual Hangman Stages:** Displays classic ASCII art of the hangman that updates dynamically with every wrong guess.
* Live Tracking:** Displays your remaining lives, correct guesses, and incorrect letters after each turn.

---

## 🛠️ How It Works

1. The game sets up 6 lives for the player.
2. At each turn, you are prompted to guess a single letter.
3. If the letter is in the word, it reveals its position(s).
4. If the letter is incorrect, you lose a life, and a piece of the hangman is drawn.
5. The game ends when you either reveal the whole word (**Win**) or run out of lives (Lose).

---

## 📋 Prerequisites

To run this game, you just need Python 3 installed on your machine. No external libraries are required!

---

## 🏃 How to Run

1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `hangman.py`.
4. Run the following command:

```bash
python hangman.py
