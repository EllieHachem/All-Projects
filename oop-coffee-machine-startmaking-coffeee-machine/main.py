#attribites = charachtersitcs
#methods = functions / list/dicontires
#always remember warframe 
#class = blueprint and it makes objects and those objects has and do 
#both attributes and methods we use .method() .attrubites but attribtues have no () as we are only calling a variable 
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#WE NEED TO STORE CLASS IN AN OBJECT(variable) to use its attributes and functions add () to add class to object 
#ONCE we import the class we use its methods and attributes 
#so from each class we can make multipe objects with differents charachtersies
#usually object named same as class but lowercass 
bro_money_machine = MoneyMachine() #like car(object) = carblueprint(class)
coffee_maker_bro = CoffeeMaker()
menu = Menu()
is_on = True 

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like {options}:\n ")
    if choice == "off":
         is_on = False
    elif choice == "report":
        coffee_maker_bro.report()
        bro_money_machine.report()
    else:
        drink = menu.find_drink(choice) 
        if coffee_maker_bro.is_resource_sufficient(drink):
            if bro_money_machine.make_payment(drink.cost):
                coffee_maker_bro.make_coffee(drink)# we pass the attribute of something like drink here epic way
                #or use and instead of 2 ifs
  
#imagine they are inbuild functions used like .lower() okay 




