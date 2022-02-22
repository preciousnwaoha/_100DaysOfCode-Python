from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, color="green", shape="circle"):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
