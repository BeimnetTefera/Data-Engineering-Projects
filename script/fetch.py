import requests
import json
import os

# Make sure the data folder exists
if not os.path.exists('data'):
    os.makedirs('data')

def fetch_weather(city='London'):
    # Build the API
    url = f"https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&hourly=temperature_2m"

    try:
        response = requests.get(url)
        print(f"HTTP Status Code: {response.status_code}") 
        response.raise_for_status()
        data = response.json()
        print("Sample data keys:", list(data.keys()))  

        """
        Fetch weather data from Open-Meteo API
        """
        with open('data/weather.json', 'w') as f:
            json.dump(data, f, indent=4)

        print("Weather data saved to data/weather.json")
        return data

    except requests.exceptions.RequestException as e:
        print(f'Error Fetching Weather: {e}')
        return None

if __name__ == '__main__':
    fetch_weather()