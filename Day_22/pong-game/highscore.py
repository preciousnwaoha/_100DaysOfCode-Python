from turtle import Turtle

import shelve


ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class HighScore(Turtle):

    def __init__(self, position):
        super().__init__()
        # High score should never be reset.
        d = shelve.open('high_score')
        if d:
            self.high_score = d['high_score']
        else:
            d['high_score'] = 0 
            self.high_score = d['high_score']
        d.close()
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_high_score()

    
    def update_high_score(self):
        self.write(f"HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def check_high_score(self, sb):
        """Check to see if there's a new high score."""
        if sb.score > self.high_score:
            d = shelve.open('high_score')
            d['high_score'] = sb.score
            self.high_score = d['high_score']
            self.clear()
            self.update_high_score()
            d.close()