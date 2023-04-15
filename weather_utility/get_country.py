values = {"sys":{"type":1,"id":1185,"country":"NG","sunrise":1679118622,"sunset":1679162163},
 "main":{"temp":304.33, "feels_like":308.13, "temp_min":304.33,"temp_max":304.33, "pressure":1006, "humidity":59, "sea_level":1006, "ground_level":1006},}

def get_country_name(system_details):
    country_name = system_details["sys"]["country"]
    return country_name

def get_temperature(temp_details):
    temperature = temp_details["main"]["temp"]
    return (temperature - 273)

print(get_country_name(values))
print(get_temperature(values))