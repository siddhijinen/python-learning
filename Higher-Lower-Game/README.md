# Higher Lower Game ↕️

A command-line Python application that challenges players to guess which celebrity or public figure has more social media followers. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program draws comparison data from an external dataset, manages a continuous score streak, and swaps competitors dynamically as long as you keep guessing correctly.

## Features

* **Data-Driven Comparison:** Dynamically unpacks dictionary records to display a clean overview of each person's name, description, and country.
* **Smart Duplicate Prevention:** Uses a tracking list to ensure you never face a competitor you have already encountered in the current round.
* **Seamless Turn Progression:** When you guess correctly, Competitor B automatically shifts into the Competitor A slot for the next round.
* **Persistent Scoring & Replays:** Tracks your consecutive score streak in real-time and clears the screen between turns to keep the interface tidy.
* **Modular Code Structure:** Seamlessly imports stylized ASCII game assets and external dictionaries from separate source files.

## How to Run

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open your terminal or VS Code terminal in the project directory.
4. Run the script using the following command:

```bash
python higher-lower.py

```

## How to Play

1. Read the profiles for Compare A and Against B.
2. Type `A` or `B` to lock in your guess on who has the higher follower count.
3. A correct guess increments your score and brings up a new opponent to challenge.
4. An incorrect guess ends your streak immediately and displays your final score.
5. Type `y` at the final prompt if you want to wipe the slate clean and restart.

## Built With

* **Python 3** - Pure standard library implementation.
* **Random Module** - Used to shuffle and grab random choices from the game dataset.
* **Custom Modules** - Modularly imports UI graphics (`art.py`) and profile information (`game_data.py`).
