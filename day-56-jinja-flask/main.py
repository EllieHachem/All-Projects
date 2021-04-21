from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@web_site.route('/')
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

@web_site.route('/page')
def random_page():
  return render_template('page.html', code=choice(number_list))

web_site.run(host='0.0.0.0', port=8080)

#most of time u want to create html from scratch 
#that is why jinja it is build for python 

# we need simple flask application 
#create html file and name it index 
#import render_template method 
#jina is in flask so no need to install and it is speecfic for python and it is in template  folder 
#using in templates {{}} will make it a python code 
#when we are working with something that requires an import we should write the import in main server location + save the funciton in a variable to add in an argument after the index hml in the return **context = same as **arg or **kwarg so ya import then make variable with value then use the variable  name as arrgument and inside the tempalte use parameter too with the argument #KEYORD ARGUMENT REEMEMBER 

#so now our page gives dymanic data as everytime we refresh we get a random number pretty epic tbh 
#python expression = python codes 

#hardcored  text = text that does not change automatically = not coded dynamically like random generator

#route spelled rawt = path 

#object.rout("/page/<variable>")
#def funcction(vairbale)
#this need to be written to make code function properly 
#.title() = title case = first letter is capital = like used for names 

# so far we were creating single statment but what if want to create multiple like if statment or for loop 

#npoint.io is cool u can even create json that is like api then u save them in requests then use them on server 

# for multi line we add {% and close it as for other line nested they can have normal line {{}} and end is with them {% endfor %} also add endfor inside 

#same for if else say endelse and say endif 


#url bulding = direct user to a specfic page and it can be dynmaic 
#use anchor tag href and {{url_for(name of function here )}}