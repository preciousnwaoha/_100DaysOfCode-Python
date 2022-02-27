from turtle import Turtle

from matplotlib.pyplot import draw
from numpy import half


class MidLine(Turtle):

    def __init__(self, height):
        super().__init__()
        self.height = height
        self.draw_line(self.height)
    

    def draw_line(self, height):
        half_of_height = height/2
        y_cor = half_of_height * -1
        
        while y_cor < half_of_height + 20:
            line_part = Turtle("square")
            line_part.turtlesize(stretch_wid=0.5, stretch_len=0.2)
            line_part.color("white")
            line_part.penup()
            line_part.goto(0, y_cor)
            y_cor += 20
