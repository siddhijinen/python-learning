from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")

is_race_on = False
screen.setup(width=800, height=600)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-380, -210 + (colors.index(color)) * 70)
    new_turtle.shapesize(2)
    # turtle_name = color + "_turtle"
    all_turtles.append(new_turtle)

timmy_the_host = Turtle()
timmy_the_host.shape("turtle")
timmy_the_host.color("white")
timmy_the_host.penup()
timmy_the_host.goto(380, -300)
timmy_the_host.shape("square")
timmy_the_host.shapesize(0.4)

timmy_the_host.goto(380, -280)
timmy_the_host.speed("fastest")
for y in range(-280, 310, 20):
    timmy_the_host.goto(380, y)
    timmy_the_host.stamp()
for y in range(-290, 310, 20):
    timmy_the_host.goto(370, y)
    timmy_the_host.stamp()
for y in range(-280, 310, 20):
    timmy_the_host.goto(360, y)
    timmy_the_host.stamp()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 375:
            winner = turtle.pencolor()
            if user_bet == turtle.pencolor():
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")
            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
