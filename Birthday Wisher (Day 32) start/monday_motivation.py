
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
quotes = []
with open("quotes.txt", mode="r") as data:
    quotes.append(data.readlines())

print(quotes)

my_email = "pymac24@yahoo.com"
password = ###PASSWORD HERE

if now.weekday() == 0:
    the_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pymac24@gmail.com",
            msg = f"Subject:Monday Motivation!\n\nQuote of the day: {the_quote}. Keep believing! You got this."
        )



