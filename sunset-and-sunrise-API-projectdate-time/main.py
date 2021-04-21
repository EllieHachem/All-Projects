import requests

#go to https://www.latlong.net/ to find those for ur country 
from datetime import datetime
MY_LAT = 33.854721
MY_LNG = 35.862286
FORMATTED = 0
paramters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":FORMATTED, #GIVE HERE , EVEN IF NO KEY AFTER IT
}
response = requests.get("https://api.sunrise-sunset.org/json",params=paramters)
response.raise_for_status() #this code wont run unless you give paramters that is why when you run it solo it will give 400 error = bad request
data = response.json() #MAKE SURE EXENTION IS WROTE SAME CASE TOO NOT JUST NAME 
# print(data) #if getting error has no attribute =  u must install the external package 

#so to add paramters to end point write the endpoint then question mark then thee paramters and fused with & mark #an exampl shown here 

#https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] #the code made one in print(sunrise.split("T")[1].split(":")[0] is used)
sunset = data["results"]["sunset"].split("T")[1].split(":")[0] #samee sunrise is used here 
# print(sunrise.split("T")[1].split(":")[0]) #very cool concept as here we split from the 2 into 2 index then from second index we split the : then we call it again 
print(sunrise)
print(sunset)
#this way we have the other format
# time_now = datetime.now()
# print(time_now.hour) comparing just data time to sunrise time pretty epic 



