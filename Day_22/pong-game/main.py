from turtle import Screen

from midline import MidLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from highscore import HighScore
from lifebar import LifeBar
import time


screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.bgcolor((0, 0, 10))
screen.setup(width=800, height=600)
screen.title("Pong")

screen.update()

allowed__no_of_players = ["1","2"]
no_of_players = screen.textinput(title="Choose", prompt="How many players (1 or 2)")


while no_of_players not in allowed__no_of_players:
    no_of_players = screen.textinput(title="Choose", prompt="How many players (1 or 2)")

no_of_players = int(no_of_players)

if no_of_players == 1:
    life_bar = LifeBar(3, (300, 270))
    scoreboard = Scoreboard("Score", (0, 250))
    high_score = HighScore((-280, 270))
else:
    mid_line = MidLine(600)
    r_scoreboard = Scoreboard("Right", (300, 250))
    l_scoreboard = Scoreboard("Left", (-300, 250))


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
    
game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if no_of_players == 1:
            scoreboard.increase_score()
            high_score.check_high_score(scoreboard)



    if no_of_players == 1:
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.reset_position()
            life_bar.decrease_life()
            if life_bar.lifes_left < 1:
                scoreboard.game_over("")
                game_is_on = False
    else:
        # Detect L paddle miss
        if ball.xcor() > 380:
            l_scoreboard.increase_score()
            ball.reset_position()
            if l_scoreboard.score == 100:
                l_scoreboard.game_over("Left Player Win!")
                game_is_on = False
            
        # Detect R paddle mis
        if ball.xcor() < -380:
            r_scoreboard.increase_score()
            ball.reset_position()
            if r_scoreboard.score == 100:
                r_scoreboard.game_over("Right Player Win!")
                game_is_on = False


    screen.update()


screen.exitonclick()