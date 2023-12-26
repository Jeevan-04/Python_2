import requests

# Replace 'your_api_key' with the actual API key you obtained from OpenWeatherMap
api_key = 'ef374978325e8ff38db840f71f5f2d09'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}  # Adjust 'units' as needed (metric, imperial, standard)

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()

        # Process and print the weather data
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)

    except requests.exceptions.RequestException as err:
        print("Oops! Something went wrong:", err)

# Example: Get weather for a specific city
x=input("Region: ")
get_weather(x)
