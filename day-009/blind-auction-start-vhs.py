from replit import clear
# HINT: You can call clear() to clear the output in the console.

# Printing art, greeting, creating dictionary
from art import logo

print(logo)
print("Welcome to the secret auction program.")
auction_record = {}
end_of_auction = False


def highest_bidder(auction_data):
    highest_bid = 0
    winner = ""
    for bidder in auction_data:
        bid_amount = auction_data[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}.")


while not end_of_auction:
    name_bidder = input("What is your name? ")
    bid_value = float(input("What is your bid? $"))
    auction_record[name_bidder] = bid_value
    shall_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if shall_continue == "no":
        end_of_auction = True
    elif shall_continue == "yes":
        clear()
else:
    clear()
    highest_bidder(auction_record)
