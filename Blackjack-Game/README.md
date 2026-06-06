# Blackjack Game 🃏

A command-line Python application that simulates a classic game of Blackjack between a player and a computer dealer. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program handles the logic of card dealing, score tracking, and the specific house rules of Blackjack, providing a realistic casino-style experience in the terminal.

## ✨ Features

* **Flexible Ace Logic:** Automatically detects if a player busts and converts an Ace from 11 to 1 to keep the game alive.
* **Automated Dealer AI:** The computer follows professional rules, automatically hitting until it reaches a score of at least 17.
* **Instant Win Detection:** Checks for natural Blackjacks immediately after the initial deal to award instant victories.
* **Clean User Interface:** Utilizes screen clearing to keep the game loop focused and displays an ASCII art logo for styling.

## 🚀 How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python blackjack.py

```

## 🎮 How to Play

1. Type 'y' to start a new game and receive your first two cards.
2. View your total score and the dealer's first card.
3. Type 'y' to **Hit** (take another card) or 'n' to **Stand** (keep your current score).
4. Watch the dealer play out their hand and see if you won, lost, or tied!

## 🧠 Things Learnt

* **Function Outputs & Return Values:** Mastered using return statements to pass game states and boolean flags between logic checks.
* **List Manipulation:** Used `.append()` to manage hands and `.index()` to locate and modify specific cards like Aces.
* **Recursive Logic:** Implemented recursive function calls to re-evaluate hand conditions after a card value (Ace) has been changed.
* **Complex Conditionals:** Managed multiple win/loss scenarios including busts, blackjacks, and ties using nested `if/elif/else` logic.

## 🛠️ Built With

* **Python 3** - Pure standard library implementation.
* **Random Module** - Utilized for fair and randomized card dealing.
* **ASCII Art** - Embedded for a stylized terminal visual experience.
