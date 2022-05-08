# importing the required libraries
import requests
# Enter the api key of openweathermap here
api_key = "d2a323fb1f5fb7601a4ffe0b2707cafd" # Api key from the open weather website
root_url = "http://api.openweathermap.org/data/2.5/weather?" # Url for the open map api
city_name = input("Please Enter The City Name : ") # Enter the city needed for weatrher data
zip_code = input("Please enter the zipcode: ") #Enter the zipcode for weather data
url = f"{root_url}q={city_name},{zip_code}&appid={api_key}&units=metric" #final url for the API call
r = requests.get(url) # sending a get request at the url
data = r.json() # storing the returned json data into a variable
# Checking If there is no error and the status code is 200
if data['cod'] == 200:
    # getting the temperature from the json data
    temp = data['main']['temp']
    # getting the pressure from the json data
    pressure = data['main']['pressure']
    # getting the humidity from the json data
    humidity = data['main']['humidity']
    # getting the description from the json data
    descrip = data['weather'][0]['description']
    # getting the wind speed from the json data
    wind = data['wind']['speed']
    # Displaying all the data
    print(f"City Name : {city_name}")
    print(f"The Weather Condition is {descrip}")
    print(f"The temperature is {temp}°C")
    print(f"The pressure is {pressure} hPa")
    print(f"The humidity is {humidity}%")
    print(f"The speed of wind is {wind}m/s")
else:
    print("Error request")  # In the event of an error, this line of code prints #Error request
