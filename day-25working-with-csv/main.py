#work with csv files (data files) with a library called pandas 
#most popular python data anylsys library (pandas)
#now to read data files in python 
#csv is called comma seperated values  #usually it is data seperated by comma but in excel it appear different 
#csv very common way of representing tabular data = data that fits into tables like spread sheets each row is a set  of data and each piece of data is seperatey a comma 

# basic way 
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#main way 
#python is heavly used for data analysing and processing = a lot of tools to work with tabular data like this 
import csv 

with open("weather_data.csv") as data_file:
   data = csv.reader(data_file) # method of csv library to read csv data files 
   print(data)
   #so it created an object that can be looped through 
   #like here the for loop variable was named the meaning of it not the singular data  kinda cool to make  csv to be read as txt 
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
# print(temperatures) 
# we did so much to do this code so we should use pandas library to make life easier
#pandas have a good documtion 
#getting started is the most important  thing in a guide  

# import pandas 

# data = pandas.read_csv("weather_data.csv") # makes it turbular data 
# print(data)
# print(data["temp"])
# print(type(data))
#pandas have 2 data types series and data frame 
#check know type it is dataframe 
#data frame = whole table 
#but series means part of the table 
#very epic = single list = single collmon = y axis 
#row = x asis = h  rowxh
#colum = y = v columyv
#api reference  = methods to be used on data types 
#use type to find data type before u use stuff on it from api refreance
#api is like data type 

# data_dict  = data.to_dict() #convet to dicontary 
# print(data_dict)

# temp_list = data["temp"].to_list() # now we used series methods to print the list from the column temp 
# # print(temp_list) # we can do to it as any list like using len function 

# # average = sum(temp_list) / len(temp_list) #average = mean
# # print(average)

# #another way and easy

# print(data["temp"].mean()) #this is like dictonary  #here string/key
# print(data["temp"].max())
# #or 
# print(data.temp) #so 2 ways but better first way   #this way is like an object #here we use attribite
# #all are case sensitiv though 


# #get data in rows 
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Monday = data[data.day == "Monday"]
# print(Monday.condition)
# Monday_temp = int(Monday.temp)
# print(Monday_temp)
# Monday_temp_F = Monday_temp * 9/5 + 32
# print(Monday_temp_F)


#create dataframe from scratch 
#bring any diconary then type 
# data = pandas.DataFrame(nameofdicontary)
#we can also conver it to csv
# data.to.csv("new.data.csv")

import pandas 
data = pandas.read_csv("weather_data.csv")
print(data)
#print(data.temp)
#print(data["temp"])
# print(data[data.temp == 12 ])

# new_data = pandas.DataFrame(dicname)
# #then 
# new_data.to.csv("new_name.csv")
