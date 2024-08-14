# import colorgram as cg
#
# colors = cg.extract('images.jpg', 30)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
#
# print(rgb)

import turtle as T
import random as rr

color_list = [(221, 155, 103), (224, 67, 88), (128, 170, 198), (20, 120, 159), (214, 133, 154), (240, 209, 99),
              (126, 177, 149), (34, 125, 81), (20, 165, 206), (154, 77, 49), (165, 58, 77), (217, 84, 70),
              (236, 160, 176), (240, 168, 152), (184, 156, 53), (178, 185, 217), (245, 217, 1), (170, 210, 171),
              (215, 10, 41), (4, 91, 112), (159, 204, 216), (58, 162, 125), (51, 58, 89), (26, 91, 54),
              (29, 53, 78), (99, 127, 174)]

tur = T.Turtle()
tur.speed("fastest")
T.colormode(255)
tur.hideturtle()

def draw_dots(dots, step_size):
    for _ in range(dots):
        tur.dot(20, rr.choice(color_list))
        tur.up()
        tur.forward(step_size)
        tur.dot(20, rr.choice(color_list))


def turn_back_left(step_size):
    tur.left(90)
    tur.forward(step_size)
    tur.left(90)


def turn_back_right(step_size):
    tur.right(90)
    tur.forward(step_size)
    tur.right(90)

for _ in range(5):
    draw_dots(10, 50)
    turn_back_left(50)
    draw_dots(10, 50)
    turn_back_right(50)



screen = T.Screen()
screen.exitonclick()
