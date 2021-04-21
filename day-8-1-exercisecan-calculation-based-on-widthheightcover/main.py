#Write your code below this line 👇
import math 
def  paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"you will need {number_of_cans} cans") 
    





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
def calcu():

    test_w = int(input("Width of wall: "))
    test_h = int(input("Height of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)


calcu()

