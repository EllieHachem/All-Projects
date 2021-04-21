#entery widget 
#3 lable widegts 
#button widget 

from tkinter import *
#first of all importing tkintr


#2nd Creating a new window and configurations
window = Tk()
window.title("mile to km convetor")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20 )
##Entries
mile_input = Entry(width=10)
#Add some text to begin with
mile_input.insert(END, string="")
#Gets text in entry
print(mile_input.get())
mile_input.grid(column=1,row= 0)

#Labels
mile_lable = Label(text="This is old text")
mile_lable.config(text="miles")
mile_lable.grid(column=2,row= 0)

#Labels
km_lable = Label(text="miles")
km_lable.config(text="km")
km_lable.grid(column=2,row= 1)

#Labels
equal_to_lable = Label(text="is equal to")
equal_to_lable.config(text="is equal to")
equal_to_lable.grid(column=0,row= 1)

#Labels
the_0_lable = Label(text="This is old text")
the_0_lable.config(text="0")
the_0_lable.grid(column=1,row= 1)



#Buttons
def convertor():
    miles = float(mile_input.get())
    km = round(miles *1.609)
    the_0_lable.config(text=f"{km}")

#calls action() when pressed
button = Button(text="calcualte", command=convertor)
button.grid(column=1,row= 2)


#error no attribute can mean text paramter is not given
#weird error due to the fact it is a converted library 