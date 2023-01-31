# Number Guessing Game Objectives:

import random
from art import logo
from replit import clear


def play_game():
    # Include an ASCII art logo.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    answer = random.randint(1, 100)
    print(f"Psst, the answer is: {answer}")

    # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_difficulty == 'easy':
        attempts = 10
    elif game_difficulty == 'hard':
        attempts = 5
    else:
        print('Unnecessary illiteracy. 5 attempts penalty. 1st try...')
        attempts = 5

    # Allow the player to submit a guess for a number between 1 and 100.
    def guess():
        guess = int(input("Make a guess: "))
        return guess

    user_guess = guess()

    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    def check_guess(user_guess):
        if user_guess > answer:
            print("Too high.")
            print("Guess again.")
        elif user_guess < answer:
            print("Too low.")
            print("Guess again.")

    while user_guess != answer and attempts > 0:
        check_guess(user_guess)
        attempts -= 1
        # Track the number of turns remaining.
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = guess()
        # If they got the answer correct, show the actual answer to the player.
    if user_guess == answer:
        print(f"You got it! The answer was {answer} 😀")
        # If they run out of turns, provide feedback to the player.
    elif attempts == 0:
        print(f"You've run out of guesses... The answer was {answer}. You lose. ")


play_game()