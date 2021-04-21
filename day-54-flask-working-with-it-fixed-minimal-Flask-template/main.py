from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__) #creaeting object  one require which is the name and this is a special attribute and when we get __main__ it is run as script or interactive prompt but it is not running from imported module so it is like saying only if run as script then execute main 

#so many usees if __name__ = "__main__: as string:
## app.run this is equal to flask run but to use flask run we must give envorinment variable and secondaly  we must  stop code using control c  instad of using normal stopping but using app.run 

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@web_site.route('/') #when the user hit(nagvigatee) the pass and the user web_site  and route is / 

#this is called python decorateor and u will see it in advanced python projects what is it lets see u have a lot of functions in class and you want to add some functionalities to those functions u might use decorate function to do that so

#decorat = gives addtional functions to an existing function 

#we know function allow us to specfic package of function and increase resublity of function have input and allow us to get output to pass to another function or  do something with it 

#
def index():
	return render_template('index.html')

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)

@web_site.route('/page') #webapge 
def random_page():
  return render_template('page.html', code=choice(number_list))

web_site.run(host='0.0.0.0', port=8080)

#just here @web_site is function decoratar name and .route is like location if user goes there after the website name it will trigger that addtional function 
#though this is an already made template you might use it 

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

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

#once you run this code it wont work you need to export the main.py as ev that was flask is expeceting and ev = environment variable  

#use set FLASK_APP=main.py 
#then use flask_run to make it run 
#this will create a server 
#and it give us where to go and find our website 
#the 172.18.0.1 is like dns for website 
#but in offline it will give the local website address 127.0.0.1 
#and portn ext to it usually is 5000 
#so when go inspect elements here u will see flask already craeted elements of html automatically 
#press control c to quite serveer usually here it auto quite since if u dont stop it and try to run flask again with same address it wont work and it will give errors 

#now we gonna use the command line the shell to control the browser 
#what is shell 
#if  windows is the bean then shell is  the actuall nute  while the core the windows is perfered as kermal and shell is like UI user inerface for u as human to interact with kernal and hardware of comptuer 

#there is 2 types of shells/command line 

#GUI like windows defult or commmand line like cmd  cli is opposite of GUI 

#why use cli ? 
#at end of day it goes about greater control 
#more control + faster espically if u are a regular cli user 

#on windows the defult shell is cmd (command prompt)

#some common things to do in terminal and most part terminal of mac and os will work the same 


#open terminal and address of terminal is just before the root (prompt) and promote is the thing that is go and comes back and ~(this means  telda)


#first tip where I am? use pwd (print working directory ) though it is known in windows 

#next command is ls = list = list all the files in the working directory 


#better press shift and on a dictory place to open winddows power shell to work like this 


#cd = change directory to change wworking directory and u can also type the first of the path and windows will fill it automatically press tap to see all ppossibilities   
#like press tap to see suggestions then another tap 


#what if I wanted to create new folder  using mkdir = make directory and name to it
#easy write cd  and the inside directory no need to write full direcotory again 
#all command struactures are easy if u search their full abbriavatin 

#to create new file it is different we need to type touch then name of file.exetension 


#to delete a file then type rm = remove 


#to go back one folder back use ..

#then use rm -rf  remove remove folder (-rf) deletes everything  be really careful with this comand it deletes eeverything 


#so terminal here can do the same so we gonna do in flask 


#if u want to know everything about cmd or anything in genral search its sheetcheat like now terminal or cmd sheetcheat then u saved your self a lot of trouble that other than the documentation 

#but for now those are 99% of comands we are gonna use

#use them on regular bases so  u dont have trouble remembering them 


#note use the New-Item to create a new file in windows not the touch 

#echo does not work in powershell 