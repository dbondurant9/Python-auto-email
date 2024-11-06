#!/usr/bin/python3
import datetime
import yagmail
import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"Denver","days":"1"}

headers = {
	"x-rapidapi-key": "d4a6ba82bcmsh6cd932f93707a5fp199230jsn04744ae45b50",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())
data = response.json()

template = open("/home/kali/weather_email/weather_template.html")

email_body = ''
app_pwd = 'fecotoubpeynixkb'
email = 'cyber.project129@gmail.com'
send_to = 'dbondu16@gmail.com'
datetime = datetime.datetime.now().strftime("%m-%d-%Y")
subject = 'Weather Forecast for %s'%(datetime)
high = data['forecast']['forecastday'][0]['day']['maxtemp_f']
low = data['forecast']['forecastday'][0]['day']['mintemp_f']
rain_chance = data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
rain_tot = data['forecast']['forecastday'][0]['day']['totalprecip_in']
max_wind = data['forecast']['forecastday'][0]['day']['maxwind_mph']
city = data['location']['name']
state = data['location']['region']


for line in template:
    if "DATETIME" in line:
        line = line.replace("DATETIME",datetime)
    if "HIGH" in line:
        line = line.replace("HIGH",str(high))
    if "LOW" in line:
        line = line.replace("LOW",str(low))
    if "RAIN_CHANCE" in line:
        line = line.replace("RAIN_CHANCE",str(rain_chance))
    if "RAIN_TOT" in line:
        line = line.replace("RAIN_TOT",str(rain_tot))
    if "MAX_WIND" in line:
        line = line.replace("MAX_WIND",str(max_wind))
    if "CITY" in line:
        line = line.replace("CITY",city)
    if "STATE" in line:
        line = line.replace("STATE",state)

    email_body += line

with yagmail.SMTP(email,app_pwd) as yag:
    yag.send(send_to,subject,email_body)
    print('sent')

