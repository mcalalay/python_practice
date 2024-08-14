from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


the_menu = Menu()
the_coffee_maker = CoffeeMaker()
the_money_machine = MoneyMachine()


def main():
    turned_on = True
    while turned_on:
        order = input(f"What would you like? ({the_menu.get_items()}): ").lower()
        if order == "report":
            the_coffee_maker.report()
            the_money_machine.report()
        elif order == "off":
            turned_on = False
        else:
            the_drink = the_menu.find_drink(order)
            print(the_drink)
            if the_coffee_maker.is_resource_sufficient(the_drink) and the_money_machine.make_payment(the_drink.cost):
                the_coffee_maker.make_coffee(the_drink)


main()


