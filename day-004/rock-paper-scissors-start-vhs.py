# ASCII used for the game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, or  2 for SCISSORS.\n"))

#        0      1        2
rps = [rock, paper, scissors]

if choice >= 3 or choice < 0:
    print("You typed an invalid number. You lose!")
else:

    print(rps[choice])

    print("Computer chose: ")

    computer = random.randint(0, 2)

    print(rps[computer])

    # Rock wins against scissors.
    # Paper wins against rock.
    # Scissors win against paper.

    if choice == 0 and computer == 2:
        print("You win!")
    elif choice == 1 and computer == 0:
        print("You win!")
    elif choice == 2 and computer == 1:
        print("You win!")
    elif choice == computer:
        print("It's a draw!")
    else:
        print("You lose!")