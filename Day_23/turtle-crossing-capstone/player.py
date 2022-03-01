from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        y_cor = self.ycor() + 10
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        if self.ycor() > -280:
            y_cor = self.ycor() - 10
            self.goto(self.xcor(), y_cor)

    def go_right(self):
        if self.xcor() < 350:
            x_cor = self.xcor() + 10
            self.goto(x_cor, self.ycor())
    
    def go_left(self):
        if self.xcor() > -350:
            x_cor = self.xcor() - 10
            self.goto(x_cor, self.ycor())


    def reset_position(self):
        self.goto(0, -280)