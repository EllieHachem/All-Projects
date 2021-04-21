#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("welcome to tip calculator bro)"

Total_bill = input("what is your bro")

float(total_bill)

percentage = input("what is percentage tip you would like to give")

float(percentage)

split_people = input("how many people to split the bill")

float(split_people)

end_result = total_bill * percentage / 100

round(end_result)

print(f"your total splited bills are{end_result}[0,1]")





