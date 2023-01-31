from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:

    user_choice = input(f"What would you like? {menu.get_items()}: ")

    if user_choice == "off":
        print("Bye... 😴")
        is_on = False
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)