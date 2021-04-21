#event  listener like sccreen event =  when a user tap a spcefic key on keyboard 
#event listner means waiting for an event to happen like tapping  to do an action

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    


def move_backward():
    tim.forward(-10)
    
def move_left(): # + 10 heading and 180 is full turning left and 360 means = same postion 
    tim.left(10)

def move_right(): # - 10 heading  #same 180 full turning and 360 means same postion 
    tim.right(10)


def clear():
    tim.clear()
    tim.penup() # so that it does not draw as it goes back to home
    tim.home() #turtle goees to the orgin of screen (0,0)
    tim.pendown() # to be able to draw again once back to home

# dont worry if u did not found all methods it is matter of pateincses +  time with expreine  at end of day we test code and see if working if not fix it that is software developerment so if u manage to make the project + learn mistakes that is what most important and meaens you learned the more mistakes u fix the more you learn 

#heading = turning but ya left works  

#so usually listners need a function as input 
screen.listen() 
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=move_right)

 # when we are adding a function as argument in anothr function we dont use the paranthesis 
#here function is used as an input 
#so when we pass a function as  an input we only pass the name 
# we usually bind a key stroke = key to an event we have to use an event listener 

#higher order funtion = a function that can work with other functions

# like calculator just make 5 function and give paratmer as third fun one of other func easy 

# you can not do it in all langauges but in python it is used

#w and s A D 
# Right = clockwise and counterclock wise = A = left 
#c clears all drawing

