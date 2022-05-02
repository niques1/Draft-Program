# importing the required libraries
import requests #having problems getting pip requests to work
# Enter the api key of openweathermap here
api_key = "d2a323fb1f5fb7601a4ffe0b2707cafd" # Api key from the open weather website
root_url = "http://api.openweathermap.org/data/2.5/weather?" # Url for the open map api
city_name = input("Please Enter The City Name : ") # Enter the City needed for weather data
url = f"{root_url}appid={api_key}&q={city_name}" #final url for the API call
r = requests.get(url) # sending a get request at the url
data = r.json() # storing the returned json data into a variable
