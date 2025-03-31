import smtplib as smtp
import datetime as dt
import random

SENDER_EMAIL = "drewlauck92@gmail.com"
PASSWORD = ""
DEST_EMAIL = "drewlauck820@gmail.com"

now = dt.datetime.now()
current_day = now.weekday()

def send_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL, 
                to_addrs=DEST_EMAIL, 
                msg=f"Subject: Thurday Motivation\n\n{quote}")
            connection.close()

if current_day == 3:
    send_quote()
# print(current_day)

