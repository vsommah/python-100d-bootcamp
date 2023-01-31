# Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()
    # by using range(word_length), each iteration will be with 'int' and not 'str'
    for index in range(word_length):
        # addressing the variable 'letter' will be easier
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter

    print(display)

print("You won!")
