# # import turtle
# #
# # timmy = turtle.Turtle()
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# # timmy.color("SeaGreen4")
# # timmy.pencolor("black")
# timmy.fillcolor("SeaGreen4")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokémon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
