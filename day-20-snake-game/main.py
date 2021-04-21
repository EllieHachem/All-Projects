from turtle import Screen, Turtle
from food import Food
from snake import Snake
from score import ScoreBoard
import time 
#note gray in pycharm means not used happens 
screen = Screen()
screen.setup(width = 600, height = 600) #more clear to us and person seeing the paramters so they can know function with just seeing paramters cuz setup sounds bit wierd tbh 
screen.bgcolor("black") #bg  = background 
screen.title("my snack game")
screen.tracer(0) # to make the game stop drawing pixel by pixel 
#then u use update method after code to just show it being draw at high fram so that it appar as normal 

#so turtle have 20 by 20 and 600 = 300 in terms of x and y so each 2 pixels = 1 in term of x and y 

# segment_1 = Turtle(shape="square") #segment = part = piece 
# #defult is 0,0
# segment_1.color("white") 
# segment_1.penup()
# segment_2 = Turtle(shape="square") #segment = part = piece
# segment_2.color("white") 
# segment_2.penup()
# segment_2.goto(-20, 0)
# segment_3 = Turtle(shape="square") #segment = part = piece
# segment_3.color("white")
# segment_3.penup()
# segment_3.goto(-40, 0)

# game_is_on = True

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up,  "Up") # all are case sensitive 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
  
while game_is_on:
    screen.update()
    time.sleep(0.1) #delay
    snake.move()
    # new_x = segment_1.xcor()
    # new_y = segment_1.ycor()
    # segment_2.goto(new_x -20  ,new_y )
    # new_x_2 = segment_2.xcor()
    # new_y_2 = segment_2.ycor()
    # segment_3.goto(new_x_2 -20 ,new_y_2 )
    #now detecting collision with food 
    #we are gonna use the distance method as it compare 2 objects distances 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:         
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over() 
            
        #detect collision with tail 
        # pass like break in while loop for if else 





    
  




screen.exitonclick()