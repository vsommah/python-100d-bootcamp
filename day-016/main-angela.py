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

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
