#local files and directories = manuplating file systems like reading and writing to file 
#todays end project is a program that replaces specrif words in a template like the name of client to send as well as some specfic words easy and automte nice hell ya 


#how to open files/read files write to files and  close them again without touching the mouse 
#use open  method which is an inbult method so no need to import 
# it have 1  a must argment(file name as location should be in same location as main.py) to put and others are optional
# file = open("my_file.txt") # python wont open it but it is already opened and python ready for next opertation 
# contents = file.read() # read method
# print(contents)
# file.close() #must close cuz when you open file it takes some resources from computer ram,cpu those stuff 
#u can write the code other way without using close() method here

# with open("my_file.txt") as any_name_here:
#     contents = any_name_here.read() # read method
#     print(contents) # see here no close and same result
 # those as u see the variable we named is now the new name of the file 

# with open("my_file.txt",mode="w") as any_name_here: #mode defult is set to read only so we must change mode in order to be able to edit files r = read only and w = write 
#      any_name_here.write("brororororro")
    # this delete all pervious stuff and replace them by this


# if you want to add and not delete we change mode from w to a and a stands for append kinda like list to be honest

with open("my_file.txt",mode="a") as any_name_here: 
     any_name_here.write("\n nice man")


# when you are opening a file that is not made by us in write mode then python will create that file for us from scratch      
with open("my_New.txt",mode="a") as any_name_here: 
     any_name_here.write("\n nice man")