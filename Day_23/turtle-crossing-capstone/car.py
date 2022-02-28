from turtle import Turtle
import random

COLORS = ["blue", "green", "red", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car():
    
    def __init__(self):
        super().__init__()
        self.cars = []


    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=1.5)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        y_cor = random.randint(-280, 280)
        new_car.goto(380, y_cor)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            x_cor = car.xcor() - 10
            car.goto(x_cor, car.ycor())