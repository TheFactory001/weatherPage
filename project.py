# Generate  complete_url
def generate_url(city):

    base_id = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "a1d832c101f04481e98ece5a0a6cb290"

    complete_url = base_id + "appid="+api_key+"&q=" + city
    return (complete_url)
