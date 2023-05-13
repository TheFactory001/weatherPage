values = { "main":{"temp":304.33, "feels_like":308.13, "temp_min":304.33,"temp_max":304.33, "pressure":1006, "humidity":59, "sea_level":1006, "ground_level":1006},}
def get_temperature_value(temp_details):
    temperature = temp_details["main"]["temp"]
    return (temperature - 273)

#print(get_temperature_value(values))