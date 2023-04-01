values = {"coord":{"lon":3.75,"lat":6.5833},
    "weather":[{"id":803,
    "main":"Clouds",
    "description":"broken clouds",
    "icon":"04d"}],"base":"stations",
    "main":{"temp":304.33,
    "feels_like":308.13,
    "temp_min":304.33,"temp_max":304.33,
    "pressure":1006,
    "humidity":59,
    "sea_level":1006,
    "grnd_level":1006},
    "visibility":10000,
    "wind":{"speed":5.05,"deg":197,"gust":6.2},
    "clouds":{"all":59},
    "dt":1679156754,
    "sys":{"type":1,"id":1185,"country":"NG","sunrise":1679118622,"sunset":1679162163},
    "timezone":3600,"id":2332453,
    "name":"Lagos",
    "cod":200}
def create_new_dict():
    info = values
    return info["coord"]  

def get_new_value():  
    info = values
    return info["weather"]

def get_another_value():
    info = values
    return info["main"]

print(create_new_dict())
print(get_new_value())   
print(get_another_value()) 