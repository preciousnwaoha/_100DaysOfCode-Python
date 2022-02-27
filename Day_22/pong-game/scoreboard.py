
from turtle import Turtle


ALIGNMENT = "center"

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

        

    def update_scoreboard(self):
        self.write(f"{self.name}: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, text):
        self.goto(0, 50)
        self.write(f"{text}", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()
    
    