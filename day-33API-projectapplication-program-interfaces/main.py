# application program interfaces  = API 
#why we use it to create ISS trackeer = international space station 
#it is on top of earth and circles earth many times a day 
#we need to track where currectly the ISS in the sky 
#then email once it is in a particilure location 

#API? = set of commands funtions proctolcs and objects that programs can use to create software or interact with  external system(like extract data from websites)

#api = barrier/interface between ur program and external system
#like how u  makes app on windows for andriod/iphone 

#so we use API rule that presecribed to make a request to the external system(website)
#so if u have request from API with all requirments then they respond and give data

#like yahoo weather have yahoo weather API that we can use for weather sites 
#coin base also have like for stock sites 
#nba also have api  like for betting sites
#websites are resturant and data is like kitchen we can not go to kitchen and take their 
#food 
#we have a menu = API  things that tells what u can order and what u can not 
#My Tummy = Api(Menu) = Kitchen

#Api and library difference? API is restricted library that need communication most of time 
#with server or just another software/library 

#api endpoint = location
#so if we gonna get specfic data using API so we need to know the location of the data where it is stored like money of bank where is the bank ? #that is called API endpoint 
#it is mostly URl  
#LIKE crypto data api.coinbase.com
#API request on internet = like we know locaiton and know we must request money format we need a teller that tells the request like that person on bank that asks it for details 
#request depend like asking for opening hours is simple no requiremtns but some asks for requirmeents like wwhen you want to talk money they ask for id and stuff 

#ISS current location API very simple 
#json was for javascript now it is for everything 
#json is like flat is like dictonary with 1 line easy to read instead of making it hard 
#but as python dicontary it become normal as diontary 

import requests #a library used to request data from endpoint 
#is best to work with apis 
#in python pypi.org u can see statics to see how much popular is package is how good and to see if developed going good for it like requests it is cool 

response = requests.get(url="http://api.open-notify.org/iss-now.json") # to get data from endpoint")
response.raise_for_status() # so that we dont writee the error number and what it maens really saves times than saving if elif

data = response.json() #usually with exention last one from url
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longitude,latitude)
# print(response)
# print(response.status_code) like response code 
#go type https status code to find all status codes(rsponses) and what they means 


#lets see how to use response codes 
#reponse coDE? It shows if our request worked or failed like 404 reponsee codee
#the thing u are looking for does not exist
#u can summarize by looking first number example
#1xx = hold on something is happening this is not final
#2xx = here you go evrything went as excpected
#3xx = go away = no permission
#4xx = you screw up like 404  
#5xx = I = server screwedd up maybe server is down or website down or other issue 