import datetime as dt #we named it so that we make it easier for us to understand more than before 


# datatime.datatime #this is usally how u import class ya same name and no capital it is confusing so we change name 

now = dt.datetime.now() #current date and time
year = now.year
#we have month/day/hour/sec/microsecond anything it will be listed
#1 = tuestday not monday cuz start from 0 
if year == "2021":
    print("bro")
data_of_birth = dt.datetime(year=1998,month=2,day=2) # we are required only threee values cuz others are ... have defutl value and all in int 