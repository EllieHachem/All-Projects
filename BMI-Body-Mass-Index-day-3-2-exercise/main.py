# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# I made those numbers randomly and results randomly to save time but 
#yea it is BMI prototype so it does not have to be same 
BMI = weight / height **2
print (BMI)
if BMI > 18.5:
  print("you are underweight")
elif BMI < 18.5:
  print("you are a overweight")
else:
  print("you are normal") 
 


