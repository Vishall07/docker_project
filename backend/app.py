import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Fetch the API key from environment variables
API_KEY = os.getenv("API_KEY")

# If API_KEY is not set, raise an error
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set!")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # Change to the weather API you're using

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'San Francisco')  # Default to San Francisco if no city is provided
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature (Celsius)
    }

    try:
        # Make the API request to the weather service
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Format and return the weather data
        weather_data = {
            "location": data["name"],
            "temperature": f"{data['main']['temp']}°C",
            "condition": data["weather"][0]["description"],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s"
        }

        return jsonify(weather_data)

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        return jsonify({"error": "Unable to fetch weather data", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on all available IP addresses and port 5000
    app.run(host='0.0.0.0', port=5000)