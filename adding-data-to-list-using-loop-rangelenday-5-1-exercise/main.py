# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(float(student_heights[n]))
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_hieght = 0

for pro in student_heights:
  total_hieght += pro

number_of_students = 0 

for pro2 in student_heights:
  number_of_students += 1
average_height =  round (total_hieght / number_of_students)
print(average_height)