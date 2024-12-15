from flask import Flask
app = Flask (__name__)

@app.route('/getWeatherForecast')
def getWeatherOnline():
    return "Today's weather forecast is sunny"