import smtplib

my_email = "samhachem2@gmail.com"
pasrs = "233"
with smtplib.SMTP("smtp.gmail.com") as connection: #create connection
    connection.starttls() # start transport layer security is a way of secruing our connection to email server #harder for someone to inteeresept us
    connection.login(user=my_email,password=pasrs) #to log in 
    connection.sendmail(from_addr=my_email,to_addrs="alihachemnursing@hotmail.com",msg="Subject:\nhello bro")

#how does email work 

#there is an email server like gmail email server that recieve msg and if yaho server same 
#it relay on SMTP  Simple Mail Transfer Protocol = have all rules how emails how recieved or sent/stuff
#stmp =like post office and computer is mail 