import requests 
from twilio import Client 
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "G8PEDQN8FLLNQ80H"
NEWS_API_KEY = "10b6f8ea455144058fa971459dcc087f"
TWILIO_SID = "38pBm8pU2KkkBeCczLhTwXRCXD3W91Jha4" 
TWILIO_AUTH = "083481ae660c9f94bd9bfcf7a61beb56"
#EQUITY = CAPITAL = COMPANY LIKE IBM OR TSLA =stock namee = stock usually have 4 letters  max that is why it is abbrivated 

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = { #this is dictionary to use in request of api
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT,stock_params)
data = response.json()["Time Series (Daily)"] # to access this dionctary inside the json file 
#request + url and params saved in constant varibale + dicontary params inside a varaible called response

data_list = [value for (key,value) in data.items() ] #using comprehension list to acceess just the value not th keys withc each days data 
yesterday_data = data_list[0] #ya no need to have day we use index
yesterday_closing_price = yesterday_data['4. close'] #all have same key to close yes with spaces weird but what you gonna do it is common and saves a lot of time 
# print(yesterday_closing_price)
#todo list in pycharm get indented be careful from this it gives error as all codes after it are intendeed 
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#done up now to do 2 


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1] #easy 
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
# print(day_before_yesterday_closing_price) #this is simple we printed both days and comparing the closing prices 
#done lets do the todo 3 
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#python abs function 
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(difference) #abs just gives value in positive 
#todo 3 completed now 4 
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
# print(diff_percent)
#done no lets do to do 5 
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 0.1: #usually 5% or 10% will make u buy not 0.1 but for the sake of testing we used 0.1 
    
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    #have 2 end points everything is better
    news_params = {#most articals tend to show company name rather than stock 
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,news_params)
    articles = news_response.json()["articles"]
    #done number 5 and 6 now 7 ya we did it in 5 but lol
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
# print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#ya we take commmon stuff to show like title and description 
formatted_articles_list = [f"Headline:{articles['title']} .\n Brief:{articles['description']}"for articles in three_articles ]
client =Client(TWILIO_SID,TWILIO_AUTH)

for articles in formatted_articles_list:
    message = client.message.create(
        body =articles,
        from_ ='+19284874588',
        to = '+16305342963',


    )
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

