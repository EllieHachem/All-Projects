#how to creat our own class own blueprint
#type class keyword and anme of class in pascal case 
#model = create
#use pass to write empty code and negate indentdation error 
#pascal case = first letter capiclizated
#camel case = first word is lower but other is like pascal
#snake case all words lower case but sepearted by underscore 
#not much camael case in python
# class User:
#     pass


# user1 = User() # this is how u create an object 


# #how to create attrubiute 

# user1.id = "001"
# user1.username = "bro"

# print(user1.username)


#but if we have a lot of attributes
#construcotr = part of blueprint what should happen when our object is construct knoww in programming as intializing an object = set an object to their starting values with their basic attributes which is the __init__ like int but i  and 2 undeerscore from both side intilaized attributes 

# like this  and add a self in it or name self anything but use it
#u will see how later 
# so init and self we add paramteres(passed to an object as attrubute)
#so it is like function but self is never used as it is the object and counted as first input 
class User:
    def __init__(self, user_id, username): #remeber def (input here must always be filled)
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following =0 
    # alwayas make sure to put attribute and meethod in same class so that u dont get attrubute erros 
#init require all arguments those beetween( ) which are paramter 
user1 = User("bro", "123")
user2 = User("bro2","234")
print(user1.user_id)

#to also negate that argument error u can just put everything as normal but without putting it up in the parameter 
print(user1.followers)


#attribute = has and method = does like speed = 5 and we do method to change speed to 5 methods are normal like normal function
#must always have self 


user1.follow(user2)
print(user1.follwers)
print(user1.following)
print(user2.followers)
print(user2.following)