import colorgram
import random
import turtle
from turtle import Turtle, Screen

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(236, 235, 240), (238, 232, 236), (14, 12, 9), (224, 163, 65), (19, 45, 87), (136, 61, 84),
              (177, 60, 44), (126, 40, 61), (241, 231, 222), (21, 86, 61), (249, 194, 43), (15, 117, 146),
              (58, 147, 72), (229, 86, 36), (230, 172, 189), (57, 71, 39), (196, 102, 134), (155, 191, 184),
              (197, 123, 149), (31, 68, 60), (166, 204, 202), (229, 238, 234), (144, 164, 180), (4, 79, 113),
              (62, 29, 49)]

bitis = Turtle()
turtle.colormode(255)
bitis.shape("turtle")
bitis.speed("fastest")
bitis.penup()
bitis.hideturtle()
bitis.setheading(225)
bitis.forward(300)
bitis.setheading(0)
number_of_dots = 100


def random_color(user_list):
    current_color = random.choice(user_list)
    return current_color


for dot_count in range(1, number_of_dots + 1):
    bitis.dot(20, random_color(color_list))
    bitis.forward(50)

    if dot_count % 10 == 0:
        bitis.setheading(90)
        bitis.forward(50)
        bitis.setheading(180)
        bitis.forward(500)
        bitis.setheading(0)

screen = Screen()
screen.exitonclick()
