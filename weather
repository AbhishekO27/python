import requests

api_key = '7dc922103b4f6cb45bdf0bd512f952c6'

user_input = input("enter city : ")

weather_data = request.get(f"https://api.openweather.org/data/2.5/weather?q={user_input}&units=imperial&APIID={api_key}")

 weather = weather_data.json() ['weather'][0]['main']
 temp = round(weather_data.json()['main']['temp'])
 
 print(f"weather in {user_input} is = {weather}  )
  print(f"temperature in {user_input} is = {temp}F  )
