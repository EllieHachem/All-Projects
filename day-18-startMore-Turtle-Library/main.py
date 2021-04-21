#(cool graphic lesson ) we gonna draw cool colored dot with turtle 
# to use module or pacakge we use documantaiton 
#in an idle world we read all documantion but in real world we go stack flow then ask how to use those methods then read saves a lot of time
#tk = tinker = used for graphical interface = color string = all thoe colors with #
#tuple spelled tapl data type in python like list instead have () and ordered means have index and accessed same way as list but tuple u can not change value like list cool to put it in games means less hackers 
#tuple = immutable = can not be changed 
#to change tuple to list just type list(PUT HERE THE TUPLE)
#rgb color red green blue and each have percentage to give u a color so go w3scgool rgb calcualtor to test 
#make spirograph
#not sometims just copy paste something even if same word to fix error very weird but yea works 
#mak sure if parameter value is int or string or anything
#draw a circle
#how large circle should be 
#repaetdly draw cirlce
#change title of circle 
# heading means = which direction it is pointing toward in state also called titling  = shifting
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

 


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

#or use this for loop and range to repeat and save time right
#use refactor in pycharm to rename vairable that is named all at once
# pen down and pen up to drawwing stuff 
# for _ in range(4):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)


# for shape in range(3,10):
#     draw_shape(shape)

import random
# timmy_the_turtle.width(20)
timmy_the_turtle.speed("fastest")
# direction = [0,90,180,270]
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)): #learn to use _ in for loop as most of tim this vairabl is a memee
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        timmy_the_turtle.circle(100)


draw_spirograph(5)

screen = turtle.Screen() 
screen.exitonclick()




# ways to import modules
#basic way import (1st way)
#with this way to create class we do this tim = turtle.Turtle()

#2nd way from turtle import Turtle() which will make the object creation like this tim = Turtle

#3rd way most epic wwhih is import turtle * or random * means now you just write like this 

#instead of random.choice we can use choice() and it will work or even now the turtle forward() without even the need of calling anything else
#not good but in case u see it (train to use it to save time and less confusion for us at least ) though from import best one  depend on you
#4th way is import as  like import random as Bro so u call it bro now
#test all stuff after this 
#turtle is inbuilt module u can just import but others u need to install ( in pythons standered library)



























screen = Screen()
screen.exitonclick()