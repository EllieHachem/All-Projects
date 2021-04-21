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
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#in py charm put # then TODO: 1. and write
#code can be made in many different ways 
#repeated input = while LookupError\
#there is other type of quotes declartive quotes dont use them use programming quotes the one you use to use 
#in function when made all in it is a parameter 
def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
       if  order_ingredient[item] >= resources[item]:
           print(f"sorry there is not enough{item}")
           return False
       else:
           return True

          
#fuctions are really cool for on and off switch or simple calcations 


def is_transaction_succesful(money_recieved, cost_drink):
    if money_recieved >= cost_drink:
        change = round(money_recieved - cost_drink, 2) #means round number of digites after the dot 
        print(f"here is the change${change}")
        return True
    else: 
        print("sorry that is not enough money")   
        return False # must be last thing in function 
        #code would not be exusted if return false is up 











def process_coins():
    """returns total calculated coins inserts """
    print("please insert coins")
    total = int(input("how many quarters:\n ?")) * 0.25
    total += int(input("how many dime:\n ?")) * 0.10
    total += int(input("how many nickles:\n ?")) * 0.5
    total += int(input("how many pennis:\n ?")) * 0.1
    return total

def make_coffee(drink_name, order_ingredients):
     for items in order_ingredients:
         resources[items] -= order_ingredients[items]
         print(f"here is your {drink_name}")


 


while True: # program usually true so u can use while True more like global variable 
    choice =  input("what would you like to drink\n?")
    if choice == "off":
        break # or make up a variable true and down false it easy
    elif choice == "report":
        print(f"water:  {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}76g")
        print(f"money: {money}$") #shit alt dowwn in pycharm to do multi line editing 
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_succesful(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])




 