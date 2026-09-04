# Spirograph Generator 🌀

A Python application that uses the `turtle` graphics module to generate a colorful, geometric spirograph pattern. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program repeatedly draws circles of fixed radius while rotating a small angle after each iteration, picking fully randomized RGB colors to create an overlapping geometric artwork on a dark canvas.

<img width="847" height="861" alt="Screenshot 2026-09-04 at 15 02 29" src="https://github.com/user-attachments/assets/1f1cdd13-e3db-4c37-9d33-c6ed75d8ad3e" />

## Features

* **Randomized RGB Colors:** Generates vibrant, multi-colored circles using dynamic 24-bit RGB values `(r, g, b)`.
* **Precision Geometric Angles:** Calculates exact circle iterations using angular steps (`360 // turn_angle`) to complete a seamless 360-degree rotation.
* **Sleek Dark Canvas:** Configures a high-contrast black background (`"black"`) with maximum drawing speed (`"fastest"`) for instant visual rendering.
* **Interactive Screen Exit:** Keeps the graphic window open until clicked by the user.

## Prerequisites & Installation

Make sure you have **Python 3** installed on your computer. 

The `turtle` and `random` modules are included in standard Python installations, so no additional `pip` installs are required!

*Note: On Linux systems, you may need to install `python3-tk` if Turtle graphics windows fail to open:*
```bash
sudo apt-get install python3-tk
