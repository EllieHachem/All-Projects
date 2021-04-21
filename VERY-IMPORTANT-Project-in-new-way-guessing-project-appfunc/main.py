#make then quest ways
# we cut program like cucumber or subskills when making it and write them as comment as here each with each sub quest to do 
#if you see a program run it and play it bit by bit then do as this 
#usually it is best to start from the first function used to make it sequencal and as the prototype as well make it easier on you to test but hey your Choice 
#NOTE: print and input stuff are not really considred as tasks so they can be added along the quests  but I will usually add them as quest makes it more clean 
#we can change quest order but your Choice again 
#functions prefered to be at top of ConnectionAbortedError
# comments helps too to prevent some identations erros 
# always remember calculator like x and y and then u can use them as function that if it have input but if no input just action dont put input  x and y like addition or if else then input otherwise nope 
#always make CONSTANT variabls to change in functions gloabl vairables 
# capital letters really make it also not just to remember they are constant but also to find them to use them 
#better give the answer of program to be shown to see if it is working
#gloabl variabls
#prefer to train later on how to intend whole function to block though it is really irriating for me just use normal functions but try

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 
#function to check score against actual answer 
#in input it is just any random it can be anything it just states how many inputs it will have and those input you make argument for them at end
#use gloabl before variabl to use it in functions but just use return for now cuz it is not changing global 
# define just small codees of function
#make sure to usee return better than using off and true values cuz 
#those are meessy tbh 
def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return  turns - 1
    elif guess < answer:
        print("too low")   
        return  turns - 1
    else: 
        print("you got it")     

#make function to set diffuclity 
def set_diffculity():
    level = input("choose a diffuclity easy or hard: \n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS 



def game():
    #print on screen the basic stuff
    print("welcome to gussing game")
    print("I am thinking of a number betweeen 1 and 100")

    #choosing random number between 1 and 100
    #usally we type import random then use random.randint but this is epic way too 
    from random import randint
    answer = randint(1, 100)
    print(f" the answer is {answer}")

    # difficlty asking 
    turns = set_diffculity()

    #repeat the guessing functionality if guessed wrong
    #always declear a variable before loops even if not needed
    # also you can just make all those in function 
    guess = 0
    while guess != answer:
        print(f"you have {turns} left ")
        guess = int(input("make a guess\n"))
        #here it is meme you can use the return on function to update turns
        turns =  check_answer(guess,answer,turns)
        if turns == 0:
            return
        






    #let the user guess a number

    #track number of turns/attempts and reduce by 1 if they get it wrong

    # then between each comment make the event omg so easy


game()