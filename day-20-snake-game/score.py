from turtle import Turtle
#use constants to make code way easier like NameError

ALIGMEENT = "center"
FONT = ("Arial,24,normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score{self.score}", align=ALIGMEENT, font= FONT) 

    def game_over(self):
        self.goto(0,0)
        self.write(f"gameover", align=ALIGMEENT, font= FONT) 

        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        

