from turtle import Turtle
FONT = "Georgia"
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("#ffffa8")
        self.hideturtle()
        self.penup()
        self.draw_line()

        self.h_score = 0
        self.c_score = 0
        self.draw_score()

    def draw_line(self):
        # Draw partition once upon initialization
        divider = Turtle()
        divider.color("#332244")  # Subtle Dark Purple Center Line
        divider.hideturtle()
        divider.penup()
        divider.goto(0, -300)
        divider.setheading(90)
        while divider.ycor() < 300:
            divider.pendown()
            divider.forward(10)
            divider.penup()
            divider.forward(10)

    def draw_score(self):
        self.clear()
        # Draw Left Score
        self.goto(-100, 200)
        self.write(self.h_score, align=ALIGNMENT, font=(FONT, 50, "normal"))
        # Draw Right Score
        self.goto(100, 200)
        self.write(self.c_score, align=ALIGNMENT, font=(FONT, 50, "normal"))
