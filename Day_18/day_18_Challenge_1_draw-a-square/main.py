from turtle import Turtle, Screen
import random

def random_color():
    colors = ["red", "yellow", "green", "blue", "purple", "black"]
    return random.choice(colors)




timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(3)
timmy_the_turtle.d

timmy_the_turtle.color(random_color())

n = 1
x = 20
while n <= 50: 
    timmy_the_turtle.forward(x)
    timmy_the_turtle.left(90)
    timmy_the_turtle.color(random_color())
    x += 5
    n += 1















screen = Screen()
screen.exitonclick()