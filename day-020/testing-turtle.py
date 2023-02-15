import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)

test = t.Turtle("square")
test.color("black")


def up():
    test.setheading(90)
    test.forward(20)


def down():
    test.setheading(270)
    test.forward(20)


def left():
    test.setheading(180)
    test.forward(20)


def right():
    test.setheading(0)
    test.forward(20)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.exitonclick()
