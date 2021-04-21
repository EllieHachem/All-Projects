#well known automation and testing tools for web developers 

#automate process to work from a script you right and program is free 

#u can do anything a human can do using a selenium browser 

#like bulding a robot to tell him what to do in a browser 

#once we finish we can even play web game 

#like games as cookie clicker 

#u can use it to automate forms like docs or transfering information from excel to online google form or anything that is repetitive  more like mouse and keyboard recorder program 


#steps to use se 

#install chrome  is best one other can work but ya 
#dowwnload chrome driver from https://chromedriver.chromium.org/downloads and it must match the verion of chrom we are using 
#move the foldeer of chrom driver  to a known folder in day 48 in a folder called development as for here install its exention 

#install and import seleniu,

from selenium  import webdriver
import chromedriver *
#usually local u put here the path of chromedriver 

driver = webdriver.Chrome() #it can be .firefox or anything else but ya for now chrome and it is chrome with capital c so we are intilaaizing an objeect her so inside () we need executable_path location where the chrome driver is the eexutable means the program that we will execute = run = open 
#se is packaag that allow us to interact with browsers 
#chromedriver is like the api/ the bridge to work with other browser properly each browser have different driver  and to help to work with lastest version or the specfic version of browser you have chosen 

driver.get("https://www.amazon.com/") #to open a site using get function usually works locally this opens browser 

#so usually we put the site we wanna scab in the get () then 

# price =driver.find_element_by_id("")
# print(price.text)

#there is many other elements than beutiful soup like 
#now most important find_element_by 
#also just type find_element_by and you will see the list below 

# search = driver.find_element_by_name(" ") #most fourms uses name elemeent 
# print(search)
# print(search.text)
# print(search.tag_name)
# print(search.get_attribute())

logo = driver.find_element_by_class_name("")
print(logo.size)

#so we can do many things with se more than soup 
#this work even if the actual link does not have anything just by going to the parents
#as the parents here is documatnion and a is the anchor in the parents 
#easiest one 
documantion = driver.find_element_by_css_selector(".documantion a")
print(documantion)


#if all fails of all those ways there is the x path 
#just go to inspect elements right click the thing you want and press copy xpath 
xpath_link = driver.find_element_by_tag_name("") #change the double quotes into single quotes inside this xpath so that it does not give any error 
#this is so easy cuz it is like a real person surfing and saves us from making a response from the request model 
#very import note u can press in inspect element the top left so locatio any element easily then just copy paste xpath 
driver.close() #to close after the chrome is opened close just 1 tab or
driver.quit() #do same but quit quits all tabs at one 
#even up when program works it will say chrome is control by automated software 

#now how to use it to find specfic stuff like beutiful soup and scap with it 

#here is also find elements and element easy  in beutiful soup find and find all 

#in a website the most unique stuff could be in div seciton 

event_times = driver.find_elements_by_css_selector(".event-widget time")

for time in event_times:
    print(time.text)


event_names = driver.find_elements_by_css_selector(".event-widget li a ") #this comes from parents to child and we did it to remove the more section 

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text,
    }

print(events)


#now we gonna work with wikipedia 
#give path of executable 
#make object
#use driver.get 
#main stuff start now 

artical_count = driver.find_element_by_css_selector("") #find elment gives us the first element founded like beutiful soup 
print(artical_count.text)
#use .text to print on console 

#usualy we dont use the first name of the div if there is 2 names then go find by 2nd name so that it is the unique thing in the div 