from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from project import generate_url
from weather_utility import get_country_name, get_temperature
from flask_cors import CORS

import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')
app.config['SECRET_KEY'] = '#2703ARAD'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route('/')
# @app.route('/<city>/<country>/<temperature>', methods =['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/weather',  methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        if not city:
            return jsonify({'error': 'Please provide a city name.'}), 400
        url = generate_url(city)
        response = requests.get(url)
        data = response.json()
        country = get_country_name(data)
        temperature = get_temperature(data)
        return render_template('index.html', city=city, country=country, temperature=temperature)
    

@app.route('/getWeatherInfo', methods=['GET', 'POST'])
def weatherInfo():
    if request.method == 'POST':
        city = request.get_json()['city']
        if not city:
            return jsonify({'error': 'Please provide a city name.'}), 400
        url = generate_url(city)
        response = requests.get(url)
        data = response.json()
        country = get_country_name(data)
        temperature = round(get_temperature(data), 2)
        userData = {'country': country, 'temperature' : temperature}
        return userData
    return '404'

if __name__ == '__main__':
    app.run(debug=True)
