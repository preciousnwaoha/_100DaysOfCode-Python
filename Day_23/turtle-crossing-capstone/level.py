from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Level(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_level()


    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
        