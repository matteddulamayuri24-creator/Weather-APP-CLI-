import requests

# Enter your API key here
API_KEY = "bd573fbb89d36c9cd7b94281244090bc"

# Ask user for city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Get data from API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check city found or not
if data["cod"] != "404":
    main = data["main"]
    weather = data["weather"][0]

    temperature = main["temp"]
    humidity = main["humidity"]
    description = weather["description"]

    print("\nWeather Details")
    print("-------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")

else:
    print("City not found!")
