#we gonna create habit tracker using piexal api =japanese developer 
#shows intensity of how u did a day like high colored = read a lot of pages 

# we used get requests 

#there is 3 others  than get request which are post  put  delete 
#the code looks pretty much the same 
#get = ask external system for particaluar pieace of data they give that in a response

#post request we give data and we just want a reseponse of success or NotADirectoryError#
#like posting data to google sheet that means post !or post a tweet all through a post request 

#put = update external data in the external service like updating values of google sheet =updating(editing) a twitter post 

#delete = delete external data in external service = deleting a post or deleting a google sheet 

#go  to pixe.la there is 6 steps to follow 
#token is like an api key  and here in this api it should be from 8 to 120 charachter 
import requests 
from datetime import datetime
USER_NAME = "bro234135"
TOKEN = "brorororororoadsaddada"
PIEXLA_END_POINT= "https://pixe.la/v1/users" #most data are usually in string even numbers though numbers just try without string first but ya go non string if failed it will show the error (should) in console but in case they dont show 
#this dictionary made here is a json data 
GRAPH_ID ="graph14"
user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#usually see get started + open doc at same time lol #once u make the first basic api you can rock and make it better easily 

# response =requests.post(PIEXLA_END_POINT,json=user_params) #what aree the praramters/inputs that we wanna give to server? so first of all is the endpoint which is usually in guide after a word post 
# print(response.text)
#try to never start a name with a number so that it does not make errors but number after a charater 
#colors here are named in japanese so ya  sora = blue
GRAPH_END_POINT = f"{PIEXLA_END_POINT}/{USER_NAME}/graphs"
graph_para= {
    "id":GRAPH_ID,
    "name":"hahagraph",
    "unit":"hr",
    "type":"float",
    "color":"sora",
}
headers = {
    "X-USER-TOKEN":TOKEN,
}
# response = requests.post(url=GRAPH_END_POINT,json=graph_para,headers=headers)
# print(response.text) #get response as text
#ALWAYS PROVIDE PARAMTERS ALONG ARGUMENT SO THAT THE ONE READING IT KNOWS WHHAT IS HAPPENONG
#PLUS WAY LESS ERRORS LIKE NOW THE CODE WOULD NOT WORK IF WE HAD NOT GIVEN THE PARAMTERS 
#ALONG THE ARGUMENTS 
#3 ways to authiticate api key paramater like usually with request
#X-Api-Key  HTTP header 
#via the authorizat HTTP header 
#first one is like putting in browser  =  bad way anybody can hack/sniff us though it is HTTPS and s stand for secure but still u can be hacked if someone have virus on ur pc  and sometimes it might be leaked 
#follow step by step as her so that u dont waste time and get confused since each step #
#in programming is a meme that need to be checked 

PIXEL_CREATION_ENDPOINT = F"{PIEXLA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now() #this give us date format but not same as api ( that is normal )
#use method called strftime 
#she uses w3school quite alot while making project +  if she have error she search
#stack flow 
#you can give paramters here year,month,day then it will format it as well 

pixel_data= {
    "date": today.strftime("%Y%m%d"), #you can add dashes here too 
    "quantity":"10",
}
# response= requests.post(url=PIXEL_CREATION_ENDPOINT,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint = f"{PIEXLA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"4.5",
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text) # do not forget to always print response in a text format 

delete_endpoint = f"{PIEXLA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers= headers) #delete does not need data cuz it is deleting lol obvs

print(response.text) #alwaysa print out the print that you usee for test so that you dont get confused + save time worrying about naming the print name since like here all took same name 

#change the dictionary of quanitiy to input + data to now so that you can daily us this program to track your habits pretty cool 