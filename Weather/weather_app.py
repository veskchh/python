import requests

api_key = "UR API KEY"

city = input("Enter the city: ")

url = f"https://www.meteosource.com/api/v1/free/point?place_id={city}&sections=current%2Chourly&language=en&units=auto&key={api_key}"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()

    try:
        current_weather = json_data.get("current", {})
        current_temp = current_weather.get("temperature", "N/A")
        summary = current_weather.get("summary")

        print(f"\nWeather report for {city.capitalize()}:")
        print(f"Current Temperature: {current_temp}°C")
        print(f"Summary: {summary}")
    
    except KeyError as e:
        print(f"Error: Unable to retrieve weather data. Missing key: {e}")
else:
    print(f"Error: Unable to fetch weather data for {city}. Status code: {response.status_code}")
