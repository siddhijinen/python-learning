from turtle import Turtle, Screen, listen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
screen.listen()

food = Food()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

#collision with wall
    if snake.head.xcor() < -380 or snake.head.xcor() > 380 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        print("collision with wall. game over.")
        scoreboard.game_over()
        game_is_on = False

#collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            print("collision with tail. game over.")
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
