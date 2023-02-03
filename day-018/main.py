import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        direction = timmy.heading()
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(direction + size_of_gap)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
