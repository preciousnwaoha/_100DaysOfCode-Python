from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_cord = 0
gap_odd = 0
gap_even = 0

for n in range(6):
    
    turtles.append(Turtle(shape="turtle"))
    turtles[n].penup()
    turtles[n].color(colors[n])
    turtles[n].goto(x=-230, y=y_cord)
    
    if (n+1)%2 == 0:
        gap_even += 30
        y_cord = 0
        y_cord += gap_even
    if (n+1) % 2 != 0:
        gap_odd -= 30
        y_cord = 0
        y_cord += gap_odd

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()