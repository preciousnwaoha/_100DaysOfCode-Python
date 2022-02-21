# import colorgram
import turtle as t
import random

# Extract colors from image into a list
# colors = colorgram.extract("Day_18\hirst-painting\image.jpg", 40)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     check = r >= 230 and g >= 230 and b >= 230
#     if not check:
#         rgb_colors.append(new_color)

# print(rgb_colors)


t.colormode(255)
tim = t.Turtle()

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), 
(213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]

tim.penup()
tim.speed("fastest")
tim.hideturtle()


x = -250
x_change = x
y = -250

tim.setpos((x, y))

number_of_dots = 100

for dot_count in range(1, number_of_dots + 2):
    tim.dot(20, random.choice(color_list))
    tim.setpos(x, y)
    if dot_count % 10 == 0:
        x = x_change
        y += 50
    else:
        x += 50




screen = t.Screen()
screen.exitonclick()