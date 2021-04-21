################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#local scope within function within the fence of an apple

def drink_position():
    posion_strength = 2
    print(posion_strength)

drink_position()    

#but if you print(posion_strength outside function it will give error)
#so functions are like homes bro 
#so functions are cool to make same name of variables but with unique status man that is really cool 

#global scope is like creting variable without a function then you can use it in the function inside of it really epic information 


#everything you give a name have a namespace and  It is usually called namespace local and global scopee
#like a function inside function it must be indented so that it become inside the function since it is usually local so local are usually indtended 

# so scope for now variables and functions and functions inside variables 

#there is no block scope like if you create a variable inside 
#an if, while or for loop it still count as global or as its function being used in like normal logical thingy guess other programs are not that much so ya if,else,elif,while,for all those block codes still apply as global vs local scope forget the block scope concept 

#block , blocks, block,blocks of code = if,else,while,format basically
#anything to be intended or statment = same concept so even function I suppose is block of code cuz it is intendted 

#it is terrible idea to name your local and global scope same names 

# to modify a gloabl scope variable inside function we use the global word then we use name the variable 

#it is better not to use global cuz it can be anywwhere and make bugs 

# we can use return something that makes local function gives it to the gloabl  without using global filter


#an exampl


enemiese = 1

def increase_enemies():
    return enemiese + 1

enemiese = increase_enemies   

#global scope is very usefull espically when you are definining constants 

#global constants are variables you want to define and never want to change it again 

#constant something stays the same like value or Pi

# to make them usually make all variable uper classmethod

# like pi make it PI







