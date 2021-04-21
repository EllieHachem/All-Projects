from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

#steve jobs explains oop properly he explains that u are in japan having fun then u got ur tshirt dirty and u dont have curreny or anything u dont know dry cleanr or langauge so what you do ? it will be strugglee solving it alone so u go hotel they speak english and hotel takes care of everything so hotel can be object and they have methods callled langauge/dry cleaner / currency  or in basic terms object called hotel and we call its methods.dry cleaner

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu = Menu()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like({options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost): # or use and instead of 2 ifs
                coffee_maker.make_coffee(drink)