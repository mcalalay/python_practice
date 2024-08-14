##################### Hard Starting Project ######################
import smtplib
import random
import pandas as pd
import datetime as dt
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")
my_email = "pymac24@yahoo.com"
password = ###PASSWORD

for birthday in birthdays:
    the_birthday = dt.datetime(int(birthday["year"]), int(birthday["month"]), int(birthday["day"])).date()

    if dt.datetime.now().date() == the_birthday:
        name = birthday["name"]
        email = birthday["email"]

        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter:
            the_letter = letter.read()

        with open(f"Output/letter_for_{name}.txt", mode="w") as output_letter:
            the_letter = output_letter.write(the_letter.replace("[NAME]", name))


        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}!\n\n{the_letter}"
            )


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



