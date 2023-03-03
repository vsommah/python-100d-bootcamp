import turtle as t
from snake_pt2 import Snake
from food import Food
from scoreboard import Scoreboard
import time

LEFT_LIM = 280
RIGHT_LIM = -280
UP_LIM = 280
DOWN_LIM = -280

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 My Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoring()

    # Detect collision with the wall
    x_cord = snake.head.xcor()
    y_cord = snake.head.ycor()

    if x_cord > LEFT_LIM or x_cord < RIGHT_LIM or y_cord > UP_LIM or y_cord < DOWN_LIM:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    # if head collides with any segment in the tail:
        # trigger game_over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
