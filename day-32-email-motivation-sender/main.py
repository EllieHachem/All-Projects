import datetime as dt
import smtplib
import random 
my_email = "samhachem@gmail.com"
password = "13213@34broA$"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:#remember datetime takes para as int and its class same as its name meme library 
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines() #to read as list
        quote = random.choice(all_quotes)

    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Mptivation\n {quote}")

