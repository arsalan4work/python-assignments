import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")

city = input("\nEnter a city to check the weather: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}&q={city}"

weather_data = requests.get(base_url).json()

pprint(weather_data)
