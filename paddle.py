from turtle import Turtle
PLAYERS = []

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # 100px tall, 20px wide
        self.color("white")
        self.speed("fastest")
        if len(PLAYERS) == 0:
            self.goto(-350, 0)
            self.color("#00f3ff") # Neon Cyan for Left Player
            PLAYERS.append(self)
        else:
            self.goto(350, 0)
            self.color("#ff007f")  # Hot Pink for Right Computer

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)

    def auto_move(self, ball_y, ball_x_move):
        if ball_x_move > 0:
            # Move up if the ball is above the paddle
            if self.ycor() < ball_y and self.ycor() < 240:
                self.goto(self.xcor(), self.ycor() + 3)
            # Move down if the ball is below the paddle
            elif self.ycor() > ball_y and self.ycor() > -240:
                self.goto(self.xcor(), self.ycor() - 3)