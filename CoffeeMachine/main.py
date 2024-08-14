from database import MENU, resources
# TODO: 1. Print report


def report(money):
    print("inside report")
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


# TODO: 2. Check if resources are sufficient
def check_resources(the_coffee):
    water = MENU[the_coffee]["ingredients"]["water"]
    coffee = MENU[the_coffee]["ingredients"]["coffee"]
    milk = 0
    if the_coffee != "espresso":
        milk = MENU[the_coffee]["ingredients"]["milk"]

    if the_coffee in MENU.keys():
        if water <= resources["water"] and coffee <= resources["coffee"] and milk <= resources["milk"]:
            return True
        elif water > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif coffee > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        elif milk > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False


# TODO: 3. Process coins.
def process_coins(resource_check):

    if resource_check:
        print("Please insert coins.")
        quarters = int(input("How many quarters will you insert?: "))
        dimes = int(input("How many dimes will you insert?: "))
        nickles = int(input("How many nickles will you insert?: "))
        pennies = int(input("How many pennies will you insert?: "))
        total_money = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
        return total_money

# TODO: 4. Check Transaction successful


def transaction(the_coffee, received_money):
    if received_money >= MENU[the_coffee]["cost"]:
        print(f"Here is your change {round(received_money - MENU[the_coffee]['cost'], 2)}.")
        return MENU[the_coffee]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return barista()


# TODO: 5. Make Coffee

def make_coffee(the_coffee):
    resources["water"] -= MENU[the_coffee]["ingredients"]["water"]
    if the_coffee != "espresso":
        resources["milk"] -= MENU[the_coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[the_coffee]["ingredients"]["coffee"]
    print(f"Here is your {the_coffee} ☕. Enjoy!")
    return MENU[the_coffee]["cost"]


def barista():
    money = 0
    while True:
        the_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
        print(the_coffee)
        if the_coffee == "report":
            report(money)
        elif the_coffee == "espresso" or the_coffee == "latte" or the_coffee == "cappuccino":
            received_money = process_coins(check_resources(the_coffee))
            if received_money is not None:
                transaction(the_coffee, received_money)
                money += make_coffee(the_coffee)
        else:
            barista()


barista()
