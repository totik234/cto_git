import requests
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def get_weather(city):
    appid = "17048e47b5e47a122e200121efb8c1c8"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params_api = {"q": city, "appid": appid, "lang": "ru", "units": "metric"}
    try:
        r = requests.get(base_url, params=params_api)
        data = r.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        name = data['name']
        return render_template('index.html', weather=weather, temp=temp, pressure=pressure, humidity=humidity, name=name)
    except Exception:
        r = requests.get(base_url, params=params_api)
        data = r.json()
        error = data['message']
        return render_template('index.html', error=error)


@app.route('/form_weather', methods=['GET'])
def form_weather():
    city = request.args.get('city')
    return get_weather(city)


# print("Погодные условия: ", data['weather'][0]['description'])
# print("Температура:", data['main']['temp'], "\u2103")
# print("Атмосферное давление:", data['main']['pressure'], "мм рт.ст.")


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()