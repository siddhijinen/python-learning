# Calculator 🧮

A command-line Python application that performs fundamental arithmetic operations. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program utilizes a dynamic dictionary-based function mapping system to process calculations continuously, allowing you to chain mathematical operations together using previous results.

## Features

* **Core Arithmetic:** Supports standard addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Chained Calculations:** Choose to carry forward your previous result into a brand new math operation seamlessly.
* **Zero-Division Safety:** Gracefully catches attempts to divide by zero, displaying an error message instead of crashing the program.
* **Dynamic Function Mapping:** Uses a clean dictionary structure to route user inputs directly to mathematical functions.
* **Zero Dependencies:** Fully self-contained inside a single file with an embedded retro-style ASCII calculator logo—no external package installations required!

## How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python calculator.py
```

## How to Play

1. Input your first numeric value (decimals are supported!).
2. Choose an operation from the menu (+, -, *, /).
3. Enter your second numeric value to view your result instantly.
4. Choose your next step when prompted:
    *Type y to continue calculations using your current result.
    *Type n to clear the memory and start fresh with a new number.
    *Type x to cleanly exit the application.

## Built With

* **Python 3** - Pure standard library implementation.
* **Dictionaries & First-Class Functions** - Leveraged to map operator symbols straight to functional math blocks.
* **ASCII Art** - Embedded cleanly for styled terminal visual output.
