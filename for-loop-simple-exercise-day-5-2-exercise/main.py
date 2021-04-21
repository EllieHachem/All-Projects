# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

Socre_Bro = 0

for easy_naming in student_scores:
  if easy_naming > Socre_Bro:
    Socre_Bro = easy_naming

print(f"{easy_naming}")  
