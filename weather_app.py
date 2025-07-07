import requests

api_key = """user API KEY"""

def get_city(city):

    
    base_url = ("http://api.openweathermap.org/geo/1.0/direct?")

    params = {"q":city, "appid":api_key}

    response = requests.get(base_url, params = params)
    data = response.json()
    
    lat = (data[0]['lat'])
    long = (data[0]['lon'])
    return lat, long
    
def get_weather(i, j):
    
    base3_url=("https://api.openweathermap.org/data/2.5/weather?")
    params = {"lat":i, "lon":j, "appid":api_key}

    response = requests.get(base3_url,params = params)
    data = response.json()
    
    print("Current weather for " + city_input)
    print(data['weather'][0]['description'])
    print("The current temperature is: " "{:.2f}".format(data['main']['temp'] - 273.15))
    print("The current realfeel temperature is: ""{:.2f}".format(data['main']['feels_like']  - 273.15))
    print("The current wind speed is: %d m/s " % data['wind']['speed'])
    print("The current humidity is %d percent" % data['main']['humidity'])
    
city_input = input("enter a city: -\n")

lat, long = get_city(city_input)
get_weather(lat, long)
