from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        province = request.form['province']
        print(province) 
        country = request.form['country']
        print(country) 
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(port='8000', debug=True)  