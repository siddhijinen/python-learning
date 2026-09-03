# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors) #used to get a tuple list of extracted colors (one-time use)

import random
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
timmy = Turtle()
screen.colormode(255)
timmy.speed("fastest")
timmy.setx(-250)
timmy.sety(-250)

def random_color():
    colors_to_use = [(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
    color_chosen = random.choice(colors_to_use)
    r = color_chosen[0]
    g = color_chosen[1]
    b = color_chosen[2]
    color = (r, g, b)
    return color


for i in range(10):
    for j in range(10):
        timmy.pendown()
        timmy.fillcolor(random_color())
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)
    timmy.setx(-250)
    timmy.sety(-250 + (i+1)*50)
    timmy.setheading(0)
screen.exitonclick()