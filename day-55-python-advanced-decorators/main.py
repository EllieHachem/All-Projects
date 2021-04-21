#we used to look on simple python decorator function 
#but this does not take condition wwhat if we needed to call function with some sort of input 
#
## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name): #it have 2 properites 
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function): #we can only usually pass a function but what if we wanted to pass arguments assoicated with the function like create blog post takes user as argument it will give us user not defined since user was not defined  in that moment 
#here comes the concept of *args and **kwargs 
#in this case is is positional argument at index 0 so we use args[0]
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0]) 
    return wrapper

@is_authenticated_decorator
def create_blog_post(user): 
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

#basically the same except have thoe args and kwargs and we can add if statment and add the args to th function it self before it is really declcared 