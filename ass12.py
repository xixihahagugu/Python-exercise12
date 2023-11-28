import json
import requests
from requests.structures import CaseInsensitiveDict
address=input("Enter your municipality:")
url="https://api.geoapify.com/v1/geocode/search?text={address}&limit=1&apiKey=1cb11536f6b44d5582203e8d1803739d"
response = requests.get(url)
if response.status_code == 200:

    data = response.json()


    result = data["features"][0]


    latitude = result["geometry"]["coordinates"][1]
    longitude = result["geometry"]["coordinates"][0]

    print(f"Latitude: {latitude:.2f}, Longitude: {longitude:.2f}")
else:
    print(f"Request failed with status code {response.status_code}")



request = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude:.2f}&lon={longitude:.2f}&appid=7722d6e7aa4bcc7c39e92b337f5f9ea1"
#request="https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=7722d6e7aa4bcc7c39e92b337f5f9ea1"
response = requests.get(request).json()

weather_descrption=response["weather"][0]["description"]

temperature_celsius=int(response["main"]["temp"]) - 273.15

print(f"{address}     Temperature(celsius):{temperature_celsius:.1f}     Weather descrption:{weather_descrption}")