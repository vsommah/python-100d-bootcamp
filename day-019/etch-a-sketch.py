import turtle as t
import random

bitis = t.Turtle()
screen = t.Screen()
t.colormode(255)
bitis.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move_foward():
    bitis.forward(10)


def move_backward():
    bitis.backward(10)


def rotate_counter_clowise():
    new_angle = bitis.heading() - 10
    bitis.setheading(new_angle)


def rotate_clowise():
    new_angle = bitis.heading() + 10
    bitis.setheading(new_angle)


def clear():
    bitis.clear()


def go_home():
    bitis.penup()
    bitis.home()


bitis.color(random_color())

screen.title("W → Forwards / S → Backwards / A → Counter-Clockwise / D → Clockwise / C → Clear drawing / H → Go back "
             "to the origin point")

screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clowise)
screen.onkey(key="d", fun=rotate_clowise)
screen.onkey(key="c", fun=clear)
screen.onkey(key="h", fun=go_home)

screen.exitonclick()
