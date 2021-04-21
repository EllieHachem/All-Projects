from selenium  import webdriver
import chromedriver *
from selenium.webdriver.common.keys import keys  #here to import from selinum folder inside it webdriver folder inside it common driver inside it drivr as you see here they are seperateed by . and then import keys from keys folder it import constants to use like programing a charachter cosntants such as ENTER 

#to click on something 


#get hold of elment then use .click() on it like u usually use .text to print on console 


#usuall people use  find_element_by_link_text("here name of text of line") then they use 
#click()

#what about typing ? 
#firt get hold of search bar 

#find_element_by_name("search usually ") then search.send_keys("type the thing you wanna type here ")

#to use return/enter key we must import new thing when we want to send a key that is not a lettr or one of the numbers or symbols 
#then use search.send_keys(Keys.Enter) Any key on keyboard works here 


# firt_name = driver.find_element_by_name("fname")
# first_name.send_keys("bro")

# last_name = driver.find_element_by_name("lname")
# last_name.send_keys("bro2")
# email = driver.find_element_by_name("email")
# email.send_keys("man@gmail.com")

# sumbit = driver.find_element_by_css_selector("form button")
# sumbit.click()