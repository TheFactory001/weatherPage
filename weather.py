from flask import Flask, render_template, request, jsonify, redirect, url_for
from project import generate_url

import json
# import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather',  methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        print(city)
    return redirect(url_for('index'))
    # city = request.args.get('city')
    # if not city:
    # return jsonify({'error': 'Please provide a city name.'}), 400


# url = 'complete_url'

# response = requests.get(url)
# data = response.json()

# if data['cod'] == '404':
    # return jsonify({'error': 'City not found.'}), 404


if __name__ == '__main__':
    app.run(debug=True)
