from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#ffea00")  # Bright Yellow Ball
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.refresh()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def refresh(self):
        self.goto(0, 0)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
