#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
import smtplib

MY_EMAIL = "fakeemail@gmail.com"
TO_EMAIL = "anotherfakeeemail@gmail.com"
PASSWORD = "qwerty"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypts email
        connection.login(user=MY_EMAIL,
                         password=PASSWORD)
        connection.sendmail(

            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="It's going to rain today. Remember to bring an ☔️")

