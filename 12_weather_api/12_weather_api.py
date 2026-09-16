import requests

print("====== WEATHER ======")
city = input("Enter city: ")
if not city.strip():
    print("City cannot be empty!")
    exit()

def get_coordinates(city):
    params = {
        "name": city
    }

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(url, params=params)
    # print(response.status_code)
    data = response.json()

    if "results" not in data or not data["results"]:
        print("City not found!")
        return None

    else:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        return latitude, longitude

def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    try: 
        weather_response = requests.get(weather_url, params= weather_params)
    except requests.exceptions.RequestException:
        print("Unable to connect!")
        return None

    weather_response.raise_for_status()
    # print(weather_response.status_code)
    weather_data = weather_response.json()
    # print(weather_data)
    
    return weather_data

coordinates = get_coordinates(city)
if coordinates is None:
    exit()

latitude, longitude = coordinates

weather_data = get_weather(latitude, longitude)
if weather_data is None:
    exit()

temperature = weather_data["current"]["temperature_2m"]
relative_humidity = weather_data["current"]["relative_humidity_2m"]
wind_speed = weather_data["current"]["wind_speed_10m"]
weather_code = weather_data["current"]["weather_code"]

weather_conditions = {
    0: "Clear sky",
    1: "Cloudy / partly cloudy",
    2: "Cloudy / partly cloudy",
    3: "Cloudy / partly cloudy",
    45: "Fog",
    48: "Fog",
    51: "Drizzle",
    53: "Drizzle",
    55: "Drizzle",
    61: "Rain",
    63: "Rain",
    65: "Rain",
    71: "Snow",
    73: "Snow",
    75: "Snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Rain showers",
    95: "Thunderstorm"
}

weather_condition = weather_conditions.get(weather_code, "Unknown")

print(f"Temperature: {temperature}°C")
print(f"Humidity: {relative_humidity}%")
print(f"Wind Speed: {wind_speed} km/h")
print(f"Weather Condition: {weather_condition}")
