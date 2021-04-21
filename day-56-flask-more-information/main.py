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


#create new html file create it as a normal site 
#flask is not library it is framework net set of rules so in order to use the html we need to put it in a folder 
#from flask import render_template  method 
# return render_template(pass file name )
#this save time as u also get assistance when writing html in html editor 
#so when fusing  codes or writing hug projct that consists of many cods bttr makee each with its prefered editor 
#.htm is like html but some service does not accept 4 letter exetions 
#name should always be in one not spaces 

#the html will work but not the img since it is a static file we will not discus it 
#save as to download page as html 
#rendered = uses or like conevrted to be able to be used 
#so render html = converting html to be used 

#even if we add imagee in same folder as html and changed name of location of img it wont work 
#same as html we have put it in a folder named template
#images should be in a folder called static
#both folders not capitlzied #though change path to static/image_name

#most flask applciations need static and tempalte folder 
#templates just for html 
#and others like css/videos/images /static files nearly everything in static 
#dont forget to add the html basic template from here in replit so that it work with flask 
#chrome likes to cache static files 
# means if the background color was pink and u changed it to red it will remain cuz it will remain on cache 
#since wbsitee is unlikely to change in one day to save bandwith that is cool for live website  not for testing 
#to fix it we need chrome to do hard reload by pressing shift reload = delete all cache files and pull new files of a certain website very helpful if u are facing bug instead of deleting all caches as u always do.

#index.html = first page shown to user more like home page 
#change always the path to new one when using flash cuz there is always 2 folder used in process which are static and templates 

#in pycharm use control r after hoverign in a common world and replace all its variation to save time 

#gradient image = is like blurry hidden image to hide contents


#in flask u can add as much folders u want inside the static and tempalte as long as u 
#specify the path at end 