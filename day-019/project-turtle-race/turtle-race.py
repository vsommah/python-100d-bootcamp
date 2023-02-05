import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput(title="🐢 Turtle Race 🐢", prompt="Who is going to win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [90, 60, 30, 0, -30, -60, -90]

# red = t.Turtle(shape="turtle")
# red.penup()
# red.color(colors[0])
# red.goto(x=-230, y=90)
#
# orange = t.Turtle(shape="turtle")
# orange.penup()
# orange.color(colors[1])
# orange.goto(x=-230, y=60)
#
# yellow = t.Turtle(shape="turtle")
# yellow.penup()
# yellow.color(colors[2])
# yellow.goto(x=-230, y=30)
#
# green = t.Turtle(shape="turtle")
# green.penup()
# green.color(colors[3])
# green.goto(x=-230, y=0)
#
# blue = t.Turtle(shape="turtle")
# blue.penup()
# blue.color(colors[4])
# blue.goto(x=-230, y=-30)
#
# indigo = t.Turtle(shape="turtle")
# indigo.penup()
# indigo.color(colors[5])
# indigo.goto(x=-230, y=-60)
#
# violet = t.Turtle(shape="turtle")
# violet.penup()
# violet.color(colors[6])
# violet.goto(x=-230, y=-90)

racers = []

for turtle_index in range(0, 7):
    bitis = t.Turtle(shape="turtle")
    bitis.penup()
    bitis.color(colors[turtle_index])
    bitis.goto(x=-280, y=y_positions[turtle_index])
    racers.append(bitis)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 260:
            winning_racer = racer.pencolor()
            if winning_racer == user_bet:
                print(f"You've won! The winner is the {winning_racer} turtle.")
            else:
                print(f"You've lost. The winner is the {winning_racer} turtle.")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)

screen.exitonclick()
