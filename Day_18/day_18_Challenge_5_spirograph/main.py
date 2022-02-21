import turtle as t
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


tim = t.Turtle()
t.colormode(255)


tim.speed("fastest")
tim.color(random_color())

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()