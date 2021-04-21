# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n ")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0



if size == "S":
  bill = bill + 3
elif size == "M":
  bill = bill + 6
elif size == "L":
  bill = bill + 9
else:
  bill = 0


if add_pepperoni == "Y":
   bill += 3
else: 
   bill += 0


if extra_cheese == "Y":
   bill += 2
else: 
  bill += 0

print(f"your total bill is {bill}")     



