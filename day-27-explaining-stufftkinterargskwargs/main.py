#advanced python arguments not how to argument but how to specfify a large range of inputs u know keyword argument? it is better while you create the function u specfify paramter and argument together then u  just clal function name easy though we can change it while declaring but yea it will always have defulte value so when you Hover over a function and see =... = defult value is given arg = argumeent if u hover a function you would know what argument(value)to give too optional = no need to wirte them since they have defult value(hover to see) you can implement using paramter or not also optional very epic 

#Unlimited argument  use *then name of paramter mostly #args u can use other name if u  Warning lets test it lets test it 



# def add(*args):
#     sum = 0  #also can do positions args[0]
#     for n in args:
#         sum += n
#     return sum #notice return is never in a for loop
#here it does in tuple list do the stuff 
# print(add(45,1,1))        
   
# **kwargs = keywoard arguments and ** = many  so many kwargs 
#here is a test

# def calculate(n,**kwargs):
#     print(kwargs) # it is like dictionary
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # or simply 
#     print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# so they took thee code and did like this since intially tinenter was not based on python also this way does not show agruments 

# calculate(2,add= 5,multiply = 3)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


#use.get so that u dont get error dont use other ay
car = Car(make = "bro") # if u dont specficy then it ill give 0 
#this is conveting that is why we use this way and it is like this not that effient as others 
print(car.make)