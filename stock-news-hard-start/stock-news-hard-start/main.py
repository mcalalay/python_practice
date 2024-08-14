import os
import requests
import datetime as dt
import random
from twilio.rest import Client

os.environ["AV_API_KEY"] = ###
os.environ["NEWS_API_KEY"] = ####
os.environ["TWILIO_ACCOUNT_SID"] = #####
os.environ["TWILIO_AUTH_TOKEN"] = ####

SYMBOL = "BTC"
MARKET = "USD"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
dates = [str(dt.datetime.now().date()-dt.timedelta(days=1)), str(dt.datetime.now().date()-dt.timedelta(days=2)),
         str(dt.datetime.now().date())]


AV_PARAMETERS = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": SYMBOL,
    "market": MARKET,
    "apikey": os.environ.get("AV_API_KEY")
}

NEWS_PARAMETERS = {
    "apiKey": os.environ.get("NEWS_API_KEY"),
    "q": "crypto or bitcoin or btc",
    "from": dates[0],
    "to": dates[2],
    "language": "en",
}

response = requests.get(STOCK_ENDPOINT, params=AV_PARAMETERS)
response.raise_for_status()
data = response.json()


two_day_report = [data["Time Series (Digital Currency Daily)"][date] for date in dates]

print(two_day_report)


price_close_difference = (float(two_day_report[0]["4a. close (USD)"]) - float(two_day_report[1]["4a. close (USD)"]))
percent_change = float((price_close_difference / float(two_day_report[0]["4a. close (USD)"])) * 100)
print(percent_change)
print(price_close_difference)


def get_news():
    number_of_articles = range(0,3)
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = [random.choice(news_data["articles"]) for _ in number_of_articles]
    title = [articles[index]["title"] for index in number_of_articles]
    description = [articles[index]["description"] for index in number_of_articles]
    url = [articles[index]["url"] for index in number_of_articles]

    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    for i in number_of_articles:
        if percent_change > 0:
            body = f'''{SYMBOL}: 📈{round(percent_change, 2)}% \n
            Headline: {title[i]} \n
            Brief: {description[i]}
            '''
        elif percent_change < 0:
            body = f'''{SYMBOL}: 📉{round(percent_change, 2)}% \n
            Headline: {title[i]} \n
            Brief: {description[i]}
            '''

        print(body)

        message = client.messages.create(

            body= body,
            from_ ='+14055834915',
            to='+639338202833'
        )

    print(title[0])
    print(description[0])
    print(url[0])


if percent_change > 5 or percent_change < -5:
    get_news()


