from turtle import Turtle
ALIGN ="center"
FONT = ("Georgia", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Initialises Scoreboard"""
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("dark green")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates Score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increases Score by 1."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Ends Game and Displays Final Score"""
        self.color("red")
        self.goto(0, -20)
        self.update_scoreboard()
        self.goto(0,20)
        self.write("GAME OVER!!", align=ALIGN, font=FONT)

