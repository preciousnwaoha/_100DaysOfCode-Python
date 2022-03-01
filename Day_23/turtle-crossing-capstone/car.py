from turtle import Turtle
import random

COLORS = ["blue", "green", "red", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car():
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=1.5)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_cor = random.randint(-280, 280)
            new_car.goto(380, y_cor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            

    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT