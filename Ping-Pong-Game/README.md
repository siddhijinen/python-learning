# Ping Pong Game 🏓

A classic arcade Pong game built in Python using the `turtle` graphics module. The application features an interactive player paddle versus an automated computer opponent, complete with collision physics and score tracking across separate modules (`main.py`, `paddle.py`, `ball.py`, `scoreboard.py`).

The game runs on an 800x600 dark canvas where players bounce a ball back and forth to score points when the opponent misses.

## Features

* **Modular OOP Architecture:** Organized cleanly across custom classes (`Paddle`, `Ball`, `Scoreboard`) for manageable object states and methods.
* **Automated AI Opponent:** Features a computer-controlled right paddle that dynamically tracks ball coordinates.
* **Collision Physics:** Handles bouncing dynamics for top/bottom wall boundaries and paddle collisions (`bounce_x`, `bounce_y`).
* **Live Scoreboard & Divider:** Draws a dashed center partition line and dynamically tracks points for both player and computer.

## How to Play

1. Execute the main program file:
   ```bash
   python main.py
   ```
2. Use the **Up/Down arrow keys** or **W/S keys** to control the left player paddle.
3. Defend your side of the screen and attempt to hit the ball past the computer paddle on the right side.

## Prerequisites & Installation

Make sure you have **Python 3** installed on your computer.

The `turtle` and `time` modules are included in standard Python installations, so no additional `pip` installs are required!

*Note: On Linux systems, you may need to install `python3-tk` if Turtle graphics windows fail to open:*
```bash
sudo apt-get install python3-tk
```
