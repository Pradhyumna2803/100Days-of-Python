from MenuItem import Menu, MenuItem
from MoneyMachine import MoneyMachine
from CoffeeMaker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.getItems()
    choice = input(f"What would you like to have ? {options} : ")
    if(choice == 'off'):
        is_on = False
    elif(choice == "report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.findDrink(choice)
        if( coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) ):
            coffee_maker.make_coffee(drink)