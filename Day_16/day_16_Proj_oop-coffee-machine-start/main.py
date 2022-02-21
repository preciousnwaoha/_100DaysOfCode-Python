from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

our_menu = Menu()
machine = CoffeeMaker()
cashier = MoneyMachine()

machine_is_on = True
while machine_is_on:
    available_items = our_menu.get_items()
    choice = input(f"What would you like? ({available_items}):").lower()

    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        machine.report()
        cashier.report()
    else:
        drink_found = our_menu.find_drink(choice)
        if drink_found.name == choice:
            if machine.is_resource_sufficient(drink_found):
                made_payment = cashier.make_payment(drink_found.cost)
                if made_payment:
                    machine.make_coffee(drink_found)