#flask is one of the most web development framewwork 

#now libarby vs framework 

#both are package of code but see tablee for full differeence though one of the biggest differences is 

#Library you call to do something specfic where framork you have to obey by rules and when it comes to trigger certain functionality is thee framework that calls upon your work 
#ya near api charachteersitcs 

#remebr when we used the request library 

# we use request.get this is us tapping into library and telling it to do something 
#now in framework it does not work as this it work as 
#we giving the code and the framework will call wheen the time is right all we have to do is plan to certain situation more like if  

#like just say making a function hello world that return hello world 



#never write file name of code like main.py  to be same as library or framework name like 
#if ur file name is requests then u import requests then the code wont work 
#exit code = 0 means everything as successful
#you can also use pip to install packages is something that allow use to install packages from pypi so anything from there (pypi) you can install  using pip 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#once you run this code it wont work you need to export the main.py as ev that was flask is expeceting and ev = environment variable  

#use set FLASK_APP=main.py 
#then use flask_run to make it run 
#this will create a server 
#and it give us where to go and find our website 