import requests
import datetime as dt
import smtplib
import time

MY_LAT = 14.599512
MY_LONG = 120.984222
MY_EMAIL = "pymac24@gmail.com"
MY_PASSWORD = ###PASSWORDS HERE

#-----------------------ISS POSITION----------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
#-----------------------Sunrise/Sunset----------------#


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True


def is_close():
    if MY_LAT-5 <= iss_position[0] >= MY_LAT+5 and MY_LONG-5 <= iss_position[1] >= MY_LONG+5:
        return True


while True:
    time.sleep(60)
    if is_close() and is_night():
        with smtplib.SMPTP("smtp.yahoo.mail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up!\n\nThe ISS is above you, in the sky."
            )

