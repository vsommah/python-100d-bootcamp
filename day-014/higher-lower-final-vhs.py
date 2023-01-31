import art
import game_data
import random
from replit import clear

score = 0


# Print logo
def print_logo():
    print(art.logo)


print_logo()


def XX_game():
    # Random pick one dictionary from data list
    def random_person(data):
        person = random.choice(data)
        return person

    person_a = random_person(game_data.data)
    person_b = random_person(game_data.data)

    # Print person A
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']} ")
    # Print vs
    print(art.vs)
    # Print person B
    print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']} ")

    # Check who has more followers
    def who_have_more(person_a, person_b):
        num_followers_a = int(person_a['follower_count'])
        num_followers_b = int(person_b['follower_count'])
        if num_followers_a > num_followers_b:
            return "A"
        elif num_followers_a < num_followers_b:
            return "B"
        else:
            return "Draw"

    # Address the result to an variable called 'answer'
    answer = who_have_more(person_a, person_b)
    print(f"Psst, this is the answer: {answer}")

    # Print question + request input
    guess = input("Who has more followers? Type 'A' or 'B': ")
    print(f"user guess: {guess}")

    # Check guess and score
    def check_guess(answer, guess, score):
        if answer == guess:
            return score + 1
        else:
            return score

    current_score = check_guess(answer, guess, score)

    while answer == guess:
        check_guess(answer, guess, score)
        clear()
        print_logo()
        print(f"You're right! Current score: {current_score}")
        XX_game()
    else:
        clear()
        print_logo()
        print(f"Sorry, that's wrong. Final score: {current_score}")


XX_game()
