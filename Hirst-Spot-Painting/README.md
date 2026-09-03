# Hirst Painting Generator 🎨

A Python application that uses the `turtle` graphics module to generate a Damien Hirst-inspired spot painting. This project is part of the *100 Days of Code: The Complete Python Pro Bootcamp*.

The program draws a 10x10 grid of colored filled dots on a dark canvas, picking RGB color tuples extracted from an image artwork palette.

## ✨ Features

* **Image Color Extraction:** Utilizes commented setup code using `colorgram.py` to extract RGB color palettes from local image files.
* **Turtle Graphics Grid:** Draws a precise 10x10 array of filled circular dots with uniform grid spacing using nested loops.
* **Dynamic Color Selection:** Randomly samples RGB tuples on the fly to render unique color combinations across the canvas.
* **Canvas Styling:** Customizes background presentation to dark mode (`"black"`) and maximizes render speed (`"fastest"`).

## 📋 Prerequisites & Package Installation

Make sure you have **Python 3** installed. 

While `turtle` and `random` are included in standard Python installations, you may need to install external packages if you plan to extract colors from your own images or if your Python environment doesn't include GUI components.

Run the following in your terminal:

```bash
pip install colorgram.py
