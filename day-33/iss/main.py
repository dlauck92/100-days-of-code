import requests
from datetime import datetime
import smtplib as smtp
import time

MY_LAT = 41.463303605077044 # Your latitude
MY_LONG = -81.92606819005711 # Your longitude
SENDER_EMAIL = "drewlauck92@gmail.com"
PASSWORD = ""
DEST_EMAIL = "drewlauck820@gmail.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
def send_email():
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=DEST_EMAIL, 
            msg=f"Subject: ISS Inbound\n\nThe ISS is close to you. Look up!")
        connection.close()

if is_iss_overhead() and is_night():
    time.sleep(60)
    send_email()



