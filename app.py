from flask import Flask, render_template, request, json, redirect, url_for
import requests
from project import generate_url
from get_description import get_weather_description
from get_temperature import get_temperature_value
from get_values import *

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # The request takes the value of city assigned in the html template to be utilized in the python file
        city = request.form['city']
        print(city)
        # With the import request at the top, the return value in the function can be returned in the terminal
        url = generate_url(city)
        print(url)
        # The response is set to a request function which allows the user to return data contained in the url variable 
        response = requests.get(url)
        # The json function makes it easy to transfer the data stored in response easy to transfer
        data = response.json()
        print(data)
        
    return render_template('weather.html')

    

if __name__ == '__main__':
    app.run(port='8000', debug=True)  