import requests
from datetime import datetime

    #Helper function to fetch weather data with error handling if API call fails
def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API.")

    #Fetch current weather data
def display_current_weather(city_name):
    api_key = "04e13864eb3t2f8af00833563db7ofc6"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city_name}&key={api_key}"

    weather_data = fetch_weather_data(api_url)

    # Extract current weather data
    city = weather_data['city']
    country = weather_data['country']
    temperature = weather_data['temperature']['current']
    description = weather_data['condition']['description']
    humidity = weather_data['temperature']['humidity']
    wind_speed = weather_data['wind']['speed']

    rounded_temperature = round(temperature)

    #Display results.
    print(f"The current weather in {city}, {country} is:")
    print(f"- Temperature: {rounded_temperature}°C")
    print(f"- Description: {description}")
    print(f"- Humidity: {humidity}%")
    print(f"- Wind speed: {wind_speed} m/s")

    #Fetch forecast weather data for next 3 days

def display_weather_forecast(city_name):
    api_key = "04e13864eb3t2f8af00833563db7ofc6"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

    forecast_data = fetch_weather_data(api_url)

    # Extract forecast data and display forecast results for next 3 days with name of weekdays
    forecast_days = forecast_data['daily'][:3]
    print("\nWeather forecast for the next 3 days:")
    for day in forecast_days:
        weekday_name = datetime.utcfromtimestamp(day['time']).strftime('%A')
        description = day['condition']['description']
        temperature = round(day['temperature']['day']) 
        humidity = day['temperature']['humidity']
        wind_speed = day['wind']['speed'] 

        print(f"\n{weekday_name}:")
        print(f"- Condition: {description}")
        print(f"- Temperature: {temperature}°C")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind speed: {wind_speed}m/s")

if __name__ == "__main__":
    city_name = input("Enter a city name: ").strip()
    display_current_weather(city_name)
    display_weather_forecast(city_name)
 
