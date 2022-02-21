import turtle as t
import random

def random_color():
    colors = ["red", "yellow", "green", "blue", "purple", "black"]
    return random.choice(colors)

tim = t.Turtle()


def draw_shapes(sides, max_size):
    while sides <= max_size:
        deg = 360/sides;
        tim.color(random_color())
        for n in range(sides):
            tim.forward(50)
            tim.right(deg)
        sides += 1

draw_shapes(3, 10)

screen = t.Screen()
screen.exitonclick()