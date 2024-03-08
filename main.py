import smtplib
import datetime as dt

my_email = ""
my_password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=5, day=15, hour=4)

