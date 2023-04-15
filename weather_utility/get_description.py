values = {"weather":[{"id":803, "main":"Clouds", "description":"broken clouds", "icon":"04d"}, 5]}
def get_weather_description(weather_info):
    weather_value = weather_info["weather"][0]
    weather_description = weather_value["description"]
    return weather_description

print(get_weather_description(values))

'''
weather_details = values["weather"]
weather_details_item1 = weather_details[0]
weather_description = weather_details_item1["description"]
print(weather_description)
print(values["weather"][0]["description"])
'''
