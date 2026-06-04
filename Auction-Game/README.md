# Blind Auction 🔨

A command-line Python application that manages a secret bidding process and automatically determines a winner. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program collects names and secret bids from multiple users, clearing the screen dynamically between turns to keep all offers completely hidden until the auction closes.

## ✨ Features

* **Secret Bidding Process:** Keeps bids private by printing blank spacing to hide entries from the next user.
* **Winner Calculation:** Automatically evaluates all records at the end to declare the highest bidder and their winning amount.
* **Dynamic Loop Execution:** Seamlessly accepts an unlimited number of participants until the host explicitly closes the auction.
* **Zero Dependencies:** Fully self-contained inside a single file with embedded ASCII art—no external package installations required!

## 🚀 How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python blind-auction.py

## 🎮 How to Play
Input your name when prompted by the terminal.

Enter the numeric amount you are willing to bid.

Type yes if there are more participants to clear the screen, or no to close the bidding.

View the final winner and their winning bid instantly!

🧠 Things Learnt
Python Dictionaries: Learned how to store key-value pairs (name: amount) to dynamically collect user data.

While Loops & Flags: Utilized boolean flags (auction_active) to cleanly control game states and loop iterations.

Dictionary Iteration: Learned how to loop through a dictionary to compare values and extract the maximum bid.

Type Casting: Practiced converting standard string inputs into integers (int()) to perform numerical comparisons.

🛠️ Built With
Python 3 - Pure standard library implementation.

ASCII Art - Embedded cleanly for styled terminal visual output.
