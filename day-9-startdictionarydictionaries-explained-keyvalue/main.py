programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and    over again.",
    "loop":"a meme test"
}

print(programming_dictionary["Bug"])


#adding new item in dictionary

programming_dictionary["okay"] = "okay bro"

print(programming_dictionary)


#create new empty ditionary is like list

bro_empty = {}

# for list same but []

#wipe an existing dictionary 

#programming_dictionary = {}
#print(programming_dictionary)

programming_dictionary["Bug"] = "wow"
print(programming_dictionary)


#looping through a dictionary it is tricky

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
