import requests
from datetime import datetime

#Fetch current weather data.

def display_current_weather(city_name):
    api_key = "04e13864eb3t2f8af00833563db7ofc6"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city_name}&key={api_key}"

    #Make API call
    response = requests.get(api_url)
    weather_data = response.json()

    # Extract relevant data
    city = weather_data['city']
    temperature = weather_data['temperature']['current']
    description = weather_data['condition']['description']

    #Display results.
    print(f"The current weather in {city} is:")
    print(f"- Temperature: {temperature}°C")
    print(f"- Description: {description}")


if __name__ == "__main__":
    city_name = input("Enter a city name: ").strip()
    display_current_weather(city_name)

 
