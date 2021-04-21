## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


#
##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc. #functiosn can be passed as a number as argument 
#first class objeect = interger/float/string etc 
#so we can tae this function and build another function that uses this function 

def calculate(calc_function, n1, n2): #so here we added the calc function and added 2 inputs so it 
    return calc_function(n1, n2)

result = calculate(add, 2, 3) #here we added extra functionality python is really  epic 
print(result)

##Functions can be nested in other functions
#scope means  it is only accessiable inside the outr function 
#if we go outside function the nstd function wont work and we get not defined 
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()
#basically if we save the outfunction as variable then we can use its inner funtion as long as we return its inner function  

## Simple Python Decorator Functions
#we start by creating a normal function 
import time


def delay_decorator(function): #here is normal function that takes anotheer function as input  #NOW WHENEVER WE MAKE A FUNCTION WITH DECRATOR THEN IT WILL MAKE IT SLEEP 
    def wrapper_function(): #here neseting wrapper function and this function will trigger the actual function passed in 
        time.sleep(2) #HERE IS THE DAY ADDED BEFORE THE FUNCTION is triggered 
        #Do something before
        #do something before u add the function (BEFORE FUNCTION EXECUTED )
        function()
        function()
        #OR HEREE RUN THE FUNCTION TWICE AS HERE FUNCTION IS COPY PASTED TWICE 
        #Do something after the function (AFTER FUNCTION IS EXECUTED )
    return wrapper_function #then we return function without the paranethsis 
    #remember a dcecitor function wraps the function (nest it) and gives the function an addonal functionality 
#@delay_decorator is equal to delay_decorator(say_hello) then save it as variablee then dont print just use the vairable with () to use that is same thing but this is much easier way 
@delay_decorator #We pass decrator before the function just give its name  + @ sign 
def say_hello(): #this is simplest form of function now what if we dont want to run this imeddiality when we hit run like what if wanted to add a delay to this function it is easy usually we add time module 
#but what if we made a lot of functiosn like now say_bye or say_greeting and add delay on each usually copy on all three places so this is where the decorator come in handy it is very useful for huge projects we add delay up 
    print("Hello")

#With the @ syntactic sugar
@delay_decorator 
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

#the @ sign is called syntaxic sugar it is some synatx that you can write to make it easier to write an alternative line of code  