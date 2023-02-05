from turtle import Turtle, Screen

luke = Turtle()
screen = Screen()


def move_forwards():
    luke.forward(30)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
