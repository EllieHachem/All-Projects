#turtle only work with .gif format 
import turtle
from turtle import Turtle, Screen
#coordinate = spelled like cowardinate = x,y postions = coor 
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif" #epic storing path ways 
screen.addshape(image) # this add shape to turtle
turtle.shape(image) # and here we added the image to turtle 

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) #wwe use this method and put inside of it this function that have 2 inputs 

# turtle.mainloop() # better replaced for exitonclick = keeps screen open 


#though we have better way

answer_state = screen.textinput(title= "guess the state",prompt= "what is another state name")