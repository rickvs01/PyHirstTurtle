###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('motmot.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as trt
import random


Jebbediah = trt.Turtle()
screen = trt.Screen()
rgb_color = trt.colormode(255)

Jebbediah.shape("turtle")
Jebbediah.color("green")
screen.bgcolor("white")
Jebbediah.pensize(20)


color_list = [(60, 117, 83), (131, 175, 129), (27, 87, 61), (92, 152, 104), (224, 232, 190), (101, 121, 36), (201, 217, 135), (17, 68, 49), (163, 187, 115), (38, 110, 134), (130, 161, 42), (10, 42, 56), (197, 215, 193), (139, 178, 190), (79, 89, 16), (47, 43, 12), (179, 203, 174), (13, 88, 100), (186, 206, 214), (59, 158, 177), (140, 212, 221), (23, 62, 118), (37, 13, 20), (72, 124, 192), (143, 16, 25), (101, 78, 86), (130, 29, 23), (176, 192, 208), (178, 145, 157), (237, 209, 219)]

#print(random.choice(color_list))

#print(color_list[random.choice(0, len(color_list))])

def horizontal():
    for i in range(0, 10):
        Jebbediah.pencolor(random.choice(color_list))
        Jebbediah.pendown()
        Jebbediah.forward(1)
        Jebbediah.penup()
        Jebbediah.forward(50)
def left():
    Jebbediah.left(90)
    Jebbediah.forward(50)
    Jebbediah.left(90)
    Jebbediah.forward(50)

def right():
    Jebbediah.right(90)
    Jebbediah.forward(50)
    Jebbediah.right(90)
    Jebbediah.forward(50)

for i in range(0,5):
    horizontal()
    left()
    horizontal()
    right()





screen.exitonclick()