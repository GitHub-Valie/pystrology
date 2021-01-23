from flask import Flask, render_template, request
from datetime import datetime
import requests, random

app = Flask(__name__)

@app.route('/')
def index():
    title = "PyStrology"
    time = datetime.now().strftime("%H:%M:%S")
    zodiac_signs = [
        'aquarius', 'pisces', 'aries', 
        'taurus', 'gemini', 'cancer',
        'leo', 'virgo', 'libra',
        'scorpio', 'sagittarius', 'capricorn'
    ]
    return render_template(
        'index.html', 
        title = title,
        zodiac_signs=zodiac_signs
    )

@app.route('/horoscope', methods=['POST'])
def horoscope():
    sign = request.form['zodiac_sign']
    day = "today"
    api_url = "https://aztro.sameerkumar.website/?sign="+sign+"&day="+day
    json = requests.post(api_url).json()
    sign_title = sign.title()
    return render_template(
        'horoscope.html',
        sign = sign_title,
        color = json['color'],
        compatibility = json['compatibility'],
        date_range = json['date_range'],
        description = json['description'],
        lucky_number = json['lucky_number'],
        lucky_time = json['lucky_time'],
        mood = json['mood']
    )


if __name__ == "__main__":
    app.run(debug=True)