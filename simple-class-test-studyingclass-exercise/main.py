#first create class
#use slash forward to comment and uncomment them  easy learning way and many test at once in same project
# class bro:
#     x = 5
#     m = 4

# print(bro)

#now creating an object 

# class Bro:
#     x = 5
#     m = 4

# bro = Bro()
# print(bro.x)
# print(bro.m)

# class Person:
#     def __init__(self,name,age,weight,tall,meme_level):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.tall = tall
#         self.meme = meme_level
    


# person_1 = Person("Sami","20","fourty kg","182cm","high")
# print(person_1.meme)

# class Person:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

#     def my_function(self):
#         print(f"hello bro my name is {self.name}") 

# person_1 = Person("20","bobby") #inheriting + data filling
# person_1.my_function() #functiong after inheriting and data filling 


# NOTE YOU DONT NEED TO USE SELF BUT YOU MUST ALWAYS USE SOMETHING AT FIRST AN EXAMPLE 


# class Person:
#     def __init__(bro,age,name):
#         bro.age = age
#         bro.name = name

#     def my_function(bro):
#         print(f"hello bro my name is {bro.name}") 

# person_1 = Person("20","bobby") #inheriting + data filling
# person_1.my_function() #functiong after inheriting and data filling 

#modifying properties 

# class Person:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

#     def my_function(self):
#         print(f"hello bro my name is {self.name}") 

# person_1 = Person("20","bobby") #inheriting + data filling
# person_1.my_function() #functiong after inheriting and data filling 

# person_1.age = "56.5" #data changing 
# print(person_1.age)


#deleteing attrubute in general use del keyword

# class Person:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

#     def my_function(self):
#         print(f"hello bro my name is {self.name}") 

# person_1 = Person("20","bobby") #inheriting + data filling
# person_1.my_function() #functiong after inheriting and data filling 

# person_1.age = "56.5" #data changing 
# print(person_1.age)

# del person_1.age
# print(person_1.age)

#now deleting object same but del and object name alone 

# class Person:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

#     def my_function(self):
#         print(f"hello bro my name is {self.name}") 

# person_1 = Person("20","bobby") #inheriting + data filling
# person_1.my_function() #functiong after inheriting and data filling 
#so function is giving to the object inhrerting + flled with attributes so as normal function FOCUS on attrubutes inhriting jsut = with () and between parnthges put the inherting(data) just like making new function  but this time we use () to add data 




# person_1.age = "56.5" #data changing 
# print(person_1.age)

# del person_1
# print(person_1.age)



#use pass to stop indentation expected error if u want to make an empty class an example

# class Pro:
#     pass
#     #here we get no errors 


#but here we get 

# class pro:

# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
#this is a great way to inherit  class from another class
#also study in w3school after each topic u dont undeertand or missing but u still need to know basics before going there like now 

# class 
# Student(Person)
# :

# well this wwas for inherities but it is easy as u saw () and type class normally
#that is how u inherit then u but pass
#and then use the other classes properties as if it isinstance
#u got What I mean 
# class Person:
#   def __init__(self, fname):
#     self.firstname = fname

#   def printname(self):
#     print(self.firstname)

# class Student(Person):
#   pass

# x = Student("Mike")
# x.printname()


class Questions:
    def __init__(self,age,name,country):
        self.age = age
        self.name = name
        self.country = country

    def func(self):
        input("what is your age:\n")



    def func2(self):
        input("what do you do in life\n")


question_1 = Questions("20","40","")
print(question_1.country)

question_1.func()
question_1.func2()
