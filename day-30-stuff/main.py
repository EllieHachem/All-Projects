#json stuff 
#error handle stuff 
#handling erros and exceptions 

#file not found = fix file name or filter
#keyerror: key doees not eexist in the dictonary
#index error = index out of range 
#type error = pieace of data is str and int = opposite
#those are most famous errors but there is exceptions 
#here is example when dealing with them
#try,except,else,finally so 4 normal erros and 4 codes to deal with exceptions 
#try : something that might cause Exception
#except: run with the Exception
#else:do this if there was no Exception
#finally run code no matter what 
#an example
# so erroor now is FileNotFoundError

try: #so try means try youu use it with except like if 
    file = open('a_file.text')
    hro= diconartyadasd+"23" #it will cause an error cuz we do not have a file called that
except FileNotFoundError : #if there is an error it will do this else
    # print("There was an error ") #printing error is meme we must make except to work no matter what happens the program will work 
    #like if file does not exit we create it
    file = open("a_file.txt",mode="w")
    file.write("something")
else:
    content = file.read()
    print(content) #if not exception and try worked so we use  so else work if try work
finally:#code that runs no matter what happens
    file.close()
    print("file is closed ")



#here it skipped the error of diconary so except should have the error name like file not found next to it so that it does not skip

#except is a cool way to run program in aplha state with many bugs lol 
# we can have multiple exceeption to negate just 2 errors epic  too
#you can also say except error_name as error_message: then put except in f string so that program still run but gives the error 

#example 

# except KeyError as error_message:
#     print(f"this{error_message} does not exit") #pretty cool to show error without crashing program 


#final keyword is raise which allow us to raise our own exceptions

#like here is an example

finally:
    raise TypeError("you can also write msg here") #so an error will appear no matter what
#keyword / caluse
#u can use raise with if state/clasue/keyword or anything nearly

