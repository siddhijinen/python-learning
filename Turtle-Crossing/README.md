# Turtle Crossing Game 🚦

A Frogger-style road crossing arcade game built in Python using the `turtle` graphics module. The game utilizes modular, object-oriented programming across separate files (`main_2.py`, `player.py`, `car_manager.py`, `scoreboard_2.py`) to handle character movement, dynamic obstacle generation, collision physics, and level progression.

Players guide a turtle safely across a busy screen filled with moving cars to reach the finish line, advancing through increasingly difficult speed levels.

## Features

* **Modular OOP Design:** Structured across distinct classes (`Player`, `CarManager`, `Scoreboard`) for clear separation of game logic, movement, and UI.

* **Dynamic Traffic Generation:** Spawns colorful cars at randomized intervals and lane coordinates while cleaning up off-screen objects to optimize performance.

* **Progressive Difficulty Scaling:** Increases car movement speed each time the player successfully crosses the top finish line.

* **Collision Physics & Level Tracking:** Checks distance thresholds between player and vehicle instances, resetting state and displaying a high-contrast level indicator.

## How to Play

1. Execute the main program file:
   ```bash
   python main_2.py
   ```
2. Press the **Up** arrow key to step the turtle forward across the road.
3. Dodge incoming cars and reach the top boundary ($y > 280$) to advance to the next level.

## Prerequisites & Installation

Make sure you have **Python 3** installed on your computer.

The `turtle`, `random`, and `time` modules are included in standard Python installations, so no external package installations are required!

*Note: On Linux systems, you may need to install `python3-tk` if Turtle graphics windows fail to open:*
```bash
sudo apt-get install python3-tk
```
