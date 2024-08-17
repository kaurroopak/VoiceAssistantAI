import requests
from keys import weather_api_key

weather_api_address ="https://api.openweathermap.org/data/2.5/weather?q=Patiala&appid="+ weather_api_key
json_data = requests.get(weather_api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description
