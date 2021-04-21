BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import math
import random
import pandas
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv") # this is data frame  now
except FileNotFoundError:
    original_data = data.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:    
    to_learn = data.to_dict(orient="records")
#4 steps to do 
#to translate in google sheet write =GOOGLETRANSLATE(prss on the row ,langaugee to be transalte,lanaguge to translate too) wll be like (A2,fr,en)
def next_card():
    global this_card,flip_timer
    window.after_cancel(flip_timer)
    this_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=this_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text ="English",fill="white")
    canvas.itemconfig(card_word, text= this_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)
def is_known():
    to_learn.remove(this_card)
    data = Pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index= False)
    next_card()
window = Tk()
window.title("flash card game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
canvas= Canvas(width=800,height=526) #many stuff on top of each others 

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file ="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
 
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)

check_image= PhotoImage(file="images/right.png")
right_button = Button(image=check_image,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

next_card() #so that it trigger function once 
#dont worry about the highlighted between the check mark and unknown mark it is needed to give the depression while pressing 
window.mainloop()