from turtle import Screen

from player import Player
from car import Car
from level import Level
from highscore import HighScore
import time
import random



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#fafafa")
screen.tracer(0)

high_score = HighScore((280, 260))
level = Level((-320, 260))
player = Player()
car_manager = Car()



screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    car_manager.create_car()

    # Detect a successful crossing
    if player.ycor() > 280:
        level.increase_level()
        player.reset_position()
        car_manager.speed_up()
        high_score.check_high_score(level)

    # Detect playe-car collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
    
    screen.update()


screen.exitonclick()