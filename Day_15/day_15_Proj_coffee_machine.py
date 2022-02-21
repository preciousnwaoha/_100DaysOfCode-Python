from importlib import resources


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water":200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water":250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_menu(menu_list):
    menu = "\n\tMENU\n"
    num = 1
    for item in menu_list:
        num += 1
        menu += f"{num}. {item}\n"
    return menu

def get_report(money_):
    report = ""
    for resource in resources:
        if resource == "coffee":
            report += f"\t{resource}: {resources[resource]}kg\n"
        else:
            report += f"\t{resource}: {resources[resource]}ml\n"

    report += f"\tMoney: ${money_}\n"
    return report


def check_resources_sufficient(drink):
    enough_resources = True
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            enough_resources = False
    return enough_resources


def calc_cash(quater, dime, nickel, penny):
    quater_value = quater * 0.25
    dime_value = dime * 0.10
    nickel_value = nickel * 0.05
    penny_value = penny * 0.01
    cash = quater_value + dime_value + nickel_value + penny_value
    return cash


def make_coffee(drink, money_back):
    text = f"\nDone, enjoy your {drink} "
    money_back = round(money_back, 2)
    if money_back != 0:
        text += f"and take your ${money_back} Change"
    return text

money = 2.5
# Turn on machine
machine_on = True

# TODO: 1. Prompt user by asking
while machine_on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if request in MENU:
        if check_resources_sufficient(request):
            print("Insert coins")
            quaters = float(input("Quaters: "))
            dimes = float(input("Dimes: "))
            nickles = float(input("Nickles: "))
            pennies = float(input("Pennies: "))
            money_inserted = calc_cash(quaters, dimes, nickles, pennies)
            cost_of_drink = MENU[request]['cost']

            change = money_inserted - cost_of_drink

            if change >= 0:
                money += cost_of_drink
                print(make_coffee(request, change))
            else:
                print("Sorry that's not enough money. Money refunded.")         
    elif request == "off":
        machine_on = False
    elif request == "report":
        print(get_report(money))
    elif request == "menu":
        print(get_menu(MENU))
    else:
        print(f"Sorry, {request} is not availiable")
