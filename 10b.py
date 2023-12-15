import json
with open('weather_data.json')as f:
    data=json.load(f)
currenttemp=data['main']['temp']
humidity=data['main']['humidity']
weatherdesc=data['main']['description']
print(f"TEMPERATURE:{currenttemp} degree celsius")
print(f"HUMIDITY:{humidity} %")
print(f"WEATHER:{weatherdesc} ")