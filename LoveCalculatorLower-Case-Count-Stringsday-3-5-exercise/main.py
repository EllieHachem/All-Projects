# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator bros!")
name1 = input("What is your name bro? \n")
name2 = input("What is their name bro? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name3 = name1 + name2
lower_case = name3.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true =  t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if love_score > 10 or love_score > 20 or love_score > 30:
   print(f"your score is {love_score}")



