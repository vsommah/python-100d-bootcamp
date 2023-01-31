"""
All exercises and code below are parts of 'Day 006' class on https://reeborg.ca/index_en.html

"""

# # Using a function
#
# def turn_around():
#     turn_left()
#     turn_left()
#

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#

# def jump(x):
#     for barrier in range(x):
#         move()
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#

# jump(6)
#
# # Using while
#
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# num_jumps = 6
#
# while num_jumps > 0:
#     jump()
#     num_jumps -= 1
#
# # Using at_goal()
#
# while not at_goal():
#     jump()
#
# # Hurdles race
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

# Variable Heights

# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#
# # # PROJECT: Escaping the Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def keep_moving():
    turn_left()
    while wall_on_right() and front_is_clear():
        move()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        keep_moving()
