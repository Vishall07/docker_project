// JavaScript to fetch weather data from the OpenWeather API

// Function to fetch weather data from the OpenWeather API
async function getWeather() {
    const city = document.getElementById("city").value;
    const apiKey = "853d4ed410b7cea5ed1038d6b4cb00ed";
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        // Check if the city is valid
        if (data.cod === 200) {
            displayWeather(data);
        } else {
            alert("City not found. Please try again.");
        }
    } catch (error) {
        alert("An error occurred while fetching the data.");
    }
}

// Function to display weather data on the page
function displayWeather(data) {
    const location = `${data.name}, ${data.sys.country}`;
    const temperature = `Temperature: ${data.main.temp}°C`;
    const description = `Weather: ${data.weather[0].description}`;
    const humidity = `Humidity: ${data.main.humidity}%`;
    const windSpeed = `Wind Speed: ${data.wind.speed} m/s`;

    // Display weather data
    document.getElementById("location").innerText = location;
    document.getElementById("temperature").innerText = temperature;
    document.getElementById("description").innerText = description;
    document.getElementById("humidity").innerText = humidity;
    document.getElementById("wind-speed").innerText = windSpeed;
}
