from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer} 😀")


# Make function to set difficulty
def set_difficulty():
    game_difficulty = input("Choose a difficulty. Type 'easy' (10 att.) or 'hard' (5 att.): ")
    if game_difficulty == 'easy':
        return EASY_LEVEL
    elif game_difficulty == 'hard':
        return HARD_LEVEL
    else:
        print('Unnecessary illiteracy. 5 attempts penalty. 1st try...')
        return HARD_LEVEL


def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the answer is: {answer}")
    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses... The answer was {answer}. You lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
