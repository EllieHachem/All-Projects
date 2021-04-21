# we create many objects from class and each objects are called
#instances

# okay so 2 turtle objects they can have different attributes and be 
#doing different things 

#like timmy.color = green and tommy.color = red = called state 
#state means can perform different attribute and function 
#lik state of timmy color is gree and tommy = red  so stat meeans differeent thing so state = proprtis(thing) state can be used as function lik state of timmy = standing or moving backward while tommy moveing forwardd 

#different state = different instance of same obbject with different methods and attribute 

#in documantion methods can be used with all objects types nearly like here the width of tutre also apply for screen object 
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "make your bet",prompt = "which turtle will win the race")
colors = ["red","green","blue","orange"]
y_positions = [-70,-40,-10,20 ]
all_turtles = []
for turtle_index in range(0,3):
    tim = Turtle(shape ="turtle") # u can put shape here not just with a method 
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x= -230, y =y_positions[turtle_index]) #but ya put it -230 cuz on edge of screen it really does not show
    all_turtles.append(tim) #tim heree is a new turtle intance

if user_bet: #tutle object is 40 by 40 so we must put 230 cuz 250 (40/2) = 2 if very confusing put end race 210 and test out 
    is_race_on = True

while is_race_on: #xcore means x cordinate
    for turtle in all_turtles:
            distance = random.randint(0,10) #not like range here can have 0
            turtle.forward(distance) 
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"you have won the winner is {winning_color}")
        else:
            print(f"you have lost the winner is {winning_color}")    
   

#usally x axsis 250 and y axis 200
# x horizantal Y vertical easy function lesson in mathon and exponent 

screen.exitonclick() 