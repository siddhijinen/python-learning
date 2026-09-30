from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#0d0d1a")  # Deep Navy background
screen.title("Ping Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle()
computer = Paddle()
ball = Ball()

screen.listen()

screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_up, "w")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.015)
    screen.update()
    ball.move()

    computer.auto_move(ball.ycor(), ball.x_move)

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle (computer) or left paddle (paddle)
    if (ball.distance(computer) < 50 and ball.xcor() > 320) or (ball.distance(paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right paddle missed (Left player scores)
    if ball.xcor() > 380:
        ball.refresh()
        ball.bounce_x()
        scoreboard.h_score += 1 # Increments left score
        scoreboard.draw_score()

    # Left paddle missed (Right player scores)
    if ball.xcor() < -380:
        ball.refresh()
        ball.bounce_x()
        scoreboard.c_score += 1
        scoreboard.draw_score()

screen.exitonclick()