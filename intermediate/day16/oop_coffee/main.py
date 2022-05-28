from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()
myMenu = Menu()

is_on = True
while is_on:
    options = myMenu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        is_on = False
        print("Turning off")
    elif choice == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    else:
        drink = myMenu.find_drink(choice)
        if myCoffeeMaker.is_resource_sufficient(drink):
            if myMoneyMachine.make_payment(drink.cost):
                myCoffeeMaker.make_coffee(drink)

      