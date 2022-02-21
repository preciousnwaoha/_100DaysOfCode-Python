import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def random_degree():
    num = random.randint(0,3)
    return 90*num

tim = t.Turtle()
t.colormode(255)


tim.speed(2)
tim.pensize(10)

def mazy_move(times):
    for _ in range(times):
        tim.color(random_color())
        tim.setheading(random_degree())
        tim.forward(25)


mazy_move(500)

screen = t.Screen()
screen.exitonclick()

