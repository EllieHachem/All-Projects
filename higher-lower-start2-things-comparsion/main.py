#do to do list based on the problems you want to do to make a program
#start with easiest to do list 
#write code > run code > fix then redo this 
#play project like 10 times or one by one to know how it works
# big problem have 2 hashtage and even 3 if needed to know how to make it more simpler 
#program can be simple but if you compare final project with this it seems this program is really tough 
#write import  above the comments of it 
#ALWAYS remember basic programing stuff to fix most of your problems 
#import 2  stuff from module by , 
from art import logo, vs
from game_data import data 
import random  
score = 0
game_should_continue = True
account_b = random.choice(data)
from replit import clear 
#display asiacrt 
print(logo)
#formate account data into printable format 
def format_data(account):
    """this function takes one input and lists its 3 keys so functions can be called like easy this way as long as argument is acceptable"""
    account_name = account["name"]
    account_description = account["description"]
    account_country =account["country"]
    return f"{account_name},{account_description},{account_country}"


#simple function    # you can use 3 outputs and more as well as use f with return this way is epic and saves line 
def check_answer(guess, a_follower_count, b_follower_count ):
    """if statment to make sure answer is correct"""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


#repeatable action 
while game_should_continue:
    #generate random accounts from game data  if same random make if statment to fix it epic so always remember basics to those types of problem  # this account a = b is a trick cuz it loops in while while it is store at end of program have some logical but meh meme thing to do 
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"compare B: {format_data(account_b)}")

    #ask user to guess #user.lower always when asking for string typing
    #better precise  
    guess = input ("who has more followers A or B?\n").lower()

    #check if user is correct 
    ##get follower account if each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #clear function hav time clear them here proper time to clear remember + add logo or stuff if u want after clear so even clear function have timing 
    clear()
    print(logo)
    ##if statment if user is correct 

    #give user feedback(a comment) for their guess 
    if is_correct:
        score += 1
        print(f"you are right right current score is {score}") 
    else:
        game_should_continue = False
        print(f"sorry you are wrong final score {score}")   
#score keeping 

#make game repeatable 


#making account as postion B to become at postion A 

#clear screen between rounds 