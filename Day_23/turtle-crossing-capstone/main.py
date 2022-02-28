from turtle import Screen

from player import Player
from car import Car
from level import Level
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#fafafa")
screen.tracer(0)

level = Level((-320, 260))
turtle = Player()
car = Car()



screen.listen()
screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")
screen.onkey(turtle.go_left, "Left")
screen.onkey(turtle.go_right, "Right")

game_is_on = True
distance = 1
while game_is_on:
    time.sleep(0.1)
    car.move()

    if distance % 3 == 0:
        car.create_car()

    if turtle.ycor() > 280:
        level.increase_level()
        turtle.reset_position()
    
    screen.update()

    distance += 1

screen.exitonclick()