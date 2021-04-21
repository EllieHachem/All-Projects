# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

years_remaining =  90 - age_as_int
days_remaining =  years_remaining*365
weeks_remaining = years_remaining*52
month_remaining = years_remaining *12

message = f" you have {days_remaining} days left and  {weeks_remaining} weeks left and months left man {month_remaining}"
  
print(message)





