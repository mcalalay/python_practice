import requests
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = #####
TWILIO_AUTH_TOKEN = #####




URL= "http://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "appid" : "118dd1bf29a6f536819f3d68447dc3aa",
    "lat" : 14.599512,
    "lon" : 120.984222,
    "exclude": "current,daily,minutely"
}


response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()

data = response.json()
print(data)
# first_hours = [data["hourly"][i] for i in range(0, 13)]
first_hours = data["hourly"][:12]
print(first_hours)

for weather in first_hours:
    if weather["weather"][0]["id"] > 500:
        reminder = "Bring an umbrella. It gonna be a rainy day ☔"
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=reminder,
            from_='+14055834915',
            to='+639338202833'
        )
    else:
        reminder = "You are fine."


print(reminder)

