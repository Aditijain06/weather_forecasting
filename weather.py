import requests
import json
import sys

def get_weather(city_name):
    api_key = "487111d3acc9f9740d7b6f09978b3e4b"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == "404":
            print(f"City '{city_name}' not found.")
        else:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            print(f"Weather in {city_name}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the weather data:", str(e))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        city = sys.argv[1]
        get_weather(city)
    else:
        print("Usage: python weather.py <city>")
