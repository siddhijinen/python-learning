import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
tim.color("white")
tim.shape("turtle")
tim.speed("fastest")

turn_angle = 4

for _ in range(360 // turn_angle): #52
    tim.color(random_color())
    tim.circle(100)
    tim.right(turn_angle)

screen.exitonclick()
