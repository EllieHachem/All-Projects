Loggy = """
╔═══╗
║╔══╝
║╚══╦══╦╦══╗╔══╦═╦══╗
║╔══╣╔╗╠╣╔═╝║╔╗║╔╣╔╗║
║╚══╣╚╝║║╚═╗║╚╝║║║╚╝║
╚═══╣╔═╩╩══╝║╔═╩╝╚══╝
────║║──────║║
────╚╝──────╚╝"""
import random
attempts = 10
easy_level = []
hard_level = []
print(Loggy)
print("welcome to my awesome guessing application")
print("I am thining of a number between 1 to 100")
chosing_diffculty = input("what is your diffculty easy or hard: ?")
if chosing_diffculty == "easy":
    easy_level = True
elif chosing_diffculty == "hard":
    hard_level = True  
else: 
    print("please choose a diffuclty")     
 
 
 
while easy_level and attempts > 0 :
    print(f"you have  {attempts} attempts")
    number = random.randrange(1, 100)
    guess = int(input("make a guess"))
    if guess == number:
        print("you won")
        easy_level = False
    elif guess > number:
        print("too high guess again")
        input("type again")  
        attempts = attempts - 2 
    else: 
        print("your guess is too low guess again")
        input("type again") 
        attempts = attempts - 2  

while hard_level and attempts >= 5:
    print("you have 5 attempts")
    number = random.randrange(1, 100)
    guess = int(input("make a guess"))
    if guess == number:
        print("you won")
        hard_level = False
    elif guess > number:
        print("too high guess again")
        input("type again")
        attempts = attempts - 2     
    else:
        print("your guess is too low guess again")
        input("type again") 
        attempts = attempts - 2