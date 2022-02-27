from turtle import Turtle


ALIGNMENT = "center"

FONT = ("Courier", 16, "bold")


class LifeBar(Turtle):

    def __init__(self, lifes, position):
        super().__init__()
        self.lifes_left = lifes
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_lifes()
    
    def update_lifes(self):
        self.write(f"Lifes: {self.lifes_left}", align=ALIGNMENT, font=FONT)


    def decrease_life(self):
        self.lifes_left -= 1
        self.clear()
        self.update_lifes()