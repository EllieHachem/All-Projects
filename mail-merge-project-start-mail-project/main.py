#TODO: Create a letter using starting_letter.txt
#so alwways use ./ from now on easier


PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file: 
    names = names_file.readlines() #replaces each line in a data.txt as a list there is readline method so be careful and this is read variation method no neeed to use read before using it  
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() #normal read
    for name in names:  
        stripped_name = name.strip() #removes spaces 
        new_letter = letter_contents.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_as_{stripped_name}.docx",mode ="w") as completed_letter:
            completed_letter.write(new_letter)
        #in for loop usually variable should be the singular value of what you want through 

