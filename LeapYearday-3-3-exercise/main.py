# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
 if year % 100 == 0:
  print("okay")
  if year % 400 == 0:
    print("leepz")
 else: 
  print("leap year")
else:
  print("this is not a leap year ")
