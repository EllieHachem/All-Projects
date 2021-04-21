from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json() #most values are in .json even when it is not mentioned
    quote = data["quote"]
    canvas.itemconfig(quote_text,text=quote)
    #Write your code here.

#basically import requests then variable = request.get(url=) then varibale.raaise_for_status() then data = variable.json() most of time it is json format then new variable = data[key]
#then use it with anything or ike now tkinter canvas.itemconfig(quote_test whih is the thing u wanna change , text(the thing u wanna change)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()