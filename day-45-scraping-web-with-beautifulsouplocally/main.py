# some websites does not have api so we use webscarbing 
#or api does not let us do what we want to do 
#webscarbing = look in underline html code to get the information we want 
#so today we will learn how to make soup beautiful soup it is a library that help people like us make sense of websites like even webpage as google.com if we see page source it is so big and complicated and if u want to make sense of it and pull main important information then we need html passer like beutiful  soup to pull out the html stracture once we make it we can take any website so at end we can pull data with the stracutre pretty epic to copy websites too 
#beutoful soup is used to pass html data = helps you extract data contained in a website 
#it can also pull data from xml files and html are both stractural langauges 
#it saves us a lot of time to geet the data you want from a website 

from bs4 import BeautifulSoup #bs4 means beutifulsoup 4
import lxml 
with open("website.html") as file: 
    content = file.read() #once file is read then we can save it as content 
    #now we can start using beutiful soup 


soup = BeautifulSoup(content,"html.parser")
# soup = BeautifulSoup(content,"lxml")
#creating new object from that imported class 
#markup = the html site 
#next paramter is the passer = what type of document is this = it can be html or xml 
#called parser 
#though better use lxml we install and import it 
#html parser gives error sometimes os ya stick to lxml 

#now this soup object allow access various part of our website using code
# an example

# print(soup.title)
# print(soup.title.name) #name of title tag is title 

# print(soup.title.string)

#note very important soup here is basically the eentire html site

# print(soup)

#there is a method called prettyfiy that indent all the site to make it look more clear 

# print(soup.prettify())

# print(soup.a) #this give us the first anchor  tag in our website 

#we can change/swap this with first p or first li = first paragraph or list 
#but what if we want all the paraghraphs and achor tag in our website 

#then we use a meethod called find_all it is the most commonly used 

#example 

# all_anchor = soup.find_all(name="a") #change this a string to anything u want to find 
# print(all_anchor)

# #what if we want to just know the text in the acnhor tag 

# # we neeed for loop 

# for tag in all_anchor:
#     # print(tag.getText())  #this method prints all the text in the anchor tag 
#     #what if we want to get hold of the hrehf the link
#     print(tag.get("href")) #it will give thee link we used the get method alone 

#using the find_all method we can not just search names but also search attributes very useful if we want to search by id/class  

# heading = soup.find(name = "h1",id="name")   #or soup.find_all() #this seearches for first item in quiry that is usually the defult

# print(heading)

#same with class 

# section_heading = soup.find(name="h3",class_="heading") #easy fix use _ after class to fix the resvered keyword bug usually in most library they do that for resvered keywords 
# print(section_heading)
# #though we usually get error cuz class keyord is a resevered keyword in python = special word which can only be used for creating class if other word the same resvered keyword means a word that can only be used to do one thing like pass or break

# print(section_heading.getText())
# print(section_heading.name) #name of tag
# print(section_heading.get("class"))

#those wasy might not work cuz some sites are so big and that is by narrowing the thing by its unique like this anchor tag is inside a p tag inside an em tag inside a strong tag

#we can use seleectiors 
#example

company_url = soup.select_one(selector="p a") #select gives all matching item and selectone one just the firt matching item
#so here we are looking for an anchor tag that sits in a paragraph tag and this string 
#is the css selector 

print(company_url)

#we can also use the class or id 

name = soup.select_one(selector="#name") #to select id we use pound sign = hash tag then name of id  #same as id using in css we use # 

print(name)
#note css selector is how u work with css like .class #id and normal p a where a inside p
#both and p are tags so it is a tag inside a tag it can be different tags 
headings =  soup.select(selector=".heading") # same as we using in css we use . for class

print(headings)


#this can be useful to seend our self daily msg to see the most highest number all those  cool for statics 