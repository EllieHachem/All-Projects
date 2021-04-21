# normal programming = procdueral 
# oop = object oritned program = more complex = used for teams 
# it models real life project like virtual resutrant 
# so we have manager waitress and cleaner and cheft 
# if we need to modle waitrness we need to know what it has and what it does 

#what it has? holding ap lat  = true which tables is it resposible for
#what it does ? take an orer to chef or payment and add money to resturant 


#object is made of attributes and methods  has and does 
#has variables/ list and does functions we call it a method cuz it is a function for a particaler object and attribute is a variable associated with object it is not a free floating variable (not attached to an object not attacked to main.py free floating functions is the same and waitress is called module/library)

#in nut shell OOP we are trying to modle a real life objeect   and those objects have attrubites and methods has things and can do things
#the attribites  moduled(made with) variables and as for methods meoduled by functions so remember oop is an object it can be waitress or sonic of real life thing so waitress is called object but we can have more than one object and thy all are derived from something called class

#oop > classses/class blue prints that contains objects that repulicate real stuff stuff  more like warframe blueprints where we farm items to create an object that is related to the class of primary weapon or seconday weapon when it says installing press run then check if it iis in installed packages section in package Stection press - to remove pacakg section  
#afer installing we import normal
# to see source code go to implemenation in pycharm or here gethub to set
#all we have to do is look at documantation for project in  toturial wiki and see how to impletment it in our project  


#not from pythin = external library/module/program and in pythin is called in build library/module/program 

#now to practice using mehtod and attriutes of this package always go to documenation 


from prettytable import PrettyTable #this is class see the Big capital letter wwe need to create an object from this classa 
#this to create an object form class 
#in documantion x = object 
#x = PrettyTable() x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
#so he gave the attribute and the method = easy 

Table = PrettyTable() #so here giving attributes = making the object or giving variable to object or naming it 

Table.add_column("Pro",["1","2","3","4","Sydney","5","nICE"]) #giving function to it like .lowerfunction 
Table.add_column("okay",["5","7","8","4","Sydney","5","nICE"])
#using attrbiite here as function but wwe do = mostly style and most stuff is like this  for attribute 
#style = attributes but functions = methods list or dicontaries all are in functions though just read manual easy stuff 



Table.align = "c"

print(Table)


 

#imaging traviling japan then ur tshirt get dirty u dont know city u dont know langauge even currecny u dont have so u go to hotel and probaly they have someone who speak english and u tell her ur t-shirt is soiled = got dirty they tell u they have everything they can pay them in local currency and find dry cleaner OBJECTS
#Works the same imagine you have hotel object all you have to do is to
#call its associated method hotel.dry_cleaner()