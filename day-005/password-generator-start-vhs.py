# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# empty variables

# pass_letters = ''
# pass_symbols = ''
# pass_numbers = ''

# loop in each one of the lists based on the input asked
# generate random indexes to go through the lists

# for l in range(1, nr_letters + 1):
#   random_letters = random.randint(0, len(letters) - 1)
#   pass_letters += letters[random_letters]

# for s in range(1, nr_symbols + 1):
#   random_symbols = random.randint(0, len(symbols) - 1)
#   pass_symbols += symbols[random_symbols]

# for n in range(1, nr_numbers + 1):
#   random_numbers = random.randint(0, len(numbers) - 1)
#   pass_numbers += numbers[random_numbers]

# stacking the results

# final_password = pass_letters + pass_symbols + pass_numbers

# print(f"Here's your password: {final_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# empty list

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# shuffle and back to string

random.shuffle(password_list)

final_password = ''

for char in password_list:
    final_password += char

# printing the results

print(f"Here's your password: {final_password}")
