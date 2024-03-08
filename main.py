import smtplib
import datetime as dt
import random

my_email = ""
my_password = ""

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 0:
    # open a file quotes.txt
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote = random.choice(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg="Subject:Monday Motivation\n\n{quote}"
        )
        print("Email sent successfully")
