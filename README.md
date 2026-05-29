# Weather-APP-CLI-
This project is a simple Command Line Interface (CLI) Weather Application developed using Python. It fetches real-time weather data from the OpenWeatherMap API and displays information such as temperature, humidity, and weather conditions for any city entered by the user.

Features Real-time weather updates Displays temperature in Celsius Shows humidity levels Displays weather conditions Beginner-friendly Python project Uses API integration and JSON data Technologies Used Python Requests Library OpenWeatherMap API Project Structure weather-app/ │ ├── weather.py ├── README.md └── requirements.txt Installation

1.Clone the Repository git clone https://github.com/your-username/weather-app.git

2.Navigate to Project Folder cd weather-app

3.Install Required Package pip install requests Get API Key

Create a free account and generate an API key from:

OpenWeatherMap API

Replace your API key in the code:

API_KEY = "YOUR_API_KEY" Run the Project python weather.py Example Output Enter city name: Hyderabad

Weather Details
City: Hyderabad Temperature: 31°C

Humidity: 60% Condition: Clear Sky

Sample Code:

import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:

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
else: print("Error:", data["message"])Learning Outcomes

By completing this project, you will learn:

Python basics API integration JSON data handling Error handling CLI application development Future Improvements Add 5-day weather forecast Add graphical user interface (GUI) Add weather icons Add automatic location detection Add colored terminal output
