#in avriables - does not work not just first letter having number in it 
#we can do like x = z = y = "orange" epic to assign 4 variables at once

#epic test + we can add variable next to each other in print and after it a comma , very epic 
# x = z = y = "orange"
# print(x,z,y,x)

#from index we use : and example

# txt = "hello"
# x = txt[2:5]
# print(x)

#global = make the variable in gloabl scope 

#str = string  = "" and int = whole number  #float = decimal like written at first like flo not fla

#tuple is like list but with () and can not be changed 

#dict = dictonary 
#bool = boolean 

#A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers, and i represents the “imaginary unit”, satisfying the equation i2 = -1. Because no real number satisfies this equation, i is called an imaginary number

#we use complex 

# x = 5 
# complex(x)
# print(x)

# no spaces = .strip
# txt = " Hello World "
# x = txt.strip()
# print(x)

#uper cass use upper function 
# txt = "Hello World"
# txt = txt.upper()
# print(txt)
#as for lower wwe use lower()

# #Replacing strings 

# txt = "Hello World"
# txt = txt.replace("H", "J")
# print(txt)


#bool 0 = false but as normal stuff it is true 


# see here insert to add something in postion not like append at end
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1,"lemon")
# print(fruits)

#this way to remove fron list () and not [] since functions are like ()
#not like []
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)


#negative indexing like -1 from end of list
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

# set like diocntary but not dictnary 
# we use the .add to add to set 
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)


# use .update method to add multiple items


# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)
# print(fruits)

#discard method to remove item 
#not sure about remove lets see 


#so discard is like remove method 
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
# fruits.remove("apple")
# print(fruits)

#you can put if at same line without indentation kinda cool if you have on statment but not recommended like

# if 5 > 2: print("Five is greater than two!")
#and if in print("Yes") if 5 > 2 else print("No") here you dont even type : to else a meme way tbh

#to stop loop use break word epic too 
#example :

# i = 1
# while i < 6:
#   if i == 3:
    
# break

#   i += 1

#continue to next code(test this later)
#an example 

# In the loop, when i is 3, jump directly to the next iteration.
#use continue keyword 

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
    
# continue

#   print(i)

#once condition is false = else in questions or anything 

#dont forget to use : in answering qusetions very important 

#continue= jump directly to next code 

#test of continue 
#continue is like skipping that part of code so contunue = skipping
#like here skipped to print someething 
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "cherry":
#     continue
    
#   print(x)

#exiting loop = useb break keywrods 

#keywords are like print keyword or len keyword while function same with () also called method espically if in class 


#If you want to refer to a module by using a different name, you can create an alias.

# to import the correct syntax for creating an alias for a module?


# import mymodule  as as mx like 

#import random as bro  then we use it as bro 

# The correct syntax of printing all variables and function names of the "mymodule" module?

#so here e use dir to print all variables and functions of the module 
# import mymodule

# print(dir(mymodule))


#Using  the get method to print the value of the "model" key of the car dictionary.
#so we use .get() to take somethign from dicoctionary kkey 


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(
# car.get("year"))

#here to edit a key just type name of dic with ["key"] and assign it to a new value 
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["year"] = 2020 #old key = key  this is like updating 
# print(car.get("year"))

#to add new key (so memeorize this first )
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red" #old key = key  this is like adding  same way though ya logic  
# print(car.get("color"))


#use pop method to remove key/value from dictionary
#discard and remove remove so ya pop and get to use and to add or update just usee [] and assign new value easy 
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")
# print(car)

#to clear a dicontary we use clear method 
#an example 
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

#A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression. exprssion is like a OSError

#example 

# x = lambda a: a + 234 +45
# print(x(6))

# so it is like x = 1 and it is doubled by lambda 



