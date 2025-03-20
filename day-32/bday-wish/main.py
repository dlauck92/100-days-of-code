##################### Hard Starting Project ######################
import smtplib as smtp
import datetime as dt
import pandas as pd
import random

SENDER_EMAIL = "drewlauck92@gmail.com"
PASSWORD = ""
DEST_EMAIL = ""

today = dt.datetime.today()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    # print(bday_person["name"])
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])
        
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=bday_person["email"], 
            msg=f"Subject: Happy Birthday!\n\n{contents}")
        connection.close()



