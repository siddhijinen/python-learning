# Snake Game

A classic Snake game built in Python using the `turtle` graphics module. The application uses object-oriented programming to structure game elements across separate modules (`main.py`, `snake.py`, `food.py`, `scoreboard.py`).

The player controls a snake on an 800x600 dark canvas, eating food to grow and gain points while avoiding collisions with the boundary walls and the snake's own tail.

## Features

* **Modular Structure:** Built using Object-Oriented Programming (OOP) principles split across distinct classes (`Snake`, `Food`, `Scoreboard`).
* **Smooth Rendering:** Utilizes `screen.tracer(0)` and manual screen updates for seamless movement animations without visual flicker.
* **Collision Detection:** Accurate distance checking for food consumption, wall boundaries, and tail self-collisions.
* **Score Tracking:** Dynamically updates your current score and displays a "Game Over" message upon collision.

## How to Play

1. Run the main script to start the game:
```bash
python main.py
```
2. Use the arrow keys (**Up**, **Down**, **Left**, **Right**) on your keyboard to navigate the snake.
3. Collect food to grow longer and score points. The game ends if you collide with a wall or your own tail.

## Prerequisites & Installation

Make sure you have **Python 3** installed on your computer. 

The `turtle` and `time` modules are included in standard Python installations, so no additional `pip` installs are required!

*Note: On Linux systems, you may need to install `python3-tk` if Turtle graphics windows fail to open:*
```bash
sudo apt-get install python3-tk
```