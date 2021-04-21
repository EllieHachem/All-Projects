#go pypi.org python package index spelled pypi
#focusing casing in class stuff using from and import class
#search for x. or object. or self or anything to save time reading manual 
from  prettytable import PrettyTable

table = PrettyTable
table.add_column("bro",["my man","nice","it is working"])
table.add_column("bro2",["my man2","nice2","it is working2"])
table.align = "l"
# we can print attrubite like no 
print(table.align)
#very helpful to know defult of attrubute as here it c = center
print(table)

