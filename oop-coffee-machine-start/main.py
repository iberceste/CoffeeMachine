
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


check_money = MoneyMachine()
make_coffee = CoffeeMaker()
menu = Menu()


machine_working = True

while machine_working:
    choice = input("What would you like? (espresso/latte/cappuccino/):")

    if choice == "off":
        print("Machine off")
        machine_working = False

    elif choice == "report":
        make_coffee.report()
        check_money.report()

    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and check_money.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
