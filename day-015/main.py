import menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# machine_ON = True
# while machine_ON:
#     run_program()


def run_program():
    user_option = input("What would you like? (espresso/latte/cappuccino): ")

    # returning data from the MENU file
    def requirements(drink, info):
        return menu.MENU[drink][info]

    # checking if we have all ingredients needed
    def check_resources():
        list_ingredients = requirements(user_option, "ingredients")
        for item in list_ingredients:
            if int(list_ingredients[item]) > int(resources[item]):
                print(f"Sorry there is not enough {item}. 🙁")
                return False
            else:
                return True

    # processing coins
    def processing_coins():
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        total_amount = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)
        return total_amount

    # checking if we have enough money
    def check_money(coins_in_machine):
        drink_price = float(requirements(user_option, "cost"))
        profit = resources["money"]
        if coins_in_machine < drink_price:
            print("Sorry, that's not enough money. Money refunded. 💵")
            return False
        elif coins_in_machine > drink_price:
            total_change = coins_in_machine - drink_price
            profit += drink_price
            resources["money"] = profit
            print(f"Here is ${'{:.2f}'.format(total_change)} in change.")
            return True
        elif coins_in_machine == drink_price:
            profit += drink_price
            resources["money"] = profit
            return True

    # deducting ingredients
    def make_coffe():
        list_ingredients = requirements(user_option, "ingredients")
        for item in list_ingredients:
            new_qty = int(resources[item]) - int(list_ingredients[item])
            resources[item] = new_qty
        print(f"Here is your {user_option}. Enjoy! ☕")

    # running the machine
    if user_option == "off":
        print("Bye... 😴")
    elif user_option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        run_program()
    elif user_option == "espresso" or user_option == "latte" or user_option == "cappuccino":
        if check_resources():
            money_inserted = processing_coins()
            if check_money(money_inserted):
                make_coffe()
        run_program()
    else:
        print("Invalid option.")


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.

run_program()
