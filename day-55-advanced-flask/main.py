from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__) 

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@web_site.route('/') #website is an object that lives in the flask class 
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


# @web_site.route('/bye')   #so here wwhen u go to /bye it will bring bye
#     return "Bye"

#passing url means getting hold of url = using url like / in route  
#so pass variable it is like this 

# @web_site.route('/username/<name>')   #so here wwhen u go to /bye it will bring bye
# #just use <> to declear variable it can be even ithout usernamee 
# #but for all changes u must restart server  
# #but is pretty pain to keep restarting server to change its files 
# #there is debug mode it is usually off 
# #if on it will auto reeload server for any change / activate debugger/  enable debug modeo n flask application
#     return f"hello {name} 

# if __name__ == "__main__":
#     web_site.run(debug=on)

#to enable debug mode     


#then we get debugger pin and have it active 

#in debug the server would remain but give u error if u make in changes and gives u the error on the client side 


#we can open debugger on sit and it will ask for pin code so that somone else can not mess with ur code if u have the site on debug mode 
#this would open console for u to diagnose 

#we can add path before or after variable 


#there is something called convertor = converts url into any data type you want 
#by defult it convert it to a string means accept any text without a slash or have more than one variable like convettor:<variable>  and convetor can be int or anything specficed on document this is called vairable path 


#noww render actually html cuz usually flask defult just stuff everything in a body tag without any real html tag that gives it structure that not what u want when u make a website 

#flask accepts in return that is simple way to add  like return h1 tag and it will create it we can give inline css with it too 

#what if u wanted to rendeer more than one html element all you have to do is continue typing so after tag is closed add anotheer tag easy like creating a website n same line if 
#Line so long u can add \ and add as many string as you want 

#2nd way instead of adding as strng u can create decorator functions and reuse them 

