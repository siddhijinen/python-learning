# Coffee Machine Program ☕

A command-line Python application that simulates a digital vending coffee machine. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program manages a real-time inventory of physical resources (water, milk, coffee beans) and calculates financial coin transactions to dispense espresso, lattes, or cappuccinos while handling change distribution.

## Features

* **Resource Management:** Tracks available ingredients dynamically and blocks orders if any item falls below the required threshold for a recipe.
* **Coin Processing System:** Accepts manual values for quarters, dimes, nickels, and pennies, automatically computing the total currency value.
* **Dynamic Cost & Change Ledger:** Evaluates transaction totals to ensure sufficient funds, issues exact change for overpayments, and securely builds up profit balances.
* **Administrative Controls:** Hidden maintenance triggers like `report` reveal structural ingredient levels, while `off` shuts down the game loop gracefully.
* **Zero Dependencies:** Fully self-contained inside a single file utilizing foundational data structures—no package installations required!

## How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python coffee-machine.py

```

## How to Play

1. Type `y` at the initial prompt to flip the master power switch on.
2. Select your beverage of choice by typing `espresso`, `latte`, or `cappuccino`.
3. Input the quantities of coins requested to complete your financial purchase.
4. Monitor resource capacities at any time by typing `report` into the choice selection prompt.
5. Safely turn off the machine by entering `off` to terminate operational routines.

## Built With

* **Python 3** - Pure standard library implementation.
* **Nested Dictionaries** - Employed to cleanly map ingredient data requirements, recipe compositions, and pricing levels.
* **Exception Handling** - Leveraged `try/except` safeguards to prevent execution crashes when filtering improper coin values.
